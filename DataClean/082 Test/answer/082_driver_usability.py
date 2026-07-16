import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "driver_private.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

numeric_fields = ['age', 'work_years', 'monthly_mileage']
df = pd.read_csv(data_path, dtype={"phone": str})

def mask_name(value):
    text = str(value)
    return text[:1] + "*" * max(len(text) - 1, 0)

def mask_phone(value):
    text = str(value)
    return text[:3] + "*" * max(len(text) - 7, 0) + text[-4:]

masked = df.copy()
masked["name"] = masked["name"].map(mask_name)
masked["phone"] = masked["phone"].map(mask_phone)

# 对比均值与样本标准差，正确脱敏时差值应为 0。
before_mean = df[numeric_fields].mean()
after_mean = masked[numeric_fields].mean()
before_std = df[numeric_fields].std()
after_std = masked[numeric_fields].std()
stats = pd.DataFrame({
    "field": numeric_fields,
    "mean_before": before_mean.values,
    "mean_after": after_mean.values,
    "mean_difference": (after_mean - before_mean).values,
    "std_before": before_std.values,
    "std_after": after_std.values,
    "std_difference": (after_std - before_std).values,
})

pearson_before = df[numeric_fields].corr(method="pearson")
pearson_after = masked[numeric_fields].corr(method="pearson")
pearson_difference = pearson_after - pearson_before

def save_heatmap(matrix, title, filename):
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_dir / filename, dpi=160)
    plt.close()

save_heatmap(pearson_before, "Pearson Correlation Before Masking", "driver_pearson_before_heatmap.png")
save_heatmap(pearson_after, "Pearson Correlation After Masking", "driver_pearson_after_heatmap.png")

max_mean_diff = float(stats["mean_difference"].abs().max())
max_std_diff = float(stats["std_difference"].abs().max())
max_corr_diff = float(pearson_difference.abs().to_numpy().max())
numeric_unchanged = masked[numeric_fields].equals(df[numeric_fields])
passed = numeric_unchanged and max_mean_diff < 1e-12 and max_std_diff < 1e-12 and max_corr_diff < 1e-12
report = pd.DataFrame([
    {"metric": "原始数据行数", "value": len(df)},
    {"metric": "脱敏后数据行数", "value": len(masked)},
    {"metric": "数值字段完全一致", "value": numeric_unchanged},
    {"metric": "均值最大绝对差", "value": max_mean_diff},
    {"metric": "标准差最大绝对差", "value": max_std_diff},
    {"metric": "Pearson相关系数最大绝对差", "value": max_corr_diff},
    {"metric": "脱敏后数据可用性验证结论", "value": "通过" if passed else "未通过"},
])

masked.to_csv(output_dir / "driver_masked.csv", index=False, encoding="utf-8-sig")
stats.to_csv(output_dir / "driver_stats_comparison.csv", index=False, encoding="utf-8-sig")
pearson_before.to_csv(output_dir / "driver_pearson_before.csv", encoding="utf-8-sig")
pearson_after.to_csv(output_dir / "driver_pearson_after.csv", encoding="utf-8-sig")
pearson_difference.to_csv(output_dir / "driver_pearson_difference.csv", encoding="utf-8-sig")
report.to_csv(output_dir / "driver_usability_report.csv", index=False, encoding="utf-8-sig")
print(report.to_string(index=False))
