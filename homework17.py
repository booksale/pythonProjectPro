#Task1
def sequence(n):
    p = 1
    for i in range(1, n + 1):
        p *= 2
        yield p

for i in sequence(10):
    print(i)

#Task2
def new_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for start in new_range(1, 10, 2):
    print(start)

#Task3
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        return True

def prime_number(n):
    for i in range(n + 1):
        if is_prime(i):
            yield i

for i in prime_number(100):
    print(i)

# Task4
n = 10
lst = [i ** 2 for i in range(2, n + 1)]
print(lst)
#
n = 10
x = (i ** 2 for i in range(2, n + 1))
print(list(x))

#Task5
def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

x = fibonacci()
for i in range(10):
    print(next(x))

#Task6
from datetime import datetime, timedelta

def date(start, end):
    current_date = start
    while current_date <= end:
        yield current_date
        current_date += timedelta(days=1)

start = datetime(2024, 3, 1)
end = datetime(2024, 3, 10)

for date in date(start, end):
    print(date.strftime('%Y-%m-%d'))

