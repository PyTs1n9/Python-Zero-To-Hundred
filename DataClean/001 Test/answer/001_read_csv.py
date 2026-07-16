import pandas as pd
from pathlib import Path

# 使用脚本所在目录定位文件，避免因运行目录不同而找不到数据。
base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "student_scores.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# 读取数据并完成最基础的数据质量观察。
df = pd.read_csv(data_path, dtype={"student_id": str})
head = df.head(5)
missing = df.isna().sum()

print("行数：", df.shape[0])
print("列数：", df.shape[1])
print("前 5 行：\n", head)
print("字段类型：\n", df.dtypes)
print("缺失值数量：\n", missing)

# index=False 可以避免保存出多余的索引列。
head.to_csv(output_dir / "data_head.csv", index=False, encoding="utf-8-sig")
with open(output_dir / "data_overview.txt", "w", encoding="utf-8-sig") as file:
    file.write(f"行数：{df.shape[0]}\n")
    file.write(f"列数：{df.shape[1]}\n\n")
    file.write("字段名（数据类型）：\n")
    for column, dtype in df.dtypes.items():
        file.write(f"{column}（{dtype}）\n")
    file.write("\n缺失值数量：\n")
    file.write(missing.to_string())
    file.write("\n")
