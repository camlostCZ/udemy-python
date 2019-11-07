'''
Udemy / Complete Python Bootcamp

Euler's Number
'''

def factorial(n):
    if n < 0:
        raise Exception("Number has to be >= 0")
    result = 1
    if n > 1:
        result = n * factorial(n - 1)
    return result


def compute_e(iter_count):
    result = 0
    for i in range(iter_count):
        result += 1 / factorial(i)
    return result

def main():
    for n in range(1, 33):
        eulers_num = compute_e(iter_count = n)
        print("Euler's number: {}  / (n = {})".format(eulers_num, n))

main()
