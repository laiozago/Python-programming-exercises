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
factorial = int(input("Enter a number: "))

for i in range(1, factorial):
    factorial = factorial * i
print(factorial)

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
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such 
that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

"""
num = int(input("Enter a number: "))
mapa = dict()
for n in range(1, num+1):
    mapa[n]=n**2
print(mapa)
"""

"""
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""
"""
def ex_4():
    values = input("Enter some comma separated numbers : ")
    l = values.split(",")
    t = tuple(l)
    print(l)
    print(t)
    
ex_4()
"""

"""
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""
"""
class ex_5:
    def __init__(self):
        """
""" Initializes a new instance of the class.

        Parameters:
            self: The object itself.

        Return:
            None"""
"""
        self.s = ""
    def get_String(self):
        """
"""Get a string from the user.

        This method prompts the user to enter a string and stores it in the 's' attribute of the class.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None"""
"""
        self.s = input("Enter a string: ")
    def print_String(self):
        """
"""Print the string in uppercase."""
"""
        print(self.s.upper())

ex_5 = ex_5()
ex_5.get_String()
ex_5.print_String()
"""

"""
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
"""
import math
def ex_6():
    c = 50
    h = 30
    value = []
    items = [x for x in input("Enter values separated by comma: ").split(',')]
    for d in items:
        value.append(str(int(round(math.sqrt(2 * c * int(d) / h)))))
    print(",".join(value))
ex_6()
"""

"""
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1...,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

"""
"""

def ex_7():
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    z = [[i*j for i in range(y)] for j in range(x)]
    print(z)

ex_7()

"""

"""
### Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a 
comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""


def ex_8():
    words = [x for x in input("Enter values separated by comma: ").split(',')]
    words.sort()
    print(words)


"""
### Question 9
Level 2

Question
Write a program that accepts sequence of lines as input and prints the lines after making
all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""


def ex_9():
    frases = []
    while True:
        frase = str(input("Enter the frase, enter 'END' to finish: "))
        if frase == "END":
            break
        frases.append(frase.upper())
    for n in frases:
        print(n)


"""
### Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


def ex_10():
    words = [word for word in input("Enter a frase: ").split(" ")]
    words.sort()
    set(words)
    print(words)


"""
### Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

"""


def ex_11():
    num_bin = input("Enter a binary number: ")
    num_dec = int(num_bin, 2)
    if num_dec % 5 == 0:
        print(f"The number {num_bin} is divisible by 5")
    else:
        print(f"Not divisible")


ex_11()
