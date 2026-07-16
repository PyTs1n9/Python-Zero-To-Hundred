训练内容  
隐私数据识别与掩码脱敏第 4 级：识别敏感字段并完成全字段与部分掩码。  
训练成功  
能在隐藏敏感信息的同时保持数据结构和非敏感分析字段完全不变。

现有一份 邮箱掩码 数据 emails_private.csv，共 165 行。敏感字段为 email；age、salary、city 用于后续统计，不得修改。

任务一：将敏感字段全部字符替换为等长星号，保存为 emails_masked_full.csv。  
任务二：完成部分掩码：email 保留账号前 2 个字符和完整域名，保存为 emails_masked_partial.csv。  
任务三：检查两种结果的行列数、敏感字段是否发生变化、非敏感字段是否与原始数据完全一致，保存为 emails_mask_validation_report.csv。  
读取 phone 和 id_card 时应指定字符串类型；保存 CSV 时不得产生多余索引列。
