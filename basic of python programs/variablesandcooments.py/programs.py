"""
Ravi has a fruit shop. Every morning, he prepares two baskets: one with apples and another with bananas. However, one day his little brother mischievously swapped the fruits. Ravi now wants to swap them back to their original baskets using Python.

You are to write a program that accepts the number of apples and bananas (currently misplaced), and then swaps the values so that apples go to the apple basket and bananas to the banana basket.

Your task is to:
Take the current count of apples and bananas as input.
Swap the values using variable swapping.
Print the final count of apples and bananas in their correct baskets.

Input Format:
Two integers, the first indicating the number of apples in the banana basket, the second indicating the number of bananas in the apple basket.

Output Format:
Two integers in a single line separated by a space: the corrected number of apples in the apple basket and bananas in the banana basket.
"""
"""
apples=int(input("enter the number of apples "))
bananas=int (input("enter the number of bananas "))
apples,bananas=bananas,apples
print(apples,bananas)
"""
"""
Help Anaya write a program that correctly reorders the numbers using multiple assignment.

Input Format:
Three integers provided on three separate lines — the numbers as they were shown to the player in sequence.

Output Format:
Three integers in one line, space-separated — reordered in the intended memory order (second, third, first).
"""
"""
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
n1,n2,n3=n2,n3,n1
print(n1,n2,n3)
"""
"""
ch=input("enter the character")
vowels="aeiouAEIOU"
if ch in vowels:
    print("vowels")
else:
    print("consonant")
    """
"""
year=int(input("enter the year"))
if  year%100==0:
    print("century year")
else:
    print("not a century year")
"""
"""
n=int(input("enter the number"))
if n%1==0 and n%n==0:
    print("prime number")
else:
    print("not a prime number")
    """
"""
str=input("enter the string")
if str==str[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

"""
"""
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
difference=n1-n2
if difference>0:
    print("difference is positive")
    if difference==0:
        print("difference is zero")
else:
    print("difference is negative")
    
"""
"""
temp=int(input("enter the temperature"))
choice=input("enter the choice in c or f")
if choice=="c":
    fahrenheit=(temp*9/5)+32
    print("temperature in fahrenheit is",fahrenheit)
else:
    celsius=(temp-32)*5/9
    print("temperature in celsius is",celsius)
    """
"""
n=int(input("enter the number"))
i=1
while i<=n:
    print(i)
    i+=1
    """
"""
n=int(input("number"))
g=int(input("guess number"))
i=0
while i<=n:
    if g==n:
        print("you guessed the number")
        break
    else:
        print("try again")
        g=int(input("guess number"))
    i+=1
"""
"""
n=int(input("enter the number"))
fact=1
i=1
while i<=n:
    fact=fact * i
    i+=1
print("factorial =",fact)
"""
n=int(input("enter the number"))
for i in range(1,n+1):
    print(i)
    i+=1

