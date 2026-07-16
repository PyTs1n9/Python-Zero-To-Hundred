import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "course_score_missing.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# 明确目标字段，避免误修改编号等无需填充的字段。
numeric_fields = ['written_score', 'practice_score']
categorical_fields = []
fixed_values = {'written_score': 0, 'practice_score': 0}
df = pd.read_csv(data_path)
missing_before = df.isna().sum()

# 方法一：数值字段使用均值，分类字段使用众数。
mean_df = df.copy()
for field in numeric_fields:
    mean_df[field] = mean_df[field].fillna(mean_df[field].mean())
for field in categorical_fields:
    mean_df[field] = mean_df[field].fillna(mean_df[field].mode().iloc[0])

# 方法二：数值字段使用中位数，分类字段仍使用众数。
median_df = df.copy()
for field in numeric_fields:
    median_df[field] = median_df[field].fillna(median_df[field].median())
for field in categorical_fields:
    median_df[field] = median_df[field].fillna(median_df[field].mode().iloc[0])

# 方法三：第一个数值字段使用众数，其余字段使用题目给定固定值。
mixed_df = df.copy()
first_field = numeric_fields[0]
mixed_df[first_field] = mixed_df[first_field].fillna(mixed_df[first_field].mode().iloc[0])
for field in numeric_fields[1:]:
    mixed_df[field] = mixed_df[field].fillna(fixed_values[field])
for field in categorical_fields:
    mixed_df[field] = mixed_df[field].fillna("未知")

# 对比填充前后的均值，原始均值会自动忽略 NaN。
comparison = pd.DataFrame({
    "填充前": df[numeric_fields].mean(),
    "均值填充后": mean_df[numeric_fields].mean(),
    "中位数填充后": median_df[numeric_fields].mean(),
    "众数或固定值填充后": mixed_df[numeric_fields].mean(),
}).rename_axis("field").reset_index()

report = pd.DataFrame([
    {"metric": "原始行数", "value": len(df)},
    {"metric": "原始列数", "value": df.shape[1]},
    {"metric": "填充前缺失值总数", "value": int(missing_before.sum())},
    {"metric": "均值方案填充后缺失值总数", "value": int(mean_df.isna().sum().sum())},
    {"metric": "中位数方案填充后缺失值总数", "value": int(median_df.isna().sum().sum())},
    {"metric": "混合方案填充后缺失值总数", "value": int(mixed_df.isna().sum().sum())},
])

mean_df.to_csv(output_dir / "course_score_filled_mean.csv", index=False, encoding="utf-8-sig")
median_df.to_csv(output_dir / "course_score_filled_median.csv", index=False, encoding="utf-8-sig")
mixed_df.to_csv(output_dir / "course_score_filled_mode_fixed.csv", index=False, encoding="utf-8-sig")
comparison.to_csv(output_dir / "course_score_fill_mean_comparison.csv", index=False, encoding="utf-8-sig")
report.to_csv(output_dir / "course_score_missing_report.csv", index=False, encoding="utf-8-sig")

print("原始形状：", df.shape)
print("缺失值数量：\n", missing_before)
print("填充前后均值对比：\n", comparison)
