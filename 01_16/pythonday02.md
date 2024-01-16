# python day 02

## Data type 
값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성 

### int 정수 자료형
### float 실수 자료형
### str 문자열 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형 

## Sequence types ( str, list, tuple, range )
여러 개의 값들을 순서대로 나열하여 저장하는 자료형

1. 순서 sequence - 정렬 X
2. 인덱싱 indexing 
3. 슬라이싱 slicing 
4. 길이 length 
5. 반복 iteration 

## List 리스트 여러개의 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형

변경 가능하다 = 가변 데이터

>리스트 표현
0개 이상의 객체를 포함하여 데이터 목록을 저장

대괄호 `[]` 로 표기

데이터는 어떤 자료형도 저장할 수 있음 

리스트 안에 리스트도 저장할 수 있다 

슬라이싱을 할 때 쓰는 대괄호는 문법이고 리스트가 아님 

다른 곳에서는 배열 array 라고 부름 

```python
my_list = [1,'a',3,'b',5]
#인덱싱 
print(my_list[1])
#슬라이싱 
print(my_list[2:4])
print(my_list[0:5:2])
print(my_list[::-1])
#길이 
print(len(my_list))

my_list = [1,2,3,'python',['hello','world','!!!']]
print(len(my_list))  # 5
print(my_list[4][-1])  # !!!
print(my_list[-1][1][0])  # w
```

- 리스트는 가변 (변경 가능)

```python
my_list [1,2,3]
my_list[0] = 100
# 100이 my_list 0번째에 새로 할당됨
```

## tuple 튜플 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형

0개 이상의 객체를 포함하며 데이터 목록을 저장

소괄호 `()` 로 표기 

데이터는 어떠한 자료형도 저장할 수 있음

```python
my_tuple_1 = ()
my_tuple_2 = (1,)
# (1) -> 1 (int)

my_tuple_3 = (1, 'a', 3, 'b', 5)
#인덱싱 
print(my_tuple_3[1])
#슬라이싱 
print(my_tuple_3[2:4])
print(my_tuple_3[0:5:2])
print(my_tuple_3[::-1])
#길이 
print(len(my_tuple_3))

my_tuple_3[1] = 'z'
# TypeError : 'tuple' object does not support item assignment
```

tuple은 목적이 제한적으로 정해져 있음 

> python의 내부 동작에서 주로 사용됨 
> 
> 불변 특성을 사용하여 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등 

```python
# (10, 20) 튜플로 처리됨 
x , y = (10, 20) 

#파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능 
x, y = 10, 20
```

튜플보다 리스트를 90% 이상 사용하게 될 것임 

## range 연속된 **정수 시퀀스를 생성**하는 *변경 불가능*한 자료형 

- 함수를 쓰는 것처럼 표현함 
- range(n) : 
  - 0 부터 n-1까지의 숫자 시퀀스 
- range (n , m) : 시작점을 정할 수 있음
  - n 부터 m-1까지의 숫자 시퀀스

> 왜 n-1 일까 ?
>
> 프로그래밍에서는 0부터 시작이기 때문
> 
> 총 n개를 만드려면 n-1개여야 함 

```python
my_range_1 = range(5)
my_range_2 = range(1,10)

print(my_range_1) # range(0, 5)
print(my_range_2) # range (1, 10)

#리스트로 형 변환 시 데이터 확인 가능 

print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

```
### 0, 1, 2, 3, 4 라는 식으로 우리 눈에 보이지 않음
### 주로 반복문과 함께 사용함 - 반복 횟수가 정해져 있기 때문 
### 타입을 변환하여 사용하기도 함 - 리스트, 튜플 

str list tuple range 

## Non - sequence Types

## dict 딕셔너리 : key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

1. key - value 
2. 순서가 없음 
3. 중복이 없음 
4. 변경 가능함 

- key 는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range ...)
- value 는 모든 자료형 사용 가능 
- 중괄호 `{}` 로 표기

```python
my_dict_1 = {'key':'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

```
> 딕셔너리는 순서가 없음 
>
> 순서가 없기 때문에 인덱스로 접근 불가능 
>
> **반드시 key를 통해서 value 값을 얻어내야 함**
>
> key가 중복이 안되기 때문에 마지막에 넣은 값이 value가 됨

```python
my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3]

# 값은 변경-재할당 가능 
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3]}

# key가 중복이 안되기 때문에 마지막에 넣은 값이 value가 됨
my_dict = {
    'apple': 100, 
    'list': [1, 2, 3],
    'apple' : 12
}
print(my_dict) #{'apple': 12, 'list': [1, 2, 3]}
```

