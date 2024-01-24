# python day 05 Data Structure

## 데이터 구조 `Data Structure`
여러 데이터를 효과적으로 사용, 관리하기 위한 구조<br>
(str, list, dict 등)

### 자료구조 
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것 
![image](https://github.com/ragu6963/TIL/assets/32388270/ec3c4025-1305-4ba1-8f7a-fc355c1fa4e3)
- 단순구조


### 데이터 구조 활용
- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 <span style='color:red;'>메서드</span>를 호출하여 다양한 기능을 활용하기

### 메서드 method 
- 객체(클래스)에 속한 함수 
- 객체의 상태를 조작하거나 동작을 수행
- .함수 : .은 belonging, 객체에 속함 

> test_sky.py : `list1 = [1, 2, 3]`
>
> test1.py : 
```python
import test_sky
test_sky.list1
test_sky.list1.append(4)
print(test_sky.list1) # [1, 2, 3, 4]
```

#### 객체 
- class 
- object 
- instance 

### 데이터 타입 객체.메서드()
- `hello.capitalize()`

### 메서드 특징
- 메서드는 클래스 내부에 정의되는 함수
- 클래스는 파이썬에서 '타입을 표현하는 방법'
- 데이터 타입의 객체가 호출하는 함수
- `객체.메서드()` : 본인이 가지고 있는 함수를 호출함 
- 앞쪽 객체의 데이터 타입이 무엇인지에 따라 함수가 다름 

```python
print(type('1')) # <class 'str'>
print(type([1, 2])) # <class 'list'>

# __###__ : 매직메서드 - 특수한 상황에서 자동으로 호출됨.. 
print(help(list))
# |  append(self, object, /)
# |      Append object to the end of the list.
# 클래스 list 안에 내부적으로 정의되어 있는 함수

def append() :
    pass 

append() # 함수호출 
리스트.append() # 메서드 호출 
# 데이터 타입의 객체가 호출하는 함수
```
## 메서드는 클래스에 속해 있는 함수이며, 각 타입별로 다양한 기능을 가진 함수가 존재 
### 데이터 타입 객체.메서드()

> 예시 
```python 
# 문자열 메서드 예시
print('hello'.capitalize())  # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)  # [1, 2, 3, 4]
```

## 시퀀스 데이터 구조 
### 문자열 조회/탐색 및 검증 메서드 
- `s.find(x)` : x의   ***첫 번째 위치***를 반환. 없으면 -1을 반환
- `s.index(x)` : x의   ***첫 번째 위치***를 반환. 없으면 오류 발생

- `s.isalpha()` : 알파벳 문자 여부 <br> *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)
- `s.isupper()` : 문자열이 모두 대문자인지 여부 
- `s.islower()` : 문자열이 모두 소문자인지 여부 
- `s.istitle()` : 타이틀 형식 여부 
- `s.isalnum()` : 사이트 만들 때 알파벳 하나 숫자 하나 이상이 들어가야 한다,,, 할 때 

> 이름이 is로 시작되는 경우 return값이 True, False : 여부를 알기 위해서 사용되는 함수
>
> 내가 boolean 값 리턴하는 함수 정의할때도 style guide상 권장됨

#### 데이터 타입에 `.` 찍으면 메서드 자동완성으로 리스트 뜨니 활용할 것 
```python
my_str = 'banana'

# find
print(my_str.find('a')) # 1 - 첫 번째 index
print(my_str.find('z')) # -1 

# index
print(my_str.index('a')) # 1
print(my_str.index('z')) # ValueError

# isalpha
string1 = 'Hello'
string2 = '12q3'
print(string1.isalpha()) #True
print(string2.isalpha()) #False - 알파벳이 아닌 다른 것이 섞여있는지 

# isupper, islower
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False

```

### 문자열 조작 메서드 (새 문자열 반환)
- 왜 새로운 문자열을 주는가? 
- 문자열은 불변 데이터 타입 : 바꿀 수 없음 

