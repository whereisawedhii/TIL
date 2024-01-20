import json


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



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
