训练内容  
CSV 清洗综合训练二第 1 级：加入单位清除、类型转换、标准化、字段选择和建模数据整理。  
训练成功  
能生成清洗数据、标准化数据、建模数据、统计验证报告和结构清晰的清洗说明。

现有一份 学生健康 数据 student_health_dirty.csv，共 360 行。数值字段 age、height_cm、weight_kg 中混有 岁、cm、kg 等单位、空值和无法转换的文本。

任务要求：  
读取数据，统计原始行列数、字段类型、缺失值、带单位字符串、无法转换内容和完全重复行。  
去除单位并使用 to_numeric(errors='coerce') 完成类型转换；数值缺失值用中位数填充，risk_level 用众数填充。  
删除完全重复行；使用 IQR 对数值异常值执行上下限截断。  
保存清洗结果为 student_health_clean.csv；使用 StandardScaler 标准化全部数值字段并保存为 student_health_scaled.csv。  
选择数值字段与 risk_level 形成 student_health_model_data.csv；保存标准化检查、清洗报告和比赛风格清洗说明。
