import time
def time_function(func, *args, **kwargs):
    """
    测试函数的执行时间。

    :param func: 要测试的函数
    :param args: 传递给函数的位置参数
    :param kwargs: 传递给函数的关键字参数
    :return: 函数的返回值和执行时间
    """
    start_time = time.time()  # 记录开始时间
    result = func(*args, **kwargs)  # 调用函数
    end_time = time.time()  # 记录结束时间

    execution_time = end_time - start_time  # 计算执行时间
    return result, execution_time


# 示例用法
def example_function(n):
    # 模拟一个耗时操作
    total = 0
    for i in range(n):
        total += i
    return total

# 测试 example_function 的执行时间
result, exec_time = time_function(example_function, 1000000)
print(f"结果: {result}, 执行时间: {exec_time:.6f}秒")