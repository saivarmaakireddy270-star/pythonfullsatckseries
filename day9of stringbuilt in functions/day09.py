'''
s="raju"
print(s)
print(len(s))
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.casefold())
print(s.center(10,"*"))
print(s.ljust(5,"-"))
print(s.zfill(8))
print(s.find("5"))
print(s.rfind("3"))
print(s.count("r"))
print(s.startswith("r"))
print(s.endswith("j"))
print(s.split("," ))
print(s.rsplit(","))
print(s.rsplit(","  '1'))
print(s)
d="rani raju"
print(d)
print(d)
print(d.join(["raju", "rani"]))
'''
'''
house_number = int(input("enter the house number"))
water_consumed =float(input("enter the water consumed")) 
print(f"House: {house_number} | Water: {water_consumed}L")
'''
'''
1.Q A website wants all usernames to be stored in lowercase without leading or trailing spaces.

Task:

Read a username.

Remove extra spaces.

Convert it to lowercase.
'''
'''
username=input("enter the username")
print(username.lower()) 
print(username.strip())
'''
'''
#A company wants to check whether an email address belongs to Gmail.
email=input("enter the email address")
print(email.endswith("@gmail.com"))
print(email) 
'''
'''
#. Password Strength Checker
#A website accepts passwords only if they contain at least one uppercase letter.
credentials=input("enter the password")
if credentials==credentials.title():
    print("valid")
else:
    print("invalid")
'''
#4Student Report Card
#A school wants to display student information neatly.
name=input("enter the student name")
a=int(input("enter the marks of maths"))
b=int(input("enter the marks of telugusai"))
c=int(input("enter the marks of social"))
totalmarks=a+b+c
average=totalmarks/3
print(totalmarks)
print(average)



