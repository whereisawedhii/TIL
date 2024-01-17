## 함수 functions 
- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지 
- **재사용성**이 높아지고 코드의 **가독성과 유지보수성** 향상 
- *재사용성* : 반복적으로 필요한 순간에 활용

```python
# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3

sum_result = num1 + num2
print(sum_result)

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2

# 함수 사용하여 결과 출력
num1 = 5
num2 = 3
sum_result = get_sum(num1, num2)
print(sum_result)
```
### 내장 함수 Built-in function
- 파이썬이 기본적으로 제공하는 함수 
- 별도의 import 없이 바로 사용 가능 
- ex. `print()` 터미널에 값을 출력하는 함수 
- <-> 공식적으로 외장함수 라는 단어는 존재하지 않음 
  
  #### 절대값을 만드는 함수 abs
```python
# abs 함수 호출의 반환 값을 result에 할당
result = abs(-1)

print(result) # 1
```

### 함수 호출 function call 
`function_name(arguments)`
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것 

```python
def make_sum(pram1, pram2) :
    """이것은 두 수를 받아 
    두 수의 합을 반환하는 함수입니다.

    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2
```
#### parameter : 매개변수 
#### (function) body : 함수 내용 
#### document string : 여러 줄 주석처리 ( """ """ ) - 함수를 사용하는 가이드 작성, 활용 예시
#### return value : 반환값 

### 함수의 정의와 호출 
- 함수 정의 (define)
  - 함수 정의는 `def` 키워드로 시작
  - `def` 키워드 이후 함수 이름 작성
  - 괄호안에 매개변수를 정의할 수 있음 
  - 매개변수(parameter)는 함숭 전달되는 값을 나타냄 

- 함수 반환 값
  - 함수는 필요한 경우 결과를 반환할 수 있음 (필수는 아님)
  - return 키워드 이후에 반환할 값을 명시 
  - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환

```python
# 함수 정의
def greet(name):
    """입력된 이름(name) 값에
    인사를 하는 메세지('Hello, ')를 만드는 함수
    """
    message = 'Hello, ' + name
    return message

# 함수 호출
result = greet('Alice')
print(result) # Hello, Alice
```

- 함수 호출
  - 함수의 이름과 필요한 인자(argument)를 전달해야 함 
  - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 해당됨 
  
## 매개변수와 인자 
### 매개변수 parameter
함수를 정의할 때, 함수가 받을 값을 나타내는 변수
### 인자 argument 
함수를 호출할 때, 실제로 전달되는 값

- 예시 

```python
def add_numbers(x, y): # x와 y는 매개변수(parameter)
    result = x + y
    return result


a = 2
b = 3
sum_result = add_numbers(a, b) # a와 b는 인자(argument)
print(sum_result)
```
***함수가 조금 더 다양한 일을 하려면 인자를 다양한 방식으로 받을 수 있어야 함***

## 인자의 종류 
### **위치인자 Positional Arguments**
- 함수 호출 시 인자의 위치에 따라 전달되는 인자 
- ***위치인자는 함수 호출 시 반드시 값을 전달해야 함***
- 전달하지 않을 경우 TypeError : missing argument

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요
greet('Bella') # TypeError: greet() missing 1 required positional argument: 'age'
greet(30, 'Bella') # 안녕하세요, 30님! Bella살이시군요.
greet(30, 'Bella', 'aaa') # TypeError: greet() takes 2 positional arguments but 3 were given
```
### Default Argument Values 기본 인자 값 
- 함수 정의에서 매개변수에 기본 값을 할당하는 것 
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

```python
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Bob') # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.
```
### Keyword Argument Values 키워드 인자 
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
- ***단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함***
- **Positional argument cannot appear after keyword arguments**
- 파이썬이 알아들을 수 없음 

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, 'Dave')  #  positional argument follows keyword argument
```

### Arbitrary Argument Lists 임의의 인자 목록 
- 정해지지 않은 개수의 인자를 처리하는 인자 
- ex. `print()`
- 함수 정의 시 매개변수 앞에 `*`를 붙여 사용하며, 여러개의 인자를 tuple 로 처리 
- *tuple : python 내부 동작에서 사용*

```python
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')


"""
(1, 2, 3)
합계: 6
"""
calculate_sum(1, 2, 3)
```
### Arbitrary Keyword Argument Lists 임의의 키워드 인자 목록 
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자 
- 함수 정의 시 매개변수 앞에 `**`를 붙여 사용
- 여러개의 인자가 묶임 - dict로 묶어 처리
```python
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}
```

