# 계산기 클래스 (속성이 없는 메소드만 있는 클래스 )
class SimpleCalculator:

    @staticmethod
    def add(first_number, second_number):
        return first_number + second_number

    @staticmethod
    def subtract(first_number, second_number):
        return first_number - second_number

    @staticmethod
    def multiply(first_number, second_number):
        return first_number * second_number

    @staticmethod
    def divide(first_number, second_number):
        return first_number / second_number


calculator = SimpleCalculator()

print(calculator.add(4, 6))
print(calculator.subtract(4, 2))
print(calculator.multiply(4, 6))
print(calculator.divide(4, 2))
