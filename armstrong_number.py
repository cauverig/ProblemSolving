"""
Given a number x, determine whether the given number is Armstrong number or not.
A positive integer of n digits is called an Armstrong number of order n
(order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
"""


def is_armstrong(number):
    n = len(str(number))

    sum = 0
    temp_numb = number
    while temp_numb != 0:
        i = temp_numb % 10
        sum += pow(i, n)
        temp_numb = temp_numb // 10

    if sum == number:
        print("The given number is an armstrong number")
    else:
        print("The given number is not an armstrong number")


is_armstrong(1634)