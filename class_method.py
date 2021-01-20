#  클래스 메소드 : 클래스 변수의 값을 읽거나 설정하는 메소드

class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print(f"안녕하세요. 저는 {self.name}입니다.")

    def __str__(self):
        return f"사용자:{self.name}, 이메일:{self.email}, 비밀번호:******"

    @classmethod
    def number_of_users(cls):
        print(f"총 유저수는:{cls.count}입니다.")


# 유저 생성
user1 = User("Jake", "jake@gmail.com", "12345")
user2 = User("Amy", "amy@gmail.com", "23412")
user3 = User("Tom", "tom@gmail.com", "41243")
user4 = User("Mike", "mike@gmail.com", "15243")

User.number_of_users()
user1.number_of_users()


class Client:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 코드를 쓰세요
        parameter_list = string_params.split(',')

        name = parameter_list[0]
        email = parameter_list[1]
        password = parameter_list[2]

        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        # 코드를 쓰세요
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]

        return cls(name, email, password)


# 유저 생성 및 초기값 설정
jake = Client.from_string("jake, jake@gmail.com,,123456")
mike = Client.from_list(["mike", "mike@gmail.com", "abcdef"])

print(jake.name, jake.email, jake.password)
print(mike.name, mike.email, mike.password)
