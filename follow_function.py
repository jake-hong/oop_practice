class User:
    # 인스턴스 변수값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.passowrd = password

        # 유저의 팔로우 리스트
        self.following_list = []  # 유저가 팔로우하는 리스트
        self.followers_list = []  # 유저를 팔로우하는 리스트

    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)

    # 내가 몇명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)

    # 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        return len(self.followers_list)


# 유저 생성
user1 = User("Jake", "jake@gmail.com", "12345")
user2 = User("Amy", "amy@gmail.com", "23412")
user3 = User("Tom", "tom@gmail.com", "41243")
user4 = User("Mike", "mike@gmail.com", "15243")

# 유저 간 팔로우
user1.follow(user2)
user2.follow(user1)
user3.follow(user4)
user2.follow(user2)
user4.follow(user1)

# 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력
print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())
