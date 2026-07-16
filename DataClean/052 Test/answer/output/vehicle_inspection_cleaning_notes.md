# 数据清洗说明

1. 原始数据：vehicle_inspection_dirty.csv，共 380 行。
2. 类型转换：提取数值部分，无效内容转为 NaN。
3. 缺失值：数值字段使用中位数，risk_level 使用众数。
4. 重复值：删除完全重复行，保留首次出现记录。
5. 异常值：使用 IQR 上下限截断，共处理 32 个单元格。
6. 标准化：对 vehicle_age, mileage_km, emission 使用 StandardScaler。
7. 结果：清洗后 372 行，缺失值 0 个。
