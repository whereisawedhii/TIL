# python day 08
- 상속
- 에러와 예외
- eafp and lbyl

## 상속 Inheritance 
- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것
### 상속이 필요한 이유
1. 코드 재사용
   - 상속을 통해 기존 클래스의 속성과 메서드를 재사용
   - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용, 중복된 코드 줄임
2. 계층 구조
   - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
   - 부모 클래스와 자식 클래스 간의 관계를 표현하고, <br>더 구체적인 클래스를 만들 수 있음
3. 유지 보수의 용이성
   - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 됨
   - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음


```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self) :
        print('요로시쿠오네가이시마스')

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 59, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

print(p1.department)
print(s1.gpa)
p1.talk()
s1.talk() # 인스탄스 메서드 없음 - Student 클래스에 없음 - 부모 클래스 Person 에서 찾는다 

```
### super()
- 부모 클래스 객체를 반환하는 내장 함수
- 부모 클래스를 리턴함 
- 사용하는 이유 : 다중 상속의 경우 어떻게 할 건가?

```py
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

# 상속 X 경우
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

# 상속 O 경우
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id

s1 = Student('문태성', 30, 3.3, 'zsm@gmail.com', 1145493)
print(s1.name)

```
## 다중 상속
- 둘 이상의 상위 클래스로부터 상속
- 상속받은 모든 클래스의 요소 활용 가능
- ***상속 순서*** 에 의해 중복된 속성이나 메서드를 결정

```py
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Mom, Dad):
    def swim(self):
        return '첫째가 수영'
    
    def cry(self) :
        return '첫째가 응애'

baby1 = FirstChild('응애')
print(baby1.name) # 응애
print(baby1.greeting()) # 안녕, 응애
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # (Mom, Dad)의 경우 XX, (Dad, Mom)의 경우 XY
# 상속 순서를 찾아서 올라감 -> 앞쪽 부모 클래스 부터 

```

### Diamond Problem
- A - B, C - D 
- B와 C 가 재정의한 메서드가 A에 있고, D가 이를 재정의하지 않은 경우
  - 약속이 필요함 

### MRO 메서드 결정 순서 Method Resolution Order 알고리즘
- 깊이 우선, 왼쪽에서 오른쪽으로 탐색 
  - 계층구조에서 겹치는 같은 클래스를 두번 탐색하지 않음
  - 위 상황에서 검색 순서는 D B C A

## super()
- 다중 상속 시 MRO를 기반으로, <br> 현재 클래스가 상속하는 모든 부모 클래스 중 <br> 다음에 호출될 메서드를 결정하여 자동으로 호출

```py
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    
    def __init__(self):
        super().__init__() # MRO 기반으로 ParentA 의 생성자 함수를 가져옴 
        self.value_c = 'Child'

    def show_value(self):
        super().show_value() # Value from ParentA: ParentA
        print(f'Value from Child: {self.value_c}') # Value from Child: Child

child = Child()
child.show_value()
print(child.value_a) # ParentA

print(child.value_b) # AttributeError

```

> 함수는 호출이 되면 콜스택에 들어감
>  
> 호출이 없을 때까지 스택에 쌓이게 됨
>
> ***A C B D*** 
```py
class A:
    def __init__(self):
        print('A Constructor')


class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')


obj = D() # A C B D 
print(D.mro())

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

```

### super의 2 가지 사용 사례
1. 단일 상속 구조
2. 다중 상속 구조 
- MRO 를 따른 메서드 호출
- 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지 

### MRO가 필요한 이유
- 부모 클래스들이 여러 번 액세스 되지 않도록,
- 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존 
- 각 부모를 오직 한 번만 호출 


# 스택의 자료구조를 생각해라 
- 쌓는 순서 : 1-2-3-4 
- 내리는 순서 : 4-3-2-1
- 선입후출 : FILO 선입후출 LIFO 후입선출 

## 파이썬 함수 호출 방식 : 호출 스택 
- MRO에 따라 D B C A 순서로 스택에 들어감 
- 나올때도 A C B D 순서로 나오게 됨

### 수행 순서 
- B, C 상속 
- 생성자 함수 있음
- D의 `__init__(self)` 수행하러 감 
  - `super().__init__()` 존재함 
    - 부모클래스 (B,C,A)중 B 수행하러 감 
      - `super().__init__()` 존재함 
        - 다음 부모클래스 C 수행하러 감 
          - `super().__init__()` 존재함 
            - 다음 부모 클래스 A 수행하러 감 
              - print A
          - print C 
      - print B
  - print D

### 상속 : 자식 클래스가 부모 클래스의 코드를 사용할 수 있다는 것임
