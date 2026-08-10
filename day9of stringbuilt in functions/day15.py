#forloop,nested for loop,jumping statements.
# Print numbers from 1 to 5 using a for loop.
#sol:
for i in range(1,6):
    print(i)
#Print even numbers between 1 and 10
for i in range(1,11):
        if i % 2==0:
           print(i)    
#Print multiplication table of a number
n = int(input("enter the number"))
for i in range (0,100):
        result = n *i    
        print(n, "*", i , result)
# Print all characters of a string
c = input("enter string")
for i in range(len(c)):
            print("character:",c[i])
#nested loops
c = input("Enter string: ")
for i in range(len(c)):
    for vowel in "aeiou":
        if c[i] == vowel:
            print("Vowel:", c[i])
#Finding pairs
for i in range(1,4):
      for j in range(1,4):
            print(i,j)


        
      

        
        
