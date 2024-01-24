# Python Day07
### 절차 지향 프로그래밍 Procedural Programming
- 프로그램을 '데이터'와 '절차'로 구성하는 방식의 프로그래밍 패러다임
- 순서가 매우 중요하다 

### 특징
- 데이터와 해당 데이터를 처리하는 함수(절차)가 분리되어 있음
- 함수 호출의 흐름이 중요
- 함수(데이터)
- 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
- 실제로 실행되는 내용이 무엇인가가 중요
- 데이터를 다시 재사용하기보다 처음부터 끝까지 실행되는 결과물이 나오는지

### 단점
- 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격
- 함수끼리 충돌
- 함수a에 문제가 생겼을 경우 프로그램들이 모두 다운
- 재활용도 불가능함  
- 새로운 패러다임을 생각함

## 객체 지향 프로그래밍 Object Oriented Programming
- 데이터와 해당 데이터를 조작하는 메서드(함수)를 <br> 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임

### 절차지향 vs 객체 지향 
- 절차 지향 : 데이터-**함수** (데이터는 그저 함수를 동작하기 위함임)
  - 공격을 한다 - 전사가 
- 객체지향 : 클래스 [데이터, 메서드]
  - 상위 개념과 하위 개념이 나뉨
  - 전사가 베기를 한다  
  - 객체 중심임

### 절차지향 vs 객체 지향 2
- 데이터와 해당 데이터를 처리하는 함수(절차) 가 분리 
- 함수 호출의 흐름이 중요

객체 지향
- 데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음
- 객체 간 상호작용과 메시지 전달이 중요

## 클래스 Class
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공 

### 객체 Object
- 클래스에서 정의한 것을 토대로 메모리에 할당된 것
- ***'속성'***과 ***'행동'***으로 구성된 모든 것
- 메모리 주소를 가지고 있는 모든 것
- 파이썬에서는 다 객체 (변수, 함수, ...)

### Class as Blueprint
> 클래스는 설계도다 
>
> 도장같이 객체들을 찍어냄 
>
> 클래스 - 변수 (속성) / 메서드 (행동)

## 클래스로 만든 객체를 ***인스턴스*** 라고 함
- 클래스는 객체일까? 
  - 클래스도 객체임 
- 클래스 (가수) - 객체(아이유)
  - 아이유는 가수의 인스턴스다 

***클래스를 만든다 == 타입을 만든다***
```python 
name = 'Alice'
print(type(name)) # <class 'str'>
```
- 변수 name의 타입은 str 클래스다
- 변수 name 은 **str 클래스의 인스턴스**이다
- 우리가 사용해왔던 **데이터 타입은 사실 모두 클래스**였다. 
- 결국 문자열 타입의 변수는 str 클래스로 만든 "인스턴스"다

### 문자열 타입 (클래스) 의 객체 (인스턴스)
- `'', 'hello', '파이썬'`

### 리스트 타입 (클래스) 의 객체 (인스턴스)
- `[], [1, 2, 3], ['h', 'i']`

### 인스턴스와 메서드 
- `'hello'.upper()` 
  - 문자열.대문자로()
  - 객체.행동()
  - 인스턴스.메서드()
  - belonging - 인스턴스에 속한 메서드 

- `[1, 2, 3].sort()`
  - 리스트.정렬해()
  - 객체.행동()
  - 인스턴스.메서드()

## 하나의 객체(object)는 특정 타입의 인스턴스(instance)이다

### 객체 (object)의 특징
- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
  - 속성 attribute : 어떤 상태 (데이터)를 가지는가?
  - 조작법 method : 어떤 행위 (함수) 를 할 수 있는가?
- 객체 = 속성 + 기능 

## 클래스 Class
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공 
- 클래스는 네이밍 케이스가 다름 PaskalCase - 언더바를 붙이지 않고 대문자
- 정의시 소괄호 생략 가능
- 클래스는 병사들을 생성하고 메서드와 속성값을 활용하여 프로그램을 진행함 
  - ***코드의 재사용성 증가***

