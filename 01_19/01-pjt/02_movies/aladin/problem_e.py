import json


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

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))
