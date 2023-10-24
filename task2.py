#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""




correctUser = False

while not correctUser:
    user = input("username: ")
    pas = input("password: ")
    if user != "admin" and pas != "12345":
        print("access denied")
    else:
        correctUser = True
        print("Access Granted")
        break
         
