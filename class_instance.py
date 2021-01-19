class User:
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name} 입니다!")


# User 객체의 인스턴스
user1 = User()
user2 = User()
user3 = User()

# user1의 속성 (인스턴스 변수)
user1.name = "jake"
user1.email = "jake@gmail.com"
user1.password = "12345"

# user2의 속성 (인스턴스 변수)
user2.name = "amy"
user2.email = "amy@gmail.com"
user2.password = "23456"

# user3의 속성 (인스턴스 변수)
user3.name = "mike"
user3.email = "mike@gmail.com"
user3.password = "34567"

print(user1.email)
print(user2.password)

# 메소드의 종류 인스턴스 메소드 , 클래스 메소드

# user1의 행동 (메소드)
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)

# 인스턴스 메소드의 특별한 규칙
user1.say_hello()
