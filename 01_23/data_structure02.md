# python day 06
## 비시퀀스 데이터 구조 - 세트, 딕셔너리 

### 메서드

## 비시퀀스 데이터 구조 : 순서 X, 인덱스 접근, 슬라이싱 불가

### 세트 : 집합연산에서 주로 활용 - 데이터 중복 X
- 고유한 항목들의 정렬되지 않은 컬렉션 (중복X, 순서X)
- 잘 쓰면 진짜 좋은 자료구조다 (다른 언어에는 잘 없음)
- 쓰면 멋져보이는 치트키 같은 느낌 - 짧은 코드로 구현가능

- `s.add(x)` : 세트 s에 항목 x를 추가. 이미   x가 있다면 변화 없음
- `s.clear()` : 세트 s의 모든 항목을 제거
- `s.remove(x)` : 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Key error
- `s.pop()` : 세트 s에서 임의의 요소를 제거하고 반환 (순서-인덱스가 없음)
- `s.discard(x)` : 세트 s에서 항목 x를 제거. remove와 달리 에러 없음
- `s.update(iterable)` : 세트 s에 다른 iterable 요소를 추가

```python
my_set = {} # 빈 딕셔너리 

my_set = {'a', 'b', 'c', 1, 2, 3} 
print(my_set) # 세트는 순서가 존재하지 않음 {1, 2, 3, 'c', 'a', 'b'}

# add 
my_set.add(4) 
print(my_set) # {'b', 1, 2, 3, 'c', 4, 'a'}

# 중복이 되지 않음 
my_set.add(4)
print(my_set) # {'b', 1, 2, 3, 'c', 4, 'a'}

# remove
my_set.remove('a')
print(my_set) # {1, 2, 3, 'c', 'b', 4}

my_set.remove('z') # KeyError: 'z'

# clear
my_set.clear()
print(my_set) # set() - 빈세트 출력

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # random element 

# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set) # {1, 2, 3, 4, 5, 'a', 'b', 'c'}

# discard
my_set.discard(1)
print(my_set) # {2, 3, 4, 'c', 5, 'a', 'b'}

my_set.discard('z')
print(my_set) #{2, 3, 4, 'c', 5, 'a', 'b'}

```

### 세트의 집합 메서드 

