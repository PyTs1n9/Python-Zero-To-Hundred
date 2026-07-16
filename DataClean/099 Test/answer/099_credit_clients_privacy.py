import hashlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "credit_clients_private.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

sensitive_fields = ["name", "phone", "id_card"]
numeric_fields = ['age', 'income', 'credit_amount', 'credit_score', 'default_risk']
df = pd.read_csv(data_path, dtype={"phone": str, "id_card": str})

def full_mask(value):
    return "*" * len(str(value))

def partial_mask(field, value):
    text = str(value)
    if field == "name":
        return text[:1] + "*" * max(len(text) - 1, 0)
    if field == "phone":
        return text[:3] + "*" * max(len(text) - 7, 0) + text[-4:]
    return text[:6] + "*" * max(len(text) - 10, 0) + text[-4:]

def digest(value, algorithm):
    return hashlib.new(algorithm, str(value).encode("utf-8")).hexdigest()

partial_df, full_df, sha_df, md5_df = (df.copy() for _ in range(4))
for field in sensitive_fields:
    partial_df[field] = df[field].map(lambda value, f=field: partial_mask(f, value))
    full_df[field] = df[field].map(full_mask)
    sha_df[field] = df[field].map(lambda value: digest(value, "sha256"))
    md5_df[field] = df[field].map(lambda value: digest(value, "md5"))

partial_df.to_csv(output_dir / "credit_clients_clients_masked_partial.csv", index=False, encoding="utf-8-sig")
full_df.to_csv(output_dir / "credit_clients_clients_masked_full.csv", index=False, encoding="utf-8-sig")
sha_df.to_csv(output_dir / "credit_clients_clients_hash_sha256.csv", index=False, encoding="utf-8-sig")
md5_df.to_csv(output_dir / "credit_clients_clients_hash_md5.csv", index=False, encoding="utf-8-sig")

# 哈希一致性：同一原始值在同一算法下必须得到唯一结果。
hash_rows = []
for field in sensitive_fields:
    repeated = df[df.duplicated(subset=[field], keep=False)]
    hash_rows.append({
        "field": field,
        "duplicate_group_count": int(repeated[field].nunique()),
        "sha256_consistent": all(sha_df.loc[idx, field].nunique() == 1 for idx in repeated.groupby(field).groups.values()),
        "md5_consistent": all(md5_df.loc[idx, field].nunique() == 1 for idx in repeated.groupby(field).groups.values()),
        "sha256_length_is_64": bool(sha_df[field].str.len().eq(64).all()),
        "md5_length_is_32": bool(md5_df[field].str.len().eq(32).all()),
    })
hash_report = pd.DataFrame(hash_rows)
hash_report.to_csv(output_dir / "credit_clients_hash_consistency_report.csv", index=False, encoding="utf-8-sig")

# 四种脱敏结果的数值字段理论上完全不变。
methods = {"partial_mask": partial_df, "full_mask": full_df, "sha256": sha_df, "md5": md5_df}
original_mean = df[numeric_fields].mean()
original_std = df[numeric_fields].std()
stats_rows = []
for method, result in methods.items():
    for field in numeric_fields:
        stats_rows.append({
            "method": method, "field": field,
            "mean_before": original_mean[field], "mean_after": result[field].mean(),
            "mean_difference": result[field].mean() - original_mean[field],
            "std_before": original_std[field], "std_after": result[field].std(),
            "std_difference": result[field].std() - original_std[field],
        })
stats = pd.DataFrame(stats_rows)
stats.to_csv(output_dir / "credit_clients_stats_comparison.csv", index=False, encoding="utf-8-sig")

pearson_before = df[numeric_fields].corr()
pearson_after = partial_df[numeric_fields].corr()
pearson_diff = pearson_after - pearson_before
pearson_before.to_csv(output_dir / "credit_clients_pearson_before.csv", encoding="utf-8-sig")
pearson_after.to_csv(output_dir / "credit_clients_pearson_after.csv", encoding="utf-8-sig")

def heatmap(matrix, title, filename):
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_dir / filename, dpi=160)
    plt.close()

heatmap(pearson_before, "Pearson Correlation Before Desensitization", "credit_clients_pearson_before_heatmap.png")
heatmap(pearson_after, "Pearson Correlation After Desensitization", "credit_clients_pearson_after_heatmap.png")

max_mean_diff = float(stats["mean_difference"].abs().max())
max_std_diff = float(stats["std_difference"].abs().max())
max_corr_diff = float(pearson_diff.abs().to_numpy().max())
validation_rows = []
for method, result in methods.items():
    unchanged = result[numeric_fields].equals(df[numeric_fields])
    validation_rows.append({
        "method": method, "row_count": len(result),
        "numeric_fields_unchanged": unchanged,
        "max_abs_mean_difference": max_mean_diff,
        "max_abs_std_difference": max_std_diff,
        "max_abs_pearson_difference": max_corr_diff,
        "conclusion": "通过" if unchanged and max_mean_diff < 1e-12 and max_std_diff < 1e-12 and max_corr_diff < 1e-12 else "未通过",
    })
validation = pd.DataFrame(validation_rows)
validation.to_csv(output_dir / "credit_clients_privacy_validation_report.csv", index=False, encoding="utf-8-sig")

analysis = f"""# 隐私脱敏分析报告

## 数据与敏感字段

数据文件为 credit_clients_private.csv，共 {len(df)} 行；name、phone、id_card 为模拟敏感字段。

## 四种处理规则

- 部分掩码保留少量识别片段，适合人工核验。
- 全字段掩码隐藏全部内容，保护更强但无法关联同一对象。
- SHA-256 与 MD5 保留“同值同哈希”特性，可用于分组或连接。

## 安全性比较

SHA-256 的抗碰撞能力高于 MD5；MD5 已不适合安全场景。两者均为无盐哈希，仍可能受到字典攻击，真实项目应结合盐值、密钥哈希或令牌化。

## 统计可用性

均值最大绝对差：{max_mean_diff}；标准差最大绝对差：{max_std_diff}；Pearson 最大绝对差：{max_corr_diff}。四种方法均只修改敏感字段，因此数值统计和相关结构保持不变。
"""
(output_dir / "credit_clients_privacy_analysis_report.md").write_text(analysis, encoding="utf-8")
print(validation.to_string(index=False))
