import pandas as pd
from pathlib import Path

data_dir = Path("data")
output_dir = Path("output")
data_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

student_scores_path = data_dir / "student_scores.csv"

df = pd.read_csv(student_scores_path)

print(f"行列数:{df.shape}")
print(f"前五行:\n{df.head()}")
print(f"每个字段的数据类型:\n{df.dtypes}")
print(f"每个字段缺失值的数量:\n{df.isnull().sum()}")

df_save = df.copy().head(5)
data_head_path = output_dir / "data_head.csv"
df_save.to_csv(data_head_path, index=False, encoding="utf-8-sig")
data_overview_path = output_dir / "data_overview.txt"
with open(data_overview_path, "w", encoding="utf-8-sig") as f:
	f.write(f"{df.describe()}")