### 함수 인자 *권장* 작성순서
1. 위치
2. 기본
3. 가변
4. 가변 키워드 
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함 
- **모든 상황에 적용되는 절대적인 규칙은 아님**

```python
def func(pos1, pos2, age=30, *args, **kwargs):
    print(pos1, pos2, age, args, kwargs)

func(1, 2, 3, 4, 5)
func(1, 2, 3, a=100. b=200)
    # ...
```

## 함수와 Scope
#### Python의 범위(Scope)
- 함수는 코드 내부에 ***local scope***를 생성하며, 그 외의 공간인 ***global scope***로 구분
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable 
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

- scope 예시 
    ```python
    def func():
        num = 20
        print('local', num)  # local 20


    func()

    print('global', num)  # NameError: name 'num' is not defined
    ```
  - num 은 local scope에 존재하기 때문에 global에서 사용할 수 없음 
  - 이는 변수의 ***수명주기***와 연관이 있음

### 변수의 수명주기 lifecycle
- 변수가 선언되는 위치와 스코프에 따라 결정됨 
1. built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
    - **모듈이 호출된 시점** 이후 혹은 **인터프리터가 끝날 때까지** 유지
3. local scope
    - **함수가 호출될 때 생성**되고, **함수가 종료될 때**까지 유지

#### 이름 검색 규칙(Name Resolution) - LEGB Rule
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음

- LEGB Rule : 아래와 같은 순서로 이름을 찾아 나감
    1. Local scope : 지역 범위(현재 작업 중인 범위)
    2. Enclosed scope : 지역 범위 한 단계 위 범위
    3. Global scope : 최상단에 위치한 범위
    4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

> ***함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음***

![image](https://github.com/ragu6963/TIL/assets/32388270/15b4f0c6-7f21-4986-8349-fd8740e49573)

#### LEGB Rule 예시 1
    ```python
    print(sum) # <built-in function sum>
    print(sum(range(3))) # 3

    sum = 5

    print(sum) # 5
    print(sum(range(3))) # TypeError: 'int' object is not callable
    ```
- sum이라는 이름을 global scope에서 사용하게 되면서 <br>기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨
- sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문
- sum 변수 객체 삭제를 위해 `del sum` 

```python
a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c) # 10 2 500

    local(500)
    print(a, b, c) # 10 2 3

enclosed()
print(a, b) # 1 2
```
- 함수는 호출할 때 실행됨 
- local이 어디서 호출되는지를 봐야 함 - 호출되는 시점
- LEGB Rule 
- enclosed 호출될 때도 동일 

### ‘global’ 키워드
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 함수 내에서 전역 변수를 수정하려는 경우에 사용
- 일반적으로 권장하는 사항은 아님
- global 선언 전에 접근 할 수 없음
- 매개변수에 global 사용 불가 
> global 키워드는 가급적 사용하지 않는 것을 권장
> 함수로 값을 바꾸고자 한다면 항상 ***인자***로 넘기고
> 함수의 ***반환값***을 사용하는 것을 권장

```python
num = 0 # 전역 변수


def increment():
    global num # num를 전역 변수로 선언
    num += 1


print(num) # 0
increment()
print(num) # 1

    num = 0

# global 선언 전에 접근 할 수 없음
def increment():
    # SyntaxError: name 'num' is used prior to global declaration
    print(num)
    global num
    num += 1

num = 0

# 매개변수에 global 사용 불가
def increment(num):
    # "num" is assigned before global declaration
    global num
    num += 1
```


## 재귀 함수 
- 함수 내부에서 자기 자신을 호출하는 함수 
- 종료가 되는 시점이 있음 
- 특정 알고리즘 식을 표현할 때, 변수의 사용이 줄어들며, 코드의 가독성이 높아짐 
- 1개 이상의 base case (종료되는 상황) 가 존재하고, 수렴하도록 작성
- 큰 문제를 작은 단위로 쪼개어 풀 수 있음

> 재귀함수 예시 - 팩토리얼 
> 
> f(4) = 4 * f(3)
> 
> f(3) = 3 * f(2)
> 
> f(2) = 2 * f(1)
> 
> **f(1) = 1** **base case**
- factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
- 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출

```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)


# 팩토리얼 계산 예시
result = factorial(5)
print(result) # 120
```
## 유용한 내장 함수 
### map(function, iterable)
- 순회 가능한 데이터구조 iterable 의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
- 반복문을 적용한 듯함 
```python
numbers = [1, 2, 3]
result = map(str,numbers)

print(result) # <map object at 0x00000239C915D760>
print(list(result)) # ['1', '2', '3']
```
> SWEA
```python
numbers = input().split()
print(numbers) #['1', '2', '3', '4', '5']
result = map(int, numbers)
print(result) #<map object at 0x000002DBFA680430>
print(list(result)) #[1, 2, 3, 4, 5]

result = list(map(int, input().split()))
```

### zip (*iterables)
- 가변인자를 받을 수 있는 함수
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환 
>순서쌍의 개수가 맞지 않으면 원소가 만들어지지 않음....

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) # <zip object at 0x000001C76DE58700>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]
```

### lambda 
`lambda 매개변수 : 표현식`
- 이름없이 정의되고 사용되는 익명함수
- 1줄로 일회성으로 간단한 연산, 단일한 함수 사용할 때 사용
- 함수를 매개변수로 전달하는 경우 - map과 함께 많이 쓰임 
- lambda (키워드)
    - 람다 함수를 선언하기 위해 사용되는 키워드
- 매개변수
    - 함수에 전달되는 매개변수들
    - 여러 개의 매개변수가 있을 경우 쉼표로 구분
- 표현식
    - 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성
```python
# 람다 함수 미적용 코드
def addition(x, y):
    return x + y

