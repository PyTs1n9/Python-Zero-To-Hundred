import pandas as pd
from pathlib import Path

data_dir = Path("data")
output_dir = Path("output")
data_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

product_price_missing_path = data_dir / "product_price_missing.csv"
df = pd.read_csv(product_price_missing_path)
print(f"行列数:{df.shape}")
print(f"每个字段的缺失值数量:\n{df.isnull().sum()}")

numeric_fields = ["unit_price"]

df_mean = df.copy()
df_median = df.copy()
df_mode = df.copy()
# 均值
for field in numeric_fields:
	df_mean[field] = df_mean[field].fillna(df_mean[field].mean())
# 中位数
for field in numeric_fields:
	df_median[field] = df_median[field].fillna(df_median[field].median())
# 众数
for field in numeric_fields:
	df_mode[field] = df_mode[field].fillna(df_mode[field].mode())
