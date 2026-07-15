## 093 PyInstaller 命令生成

实现函数 `build_command(script, one_file=False, windowed=False, icon=None)`，生成 PyInstaller 打包命令的参数列表。

列表以 `"pyinstaller"` 开头；`one_file` 为真时加入 `"--onefile"`，`windowed` 为真时加入 `"--windowed"`，`icon` 非空时依次加入 `"--icon"` 和图标路径；脚本路径始终放在最后。

#### 示例 1：

> 输入：script = "main.py", one_file = true, windowed = true, icon = "app.ico"
>
> 输出：["pyinstaller", "--onefile", "--windowed", "--icon", "app.ico", "main.py"]

#### 示例 2：

> 输入：script = "tool.py"
>
> 输出：["pyinstaller", "tool.py"]

#### 提示：

- 不要真正执行系统命令，只返回参数列表
- 练习默认参数以及 Python 计算生态中的程序打包工具

