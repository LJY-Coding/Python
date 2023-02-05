class User:
    def __init__(self, data):
        self.f_name = data["f_name"]
        self.l_name = data["l_name"]
        self.email = data["email"]
        self.passwd = data["password"]

    def getInfo(self):
        print(self.f_name)
        return self