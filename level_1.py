"""
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
"""
numbers = []
for i in range (2000, 3201):
    if i % 7==0 and i%5 != 0:
        numbers.append(str(i))
else:
    print(','.join(numbers))
"""


"""
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
"""
fatorial = int(input("Enter a number: "))

for i in range(1, fatorial):
    fatorial = fatorial * i
print(fatorial)

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input("Enter a number: "))
print(fact(x))
"""

"""
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

