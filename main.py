def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理边界情况
    if N <= 2:
        return ""
    
    # 使用更高效的埃拉托斯特尼筛法实现
    if N < 2:
        return ""
    
    # 初始化标记数组
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    
    # 优化筛法：只标记奇数的倍数
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 从i*i开始标记，步长为i
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集质数 - 使用生成器表达式提高内存效率
    primes = (str(i) for i in range(2, N) if is_prime[i])
    
    # 返回结果，确保末尾无空格
    return " ".join(primes)

# 额外测试大数情况
if __name__ == "__main__":
    # 测试N=10000
    result_10000 = PrimeList(10000)
    primes_list = result_10000.split()
    
    print(f"N=10000时找到 {len(primes_list)} 个质数")
    print(f"前5个质数: {primes_list[:5]}")
    print(f"最后5个质数: {primes_list[-5:]}")
    
    # 验证不包含1
    if "1" in primes_list:
        print("错误: 输出包含1")
    else:
        print("正确: 输出不包含1")
    
    # 验证格式
    if result_10000.startswith(" ") or result_10000.endswith(" "):
        print("错误: 输出格式有空格问题")
    else:
        print("正确: 输出格式正确")
