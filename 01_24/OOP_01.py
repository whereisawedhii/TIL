# 클래스 정의 - blueprint
class Person :
    # 속성 
    blood_color = 'red'
    # 생성자 함수
    def __init__(self, name) :
        self.name = name
    
    def singing(self) :
        return f'{self.name}가 노래합니다.'


# 네이밍 케이스가 다름 
# 지금까지 snake_case 활용
# 클래스는 PaskalCase - 언더바를 붙이지 않고 대문자
# 소괄호 생략 가능 

# 인스턴스 생성
singer1 = Person('김한주') #생성자 함수로 name이 만들어짐
singer2 = Person('SZA') #생성자 함수로 name이 만들어짐

# 메서드 호출 
print(singer1.singing()) # 김한주가 노래합니다.
print(singer2.singing()) # SZA가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color) # red
print(singer2.blood_color) # red