- `set1.difference(set2)` == `set1 – set2` : set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환
- `set1.intersection(set2)` == `set1 & set 2` : set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환
- `set1.issubset(set2)` == `set1 <= set2` : set1의 항목이 모두 set2에 들어있으면 True를 반환
- `set1.issuperset(set2)` == `set1 >= set2` : set1가 set2의 항목을 모두 포함하면 True를 반환
- `set1.union(set2)` == `set1 | set2` : set1 또는 set2에(혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환


```python
# difference
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1 - set2) # {0, 2, 4}

# intersection
print(set1.intersection(set2)) # {1, 3}
print(set1 & set2) # {1, 3}

# issubset
print(set1.issubset(set2)) # False
print(set1 <= set2) # False

# issuperset
print(set1.issuperset(set2)) # False
print(set1 >= set2) # False
print(set1.issuperset(set3)) # True

# union
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
print(set1 | set2) # {0, 1, 2, 3, 4, 5, 7, 9}

```

## 딕셔너리 
- 파이썬에서 리스트 다음으로 중요함 
- 리스트는 리니어 검색 
- 딕셔너리는 해시 방식으로 바로 찾을 수 있음

#### 딕셔너리 메서드

- `D.clear()` : 딕셔너리 D의 모든 키/값 쌍을 제거
- `D.get(key)` : 키 k에 연결된 값을 반환 (키가 없으면 None을 반환)
- `D.get(key[,default])` : 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값을 반환
- `D.keys()` : 딕셔너리 D의 키를 모은 객체를 반환 - - 대괄호로 묶여있음 - 반복이 가능한 객체임
- `D.values()` : 딕셔너리 D의 값을 모은 객체를 반환
- `D.items()` : 딕셔너리 D의 키/값 쌍을 튜플로 모은 객체를 반환
- `D.pop(key[,default])` : 딕셔너리 D에서 key를 제거하고 연결됐던 값을 반환 (없으면 오류 또는 Default를 반환)
- `D.setdefault(key[,default])` : 딕셔너리 D에서 key와 연결된 값을 반환 <br> key가 D의 키가 아니면 default값과 연결한 key를 D에 추가하고 default를 반환
- `D.update(other)` : other가 제공하는 키/값 쌍을 딕셔너리 D에 추가 <br>
기존 키는 덮어씀 (키워드 인자로 가능)

```python
# clear
dict = {
    'name' : 'Alice', 
    'age' : 25
    }
dict.clear()
print(dict) # {}

# get
dict = {'name' : 'Alice', 'age' : 25}

print(dict.get('name')) # 'Alice'
print(dict['name']) # 'Alice' - 같은 값을 반환하지만, 키가 없을 때 얘는 에러남

print(dict.get('country')) # None
print(dict.get('country', 'unknown')) #'unknown'

# keys
print(dict.keys()) # dict_keys(['name', 'age']) 
# 파이썬 내부적으로 키를 모은 데이터 타입 - 대괄호로 묶여있음 - 반복이 가능한 객체임
for key in dict.keys() : 
    print(key) # 'name'\n'age'

# values
print(dict.values()) # dict_values(['Alice', 25])

for value in dict.values() :
    print(value) # 'Alice'\n'25'

# items
print(dict.items()) # dict_items([('name', 'Alice'), ('age', 25)])

for key, value in dict.items() : # 언패킹
    print(key, value) # 'name Alice'\n'age 25'

# pop 
print(dict.pop('age')) # 25
print(dict) # {'name': 'Alice'}

print(dict.pop('country')) #KeyError
print(dict.pop('country', None)) # None

# setdefault 
print(dict.setdefault('country', 'Korea'))
print(dict)

# update 
other = {'name': 'Jane', 'gender': 'Female'}

dict.update(other) # 겹치는건 덮어씌우고 나머지는 추가됨
print(dict) # {'name': 'Jane', 'age': 25, 'country': 'Korea', 'gender': 'Female'}

dict.update(age=50, country='Brazil')
print(dict) # {'name': 'Jane', 'age': 50, 'country': 'Brazil', 'gender': 'Female'}

```

## 참고 - 중요, 집중 !!! 

### set.pop() : 임의의 원소를 반환하지만 1 이 많이 나왔음 - 왜?

## 해시 테이블 Hash Table
- 해시 함수를 사용하여 변환한 값을 index 로 삼아 key 와 data 를 저장하는 자료구조
- 데이터를 효율적으로 저장하고 ***검색***하기 위해 사용 

### 해시 테이블 원리 

- 키를 해시 함수를 통해 해시 값으로 변환하고, <br> 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색
- 해시 값을 인덱스로 이용하기 때문에 바로 이루어짐 - 순서가 상관이 없음 
- 데이터 검색이 매우 빠르게 이루어짐 

```python
# 반드시 선형검색을 통해 찾아야 함
list = [
    {'john : '521-1234'},
    {'Lisa' : '521-8976'},
    {'Sandra' : '521-9655'}
    ]

# 데이터 개수와 상관없이 어느 위치에 있든지 바로 찾아낼 수 있음
dict = {
    'john : '521-1234', 
    'Lisa' : '521-8976', 
    'Sandra' : '521-9655'
    }

```

## 해시 Hash
- 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것 
- input을 통해 고정된 크기의 고유한 output (지문) 출력
- 주로 해시 테이블 자료구조에 사용되며, 매우 빠른 데이터 검색을 위한 컴퓨터 소프트웨어에서 유용하게 사용 

### set의 요소 & dictionary의 키와 해시테이블의 관계
- 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장함
- 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨 
- 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장
  - 따라서 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음

```python
# 정수는 값 자체가 곧 고정된 해시 값
# 문자열은 실행될 때마다 해시 값이 다름 - 임의 
# 해시 테이블에 저장된, 나열된 순서로 pop 
# pop 해시 테이블에서 먼저 있는 값부터 출력
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}

print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)

# 1
# 2
# 3
# 100
# 4
# 39
# 9
# 10
# 52
# 87
# set()




# 해시 함수
print(hash(1)) # 1
print(hash(1)) # 1
print(hash('a')) # 실행시마다 다름 2769248058043525804
print(hash('a')) # 실행시마다 다름 -5872889763149410245

```
### 파이썬에서의 해시 함수
- 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
- 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름 

### 파이썬에서의 해시 함수 - 문자열
- 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산
- 이로 인해 문자열의 해시 값은 실행시마다 다르게 계산됨 
  
### set의 pop 메서드의 결과와
- pop 메서드는 set에서 임의의 요소를 제거하고 반환
- 실행할 때마다 다른 요소를 얻는다는 의미에서 "무작위"(Random)가 아니라 
- 임의 라는 의미에서 "무작위"(임의)
  - By 'Arbitrary' the docs don't mean 'Random'
- 해시 테이블에 나타나는 순서대로 반환하는 것 

### hashable 
- hash() 함수의 인자로 전달해서 결과를 반환 받을 수 있는 객체를 hashable 이라 함
- 대부분의 불변형 데이터 타입은 hashable
- 단, tuple 의 경우 불변형이지만 해시 불가능한 객체를 참조할 때는 tuple 자체도 해시 불가능해지는 경우가 있음

### Hashable 과 불변성 간의 관계
- 해시 테이블의 키는 불변해야 함 
  - 객체가 생성된 후에 그 값을 변경할 수 없어야 함
- 불변 객체는 해시 값이 변하지 않으므로 동일한 값에 대해 일관된 해시 값을 유지할 수 있음
- 단, hash 가능하다 != 불변하다 

### 가변형 객체가 hashable 하지 않은 이유
- 값이 변경될 수 있기 때문에 동일한 객체에 대한 해시 값이 변경될 가능성이 있음 (해시테이블의 무결성 유지 불가)
- 가변형 객체가 변경되면 해시 값이 변경되기 때문에, 같은 객체에 대한 서로 다른 해시 값이 반환될 수 있음 (해시 값의 일관성 유지 불가)

### hashable 객체가 필요한 이유
1. 해시 테이블 기반 자료 구조 사용
   - set와 dict의 키
   - 중복 값 방지
   - 빠른 검색과 조회

2. 불변성을 통한 일관된 해시 값
3. 안정성과 예측 가능성 유지

# 보충
## 학습하는 방법 - 효과적인 학습곡선 
- 나만의 효율적인 방법 : 연필? Handwriting? Typing? 
- 블룸의 교육목표 분류 (namuwiki) - Bloom's Taxonomy - Cognitive Domain
- 암기하고 설명할 수 있는 정도로 학습할 것 
- 효과적인 학습곡선

###  ***실습 코드를 부지런히 따라하라***
- 기능을 어떻게 구현하는지를 직접 실습해야, 체화, 각인 - 설명까지 가능할 수 있다 
- 앞으로 점점 라이브 때 코드들이 많이 나올 텐데, 실습을 직접 해야 는다 

### 정보 저장과 검색 
- 고객 정보를 빨리 검색하는게 중요한 이슈 
- sorting and search 
- 다양한 방법 중 하나가 hash : 고유값을 만들기 위함 
- git commit id 가 hash 값임 

### Hash 값 
- 3 자리 hash 값을 찾는다 : 정수일 경우 10e3 
- git commit id : 16자리, 알파벳도 가능 : 36e16
- 너무나 많은 자료 중 검색을 빨리 하기 위해서
- 고유한 값을 만들기 위해서 
- 모든 문제의 답은 아니지만 대부분의 DB에서 적용중임 

### 메서드 사용법
Dict.get(key) None 
Dict.["key"] Error 
- id 는 고유한 값 : Error시에는 서비스 전체 다운으로 접근이 안됨, None을 리턴하고 존재하지 않습니다 라고 보여주는 기능 구현해야함 
- 딕셔너리에 접근할 수 있는 사람들이 너무 중요해서 아닌 사람들이 접근했을 경우 프로그램을 멈추는 것이 더 좋은 의사결정일 때 - 극비보안문서를 다루는 서비스, - 권한 있는 사람만 접근해야함 

```python
id = input("id를 입력하세요.", )
# id sky 
if customer_dict.get(id) == : ...

customer_dict = {
    'id' :  , 
    'password' :  , 
    'name' : 
    }
customer_dict.keys() # dict_keys(['id', 'name']) - 미리 메모리에 올려놓지 않음
customer_dict.update() # 많이 쓰는 기능임 

```


