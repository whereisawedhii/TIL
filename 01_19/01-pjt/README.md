# 관통 Project_day01
### 02_movies 주제를 선택한 이유
- 영화 추천 알고리즘을 만든다는 전체 프로젝트의 주제가 더 끌렸음 
- 폴더 명에 스포티파이가 있어 평소 음악을 좋아하여 더 끌렸음 
- 명세서 페이지 수가 3배 가까이 차이났고, 문제 수도 2배 이상 차이가 나서 두려웠지만 <br> 더 챌린져블한 과제라고 생각했음

## 이번 project 통해 학습한 내용 
- API를 통해 서버에 데이터를 요청하여 JSON 값을 response로 받아올 수 있음
- 딕셔너리 형태의 JSON값을 다루고, 조회하여 원하는 key - value 값을 가져올 수 있음 
- 그 중 특정 key - value 값을 통해 다른 JSON를 조회하여 원하는 key - value 값을 가져올 수 있음 
- JSON 값들을 여러 개 모은 리스트에서 제어문을 사용하여 위의 작업을 수행할 수 있음 

### 문제 A

#### 요약
- 딕셔너리 형태의 JSON값에서 원하는 key - value 값만 추출하는 함수 작성 

#### 구현 결과
```python
def book_info(book):
    # 필요 정보들의 키 값들을 리스트화
    needed_info = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
    # 결과값을 담을 info 딕셔너리 생성
    info = {}

    # 딕셔너리 형태의 book.json 값에서 필요한 정보들을 info 에 저장
    for i in needed_info :
        info[i] = book[i]
    
    # 결과값 딕셔너리 info 리턴
    return info
```
#### 막혔던 부분 및 해결
- 가장 간단한 형태라 막히지 않고 진행함 

### 문제 B
#### 요약 
- A에서 필요 정보들을 가져온 후, 그 중 카테고리 id를 활용하여 <br> 다른 JSON에 있는 카테고리명을 추출 및 저장 <br> 이후 필요없어진 카테고리 id 부분은 삭제

#### 구현 결과 
```python
def book_info(book, categories_list):
    # 필요 정보들의 키 값들을 리스트화
    needed_info = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
    # 결과값을 담을 딕셔너리 info 생성 
    info = {}

    # 딕셔너리 형태의 book.json 값에서 필요한 정보들을 info 에 저장
    for i in needed_info :
        info[i] = book[i]   

    # 순회를 위해 전체 카테고리 개수 할당
    all_categories = len(categories_list)
    # 카테고리 id 만 추출하여 리스트화
    categoryId_list = info['categoryId']
    # 조회할 카테고리 id 의 개수 할당
    categories_num = len(categoryId_list)
    # 카테고리명을 저장할 리스트 생성
    categoryName_list = []

    # 카테고리id 별로 전체 카테고리에서, 카테고리id 와 일치하는 카테고리명을 리스트에 저장
    for num in range(categories_num) :
        for i in range(all_categories) :
            if categoryId_list[num] == categories_list[i]['id'] :
                categoryName_list.append(categories_list[i]['name'])
    
    # 카테고리명 리스트를 결과 딕셔너리에 추가
    info['categoryName'] = categoryName_list
    # 필요 없어진 카테고리 id 값을 결과에서 삭제 
    del info['categoryId']

    # 결과값 딕셔너리 info 리턴
    return info
```
#### 막혔던 부분 및 해결
- 반복문을 작성할 때, 개수가 아닌 직접적인 요소를 통해 순회하여 인덱싱에 실패함
  - `len()`으로 개수를 특정하여 작성하여 해결

### 문제 C
#### 요약 
- B의 방식을 여러 도서의 정보를 담은 JSON에서 반복하여 적용

#### 구현 결과 
```python
def books_info(books, categories_list):
    # 필요 정보들의 키 값들을 리스트화
    needed_info = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
    # 결과값을 담을 리스트 info_books 생성
    info_books = []
    # 반복문 작성을 위해 전체 도서의 개수 할당 
    books_num = len(books)
    # 반복문 작성을 위해 전체 카테고리의 개수 할당 
    all_categories = len(categories_list)
    
    # 전체 도서의 개수 만큼 반복 
    for counts in range(books_num) :
        # 도서 각각의 정보를 담을 딕셔너리 생성 - 반복되면서 초기화 
        info = {}

        # books.json 리스트에서 각 도서마다 필요한 정보들을 info 에 저장
        for i in needed_info :
            info[i] = books[counts][i]

        # 각 도서의 카테고리 id를 리스트화 
        categoryId_list = info['categoryId']
        # 조회할 카테고리 id 의 개수 할당 
        categories_num = len(categoryId_list)
        # 카테고리명을 저장할 리스트 생성
        categoryName_list = []
        
        # 각 도서의 카테고리 id 만큼, 전체 카테고리에서 id에 맞는 카테고리명을 추출하여 리스트에 저장
        for num in range(categories_num) :
            for i in range(all_categories) :
                if categoryId_list[num] == categories_list[i]['id'] :
                    categoryName_list.append(categories_list[i]['name'])

        # 각 도서의 카테고리명을 딕셔너리에 저장 
        info['categoryName'] = categoryName_list
        # 필요없어진 카테고리 id 를 삭제
        del info['categoryId']
        # 반복한 결과를 리스트에 저장 - 돌아가서 초기화됨 
        info_books.append(info)

    # 결과값 리스트 info_books 리턴 
    return info_books
```
#### 막혔던 부분 및 해결
- 도서 각각의 정보를 담은 info 가 초기화되지 않았음 
  - 반복문 내에서 위치를 조정하여 해결함

