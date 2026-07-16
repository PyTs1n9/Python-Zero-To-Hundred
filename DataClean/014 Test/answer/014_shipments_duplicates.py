import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
data_path = base_dir / "data" / "shipments_dirty.csv"
output_dir = base_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_path, dtype={"shipment_id": str, "phone": str})

# duplicated() 默认比较所有字段，keep=False 可统计重复组中的全部记录。
full_duplicate_extra = int(df.duplicated().sum())
full_duplicate_records = int(df.duplicated(keep=False).sum())
no_full = df.drop_duplicates(keep="first").copy()

# 关键字段重复统计在删除完全重复后进行，避免同一问题被重复计数。
key_duplicate_records = int(no_full.duplicated(subset=["shipment_id"], keep=False).sum())
clean_key = no_full.drop_duplicates(subset=["shipment_id"], keep="first").copy()

no_full.to_csv(output_dir / "shipments_no_full_duplicates.csv", index=False, encoding="utf-8-sig")
clean_key.to_csv(output_dir / "shipments_clean_keep_first.csv", index=False, encoding="utf-8-sig")

final_rows = len(clean_normalized) if "clean_normalized" in locals() else len(clean_key)
report = pd.DataFrame([
    {"metric": "原始数据行数", "value": len(df)},
    {"metric": "原始数据列数", "value": df.shape[1]},
    {"metric": "完全重复的多余行数量", "value": full_duplicate_extra},
    {"metric": "完全重复组涉及记录数量", "value": full_duplicate_records},
    {"metric": "删除完全重复后的行数", "value": len(no_full)},
    {"metric": "shipment_id重复组涉及记录数量", "value": key_duplicate_records},
    {"metric": "按shipment_id保留第一条后的行数", "value": len(clean_key)},
    {"metric": "最终结果行数", "value": final_rows},
])
if "near_duplicate_records" in locals():
    report.loc[len(report)] = ["标准化后近似重复组涉及记录数量", near_duplicate_records]
report.to_csv(output_dir / "shipments_duplicate_report.csv", index=False, encoding="utf-8-sig")

print(report.to_string(index=False))
