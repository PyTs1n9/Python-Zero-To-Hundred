import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "room_temperature.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

fields = ['temperature']
df = pd.read_csv(data_path)

# 基础统计帮助观察数据范围和中心位置。
summary = df[fields].agg(["min", "max", "mean", "median"]).T
summary = summary.rename_axis("field").reset_index()

# 对每个字段独立计算 IQR 边界，并合并各字段的异常条件。
any_outlier = pd.Series(False, index=df.index)
bounds_rows = []
field_counts = {}
for field in fields:
    q1 = df[field].quantile(0.25)
    q3 = df[field].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    field_mask = (df[field] < lower) | (df[field] > upper)
    field_counts[field] = int(field_mask.sum())
    any_outlier |= field_mask
    bounds_rows.append({
        "field": field, "Q1": q1, "Q3": q3, "IQR": iqr,
        "lower_bound": lower, "upper_bound": upper,
        "outlier_count": int(field_mask.sum()),
    })

bounds = pd.DataFrame(bounds_rows)
outliers = df.loc[any_outlier].copy()
report_rows = [
    {"metric": "原始数据行数", "value": len(df)},
    {"metric": "检测字段数量", "value": len(fields)},
    {"metric": "最终异常行总数", "value": len(outliers)},
]
report_rows.extend({"metric": f"{field}异常值数量", "value": count} for field, count in field_counts.items())
report = pd.DataFrame(report_rows)

summary.to_csv(output_dir / "room_temperature_numeric_summary.csv", index=False, encoding="utf-8-sig")
bounds.to_csv(output_dir / "room_temperature_iqr_bounds.csv", index=False, encoding="utf-8-sig")
outliers.to_csv(output_dir / "room_temperature_iqr_outliers.csv", index=False, encoding="utf-8-sig")
report.to_csv(output_dir / "room_temperature_iqr_report.csv", index=False, encoding="utf-8-sig")
print(bounds.to_string(index=False))
print("最终异常行总数：", len(outliers))
