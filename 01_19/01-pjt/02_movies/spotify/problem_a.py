import json
from pprint import pprint


def artist_info(artist_dict):
    info = {}
    needed_info = ['id', 'name', 'genres_ids', 'images', 'type']
    for i in needed_info : 
        info[i] = artist_dict[i]
    return info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))