"""093 PyInstaller 命令生成。"""


def build_command(script, one_file=False, windowed=False, icon=None):
    """按固定顺序生成 PyInstaller 命令参数列表。"""
    command = ["pyinstaller"]
    if one_file:
        command.append("--onefile")
    if windowed:
        command.append("--windowed")
    if icon:
        command.extend(["--icon", icon])
    command.append(script)
    return command


if __name__ == "__main__":
    print(build_command("main.py", one_file=True, windowed=True, icon="app.ico"))
