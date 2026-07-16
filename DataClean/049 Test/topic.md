训练内容  
CSV 清洗综合训练一第 9 级：串联缺失值填充、重复值删除、IQR 异常值截断和统计摘要。  
训练成功  
能搭建顺序正确、结果可追踪的完整清洗流程，并输出清洗数据与前后报告。

现有一份 建筑材料 数据 construction_materials_dirty.csv，共 420 行，字段包括 material_id、material_type、length、width、weight、strength、qualified，同时存在缺失值、完全重复行和异常值。

任务要求：  
读取数据并查看行列数、字段类型、缺失值数量和完全重复行数量。  
对 length、width、weight、strength 使用中位数填充，对 material_type、qualified 使用众数填充。  
删除完全重复行；对数值字段使用 IQR 上下限截断异常值，不删除整行。  
保存 IQR 边界为 construction_materials_iqr_bounds.csv，保存清洗结果为 construction_materials_clean.csv。  
分别保存清洗前后数值统计摘要，并生成 construction_materials_cleaning_report.csv，记录行数、缺失值、重复值和异常单元格处理数量的前后变化。
