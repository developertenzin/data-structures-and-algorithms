def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
user_input = int(input("Enter the nth fibonacci number you want: "))
print(fib(user_input))
