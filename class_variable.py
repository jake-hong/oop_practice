class User:
    # 클래스 변수
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1


# 유저 생성
user1 = User("Jake", "jake@gmail.com", "12345")
user2 = User("Amy", "amy@gmail.com", "23412")
user3 = User("Tom", "tom@gmail.com", "41243")
user4 = User("Mike", "mike@gmail.com", "15243")

print(User.count)
print(user1.count)
