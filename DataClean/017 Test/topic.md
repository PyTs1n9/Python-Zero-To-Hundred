训练内容  
重复值处理专项第 7 级：区分完全重复、关键字段重复。  
训练成功  
能使用 duplicated()、drop_duplicates() 生成分阶段去重结果及数量变化报告。

现有一份 门诊预约 数据 medical_appointments_dirty.csv，共 240 行、6 个字段：appointment_id、user_id、product_id、event_time、amount、status。

任务要求：  
使用 pandas 读取 medical_appointments_dirty.csv，输出原始行数和列数。  
使用 duplicated() 统计完全重复行数量，并删除完全重复行，保存为 medical_appointments_no_full_duplicates.csv。  
统计关键字段 appointment_id 的重复记录数量；在删除完全重复行的基础上按 appointment_id 去重并保留第一条，保存为 medical_appointments_clean_keep_first.csv。  
生成 medical_appointments_duplicate_report.csv，至少记录原始行列数、完全重复行数量、删除完全重复后的行数、关键字段重复记录数量和最终行数。
