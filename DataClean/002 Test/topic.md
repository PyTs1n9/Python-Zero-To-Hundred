训练内容  
缺失值处理专项第 1 级：练习均值、中位数、众数和固定值填充，并观察统计量变化。  
训练成功  
能生成三份填充结果、均值对比表和缺失值处理报告，且所有结果均无目标字段缺失值。

现有一份 商品价格缺失值 数据 product_price_missing.csv，共 100 行，字段包括 record_id、unit_price。

任务要求：  
使用 pandas 读取 product_price_missing.csv，输出行数、列数和每个字段的缺失值数量。  
对数值字段 unit_price 分别完成均值填充、中位数填充以及“众数或固定值”填充。  
第三种方式中，第一个数值字段使用众数，其余数值字段使用固定值；分类字段使用“未知”填充。  
分别保存为 product_price_filled_mean.csv、product_price_filled_median.csv、product_price_filled_mode_fixed.csv。  
统计填充前后三种结果中各数值字段的均值，保存为 product_price_fill_mean_comparison.csv。  
将行列数和填充前后缺失值总数保存为 product_price_missing_report.csv，保存 CSV 时不得产生多余索引列。