## set 세트 : 순서와 중복이 없는 변경 가능한 자료형

- 수학에서의 집합과 동일한 연산 처리 가능 
- 중괄호 `{}`로 표기 
- 빈 값의 세트를 만들고 싶으면 `set()` 사용해야 함 

```python
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1) # set()
# 순서가 없다, 인덱스 접근이 안된다
print(my_set_2) # {1, 2, 3}
# 세트는 중복이 안된다
print(my_set_3) # {1}
```
> 순서가 없다, 인덱스 접근이 안된다
>
> 세트는 중복이 안된다
>
> 집합 연산이 가능하다 
>

```python
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

#합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}
#차집합
print(my_set_1 - my_set_2) # {1, 2}
#교집합
print(my_set_1 & my_set_2) # {3}

```
> 목적이 확실한 타입 
>
> 집합 연산이 필요한 경우 쓰임 
>
> 혹은 중복을 간단하게 제거하고 싶은 경우
>
> 다만 순서가 없기 때문에 
> 
> 중복 제거를 위해 세트를 활용하면 순서가 없어져버릴 수 있음 

## Other Types 

## None '값이 없음'을 표현하는 자료형

- a = 0 은 값이 없음 이 아님 
```python
variable = None
print(variable) # None
```
## Boolean 참( True )과 거짓( False )을 표현하는 자료형

- True, False 
- 비교, 논리 연산의 평가 결과로 사용됨
- 주로 조건문, 반복문과 함께 사용

```python
bool_1 = True
bool_2 = False 

print(bool_1) # True
print(bool_2) # False
print(3 > 1) # True
print('3' != 3) # True
```

시퀀스와 넌시퀀스 타입의 공통점 = 여러개의 항목 또는 요소를 담는 자료구조
## Collection 여러개의 항목 또는 요소를 담는 자료구조 
## str, list, tuple, set, dict

|컬렉션|변경가능여부|순서여부|
|---|---|---|
|str|X|O|
|list|O|O|
|tuple|X|O|
|set|O|X|
|dict|O|X|


### 불변과 가변의 차이 
> 파이썬 튜터 결과 
> 문자열은 문자열 통째로 하나로 들어가 있음 - 주소가 바뀔 수 없음 
> 리스트는 리스트 공간을 바라보고 있고 인덱싱 항목이 각 요소를 바라보고 있음 

## Type Conversion 형변환 = 타입 변환

### Implicit Type Conversion 암시적 형변환 - 파이썬이 자동으로 변환
- Boolean 과 Numeric Type 에서만 가능 
```python
print(3 + 5.0) # 8.0

# Boolean + Numeric -> Boolean이 Numeric으로 변환
print (True + 3) # 4

# True = 1, False = 0
print (True + False) # 1
```


### 명시적 형변환 - 개발자가 의도적으로 변환, 암시적 형변환이 아닌 다른 모든 경우 

- str -> integer : 형식에 맞는 숫자만 가능 
- integer -> str : 모두 가능 
```
print(int('1')) # 1

print(str(1) + '등') # 1등

print(float('3.5')) # 3.5

print(int(3.5)) # 3

# print(int('3.5')) <<< ValueError 
```
### 컬렉션 간 형변환 정리
|              	|     str    	|           list         	|         tuple        	|     range    	|          set         	|     dict    	|
|:------------:	|:----------:	|:----------------------:	|:--------------------:	|:------------:	|:--------------------:	|:-----------:	|
|      str     	|            	|            O           	|           O          	|       X      	|           O          	|       X     	|
|      list    	|      O     	|                        	|           O          	|       X      	|           O          	|       X     	|
|     tuple    	|      O     	|            O           	|                      	|       X      	|           O          	|       X     	|
|     range    	|      O     	|            O           	|           O          	|              	|           O          	|       X     	|
|      set     	|      O     	|            O           	|           O          	|       X      	|                      	|       X     	|
|      dict    	|      O     	|     O       (key만)    	|     O     (key만)    	|       X      	|     O     (key만)    	|             	| 


## 연산자 
지금까지는 피연산자를 다뤘음 

피연산자 = 값

값은 연산자와 함께 쓰임 

### 산술 연산자 

|     기호    	|           연산자          	|
|:-----------:	|:-------------------------:	|
|       -     	|         음수   부호       	|
|       +     	|            덧셈           	|
|       -     	|            뺄셈           	|
|       *     	|            곱셈           	|
|       /     	|           나눗셈          	|
|      //     	|     정수   나눗셈 (몫)    	|
|       %     	|           나머지          	|
|      **     	|      지수   (거듭제곱)    	|

