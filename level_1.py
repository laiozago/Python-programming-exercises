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
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""
"""
def ex_4():
    values = input("Enter some comma seprated numbers : ")
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

class ex_5:
    def __init__(self):
        """
        Initializes a new instance of the class.

        Parameters:
            self: The object itself.

        Return:
            None
        """
        self.s = ""
    def get_String(self):
        """
        Get a string from the user.

        This method prompts the user to enter a string and stores it in the 's' attribute of the class.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None
        """
        self.s = input("Enter a string: ")
    def print_String(self):
        """
        Print the string in uppercase.
        """
        print(self.s.upper())

ex_5 = ex_5()
ex_5.get_String()
ex_5.print_String()
