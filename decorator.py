#  데코레이터 : 기존 함수에 어떤 함수로 꾸며서 새로운 기능을 추가한다.

def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper


@add_print_to
def print_hello():
    print("안녕하세요!")


print_hello()
