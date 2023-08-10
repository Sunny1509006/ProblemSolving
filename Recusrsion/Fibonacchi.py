def Fib(n: int):
    if n <=1:
        return n 
    return Fib(n-1) + Fib(n-2)


if __name__ == '__main__':
    n = int(input("Enter the number: "))

    result = Fib(n)
    print(result)
