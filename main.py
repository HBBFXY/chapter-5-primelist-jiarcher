def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""
    
    # 使用埃拉托斯特尼筛法
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    
    # 筛选质数
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 标记i的所有倍数为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集质数并格式化为字符串
    primes = [str(i) for i in range(2, N) if is_prime[i]]
    return " ".join(primes)

# 测试代码
if __name__ == "__main__":
    # 测试不同输入
    test_values = [10, 20, 30, 50, 2, 1, 100]
    
    for n in test_values:
        result = PrimeList(n)
        print(f"小于 {n} 的质数: {result}")
        print(f"输出长度: {len(result)}")
        print("-" * 30)
