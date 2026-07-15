## 088 turtle 模拟钟面

使用 `turtle` 库绘制一个半径为 `radius` 的模拟钟面，包括外圆、12 个刻度和时针、分针。

给定小时 `hour` 和分钟 `minute`。`12` 点方向为 `0` 度，指针顺时针旋转；时针位置必须随分钟连续变化。

#### 示例 1：

> 输入：radius = 150, hour = 3, minute = 0
>
> 输出：分针指向 12，时针指向 3

#### 示例 2：

> 输入：radius = 150, hour = 6, minute = 30
>
> 输出：分针指向 6，时针位于 6 与 7 的正中间

#### 提示：

- `50 <= radius <= 300`
- `0 <= hour <= 23`，`0 <= minute <= 59`
- 分针角度为 `minute × 6`，时针角度为 `(hour % 12) × 30 + minute × 0.5`
- 使用 `penup()`、`pendown()`、`goto()`、`setheading()` 和 `circle()`

