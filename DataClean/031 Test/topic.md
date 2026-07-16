训练内容  
异常值进阶训练第 1 级：理解 Z-score，并与 IQR 对比，练习三种处理策略。  
训练成功  
能生成两种检测方法的对比，以及删除、截断、替换三类可复核的处理结果。

现有一份 元件长度 数据 component_length.csv，共 220 行，数值字段为 length。

任务要求：  
计算各字段均值和总体标准差，使用 |Z-score|>3 检测异常值，同时使用 IQR 方法检测异常值并比较两种方法。  
保存 Z-score 与 IQR 边界及异常数量对比为 component_length_outlier_detection_comparison.csv，并保存 Z-score 异常行为 component_length_zscore_outliers.csv。  
分别使用删除、上下限截断、字段中位数替换三种方式处理 Z-score 异常值，保存为 component_length_clean_delete.csv、component_length_clean_clip.csv、component_length_clean_replace.csv。  
生成 component_length_treatment_comparison.csv，比较行数、修改值数量和数据保留程度。
