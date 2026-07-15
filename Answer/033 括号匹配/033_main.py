"""033 括号匹配。"""


def brackets_are_valid(text):
    """使用列表模拟栈，判断括号闭合顺序是否正确。"""
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    for character in text:
        if character in "([{":
            stack.append(character)
        else:
            if not stack or stack.pop() != matching[character]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(brackets_are_valid("{[()]}"))
