'''
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares
of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.
'''

MAX_ITERATIONS = 500

def is_happynumber(number, max_iters):
    result = False
    total = sum([int(x) ** 2 for x in str(number)])
    result = total == 1
    if not result and max_iters > 0:
        result = is_happynumber(total, max_iters - 1)
    return result

def main():
    #number = int(input("Enter an integer value > 0: "))
    lst_happy = []
    for number in range(1, 300):
        if is_happynumber(number, MAX_ITERATIONS):
            lst_happy.append(number)

    s = ', '.join([str(x) for x in lst_happy])
    print("Happy numbers:\n{}".format(s))

#main()

print(is_happynumber(19, 100))
