"""070 目录文件分类。"""

import os
import tempfile
from pathlib import Path


def count_extensions(directory):
    """统计目录直接子文件的扩展名，不进入子目录。"""
    counts = {}
    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)
        if os.path.isfile(full_path):
            extension = os.path.splitext(name)[1].lower()
            counts[extension] = counts.get(extension, 0) + 1
    return {extension: counts[extension] for extension in sorted(counts)}


if __name__ == "__main__":
    # 临时目录会在示例运行结束后自动清理。
    with tempfile.TemporaryDirectory() as temporary_folder:
        for name in ["a.py", "b.PY", "readme.md", "LICENSE"]:
            Path(temporary_folder, name).touch()
        print(count_extensions(temporary_folder))
