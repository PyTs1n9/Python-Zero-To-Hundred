训练内容  
CSV 清洗综合训练二第 10 级：加入单位清除、类型转换、标准化、字段选择和建模数据整理。  
训练成功  
能生成清洗数据、标准化数据、建模数据、统计验证报告和结构清晰的清洗说明。

现有一份 模拟体检 数据 medical_check_dirty.csv，共 540 行。数值字段 age、height_cm、weight_kg、blood_pressure、blood_sugar 中混有 岁、cm、kg、mmHg、mmol/L 等单位、空值和无法转换的文本。

任务要求：  
读取数据，统计原始行列数、字段类型、缺失值、带单位字符串、无法转换内容和完全重复行。  
去除单位并使用 to_numeric(errors='coerce') 完成类型转换；数值缺失值用中位数填充，risk_level 用众数填充。  
删除完全重复行；使用 IQR 对数值异常值执行上下限截断。  
保存清洗结果为 medical_check_clean.csv；使用 StandardScaler 标准化全部数值字段并保存为 medical_check_scaled.csv。  
选择数值字段与 risk_level 形成 medical_check_model_data.csv；保存标准化检查、清洗报告和比赛风格清洗说明。
