训练内容  
异常值进阶训练第 9 级：理解 Z-score，并与 IQR 对比，练习三种处理策略。  
训练成功  
能生成两种检测方法的对比，以及删除、截断、替换三类可复核的处理结果。

现有一份 精密零件 数据 precision_parts.csv，共 350 行，数值字段为 length、width、weight、hardness、defect_rate。

任务要求：  
计算各字段均值和总体标准差，使用 |Z-score|>3 检测异常值，同时使用 IQR 方法检测异常值并比较两种方法。  
保存 Z-score 与 IQR 边界及异常数量对比为 precision_parts_outlier_detection_comparison.csv，并保存 Z-score 异常行为 precision_parts_zscore_outliers.csv。  
分别使用删除、上下限截断、字段中位数替换三种方式处理 Z-score 异常值，保存为 precision_parts_clean_delete.csv、precision_parts_clean_clip.csv、precision_parts_clean_replace.csv。  
生成 precision_parts_treatment_comparison.csv，比较行数、修改值数量和数据保留程度。
