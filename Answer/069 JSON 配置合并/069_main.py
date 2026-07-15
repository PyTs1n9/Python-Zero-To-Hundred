"""069 JSON 配置合并。"""

import copy
import json
from pathlib import Path


def deep_merge(default, user):
    """递归合并两个字典，不修改输入字典。"""
    result = copy.deepcopy(default)
    for key, user_value in user.items():
        if key in result and isinstance(result[key], dict) and isinstance(user_value, dict):
            result[key] = deep_merge(result[key], user_value)
        else:
            result[key] = copy.deepcopy(user_value)
    return result


def merge_json_configs(default_path, user_path):
    """读取两份 JSON 配置并返回合并结果。"""
    with open(default_path, "r", encoding="utf-8") as file:
        default = json.load(file)
    with open(user_path, "r", encoding="utf-8") as file:
        user = json.load(file)
    return deep_merge(default, user)


if __name__ == "__main__":
    folder = Path(__file__).parent
    print(merge_json_configs(folder / "default.json", folder / "user.json"))
