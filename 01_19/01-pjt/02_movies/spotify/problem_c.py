import json
from pprint import pprint


def artist_info(artists_list, genres_list):
    needed_info = ['id', 'name', 'genres_ids', 'images', 'type']
    artists_num = len(artists_list)
    info_artists = []

    for counts in range(artists_num) :
        info = {}

        for i in needed_info :
            info[i] = artists_list[counts][i]
        
        all_genres = len(genres_list)
        genreid_list = info['genres_ids']
        genres_num = len(info['genres_ids'])
        genreName_list = []

        for num in range(genres_num) :
            for i in range(all_genres) :
                if genreid_list[num] == genres_list[i]['id'] :
                    genreName_list.append(genres_list[i]['name'])
    
        info['genres_names'] = genreName_list
        del info['genres_ids']
        info_artists.append(info)

    return info_artists


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
