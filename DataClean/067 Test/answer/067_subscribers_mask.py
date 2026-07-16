import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "subscribers_private.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

sensitive_fields = ['phone', 'email']
df = pd.read_csv(data_path, dtype={"phone": str, "id_card": str})

# 全字段掩码只保留原值长度，不保留任何原字符。
def full_mask(value):
    """按原字符串长度生成全星号掩码。"""
    return "*" * len(str(value))

def partial_mask(field, value):
    """根据不同敏感字段执行对应的部分保留规则。"""
    text = str(value)
    if field == "name":
        return text[:1] + "*" * max(len(text) - 1, 0)
    if field == "phone":
        return text[:3] + "*" * max(len(text) - 7, 0) + text[-4:]
    if field == "id_card":
        return text[:6] + "*" * max(len(text) - 10, 0) + text[-4:]
    if field == "email" and "@" in text:
        account, domain = text.split("@", 1)
        return account[:2] + "*" * max(len(account) - 2, 0) + "@" + domain
    return full_mask(text)

# 分别创建全掩码和部分掩码副本，避免修改原始数据。
full_df = df.copy()
partial_df = df.copy()
for field in sensitive_fields:
    full_df[field] = full_df[field].map(full_mask)
    partial_df[field] = partial_df[field].map(lambda value, f=field: partial_mask(f, value))

non_sensitive_fields = [field for field in df.columns if field not in sensitive_fields]
report = pd.DataFrame([
    {"check": "原始行数", "value": len(df)},
    {"check": "原始列数", "value": df.shape[1]},
    {"check": "全掩码行列数一致", "value": full_df.shape == df.shape},
    {"check": "部分掩码行列数一致", "value": partial_df.shape == df.shape},
    {"check": "全掩码非敏感字段不变", "value": full_df[non_sensitive_fields].equals(df[non_sensitive_fields])},
    {"check": "部分掩码非敏感字段不变", "value": partial_df[non_sensitive_fields].equals(df[non_sensitive_fields])},
    {"check": "全掩码敏感字段已改变", "value": all(not full_df[f].equals(df[f]) for f in sensitive_fields)},
    {"check": "部分掩码敏感字段已改变", "value": all(not partial_df[f].equals(df[f]) for f in sensitive_fields)},
])

full_df.to_csv(output_dir / "subscribers_masked_full.csv", index=False, encoding="utf-8-sig")
partial_df.to_csv(output_dir / "subscribers_masked_partial.csv", index=False, encoding="utf-8-sig")
report.to_csv(output_dir / "subscribers_mask_validation_report.csv", index=False, encoding="utf-8-sig")
print("全字段掩码前 5 行：\n", full_df.head())
print("部分掩码前 5 行：\n", partial_df.head())
print(report.to_string(index=False))
