def Fib(n: int, memo={}):

    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = Fib(n-1, memo) + Fib(n-2, memo)

    return memo[n]


if __name__ == "__main__":

    n = int(input("Enter the number: "))

    result = Fib(n)

    print(result)