### 복합 연산자
- 연산과 할당이 함께 이뤄짐

|     기호    	|                  	|                     	|
|:-----------:	|:----------------:	|:-------------------:	|
|      +=     	|      a   += b    	|      a   = a + b    	|
|      -=     	|      a   -= b    	|      a   = a - b    	|
|      *=     	|      a   *= b    	|      a   = a * b    	|
|      /=     	|      a   /= b    	|      a   = a / b    	|
|      //=    	|     a   //= b    	|     a   = a // b    	|
|      %=     	|      a   %= b    	|      a   = a % b    	|
|      **=    	|     a   **= b    	|     a   = a ** b    	|


### 비교 연산자

|       기호      	|         내용       	|
|:---------------:	|:------------------:	|
|         <       	|         미만       	|
|        <=       	|         이하       	|
|         >       	|         초과       	|
|        >=       	|         이상       	|
|        ==       	|         같음       	|
|        !=       	|     같지   않음    	|
|        is       	|         같음       	|
|     is   not    	|     같지   않음    	|

## 할당과 같음 
- = : 할당 
- == : 같음 

### is 와 is not 
- 값을 비교 하는게 아님 
- 메모리 주소 를 비교 
- 메모리 내에서 같은 객체를 참조하는지 확인
- == 는 동등성 (equality), is 는 식별성 (identity)
- 값을 비교하는 == 와 다름 
- **값이 아니라 None, True, False 를 비교할 때 주로 사용**

```python
print(3 > 6)  # False
print(2.0 == 2)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False

# SyntaxWarning
# ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(주소)를 비교하기 때문
# is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용
print(2.0 is 2)  # False
print(1 == True) # True 암시적 형변환
print(1 is True) # False 
```

### 논리 연산자

|     기호    	|      연산자     	|                                        내용                                       	|
|:-----------:	|:---------------:	|:---------------------------------------------------------------------------------:	|
|      and    	|      논리곱     	|       두   피연산자 모두 True인   경우에만      전체   표현식을 True로   평가     	|
|      or     	|      논리합     	|     두   피연산자 중 하나라도 True인   경우      전체   표현식을 True로   평가    	|
|      not    	|     논리부정    	|                               단일   피연산자를 부정                              	|

```python
print(True and False) # False

print(True or False) # True

print(not True) # False

print(not 0) # True 암시적 형변환 

num = 15
result = (num > 10) and (num % 2 == 0)
print(result) # False


name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result) # True
```
## 단축평가 
### 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작 

- False and T/F : False 
- True or T/F : True 

```python
vowels = 'aeiou'
# b in vowels 뒤까지 평가가 됨
print(('a' and 'b') in vowels)  # False 
# a in vowels 뒤까지 평가가 됨
print(('b' and 'a') in vowels)  # True 

# 5 뒤까지 평가가 됨
print(3 and 5)  # 5 
# 3 뒤까지 평가가 됨
print(3 and 0)  # 0 
# 0 앞에서 평가가 끝남 - 암시적 형변환 False 
print(0 and 3)  # 0 
# 0 앞에서 평가가 끝남 - 암시적 형변환 False
print(0 and 0)  # 0 

# 5 앞에서 평가가 끝남 
print(5 or 3) # 5 
# 3 앞에서 평가가 끝남
print(3 or 0) # 3 
# 3 뒤까지 평가가 됨
print(0 or 3) # 3 
# 0 뒤까지 평가가 됨
print(0 or 0) # 0 
```
### 단축평가 동작
- and
    - 첫 번째 피연산자가 False인 경우, 전체 표현식은 False로 결정. <br>두 번째 피연산자는 평가되지 않고 그 값이 무시
    - 첫 번째 피연산자가 True인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정. <br>두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
- or
    - 첫 번째 피연산자가 True인 경우, 전체 표현식은 True로 결정. <br>두 번째 피연산자는 평가되지 않고 그 값이 무시
    - 첫 번째 피연산자가 False인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정. <br>두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환

### 단축평가 이유
코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함

### 멤버십 연산자
- 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인

|       기호      	|                                    내용                                  	|
|:---------------:	|:------------------------------------------------------------------------:	|
|        in       	|        왼쪽   피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인      	|
|     not   in    	|     왼쪽   피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인    	|

