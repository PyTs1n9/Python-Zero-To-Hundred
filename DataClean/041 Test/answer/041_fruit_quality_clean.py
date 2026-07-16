import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "fruit_quality_dirty.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

numeric_fields = ['weight', 'sweetness']
categorical_fields = ['fruit_type', 'qualified']
df = pd.read_csv(data_path, dtype={"batch_id": str})

# 先记录原始质量指标，方便生成清洗前后对比。
before_rows = len(df)
before_missing = int(df.isna().sum().sum())
before_duplicates = int(df.duplicated().sum())
before_summary = df[numeric_fields].describe().T.rename_axis("field").reset_index()

clean = df.copy()
# 先填充缺失值，避免缺失值干扰后续边界计算。
for field in numeric_fields:
    clean[field] = clean[field].fillna(clean[field].median())
for field in categorical_fields:
    clean[field] = clean[field].fillna(clean[field].mode().iloc[0])

# 删除完全重复行，再基于当前有效数据计算 IQR 边界。
clean = clean.drop_duplicates(keep="first").copy()
bounds_rows = []
changed_values = 0
for field in numeric_fields:
    q1, q3 = clean[field].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outlier_mask = (clean[field] < lower) | (clean[field] > upper)
    changed_values += int(outlier_mask.sum())
    bounds_rows.append({
        "field": field, "Q1": q1, "Q3": q3, "IQR": iqr,
        "lower_bound": lower, "upper_bound": upper,
        "clipped_value_count": int(outlier_mask.sum()),
    })
    clean[field] = clean[field].clip(lower, upper)

after_summary = clean[numeric_fields].describe().T.rename_axis("field").reset_index()
report = pd.DataFrame([
    {"metric": "清洗前行数", "value": before_rows},
    {"metric": "清洗前列数", "value": df.shape[1]},
    {"metric": "清洗前缺失值总数", "value": before_missing},
    {"metric": "清洗前完全重复行数量", "value": before_duplicates},
    {"metric": "异常单元格截断数量", "value": changed_values},
    {"metric": "清洗后行数", "value": len(clean)},
    {"metric": "清洗后缺失值总数", "value": int(clean.isna().sum().sum())},
    {"metric": "清洗后完全重复行数量", "value": int(clean.duplicated().sum())},
])

clean.to_csv(output_dir / "fruit_quality_clean.csv", index=False, encoding="utf-8-sig")
pd.DataFrame(bounds_rows).to_csv(output_dir / "fruit_quality_iqr_bounds.csv", index=False, encoding="utf-8-sig")
before_summary.to_csv(output_dir / "fruit_quality_summary_before.csv", index=False, encoding="utf-8-sig")
after_summary.to_csv(output_dir / "fruit_quality_summary_after.csv", index=False, encoding="utf-8-sig")
report.to_csv(output_dir / "fruit_quality_cleaning_report.csv", index=False, encoding="utf-8-sig")
print(report.to_string(index=False))
