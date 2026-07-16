训练内容  
重复值处理专项第 9 级：区分完全重复、关键字段重复和近似重复。  
训练成功  
能使用 duplicated()、drop_duplicates() 生成分阶段去重结果及数量变化报告。

现有一份 会员近似重复 数据 members_near_duplicates.csv，共 265 行、6 个字段：member_id、customer_name、phone、city、amount、status。

任务要求：  
使用 pandas 读取 members_near_duplicates.csv，输出原始行数和列数。  
使用 duplicated() 统计完全重复行数量，并删除完全重复行，保存为 members_no_full_duplicates.csv。  
统计关键字段 member_id 的重复记录数量；在删除完全重复行的基础上按 member_id 去重并保留第一条，保存为 members_clean_keep_first.csv。  
此外，将 customer_name 去除首尾空格，将 phone 去除非数字字符，以两者的标准化结果识别近似重复；保留第一条记录，保存为 members_clean_normalized.csv。  
生成 members_duplicate_report.csv，至少记录原始行列数、完全重复行数量、删除完全重复后的行数、关键字段重复记录数量和最终行数。
