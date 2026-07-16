训练内容  
脱敏可用性验证第 1 级：验证掩码脱敏不会破坏数值统计、分布和相关结构。  
训练成功  
能用统计表、相关矩阵、热力图和结论报告证明脱敏后数据仍可用于分析。

现有一份 教师数据 teacher_private.csv，共 200 行。name 和 phone 为敏感字段；age、work_years、monthly_salary 为统计分析字段。

任务要求：  
对 name 和 phone 进行部分掩码，保存为 teacher_masked.csv，且数值字段不得修改。  
计算脱敏前后数值字段的均值、标准差及差值，保存为 teacher_stats_comparison.csv。  
计算脱敏前后 Pearson 相关性矩阵及差值，分别保存 before、after、difference 三份 CSV。  
使用 seaborn.heatmap 绘制脱敏前后热力图，显示系数并固定颜色范围为 -1 到 1。  
生成 teacher_usability_report.csv，记录行数、数值字段一致性以及均值、标准差、相关系数的最大绝对差。
