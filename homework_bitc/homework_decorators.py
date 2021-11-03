import json


class User:

    def __init__(self, username, password, email, age, phone):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.phone = phone


class PyRequest:

    def __init__(self, headers=[], authorization=None, body=None, user=None):
        self.headers = headers
        self.authorization = authorization
        self.body = body
        self.user = user

    def local_login(self, username, password):
        with open("users.json", "r") as json_file:
            data = json.load(json_file)
        username_list = [i["username"] for i in data]
        try:
            user_index = username_list.index(username)
            if data[user_index]["password"] == password:
                self.user = User(data[user_index]["username"], data[user_index]["password"], data[user_index]["email"],
                                 data[user_index]["age"], data[user_index]["phone"])
            else:
                print("Wrong password!")
        except ValueError:
            self.user = None
            print("There is no user with such username!")


def login_required(func: callable):

    def user_check(obj_):
        if isinstance(obj_.user, User):
            return func(obj_)
        else:
            raise Exception("401 Unauthorized request error")

    return user_check


@login_required
def get_user_info(request: PyRequest):
    print(f"Username: {request.user.username}\nPassword: {request.user.username}\nEmail: {request.user.username}\n"
          f"Age: {request.user.username}\nPhone: {request.user.username}")


# JSON file
user_list = []


for i in range(10):
    user_list.append({
        "username": "username_" + str(i),
        "password": "password_" + str(i),
        "email": "email_" + str(i),
        "age": "age_" + str(i),
        "phone": "phone_" + str(i),
        })


with open("users.json", "w") as json_file:
    json.dump(user_list, json_file, indent=4)


# Implementation

test = PyRequest()

given_username = input("Enter the username!\n")
given_password = input("Enter the password!\n")
test.local_login(given_username, given_password)

get_user_info(test)
