训练内容  
重复值处理专项第 10 级：区分完全重复、关键字段重复。  
训练成功  
能使用 duplicated()、drop_duplicates() 生成分阶段去重结果及数量变化报告。

现有一份 订单重复值综合 数据 orders_dirty.csv，共 280 行、6 个字段：order_id、user_id、product_id、event_time、amount、status。

任务要求：  
使用 pandas 读取 orders_dirty.csv，输出原始行数和列数。  
使用 duplicated() 统计完全重复行数量，并删除完全重复行，保存为 orders_no_full_duplicates.csv。  
统计关键字段 order_id 的重复记录数量；在删除完全重复行的基础上按 order_id 去重并保留第一条，保存为 orders_clean_keep_first.csv。  
生成 orders_duplicate_report.csv，至少记录原始行列数、完全重复行数量、删除完全重复后的行数、关键字段重复记录数量和最终行数。
