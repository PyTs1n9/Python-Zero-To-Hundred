训练内容  
隐私数据识别与掩码脱敏第 5 级：识别敏感字段并完成全字段与部分掩码。  
训练成功  
能在隐藏敏感信息的同时保持数据结构和非敏感分析字段完全不变。

现有一份 访客信息掩码 数据 visitors_private.csv，共 180 行。敏感字段为 name、phone；age、salary、city 用于后续统计，不得修改。

任务一：将敏感字段全部字符替换为等长星号，保存为 visitors_masked_full.csv。  
任务二：完成部分掩码：name 保留第一个字符，其余替换为星号；phone 保留前 3 位和后 4 位，保存为 visitors_masked_partial.csv。  
任务三：检查两种结果的行列数、敏感字段是否发生变化、非敏感字段是否与原始数据完全一致，保存为 visitors_mask_validation_report.csv。  
读取 phone 和 id_card 时应指定字符串类型；保存 CSV 时不得产生多余索引列。
