import json


def dec_artists(artists_list):

    total_followers = []
    id_list = list(i['id'] for i in artists_list)
    name_list = list(i['name'] for i in artists_list)
    artists_num = len(artists_list)

    for id in id_list :
        artist = open(f'data/artists/{id}.json', encoding='utf-8')
        artist_detail = json.load(artist)
        total_followers.append(artist_detail['followers']['total'])
    
    influencer_num = []

    for i in range(artists_num) :
        if total_followers[i] > 10e6 :
            influencer_num.append(i)
    
    best_influencer = []

    for i in influencer_num :
        best_dict = {}
        artist = open(f'data/artists/{id_list[i]}.json', encoding='utf-8')
        artist_detail = json.load(artist)
        best_dict['name'] = artist_detail['name']
        best_dict['uri-id'] = artist_detail['uri'][15:]
        best_influencer.append(best_dict)

    return best_influencer

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