result = addition(3, 5)
print(result) # 8
```

```python
# 람다 함수 적용 코드
addition = lambda x, y: x + y

result = addition(3, 5)
print(result) # 8
```

```python
numbers = [1, 2, 3, 4, 5]

def func(x) :
    return x ** 2

result = list(map(func,numbers))
print(result) # [1, 4, 9, 16, 25]

result2 = list(map(lambds x : x**2, numbers)
print(result2) # [1, 4, 9, 16, 25]
```

## Packing & Unpacking

### Packing 패킹
- 여러 개의 값을 하나의 변수에 묶어서 담는 것 
- ex. `args` 가변인자 
> 변수에 담긴 값들은 tuple 형태로 묶임 
```python
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)
```
- ‘*’을 활용한 패킹
> `*b`는 남은 요소들을 리스트로 패킹하여 할당

```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
    
print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5
``` 
> print 함수에 임의의 가변 인자를 작성할 수 있었던 이유 
    > 인자 개수에 상관 없이 튜플 하나로 패킹되어 내부에서 처리 

```python
print('hello') # hello
    
print('you', 'need', 'python') # you need python
```

![image](https://github.com/ragu6963/TIL/assets/32388270/05db04bd-d01c-4f4c-a193-854e59385d67)


### Unpacking `언패킹`
- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
>튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
    
```python
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5
```
> `*` 는 리스트의 요소를 언패킹

```python
names = ['alice', 'jane', 'peter']
print(*names)  # alice jane peter
```
> `**` 는 딕셔너리의 키-값 쌍을 함수의 키워드 인자로 언패킹
    
```python
def my_function(x, y, z):
    print(x, y, z)


