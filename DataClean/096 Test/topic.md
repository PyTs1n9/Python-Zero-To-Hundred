训练内容  
隐私脱敏综合训练第 6 级：整合掩码、哈希、一致性检查、统计验证、图表和说明报告。  
训练成功  
能按比赛提交思路生成四套脱敏数据、验证文件、热力图和完整分析报告。

现有一份模拟 教育客户 数据 education_clients_private.csv，共 480 行。name、phone、id_card 为敏感字段；age、income、course_cost、completion_flag 为统计分析字段。数据均为随机模拟，不对应真实个人。

任务要求：  
完成部分掩码、全字段掩码、SHA-256 和 MD5 四套脱敏结果。  
验证重复原始值的同值同哈希特性及摘要长度，保存 education_clients_hash_consistency_report.csv。  
对原始数据和四种脱敏结果计算数值字段均值、标准差及差值，保存 education_clients_stats_comparison.csv。  
比较原始数据与部分掩码数据的 Pearson 相关矩阵，保存前后矩阵并绘制两张 -1 至 1 范围的热力图。  
生成 education_clients_privacy_validation_report.csv 和 education_clients_privacy_analysis_report.md，比较隐私保护能力、统计可用性、SHA-256 与 MD5 安全性及无盐哈希风险。
