import json


def max_polularity(artists_list):
    # 여기에 코드를 작성합니다.
    popularity_list=[]
    id_list = list(i['id'] for i in artists_list)
    name_list = list(i['name'] for i in artists_list)

    for id in id_list :
        artist = open(f'data/artists/{id}.json', encoding='utf-8')
        artist_detail = json.load(artist)
        popularity_list.append(artist_detail['popularity'])
    
    highest = popularity_list[0]
    
    for i in popularity_list :
        if highest < i :
            highest = i              
    
    most_popular = name_list[popularity_list.index(98)]
    return most_popular

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))