```python
word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word)  # True
print('z' in word)  # False

print(4 not in numbers)  # False
print(6 not in numbers)  # True
```
### 시퀀스형 연산자
- `+` 와 `*` 는 시퀀스 간 연산에서 산술 연산자일때와 다른 역할을 가짐
- 시퀀스와 시퀀스간 연산을 할 때 

|     연산자    	|          내용        	|
|:-------------:	|:--------------------:	|
|        +      	|     결합   연산자    	|
|        *      	|     반복   연산자    	|

```python
# Gildong Hong
print('Gildong' + ' Hong')

# hihihihihi
print('hi' * 5)

# [1, 2, 'a', 'b']
print([1, 2] + ['a', 'b'])

# [1, 2, 1, 2]
print([1, 2] * 2)
```

## 연산자 우선순위

|     우선순위    	|             연산자            	|               내용             	|
|:---------------:	|:-----------------------------:	|:------------------------------:	|
|       높음      	|               ()              	|        소괄호   grouping       	|
|                 	|               []              	|        인덱싱,   슬라이싱      	|
|                 	|               **              	|             거듭제곱           	|
|                 	|             +,   -            	|     단항   연산자 양수/음수    	|
|                 	|          *,   /, //, %        	|          산술   연산자         	|
|                 	|             +,   -            	|          산술   연산자         	|
|                 	|     <,   <=, >, >=, ==, !=    	|          비교   연산자         	|
|                 	|          is,   is not         	|           객체   비교          	|
|                 	|          in,   not in         	|         멤버십   연산자        	|
|                 	|               not             	|           논리   부정          	|
|                 	|               and             	|            논리   AND          	|
|       낮음      	|               or              	|            논리   OR           	|

# 하늘쌤 보충 

`if (5 > 3) # True`

### print 가 붙을 경우 결과값이 아니고 평가한 피연산자를 기준으로 생각함 
`('a' and 'b')`
- a 가 True, b 까지 평가해야함 
- 마지막에 평가한 피연산자인 b 가 리턴

`('b' and 'a')`
- b 가 True, a 까지 평가해야함 
- 마지막에 평가한 피연산자인 a 가 리턴

`('b' or 'a')`
- b 가 True 
- 뒤까지 평가할 필요 없으므로 b 가 리턴 

### Sequence Types 특징 
- 반복에 많이 쓰인다 
- 길이를 알아야 한다 

## List 
- 결과값을 도출하려면 인덱싱을 어떻게 해야하지? 를 공부해야함 
- 리스트는 가변이다, 변경 가능하다 
- list.append()

## tuple 변경이 되면 안되는 값들 - ex.역사데이터 
- 인덱싱 조회는 가능함 
- 슬라이싱도 가능

## range start number 와 end number 사이에 순서가 있는 정수 시퀀스를 생성  
- 굉장히 많이 쓴다
- range(startnum, endnum, step)
- 메모리를 활용하는 파이썬의 현명한 방법
> range (0,4) -> 0, 1, 2, 3
>
> list [0,1,2,3] -> 0, 1, 2, 3 
- range는 순서대로 생성하는구나 라고 하는 정보만 기억함 
- list는 모든 숫자를 다 만들음 
- range가 훨씬 더 비용이 적게 든다 
- **메모리를 효율적으로 사용함**
- **일일이 타이핑하는 수고가 없다**
- range는 리스트인 것처럼 동작하지만 사실 리스트가 아님
- 이터레이트할 때 원하는 시퀀스 항목들을 돌려주는 객체이지만 실제로 리스트를 만들지 않아서 공간을 절약한다 

## dict 
- 리스트는 고객명만 있는 자료구조 
- 생각해보면 현실에 있는 데이터는 레코드 : 이름도 있고, 소비금액, 주소, 전화번호 등...
- 현실의 자료는 하나의 자료에 많은 관계들이 묶여져 있음 
- 그런것들을 자연스럽게 연결할 수 있음 
- 중심에서 연결되는 정보들이 있음 (나 - 전화번호, 주소, 구매항목 등)

`dict_ = { '문재성' : ['010-xxxx-xxxx','서울시 성동구 성수1동',209,365,900],'김싸피' : [], '박삼성' : {}}`

- C : dict()
- R : 리스트는 index, dict는 key->value
- U : update 가능 
- D : del 

- 그래프 풀 때 좋음 

## set 중복이 없음 
- 나는 중복이 없다고 생각하고 있음 
- 100만가지 데이터는 dump-in 된 데이터들 : 사람이 확인할 수 없음 
- set이 없다면 100만번 돌려야 전체 check가 가능함 
- set으로 돌리면 99만 7500 등의 결과가 나올 수 없음 


