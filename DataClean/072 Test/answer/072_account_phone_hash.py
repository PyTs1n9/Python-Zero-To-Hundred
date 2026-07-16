import hashlib
import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "account_phone_private.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

sensitive_fields = ['phone']
df = pd.read_csv(data_path, dtype={"phone": str, "id_card": str})

def hash_text(value, algorithm):
    """统一转为字符串并使用 UTF-8 编码后计算十六进制摘要。"""
    payload = str(value).encode("utf-8")
    return hashlib.new(algorithm, payload).hexdigest()

sha_df = df.copy()
md5_df = df.copy()
for field in sensitive_fields:
    sha_df[field] = df[field].map(lambda value: hash_text(value, "sha256"))
    md5_df[field] = df[field].map(lambda value: hash_text(value, "md5"))

# 对每个原始重复值分组，检查组内哈希结果是否唯一。
rows = []
for field in sensitive_fields:
    repeated = df[df.duplicated(subset=[field], keep=False)]
    duplicate_group_count = int(repeated[field].nunique())
    sha_consistent = all(sha_df.loc[index, field].nunique() == 1 for _, index in repeated.groupby(field).groups.items())
    md5_consistent = all(md5_df.loc[index, field].nunique() == 1 for _, index in repeated.groupby(field).groups.items())
    rows.append({
        "field": field,
        "duplicate_group_count": duplicate_group_count,
        "sha256_consistent": sha_consistent,
        "md5_consistent": md5_consistent,
        "sha256_length_is_64": bool(sha_df[field].str.len().eq(64).all()),
        "md5_length_is_32": bool(md5_df[field].str.len().eq(32).all()),
    })

report = pd.DataFrame(rows)
sha_df.to_csv(output_dir / "account_phone_hash_sha256.csv", index=False, encoding="utf-8-sig")
md5_df.to_csv(output_dir / "account_phone_hash_md5.csv", index=False, encoding="utf-8-sig")
report.to_csv(output_dir / "account_phone_hash_consistency_report.csv", index=False, encoding="utf-8-sig")

comparison = """SHA-256 与 MD5 对比
1. 两者都具有同值同哈希特性，因此可用于分组和关联。
2. SHA-256 输出 64 位十六进制字符串，抗碰撞能力显著强于 MD5。
3. MD5 已不适合安全敏感场景，只能用于非安全校验等有限用途。
4. 无盐哈希容易受到字典攻击；真实隐私数据应结合盐值、密钥或专用令牌化方案。
"""
(output_dir / "account_phone_hash_comparison.txt").write_text(comparison, encoding="utf-8")
print(report.to_string(index=False))
