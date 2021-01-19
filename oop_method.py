class User:
    def say_hello(self):
        # 인사 메시지 출력 메소드
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, my_email, password):
        # 로그인 메소드
        if(self.email == my_email and self.password == password):
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        # 이름 체크 메소드
        return self.name == name


user1 = User()
user2 = User()
# user1의 속성 (인스턴스 변수)

user1.name = "jake"
user1.email = "jake@gmail.com"
user1.password = "12345"

# user2의 속성 (인스턴스 변수)
user2.name = "amy"
user2.email = "amy@gmail.com"
user2.password = "23456"

user1.say_hello()
user1.login("jake@gmail.com", "12345")
print(user2.check_name("jake"))
print(user1.check_name("jake"))
