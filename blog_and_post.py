class Post:
    # 게시물 클래스
    def __init__(self, date, content):
        # 게시글의 속성: 작성일, 내용
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소트
        return f"작성 날짜: {self.date}\n내용: {self.content}"


class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로서 이름과 게시글을 갖음. 
        게시글은 빈 배열로 초기화 
        """
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        self.posts.append(Post(date, content))

    def show_all_posts(self):
        # 유저의 모든 포스트 내용 출력
        for post in self.posts:
            print(post)

    def __str__(self):
        return f"안녕하세요. {self.name}입니다."


blog_user1 = BlogUser("jake")

print(blog_user1)

blog_user1.add_post("2021년 1월 22일", """
끊입없이 관찰하고 반복하며 익히자.
지금 이 순간에 집중하자.
""")

blog_user1.add_post("2021년 1월 23일", """
내일의 나는 오늘보다 더 나은 내가 되기를.
""")

blog_user1.show_all_posts()
