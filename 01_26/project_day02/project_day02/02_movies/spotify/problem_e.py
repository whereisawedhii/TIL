import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'artist:{artist}',  # 필수 파라미터
        'type': 'artist',  # 필수 파라미터
        'market': 'KR',
        'limit': 1,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    artist_id = response.json().get('artists').get('items')[0].get('id')
    
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'track:{track}',  # 필수 파라미터
        'type': 'track',  # 필수 파라미터
        'market': 'KR',
        'limit': 1,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    track_id = response.json().get('tracks').get('items')[0].get('id')

    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'seed_artists': {artist_id},
        #'seed_genres': {genre} 두 param 값으로 검색시 다른 응답을 받지만 응답 내에 genre를 확인할 수 없어 어떤 부분이 맞는지 정확하지 않음
        'seed_genres': f"{genre}",
        'seed_tracks': {track_id},
        'market': 'KR',
        'limit': 5,
    }
    response = requests.get(f'{URL}/recommendations', headers=headers, params=params)
    recommended_raw = response.json().get('tracks')

    recommended_tracks = [each.get('name') for each in recommended_raw]

    return recommended_raw



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