### 문제 D

#### 요약 
- 전체 도서의 정보를 담은 JSON 파일을 조회하여 추출한 id를 통해 <br> 도서의 세부 정보를 담은 JSON을 각각 조회
- 세부 정보에서 평점 점수를 가져와 가장 높은 평점을 가진 도서의 제목을 리턴

#### 구현 결과 
```python 
def best_book(books_list):
    # 평점 점수를 담을 리스트 생성
    score_list=[]
    # 전체 도서의 id를 추출하여 리스트화
    id_list = list(i['id'] for i in books_list)
    # 전체 도서의 제목을 추출하여 리스트화
    title_list = list(i['title'] for i in books_list)

    # 각각의 도서의 id 값을 통해 도서의 세부 정보를 조회하고, 각 평점 점수를 리스트에 할당
    for id in id_list :
        book = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(book)
        score_list.append(book_detail['customerReviewRank'])

    # 전체 도서의 개수 할당
    books_num = len(score_list)
    # [도서의 id, 도서의 평점] 으로 이루어진 리스트를 저장할 리스트 생성
    matrix = []
    # 최고 점수를 구하기 위해 원점수 생성
    best_score = score_list[0]

    # 전체 점수 리스트에서 원점수보다 큰 값이 있다면 원점수를 대체함
    for score in score_list : 
        if best_score < score :
            best_score = score

    # 최고 점수를 가진 도서의 id를 저장할 변수 생성
    best_id = None

    # 전체 도서의 개수만큼, [id, 점수]를 리스트에 저장하고, 최고 점수인 9.9 에 해당하는 id 조회
    for i in range(books_num) :
        id_score = [id_list[i] , score_list[i]]
        matrix.append(id_score)
        if matrix[-1][-1] == 9.9 :
            best_id = matrix[-1][0]
    
    # 도서 리스트에서 id를 통해 제일 높은 평점을 가진 도서의 제목을 추출 
    for i in books_list : 
        if i['id'] == best_id :
            best_title = i['title']

    # 제일 높은 평점을 가진 도서의 제목을 리턴 
    return best_title 
```
#### 막혔던 부분 및 해결
- 평점이 가장 높은 도서의 제목을 가져와야 하는 것에서 막힘 
  - 평점과 id를 묶어 저장하여 평점이 가장 높은 id를 추출하고, <br> id를 통해 다시 도서명을 조회함 
  - 너무 어렵게 생각하고 어려운 방식으로 우회하여 풀었음, <br> Spotify 에서는 가장 높은 도서의 index 를 통해 바로 추출하는 방식으로 변경함 

### 문제 E
#### 요약
- 전반적으로 D와 동일한 방식을 사용
- 단, 2023년도에 출간할 도서들의 제목만 리스트하여 리턴할 것
#### 구현결과
```python
def new_books(books_list):
    # 전체 도서의 id 리스트화
    id_list = list(i['id'] for i in books_list)
    # 결과값을 담을 리스트 생성
    title_2023 = []

    # 각 도서의 id를 통해 JSON 파일을 조회하여 pubDate를 슬라이싱해 출간년도 추출, 이후 해당 도서의 제목을 리스트에 저장 
    for id in id_list :
        book = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(book)
        pubYear = book_detail['pubDate'][:4]
        if pubYear == '2023' :
            title_2023.append(book_detail['title'])
            
    # 결과값 리턴 
    return title_2023
```

#### 막혔던 부분 및 해결 
- D를 마치고 나니 오히려 쉽게 해결되었음 
- 슬라이싱을 하지 않아 실수가 있었음

## 후기 
- 스스로 모든 문제를 비교적 빠른 시간 내에 해결하여 좋았음
- 코드 작성 중 주석을 미리 달면서 작성하는 습관을 들여야 겠다고 생각함 
  - 내 문제 해결 과정을 step 별로 구조화 하는 연습 
  - 코드를 재사용할 때 편리함 
  - 회고를 작성할 때 보기 편함 
- 추가 문제 f1, f2 에 대해서 심화 학습을 해야겠다고 생각함 
