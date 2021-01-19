class User:
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

    def say_hello(self):
        print(f"hello, I'm {self.name}!")

    # dunder_method(double_underscore)
    # print를 할 때 자동 출력
    def __str__(self):
        return f"사용자:{self.name}, 이메일:{self.email}, 비밀번호: ******"


user1 = User("jake", "jake@gmail.com", "123456")
user2 = User("mike", "mike@gmail.com", "324413")

print(user1)
print(user2)
