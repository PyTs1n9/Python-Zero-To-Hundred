训练内容  
异常值基础训练第 3 级：使用描述性统计和 IQR 方法检测多字段异常值。  
训练成功  
能正确生成统计摘要、IQR 边界、异常行和检测报告。

现有一份 网络延迟 数据 network_latency.csv，共 210 行，检测字段为 latency_ms、packet_loss。

任务要求：  
使用 pandas 读取数据，计算检测字段的最大值、最小值、均值和中位数，保存为 network_latency_numeric_summary.csv。  
分别计算 Q1、Q3、IQR、下界 Q1-1.5×IQR、上界 Q3+1.5×IQR 和字段异常值数量，保存为 network_latency_iqr_bounds.csv。  
任意检测字段超出其上下界时，将整行判定为异常行，保存为 network_latency_iqr_outliers.csv。  
生成 network_latency_iqr_report.csv，记录原始行数、检测字段数量、各字段异常值数量及最终异常行总数。
