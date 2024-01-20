import json
from pprint import pprint

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

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