```python
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

```

### 생성자 함수 `__init__`
- ***객체를 생성할 떄 자동 호출***되는 특별한 메서드 
- 무조건 수행됨, 안써도 됨
- 객체의 초기화를 담당 - 선언하여 사용한다
- 생성자 함수를 통해 인스턴스를 선언하고 필요한 ***초기값***을 설정 

### 인스턴스 변수 `self.name = name`
- 인스턴스 (객체) 마다 별도로 유지되는 변수 
- 인스턴스마다 독립적인 값을 가짐 
- 인스턴스가 생성될 때마다 초기화됨 

### 클래스 변수 `blood_color = 'red'`
- 클래스 내부에 선언된 변수 
- 클래스로 생성된 모든 인스턴스들이 공유하는 변수 
- 주의해야함 

### 인스턴스 메서드 
- 각각의 인스턴스에서 호출할 수 있는 메서드
- 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행 
- `self` 자기 자신 

### 인스턴스와 클래스 간의 이름 공간 namespace
- 클래스를 정의하면, 클래스와 해당하는 namespace 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 ***독립적인*** namespace 생성
- 인스턴스에서 특정 속성(변수) 에 접근하면, 인스턴스 -> 클래스 순으로 탐색
- `singer1.blood_color` : 본인에게서 먼저 찾고, 없으니 클래스로 넘어감 


```python
# Person 정의
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()  # unknown
"""
p1은 인스턴스 변수가 정의되어 있지 않아
클래스 변수(unknown)가 출력됨
"""

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim' # 인스턴스 변수 name 할당
p2.talk()  # Kim
"""
p2는 인스턴스 변수가 정의되어
인스턴스 변수(Kim)가 출력됨
"""

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim
"""
Person 클래스의 값이 Kim으로 변경된 것이 아닌
p2 인스턴스의 이름 공간에 name이 Kim으로 저장됨
"""
# 독립적인 이름 공간이기 때문에 상관없이 작동함 
p2.ssafy = 11 
print(p2.ssafy) # 11 

```

