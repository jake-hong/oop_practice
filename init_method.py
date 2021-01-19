class User:
    # __init__ 메소드 (특수 메소드)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user1 = User("jake", "jake@gmail.com", "31245")

user2 = User("amy", "amy@gmail.com", "12345")

print(user1.name)
print(user2.email)
