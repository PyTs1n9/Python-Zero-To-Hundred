import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "medical_check_dirty.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

numeric_fields = ['age', 'height_cm', 'weight_kg', 'blood_pressure', 'blood_sugar']
df = pd.read_csv(data_path, dtype=str)
original_rows = len(df)
original_missing = int(df.isna().sum().sum())
original_duplicates = int(df.duplicated().sum())

# 含字母、汉字或单位符号的非空内容记为带单位/文本数字，供报告使用。
string_number_count = 0
invalid_count = 0
converted = df.copy()
for field in numeric_fields:
    source = converted[field]
    string_number_count += int(source.fillna("").str.contains(r"[^0-9.+-]", regex=True).sum())
    extracted = source.str.extract(r"([-+]?\d*\.?\d+)", expand=False)
    converted[field] = pd.to_numeric(extracted, errors="coerce")
    invalid_count += int((source.notna() & converted[field].isna()).sum())

# 类型转换后再填充，可同时处理原始空值和无效文本产生的 NaN。
for field in numeric_fields:
    converted[field] = converted[field].fillna(converted[field].median())
converted["risk_level"] = converted["risk_level"].fillna(converted["risk_level"].mode().iloc[0])
clean = converted.drop_duplicates(keep="first").copy()

# 对异常值执行截断，保留样本行数。
outlier_value_count = 0
for field in numeric_fields:
    q1, q3 = clean[field].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    mask = (clean[field] < lower) | (clean[field] > upper)
    outlier_value_count += int(mask.sum())
    clean[field] = clean[field].clip(lower, upper)

# StandardScaler 使用总体标准差，因此验证时使用 ddof=0。
scaled = clean.copy()
scaler = StandardScaler()
scaled[numeric_fields] = scaler.fit_transform(clean[numeric_fields])
model_data = scaled[numeric_fields + ["risk_level"]].copy()
standard_check = pd.DataFrame({
    "field": numeric_fields,
    "scaled_mean": scaled[numeric_fields].mean().values,
    "scaled_std_ddof0": scaled[numeric_fields].std(ddof=0).values,
})

report = pd.DataFrame([
    {"metric": "原始数据行数", "value": original_rows},
    {"metric": "原始数据列数", "value": df.shape[1]},
    {"metric": "原始缺失值数量", "value": original_missing},
    {"metric": "带单位或文本数字数量", "value": string_number_count},
    {"metric": "无法转换内容数量", "value": invalid_count},
    {"metric": "完全重复行数量", "value": original_duplicates},
    {"metric": "删除重复后的行数", "value": len(clean)},
    {"metric": "异常单元格截断数量", "value": outlier_value_count},
    {"metric": "清洗后行数", "value": len(clean)},
    {"metric": "清洗后缺失值数量", "value": int(clean.isna().sum().sum())},
])

clean.to_csv(output_dir / "medical_check_clean.csv", index=False, encoding="utf-8-sig")
scaled.to_csv(output_dir / "medical_check_scaled.csv", index=False, encoding="utf-8-sig")
model_data.to_csv(output_dir / "medical_check_model_data.csv", index=False, encoding="utf-8-sig")
standard_check.to_csv(output_dir / "medical_check_standardization_check.csv", index=False, encoding="utf-8-sig")
report.to_csv(output_dir / "medical_check_cleaning_report.csv", index=False, encoding="utf-8-sig")

# 按比赛提交风格说明处理顺序、规则和产物。
notes = f"""# 数据清洗说明

1. 原始数据：medical_check_dirty.csv，共 {original_rows} 行。
2. 类型转换：提取数值部分，无效内容转为 NaN。
3. 缺失值：数值字段使用中位数，risk_level 使用众数。
4. 重复值：删除完全重复行，保留首次出现记录。
5. 异常值：使用 IQR 上下限截断，共处理 {outlier_value_count} 个单元格。
6. 标准化：对 age, height_cm, weight_kg, blood_pressure, blood_sugar 使用 StandardScaler。
7. 结果：清洗后 {len(clean)} 行，缺失值 {int(clean.isna().sum().sum())} 个。
"""
(output_dir / "medical_check_cleaning_notes.md").write_text(notes, encoding="utf-8")
print(report.to_string(index=False))
