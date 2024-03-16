
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, entered_password,name):
        return self.password == entered_password  and self.username == name

    @staticmethod
    def register(username, password):
        return User(username, password)