- `s.replace(old,   new[,count])` : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환, <br> 선택적 인자 count가 주어지면 앞의 count 개만 치환됨 
> 3번째 인자를 의미 (선택인자)
> 
> 파이썬 문법이 아님 : 공식문서의 메서드 표기
>
> 프로그래밍 언어가 python만 있는 건 아니기 때문 - 문법 통일 필요성
>
> 베커스-나우르 표기법 : 어떠한 프로그래밍 언어의 개발자가 오더라도 볼 수 있는 표기법
>
> 파이썬은 EBNF : 확장된 베커스-나우르 표기법 사용 
>
- `s.strip([chars])` : 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
- `s.split(sep=None, maxsplit=-1)` : 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
- `'separator'.join(iterable)` : 앞쪽에 구분자가 문자열로 나옴, iterable 요소들을 구분자를 이용하여 하나의 문자열로 연결 <br> split과 반대
- `s.capitalize()` : 가장   첫 번째   글자를   대문자로   변경
- `s,title()` : 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환
- `s.upper()` : 모두 대문자로 변경
- `s.lower()` : 모두 소문자로 변경
- `s.swapcase()` : 대↔소문자 서로 변경

```python 
# .replace()
text = 'Hello, world!'
new_text = text.replace('world', 'Python') # 반환이 되기 때문에 새로 할당함
print(new_text) # Hello, Python!

# .strip()
text = '   Hello, world!   '
new_text = text.strip()
print(new_text) # 'Hello, world!'

# .split
text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', ' world!']

# .join
words = ['Hello', 'world!']
text = '-'.join(words)
print(text) # 'Hello-world!'

# 기타
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()

print(new_text1) # Hello, world! - H만 대문자로
print(new_text2) # Hello, World! - 공백을 기준으로 단어 시작될 때 대문자로 
print(new_text3) # HELLO, WORLD! - 전부 대문자로
print(new_text4) # HEllO, WOrLD! - 대소문자 전환 

```

### 메서드는 이어서 사용 가능 `input().split()`
```python
text = 'heLLo, woRld!'

new_text = text.swapcase().replace('l', 'z')

print(new_text) # HEzzO, WOrLD!
```
- 주의사항 : 앞쪽 메서드가 반환값이 없는 `None`이라면 사용 불가
- `None` type은 메서드를 가지고 있지 않음 

## 리스트
- 스택이나 큐를 구현하기 좋은 자료구조 
- 데이터가 늘어났냐, 빠졌냐, 조회했냐 
- 스택으로 된 자료구조를 가지고 알고리즘을 풀 때 
- 어떻게 넣지, 빼지를 고민하는 단계면 안됨 

### 리스트 값 추가 및 삭제 메서드 
- 가변 데이터 타입
- 원본 자체를 조작하여 바뀜 
- 반환값이 없음 
- 결과를 `print` 하면 `None` 
- 메서드 종류마다 다를 수 있음
> 
- `L.append(x)` : 리턴값X - 리스트 마지막에 항목 x를 추가
- `L.extend(m)` : 리턴값X - 리스트에 다른 반복 가능한 객체의 모든 항목을 추가 (+=과 같은 기능)- <br> ***풀려서 추가***
- `L.insert(i, x)` : 리턴값X - 리스트 인덱스 i에 항목 x를 삽입
- `L.remove(x)` : 리턴값X - 리스트에서 첫 번째로 일치하는 항목을 삭제
##### pop 매우 중요 <-> append
- `L.pop()` : 리턴값O -리스트에서 지정한 인덱스의 항목을 반환 후 제거하고 ***반환*** <br>
작성하지 않을 경우 마지막 항목을 제거 
- `L.pop(i)` : 리턴값O - 리스트에서 지정한 인덱스의 항목을 반환 후 제거
- `L.clear()` : 리턴값X - 리스트의 모든 항목을 삭제 - 리스트를 제거하는 것은 아님 

```python
my_list = [1, 2, 3]

# append 
my_list.append([4, 5, 6])
print(my_list) # [1, 2, 3, [4, 5, 6]]
print(my_list.append([4, 5, 6])) # None

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]

# index
my_list = [1, 2, 3, 4, 5, 6]
my_list.insert (3, 'ssafy')
print(my_list) # [1, 2, 3, 'ssafy', 4, 5, 6]

# remove
my_list = [1, 2, 3, 'ssafy', 4, 4, 5, 6]
my_list.remove(4)
print(my_list) # [1, 2, 3, 'ssafy', 4, 5, 6]

# pop - 리턴이 있음
my_list = [1, 2, 3, 'ssafy', 4, 5, 6]
item1 = my_list.pop()
print(item1) # 6 
item2 = my_list.pop(0)
print(item2) # 1
print(my_list) # [2, 3, 'ssafy', 4, 5]

# clear 
my_list.clear()
print(my_list) # []
```

