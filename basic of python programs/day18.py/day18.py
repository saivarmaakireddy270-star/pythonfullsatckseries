'''
def number(n,even,odd):
          if n % 2 == 0:
                  print(even)
          else:
                  print(odd)

number(10,"even","odd")
'''
'''
def factorial(n):
    fact=1

    for i in range(1,n+1):
        fact = fact*i

    return fact    

print(factorial(5))
'''
'''
def prime(n):

    for i in range(2, n):
        if n % i == 0:
            print(n, "not a prime")
            break#for n numbers 
    else:
        print(n, "prime")


for n in range(10, 21):
    prime(n)
    '''
def prime(n):

    for i in range(2, n):
        if n % i == 0:
            print(n, "not a prime")
            return n
    else:
        print(n, "prime")
prime(10)
