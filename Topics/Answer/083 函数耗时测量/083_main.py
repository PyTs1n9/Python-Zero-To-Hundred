"""083 函数耗时测量。"""

import time


def measure(func, *args, **kwargs):
    """调用函数，并返回“函数结果、运行秒数”。"""
    start = time.perf_counter()
    # 如果 func 抛出异常，这里不会捕获，因此原异常会继续传递。
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    value, seconds = measure(sorted, [3, 1, 2], reverse=True)
    print(value)
    print(f"耗时：{seconds:.8f} 秒")