### 리스트 탐색 및 정렬 메서드 
- `L.index(x, start, end)` : 리턴값O - 리스트에서 첫 번째로 일치하는 항목의 인덱스를 반환
- `L.reverse()` : 리턴값X - 리스트의 순서를 역순으로 변경 (정렬 X)
- `L.sort()` : 리턴값X - 리스트를 오름차순으로 정렬 (매개변수 이용가능)
- `L.count(x)` : 리턴값O - 리스트에서 항목 x의 개수를 반환 

```python
# index 
my_list = [2, 3, 'ssafy', 4, 5]
index = my_list.index(2)
print(index) #0 

# count 
my_list = [1, 3, 2, 2, 3, 1, 3]
count_num = my_list.count(3)
print(count_num) # 3

# sort 
my_list = [3, 2, 1]
my_list.sort()
print(my_list) # [1, 2, 3] 오름차순
my_list.sort(reverse=True)
print(my_list) # [3, 2, 1] 내림차순

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)  # [9, 1, 8, 2, 3, 1]
```
> 모두 외우지 말고 찾아서 쓰세요 

## 복사 
### 데이터 타입과 복사 
- 파이썬에서는 데이터의 분류에 따라 ***복사***가 달라짐
- "변경 가능한 데이터 타입"과 "변경 불가능한 데이터 타입"을 다르게 다룸 

```python
# 리스트 == 가변데이터
a = [1, 2, 3, 4]
b = a 

b[0] = 100
# b[0] -> a를 바라보고 있기 때문에 a[0]을 따라감 (같은 주소였기 때문) - 가변 데이터이기 때문

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]

# int 
a = 100
b = a

b = 9 # b만 9로 재할당 - 새로운 주소 (불변 데이터 때문)

print(a) # 100
print(b) # 9 

```

## 복사 유형 - 반드시 내용을 알아야 함 
- 프로그램이 에러 메시지 없이 돌아감 : 
- 기대한 결과가 나오지 않을 수 있음 
- 반드시 내용을 알아야 함 

1. 할당 (Assignment)
- 리스트 복사 예시
  - 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
1. 얕은 복사 (Shallow copy)
- 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재
- 얕은 복사의 한계 : 
  - 2차원 배열과 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우
  - 내부 객체의 주소는 얕은 복사 시 결국 같은 주소를 가짐 <br> 함께 변경됨
1. 깊은 복사 (Deep copy)
- `import copy`
- `copied_list = copy.deepcopy(original_list)`
- 내부에 중첩된 모든 객체까지 새로운 주소를 참조
- 완전히 새로운 주소로 복사됨 
- 모습만 같음

```python 
# 할당 
original_list = [1, 2, 3, 4]
copy_list = original_list

copy_list[0] = 'hello'
print(original_list) ['hello', 2, 3, 4]

# 얕은 복사 - 슬라이싱 - 잘라서 새로운 리스트로 반환 - 주소가 완전히 다른 리스트다
a = [1, 2, 3]
b = a[:]

b[0] = 100

print(a) # [1, 2, 3]
print(b) # [100, 2, 3] 

# 얕은 복사의 한계 - 2차원 배열에서 b의 3번째 요소의 값은 다시 a의 3번째 요소를 바라보고 있음 = 주소가 동일함 
a = [1, 2, [100, 200]]
b = a[:]

b[2][0] = 999
print(a) # [1, 2, [999, 200]]
print(b) # [1, 2, [999, 200]]

# 깊은 복사 - 완전히 새로운 주소로 복사됨 - 모습만 같음 
import copy 

original_list = [1, 2, [1, 2]]
copied_list = copy.deepcopy(original_list)
copied_list[2][0] = 999

print(original_list) # [1, 2, [1, 2]]
print(copied_list) # [1, 2, [999, 2]]

```

### 문자열에 포함된 문자들의 유형을 판별하는 메서드
- 숫자의 범위에 따라 다름 
- 필요할 때 판단해서 볼 것 
  - `isdecimal()` : 모두 숫자인지 (지수X)
  - `isdigit()` : 유니코드 숫자로 인식 (분수X)
  - `isnumeric()` : 분수, 지수, 루트 기호도 숫자로 인식 (음수, 소수 불가)



#### JSON 파일에 있는 데이터를 열어서 조작하고 반환 
#### books.json -> import books (X)



>### it 면접 이야기 
> 자신감 있게 면접에 임할 것 - 매우 중요 
>
> but 블러핑과 거짓말은 하지 말 것 
>
> 거짓말에 대한 높은 기준을 가지고 있는 면접관 분들이 많음 
>
> 거짓말은 팀에 손해를 가져올 수 있음 
>
> 시험도 마찬가지임 - 태도가 중요함 
>
> 정직 