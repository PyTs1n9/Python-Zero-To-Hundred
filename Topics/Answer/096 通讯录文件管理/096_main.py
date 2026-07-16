"""096 通讯录文件管理。"""

import json
from pathlib import Path


def manage_contacts(json_path, operations):
    """执行添加、删除和查询操作，并把结果写回 JSON。"""
    path = Path(json_path)
    if path.exists():
        with open(path, "r", encoding="utf-8") as file:
            contacts = json.load(file)
    else:
        contacts = {}

    query_results = []
    for operation in operations:
        action = operation[0]
        if action == "add" and len(operation) == 3:
            _, name, phone = operation
            contacts[name] = phone
        elif action == "delete" and len(operation) == 2:
            _, name = operation
            contacts.pop(name, None)
        elif action == "find" and len(operation) == 2:
            _, name = operation
            query_results.append(contacts.get(name))

    contacts = dict(sorted(contacts.items()))
    with open(path, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)
    return query_results


if __name__ == "__main__":
    sample = Path(__file__).with_name("contacts.json")
    actions = [
        ("add", "Bob", "12345"),
        ("find", "Bob"),
        ("delete", "Alice"),
        ("find", "Alice"),
    ]
    print(manage_contacts(sample, actions))
