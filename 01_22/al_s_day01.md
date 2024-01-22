# 알쓰탈출 day 01
- 문제 ~
- 어떤 방식으로 접근했는지
- 무슨 오류 나서
- 어떻게 해결했는지 
- 그거 보고 배운 점 

## 1157 : 단어공부 
### 접근
- 대소문자 구분 없이 단어에서 가장 많이 사용된 알파벳 출력
- 시간초과 
- 새로 접근이 필요했으나 마지막 문제라 시험공부를 위해,, 넘김
```python
word = input().upper()
length = len(word)

if length == 1 :
    print(word)
    exit()

char_list = []
count_list = []

for i in range(length) : 
    char_list.append(word[i])

for i in char_list :
    count_list.append(int(word.count(i)))

# print(char_list)
# print(count_list)

best_num = 0
best_char = ''
best_index = 0

for i in range(length) : 
    if best_num < count_list[i] :
        best_num = count_list[i]
        best_char = char_list[i] 

    elif i == length -1 : 
        print(best_char)
        exit()

    elif best_num == count_list[i] and best_char == char_list[i] :
        continue
    
    else : 
        print('?')
        exit()
```

## 2652 최대값 
### 접근
- 런타임 에러 (NameError)
- 에러 이유를 모르겠음 
```python
biggest = input()

for i in range(8) : 
    rival = input()
    if biggest < rival :
        biggest = rival
        location = i + 2

print(biggest)
print(location)
```

## 10250 ACM 호텔 
### 접근 
- 런타임 에러 (NameError)
- 에러 이유를 모르겠음 
```python
count = int(input())

for i in range(count) : 
    H, W, N = map(int,input().split())
    floor = N % H
    walk = N // H + 1
    
    if walk < 10 : 
        walk_str = str(walk)
        walk_str = walk_str.zfill(2)

    floor_str = str(floor)
    result = int(floor_str+walk_str)
    
    print(result)
```

## 

## 8958 OX퀴즈
### 요약 
- 수가 정해진 다수의 OX출력에서 O값에 따라 달라지는 점수 출력 
### 접근 
- 첫 라인에 전체 데이터 수가 주어졌기 때문에 우선 그만큼 루프를 넣음 
- 리스트에 OX 스트링을 분리하여 요소를 넣음 
- 전체 점수, O의 개수를 세는 수를 따로 마련
- 첫 번째 경우의 수를 따로 지정 
- 두번째 부터 반복하며 이전까지 반복된 O의 개수에 따라 카운트 증가하며 점수를 더함
- X일 경우 카운트 초기화

```python 
N = int(input())

for i in range(N) :
    answer_list = []
    quiz = input()

    for i in quiz : 
        answer_list.append(i)

    answer_number = len(answer_list)
    score = 0
    counts = 0

    if answer_list[0] == 'O' :
        counts = 1
        score += counts

    for num in range(1,answer_number) :
        if answer_list[num] == 'O' :
            counts += 1
            score += counts
        elif answer_list[num] == 'X' :
            counts = 0

    print(score)
```
### 배운 점 
- 처음에 카운트를 넣지 않고 코드를 짜려다 첫번째 케이스를 따로 분리하게 됨
- 이제 보니 필요없는 코드였음 
- 쭉 읽어보고 제출하자

## 2675 : 문자열 반복
- 첫째줄에 데이터 개수, 두번째부터 공백으로 분리된 반복횟수, 문자열이 주어짐
### 접근 

```python
times = int(input())

for i in range(times) : 
    counts, input_str = input().split()
    counts = int(counts)
    for char in input_str : 
        print(char*counts, end="")
    print("")
```
### 배운 점 
- end=''로 출력하는 경우 총 출력할 데이터의 개수가 2개이기 때문에 <br> 마지막에 print('')을 한번 더 붙여서 각 케이스를 분리해줘야한다

## 3052 나머지 
### 요약
- 수 10개를 입력받아 42로 나눈 나머지 중 서로 다른 값의 개수 출력 

### 접근
- 10개의 수라는 것을 알고 있으니 10번 루프함 
- 수를 입력받고 나머지를 리스트에 각각 저장
- 리스트를 세트로 만들어 중복 제거 
- 세트의 길이 출력 

```python
reminder_list = []

for i in range(10) :
    reminder = int(input()) % 42
    reminder_list.append(reminder)

reminder_set = set(reminder_list)
print(len(reminder_set))
```
### 배운 점
- 리스트 세트로 쉽게 만들어서 중복 제거하는 것 (오늘 실습에 활용함)

## 2920 : 음계 

### 접근 
- 전체 입력값을 각각 리스트화 
- 처음에는 각 요소를 순회하며 비교하려고 생각했지만, <br> 오히려 어렵게 접근하고 있다고 생각하여 방향 선회
- 리스트를 각각 오름차순, 내림차순 정렬하여 새로운 리스트를 2개 만들고 각각 비교하여 if문으로 출력함 


```python
scale_list = list(map(int, input().split()))

sorted_scale = sorted(scale_list)
reversed_scale = sorted(scale_list,reverse=True)

if scale_list == sorted_scale :
    print('ascending')
elif scale_list == reversed_scale : 
    print('descending')
else : 
    print('mixed')
```
### 배운 점 
- 답이 안나오는 경우 처음부터 다시 접근하자.
- 의외로 쉽게 풀릴 수 있다

## 10809 알파벳 찾기 
### 요약
- 알파벳 소문자 단어에서 포함된 index, 없을 경우 -1 출력 
### 접근 
- 오늘 배운 `s.find()` 사용하면 되는 문제
- 몰라서 `s.index()` 찾아 사용하고, 오류는  `try - except` 로 대처하며 -1을 출력하도록 함 

```python 
word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz' # 26

for char in alphabet :
    try :
        index_alphabet = word.index(char)
        print(index_alphabet, end=' ')
    except : 
        print('-1', end=' ')
```
### 배운 점 
- 오류 날 경우 try-except 로 대처하는 법 
- 무턱대고 사용하다가는 오히려 결과가 이상해질 수 있겠다는 생각
- 메서드 잘 찾아보고 사용하자

## 