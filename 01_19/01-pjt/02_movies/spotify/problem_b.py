import json
from pprint import pprint


def artist_info(artist, genres):
    info = {}
    needed_info = ['id', 'name', 'genres_ids', 'images', 'type']

    for i in needed_info : 
        info[i] = artist_dict[i]

    genres_num = len(genres_list)
    genreid_list = info['genres_ids']
    genreName_list = []

    for num in range(2) :
        for i in range(genres_num) :
            if genreid_list[num] == genres_list[i]['id'] :
                genreName_list.append(genres_list[i]['name'])
    
    info['genres_names'] = genreName_list
    del info['genres_ids']

    return info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
