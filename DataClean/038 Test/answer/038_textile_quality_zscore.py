import numpy as np
import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "textile_quality.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

fields = ['width', 'weight', 'strength', 'defect_rate']
df = pd.read_csv(data_path)

# 使用总体标准差 ddof=0，与常见 Z-score 定义保持一致。
means = df[fields].mean()
stds = df[fields].std(ddof=0)
z_scores = (df[fields] - means) / stds
z_masks = z_scores.abs() > 3
z_any = z_masks.any(axis=1)

comparison_rows = []
iqr_masks = pd.DataFrame(False, index=df.index, columns=fields)
for field in fields:
    q1, q3 = df[field].quantile([0.25, 0.75])
    iqr = q3 - q1
    iqr_lower, iqr_upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    iqr_masks[field] = (df[field] < iqr_lower) | (df[field] > iqr_upper)
    comparison_rows.append({
        "field": field,
        "mean": means[field], "std": stds[field],
        "z_lower": means[field] - 3 * stds[field],
        "z_upper": means[field] + 3 * stds[field],
        "zscore_outlier_count": int(z_masks[field].sum()),
        "iqr_lower": iqr_lower, "iqr_upper": iqr_upper,
        "iqr_outlier_count": int(iqr_masks[field].sum()),
    })

# 方法一：删除任意字段出现异常的整行。
clean_delete = df.loc[~z_any].copy()

# 方法二：将每个字段截断到 mean ± 3×std 范围内。
clean_clip = df.copy()
for field in fields:
    clean_clip[field] = clean_clip[field].clip(means[field] - 3 * stds[field], means[field] + 3 * stds[field])

# 方法三：仅把异常单元格替换为该字段中位数，保留其他正常值。
clean_replace = df.copy()
for field in fields:
    clean_replace.loc[z_masks[field], field] = df[field].median()

treatment = pd.DataFrame([
    {"method": "原始数据", "row_count": len(df), "changed_value_count": 0, "retention_rate": 1.0},
    {"method": "删除法", "row_count": len(clean_delete), "changed_value_count": int(z_any.sum()), "retention_rate": len(clean_delete) / len(df)},
    {"method": "截断法", "row_count": len(clean_clip), "changed_value_count": int(z_masks.sum().sum()), "retention_rate": 1.0},
    {"method": "中位数替换法", "row_count": len(clean_replace), "changed_value_count": int(z_masks.sum().sum()), "retention_rate": 1.0},
])

pd.DataFrame(comparison_rows).to_csv(output_dir / "textile_quality_outlier_detection_comparison.csv", index=False, encoding="utf-8-sig")
df.loc[z_any].to_csv(output_dir / "textile_quality_zscore_outliers.csv", index=False, encoding="utf-8-sig")
clean_delete.to_csv(output_dir / "textile_quality_clean_delete.csv", index=False, encoding="utf-8-sig")
clean_clip.to_csv(output_dir / "textile_quality_clean_clip.csv", index=False, encoding="utf-8-sig")
clean_replace.to_csv(output_dir / "textile_quality_clean_replace.csv", index=False, encoding="utf-8-sig")
treatment.to_csv(output_dir / "textile_quality_treatment_comparison.csv", index=False, encoding="utf-8-sig")
print(treatment.to_string(index=False))
