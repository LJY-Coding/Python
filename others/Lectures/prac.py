from user2 import User

data = {
    "f_name": "",
    "l_name": "",
    "email": "bsmith@mail.com",
    "password": "1234556"
}


# Your validation
def is_valid(data):
    is_valid = True
    for key in data:
        if data[key] == "":
            print(f"You forgot to enter the information for {key}")
            is_valid = False
    return is_valid

        
if is_valid(data):
    print("All the values are validated")
    user1 = User(data)
    user1.getInfo()
else:
    print("Invalid data inputs")