my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3
```
### *, ** 패킹 / 언패킹 연산자 정리
- ‘*’
    - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶는 역할
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 <br>언패킹하여 함수의 인자로 전달
- ‘**’
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 키워드 인자로 <br>언패킹하여 함수의 인자로 전달하는 역할

# 하늘쌤 보충 
- 교사 pc는 성적 내용 + 내부 정보 있으니 touch X
1. 노트 정리 
    - image 끌고 오는 경우 많은데 : ![image]
    - https://주소는 상관 없는데 로컬 이미지는 어려움 
   1. image.png를 같은 directory에 두고 사용 ![이미지]image3.png 
   2. 없는 경우 환경변수를 정해놓은 경로를 찾는 방법에 따라 찾음
   3. 하위 디렉토리 생성하여 이미지 파일들을 모아놓기 `mkdir images` (./image_prac/image3.png)
   4. sibling direc (./../image_prac/image3.png)
   5. 상대경로로 표시하기 
2. git lab 온실 - 관리 
   - 하루에 10문제 풀면 -> 각각 clone 
   - local에 .git 폴더 생성 
   - 20230117 
   - pythonday_03
   - 내 GitHub 에서도 관리
   1. GitHub에 원격 Repository - TIL
   2. desktop - TIL -> .git - connect with 1. and push 
   3. 제출까지 끝냈으면 우선 GitLab connect 해제 - .git 폴더 삭제

## 함수 
- 처음에는 계산기만 만들어서 함수 같은거 없었음 
- 변수, 반복문, 조건문 
- 클래스가 없는 language도 많음
- 직접 써보니까 조건을 주어 계산하는 명령을 반복한다면 <br> 재사용하는 코드들은 별도로 관리하자 
- 코드를 재사용하기 위해서 함수를 만들었음
- 재사용한다는 것은 어딘가에 코드를 저장하고, 이름을 붙이는 것
- 결국 이게 함수다,,,
- 재사용 예약 : `def`

### 모듈 : 독립된 파이썬 함수 
- import : 모듈 함수를 남들도 재사용하게 하고 싶어서

### 함수 호출 : 해당 함수의 코드를 실행하는 것 
- 데이터나 파일처리 계산을 시키는 것 - 코드 값들을 전달하는 것 : 재사용하는 코드를 수행하기 위해서 필요한 데이터 : parameter - argument
- parameter : 값을 담기 위한 변수 
- argument : 실제 전달하는 값 or 주소? 
- Call by reference / Call by data - 심화학습

> 실제로 다른 사람이 쓴 코드를 보고 머리 싸매는 상황이 더 많음 
#### 인자 규칙을 잘 이해해야 하는 이유임 

### Positional Argument 
- 순서 = 번호 = 위치변경이 안됨 = 기본값 
- 무조건 1:1 이 되어야 함 
- parameter에 전달하는 순서가 있음

### Default Argument Values 
- 인자를 전달하지 않으면, 기본 값이 매개변수에 할당됨

### Keyword Argument 
- 함수 코드가 100줄인 경우 <br> 필요한 데이터는 10, 25, 1000개 일 때... <br> 틀리면 실행이 안됨 -> 키워드 인자 필요
- 함수 호출 Call 시 인자의 이름과 함께 값을 전달하는 인자 
- 순서는 중요하지 않음 
- 인자의 이름을 명시하여 전달 

`pandas.concat(objs, *, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=None)`
- 위치인자 `objs`
- `*` 임의 인자
- 나머지 Default - Keyword 

### *args - Arbitrary Argument Lists 
- 쇼핑몰에 필수정보 선택정보 
    ```python
    def sign_up(id, password, *args)
    # id, password, gender, age
    ```
- matplotlib.pyplot.plot 
  
### **kwargs 

### global keyword - 실무에 많이 쓰면 에러나서 욕먹으니 조심할 것 

### global scope 

### 재귀함수 - 실제로 메모리에서 어떻게 움직이는지, 실제 상황을 재귀함수로 짤 수 있는 technique 중요함 

### map : for 문으로 해야하는 것을 넣어놓음 - 실제로 쓸 수 있어야 함 
### zip : 알고리즘 + 데이터 분석 - 실제로 데이터들을 짝지을 때 사용됨 
### `lambda parameter : expression`
- `def func` 도 하기 귀찮을 때 
```python
def func(param1,param2)
    S1 = int(param1)
    S2 = int(param2)
    return S1, S2 

lambda x, y : int(x, y)
```
### Packing 
- `*`을 활용한 패킹 - `*var`남은 요소들을 변수에 리스트로 패킹 
    ```python
    def sign_up(id, password, *args)
        c_id = id
        c_pw = pw
        *c_etc = args
    # id, password, gender, age
    ```
- `print()` `sep` seperator 기본값이 null `end` 기본값이 줄바꿈 
```python
print(3)
print(5)
# 3
# 5
print(3, end='\t')
print(5)
# 3    5
```
### Unpacking 데이터를 하나 하나 값을 주고 이름을 줘서 재사용 


# Final Project : Service - 사용자 정보를 받아야 함 <br> 2학기는 팀에서 결정한다 - 기획의도와 기획이 중요함 <br> 1학기에는 다 똑같은 주제로 프로젝트 하니까 UI, 기능 등 technique <br> 로그인도 필수 정보만 넣게 할 것인가, 선택 정보 넣는 기능까지 구현할 것인가, <br> id 만들 때의 규칙/pw 만들 때의 규칙 등 - 따르지 않을 경우 output - value 지워버림 등 <br> 정성을 들여라 

## define, parameter, argument 
## *args **kwargs packing unpacking
