# 버그 bug
- 소프트웨어에서 발생하는 오류 또는 결함
- 프로그램의 예상된 동작과 실제 동작 사이의 불일치

- 최초의 버그는 1945년 코볼 발명자 그레이스 호퍼가 발경 
- Mark 2 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록한 것 
- 이 계기로 컴퓨터 시스템에서 발생하는 오류 또는 결함을 지칭 

## Debugging
- 결함이나 오류를 해결하는 과정
- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
- 프로그램의 오작동 원인을 식별하여 수정하는 작업

### 디버깅 방법 
- print 함수 활용 
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발 환경(text editor, IDE)에서 제공하는 기능 활용
  - breakpoint, 변수 조회 등
- Python tutor 활용 (단순 파이썬 코드인 경우)
- 뇌 컴파일, 눈 디버깅 등 

### 에러 Error 
- 프로그램 실행 중에 발생하는 버그 상황 
### 문법 에러 Syntax Error 
- 구문이 올바르지 않은 경우 
- 오타, 괄호, 콜론 누락 등 문법적 오류

- Invalid syntax (문법 오류)
    
    ```py
    while # SyntaxError: invalid syntax
    ```

- assign to literal (잘못된 할당)
    
    ```py
    5=3 # SyntaxError: cannot assign to literal
    ```

- EOL (End of Line)
    
    ```py
    print('hello   
    # SyntaxError: EOL while scanning string literal
    ```

- EOF (End of File)
    
    ```py
    print(
    #SyntaxError: unexpected EOF while parsing
    ```

### 예외 Exception 
- 프로그램 실행 중에 감지되는 에러 

### 내장 예외 Built-in Exceptions 
- 예외 상황을 나타내는 예외 클래스들 
  - 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용 

1. ZeroDivisionError : 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생
```py
10/0 # ZeroDivisionError: division by zero
```

2. NameError : 지역 또는 전역 이름을 찾을 수 없을 때
```py
print(name_error) # NameError: name 'name_error' is not defined
```

3. TypeError : 
   - 타입 불일치
    ```py
    '2' + 2  # TypeError: can only concatenate str (not "int") to str

    ```

   - 인자 누락 
    ```py
    sum()  # TypeError: sum() takes at least 1 positional argument (0given)

    ```
    
   - 인자 초과
    ```py
    sum(1, 2, 3)  # TypeError: sum() takes at most 2 arguments (3given)

    ```

   - 인자 타입 불일치
    ```py
    import random
    random.sample(1, 2)
    # TypeError: Population must be a sequence.  For dicts or sets,use sorted(d).

    ```

4. ValueError 
   - 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, <br>상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생

```py
int('1.5') # ValueError: invalid literal for int() with base 10: '3.5'

range(3).index(6) # ValueError: 6 is not in range

```

5. IndexError : 시퀀스 인덱스가 범위를 벗어날 때 발생 
```py
empty_list = []
empty_list[2]
# IndexError: list index out of range

```

6. KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우
```py
person = {'name': 'Alice'}
person['age']  # KeyError: 'age'

```

7. ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생
```py
import hahaha  # ModuleNotFoundError: No module named 'hahaha'

```

8. ImportError : 임포트 하려는 이름을 찾을 수 없을 때 발생
   - 모듈은 찾았는데 import 대상이 없을 떄 
```py
from random import hahaha
# ImportError: cannot import name 'hahaha' from 'random'

```

9.  KeyboardInterrupt : 사용자가 Control-C 또는 Delete를 누를 때 발생
- 무한루프 시 강제 종료
    
```py
while True: 
    continue
    
'''
Traceback (most recent call last):
  File "...", line 2, in <module>
    continue
KeyboardInterrupt
'''
```

1.  IndentationError : 잘못된 들여쓰기와 관련된 문법 오류
    
```py
for i in range(10):
print(i) # IndentationError: expected an indented block

```

- BaseException 에서 파생된 클래스의 인스턴스들임 

## 예외 처리 
### try - except
- try 문과 except 절을 사용하여 예외 처리 
- try 블록 안 예외가 발생할 수 있는 코드 작성
- except 블록 안 예외가 발생했을 때 처리할 고드 작성
- 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 <br>
해당 예외에 대응하는 except 블록으로 이동

```py
# ZeroDivisionError
try : 
    result = 10 / 0
except ZeroDivisionError: 
    print('0으로 나눌 수 없습니다')

# NameError
try : 
    print(name)
# 다양한 예외처리 불가 
except : 
    print('0으로 나눌 수 없습니다')

# ValueError
try : 
    num(int(input('숫자입력 :')))
except ValueError :
    print('숫자가 아닙니다')

```
### 복수 예외 처리 연습
```py
# a : ValueError
# 0 : ZeroDivisionError

try :
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError: 
    print('숫자를 넣어')
except ZeroDivisionError: 
    print('0으로 나누기가 될 것 같아?')
except : 
    print('알 수 없는 에러 발생')

except (ValueError, ZeroDivisionError):
    
except BaseException: 

```

### 내장 예외의 상속 계층구조 주의
- 내장 예외 클래스는 상속 계층구조를 가지기 때문에<br> except절로 분기 시 ***반드시 하위 클래스를 먼저 확인***할 수 있도록 작성 

### as 키워드 
- 에러 메시지를 except 블록에서 사용할 수 있음 
```py
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')

# list index out of range가 발생했습니다.
```

## 예외처리와 값 검사에 대한 2가지 접근 방식
1. EAFP
2. LBYL

### EAFP Easier to Ask for Forgiveness than Permission 
- 예외처리를 중심으로 코드를 작성하는 접근 방식 
- `try - except` 

### LBYL Look Before You Leap 
- 값 검사를 중심으로 코드를 작성하는 접근 방식 
- `if - else` 

```py
# 딕셔너리에서 키를 조회할 때 키가 없는 상황 
dict = {'condition' : 'hungry'}

# try - except
try :
    age = dict['age']
    print(age)
except :
    print('물 만큼 뭇다')

# if - else 
if 'age' in dict :
    age = dict['age']
    print(age)
else : 
    print('손투리 극혐')

```
- EAFP 
  - 일단 실행하고 예외를 처리
  - 코드를 실행하고 예외가 발생하면 예외처리 수행
  - 예외가 발생한 후에 예외를 처리 
  - 전반적인 예외를 예측하기 어려운 경우 

- LBYL
  - 실행하기 전에 조건을 검사 
  - 실행 전 예외 상황을 검사하고, 조건 적용해 예외 상황을 피하는 방식
  - 코드가 예측 가능하게 동작함, 코드가 더 길고 복잡해질 수 있음 
  - 예외상황을 미리 방지하고 싶을 때 유용 
