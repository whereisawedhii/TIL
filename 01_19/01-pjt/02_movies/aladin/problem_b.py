import json
from pprint import pprint


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

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)
    pprint(book_info(book, categories_list))
