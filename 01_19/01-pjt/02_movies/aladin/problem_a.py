import json
from pprint import pprint

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


# # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
