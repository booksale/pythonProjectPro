#Task1

sp = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sps(func):
    def wrapper():
        total = 0
        for i in sp:
            total += func(i)
        return total
    return wrapper

@sps
def customer(x):
    return x

print(customer())

#Task2
def w_file(func):
    def wrapper():
        with open("file.txt", "w") as file:
            result = func()
            file.write(str(result))
    return wrapper

@w_file
def calculation():
    return 1 + 2

calculation()

#Task4

def limit_calls(max_calls):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.calls < max_calls:
                wrapper.calls += 1
                return func(*args, **kwargs)
            else:
                print("Достигнуто максимальное количество вызовов.")
        wrapper.calls = 0
        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print("Вызов функции")

some_function()
some_function()
some_function()
some_function()

#Task5

def cache_results(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper

@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(10))