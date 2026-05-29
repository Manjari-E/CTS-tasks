def login(user, pwd):
    if user.strip() == "" or pwd.strip() == "":
        return "Fields cannot be empty"

    if user == "admin":
        if pwd == "pass123":
            return "Login Successful"
        else:
            return "Wrong Password"
    else:
        return "Invalid Username"

user = "admin"
pwd = "pass123"

print(login(user, pwd))