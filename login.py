import time
while True:
    ans = input("Login or Register?: ")
    if ans == "L":
        name = True
        print("Please Provide Login Details")

        break
    if ans == "R":
      f= open ('accounts.txt', "a")
      user =input("username: ")
      passwd= input("password: ")
      f.write('\n'+ user + '|' + passwd + '\n')
      f.close()
    else:
        print("\n L for Login, R for Register\n")
user = input("Username: ")
passw = input("Password: ")
f = open("accounts.txt", "r")

line = f.readlines()
f.close()
us =[]
pwd = []
for i in line:
    a, b = i.strip('\n').split('|')
    us.append(a)
    pwd.append(b)

if user in us:
    id = us.index(user)

    if passw == pwd[id]:
        print("Login successful!")
else:
  print("Wrong username/password")

time.sleep(2.4)

