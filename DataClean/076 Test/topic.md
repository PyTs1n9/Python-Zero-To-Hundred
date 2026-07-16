训练内容  
哈希脱敏专项第 6 级：实现 SHA-256 与 MD5，验证不可逆标识的稳定性和长度。  
训练成功  
能生成两套哈希数据、完成同值同哈希验证，并说明 MD5 与 SHA-256 的安全性差异。

现有一份 订阅用户哈希 数据 subscriber_hash_private.csv，共 280 行。敏感字段为 phone、id_card，其余字段必须保持不变。

任务要求：  
使用 hashlib.sha256 对敏感字段进行 UTF-8 编码后的十六进制哈希，保存为 subscriber_hash_hash_sha256.csv。  
使用 hashlib.md5 生成对应结果，保存为 subscriber_hash_hash_md5.csv。  
找出每个敏感字段中出现两次及以上的原始值，验证同值同哈希；检查 SHA-256 长度为 64、MD5 长度为 32。  
将重复值组数、两种算法的一致性与长度检查保存为 subscriber_hash_hash_consistency_report.csv，并生成算法安全性说明 subscriber_hash_hash_comparison.txt。
