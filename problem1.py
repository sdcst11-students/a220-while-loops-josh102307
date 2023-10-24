##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""


tries = 0
while tries != 3:

    user = input("username: ")
    pas = input("password: ")
    if user != "admin" and pas != "12345":
        tries + 1
        print("access denied")
    elif user == "admin" and pas == "12345":
        print("Access Granted")
        
else:
    if tries = 3:
    print("Too mant tries, Try again later")
    break      