![image](https://github.com/ragu6963/TIL/assets/32388270/70a65cb1-e567-4792-8b1d-ddebeb618958)

## 독립적인 이름 공간을 가지는 이점
- 각 인스턴스는 독립적인 메모리 공간을 가짐 
  - 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능
- 객체 지향 프로그래밍의 중요한 특성 중 하나임
  - 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
- 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음 
- ***코드의 가독성, 유지보수성, 재사용성을 높임***

## 인스턴스 변수와 클래스 변수 
> 클래스 변수 활용
>
> 클래스에 인스턴스의 개수 확인 - 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정
```python
    class Person:
        count = 0
        
        def __init__(self, name):
            self.name = name
            Person.count += 1
        
        
    person1 = Person('iu')
    person2 = Person('BTS')
        
    print(Person.count)  # 2
```
- 클래스 변수를 변경할 때는 항상 `클래스.클래스변수` 형식으로 변경
- `self` == 인스턴스 변수 
  - 암묵적으로 이름이 self 이지만 네이밍일 뿐임 
  - 이름 변경해도 작동함 
  - 하지만 절대로 하지 않는다

```python
    
class Circle:
pi = 3.14

def __init__(self, r):
    self.r = r


c1 = Circle(5)
c2 = Circle(10)
print(Circle.pi)  # 3.14
print(c1.pi)  # 3.14
print(c2.pi)  # 3.14 

c2.pi = 5  # 인스턴스 변수 변경
print(Circle.pi)  # 3.14 (클래스 변수)
print(c1.pi)  # 3.14 (클래스 변수)
print(c2.pi)  # 5 (새로운 인스턴스 변수가 생성됨)

Circle.pi = 5  # 클래스 변수 변경
print(Circle.pi)  # 5
print(c1.pi)  # 5
print(c2.pi)  # 5 

```
### 메서드 종류 : 누가 쓰는지 - 활용하는 주체
- 인스턴스 메서드
- 클래스 메서드
- 정적 메서드 

## 인스턴스 메서드 instance method
- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
  - 인스턴스의 상태를 조작하거나 동작을 수행
  - 클래스를 조작하지 않음
- 클래스 내부에 정의되는 메서드의 기본
- **반드시** 첫 번째 매개변수로 인스턴스 자신(`self`)를 전달받음
  - **예외는 없음**

### `self` 동작 원리
- upper 메서드 
- `'hello'.upper()` 이지만 파이썬 내부에서는 <br> `str.upper('hello')` 로 동작함 
- str 클래스가 upper 메서드를 호출했고 <br> 그 첫번째 인자로 문자열 인스턴스가 들어감 
- 객체 지향 방식의 메서드로 호출하는 표현임 (단축형 호출)
  - 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적 표현임 

# 인스턴스 메서드의 첫 번째 매개변수는 ***반드시*** 인스턴스 자기 자신

## 생성자 메서드 constructor method
- `__init__` : 생성자 매직 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출 
  - 인스턴스 변수들의 초기값을 설정 
```python
class Person:
    def __init__(self):
        print('인스턴스가 생성되었습니다.')


person1 = Person()  # 인스턴스가 생성되었습니다.

class Person:
    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')


person1 = Person('지민')  # 인스턴스가 생성되었습니다. 지민

```

## 클래스 메서드 Class Method
- 클래스가 호출하는 메서드
  - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

- @classmethod 데코레이터를 사용하여 정의 
- 호출 시, 첫 번째 인자로 호출하는 클래스 `cls` 가 전달됨 

```python
class MyClass:
        
    @classmethod
    def class_method(cls, arg1, ...):
        pass
```
> 예시 
```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population() # 인구수는 2입니다.
```

### 부모클래스 - 자식클래스 상속 : 내일 한다 기대해라 

### 스태틱 (정적) 메서드 Static Method
- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
  - 주로 클래스와 관련이 있지만, 인스턴스와 상호작용이 필요하지 않은 경우에 사용 

- @staticmethod 데코레이터를 사용하여 정의
- 호출 시 필수적으로 작성해야 할 매개변수가 없음 (일반 함수)
- 즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용 

```python
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()


text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text) # dlrow ,olleh

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text) # Hello, world

```

## 메서드 정리
- 인스턴스 메서드 : `(self)`
  - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행
- 클래스 메서드 :  `(cls)` @classmethod
  - 인스턴스의 상태에 의존하지 않는 기능을 정의
  - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
- 스태틱 메서드 @staticmethod
  - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

### 각자의 영역
- 클래스
  - 클래스 메서드
  - 스태틱 메서드
- 인스턴스
  - 인스턴스 메서드 
- 클래스, 인스턴스 메서드 영역의 메서드를 서로 호출 시 
  - 에러가 나지 않고 가능은 하지만 - 각자 영역을 나눠 사용해야 한다

## 할 수 있다 != 써도 된다
- 각자의 메서드는 OOP 패러다임에 따른 명확한 목적에 따라 설계됨
- 클래스와 인스턴스 각각 올바른 메서드만 사용하도록 해야 함

> 예시
```python
class MyClass:

    def instance_method(self):
        return 'instance method', self
    
    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'

# 클래스가 전부 호출해보기
instance = MyClass()

# 에러가 나지 않고 가능은 하지만 이런식으로 쓰지 않는다 - 각자 영역을 나눠 사용한다 
print(MyClass.instance_method(instance)) # ('instance method', <__main__.MyClass object at0x…028F10>)

print(MyClass.class_method()) # ('class method', <class '__main__.MyClass'>)
print(MyClass.static_method()) # static method

# 인스턴스가 전부 호출해보기
instance = MyClass()

print(instance.instance_method()) # ('instance method', <__main__.MyClass object at 0x0000…84EAF10>)
# 에러가 나지 않고 가능은 하지만 이런식으로 쓰지 않는다 - 각자 영역을 나눠 사용한다 
print(instance.class_method()) # ('class method', <class '__main__.MyClass'>)
print(instance.static_method()) # static method
```

## 매직 메서드
- 인스턴스 메서드에 속함 
- 일반적인 인스턴스 메서드와 다르게 특정 상황에 자동으로 호출됨 
- Double underscore __ __ : 특수한 동작을 위해 만들어짐 Dunderscore


> 예시 __str__ : 인스턴스 자체의 출력값 - 인스턴스 print시 사용
```python

```

## 데코레이터 Decorator 
- 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수 
- 데코레이터 정의 - 적용 가능함 
- 함수의 머리에 붙어서 쓰임 
- 원본 함수를 건들지 않고 수정하거나 확장하고 싶을 때 

# 절차 지향과 객체 지향은 대조되는 개념이 아니다 
- 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 <br>
객체라는 개념을 도입해 <br>
상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임 



## 
1. 클래스를 왜 쓰는지 모르겠음 
```python
result = 0

def add_cal1(num) : 
    global result
    result = result + num 
    return result

print(add_cal1(3)) 
print(add_cal1(4)) 
```
같은 코드로 100개의 값을 계산해야 한다면 
코드도, 글로벌 변수도 100개 써야 함 
보관했다 사용하기 위함 

```python
class AddCalculator : 

    def __init__(self, start) :
        self.start = start

    def add(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2       

cal_1 = AddCalculator()

# 방법 1
print(AddCalculator.add(cal_1, 0, 3))
# 방법 2 - 이렇게 쓴다 !!!
print(cal_1.add(0, 3))
```

2. __init__ 잘 모르겠음 
- 인스턴스를 만듦과 동시에 인스턴스에 어떤 값을 전달하고 싶을 때
- 안쓸 때보다 쓸 때 더 좋음
- 99.9% 는 전부 쓴다 
- 초기 데이터 값 전달 
- 기능도 넣고 싶으면 넣을 수 있음 

```python
class AddCalculator : 

# 인스턴스 선언과 동시에 어떤 값을 전달하고 싶을 때 
    def __init__(self, start) :
        self.start = start # self.start 에 매개변수를 할당해서 바인딩

    def add(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2     
    
cal_1 = AddCalculator(0) # self.start 에 0을 할당해서 바인딩

print(cal_1.start) # 0

```

```python
class Account :
    count = 0

    def __init__(self, name) :
        self.name = name 
        Account.count += 1
        print(f'안녕하세요 {name} 고객님, {Account.count}번째 가입자입니다.')

    def show_count(self) :
        print(f'가입한 고객은 {self.name}이고, 총 계좌수는 {self.count}입니다.')
        

customer1 = Account('문태성')
# customer2 = Account('갓삼성')
customer3 = Account('배고픈')
customer4 = Account('피곤한')

customer1.show_count()
```
- 알고리즘만 하다보면 클래스 까먹음 
- Django 하다보면 클래스, 데코레이터, 인스턴스 등 쏟아짐 
- 데코레이터까지 직접 코딩하게 되니 중요함 

- 제일 많이 쓰는 건 인스턴스 변수, 인스턴스 메소드다
- 인스턴스 메소드 안에 인스턴스 변수를 선언해야 함 
- 언어는 결국 상대방과 소통하기 위함 
- 내가 사회에서 지키는 매너를 지켜야 나도 존중받음 - 관행을 지키자 
- 파이썬에서 백엔드 구현할 때 - 프엔에서 정보 넘어가는데 처리할 때 사용함 ,,, 

> 새벽 5시에 카운트하는 자동화 : 5시에 수행도 해야하고, 5시에 수행했다는 증거도 리턴받아야 함 
  - 데코레이터로 구현 가능함 @show_time
  - def show_time
  - import sys
  - ....
  - show_time 먼저 수행하면서 시간부터 찍고, 그 안에서 카운트 수행하고 리턴됨 
  - 종료 시간도 찍을 수도 있음 

```python
def show_time
  import sys
  print(starttime )
  sum_account()
  print(count)
  print(endtime)

@ show_time
def sum_account() : 

```

