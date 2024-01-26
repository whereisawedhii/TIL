import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'artist:{name}',  # 필수 파라미터
        'type': 'artist',  # 필수 파라미터
        'market': 'KR',
        'limit': 1,
    }

    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해 json 타입의 데이터를 파이썬의 자료형으로 변환한다.
    response = response.json()
    # response 구조는 위의 공식 문서에서 확인할 수 있다.
    result = response.get('artists').get('items')

    try : 
        id = result[0]['id']
        
        URL = f'https://api.spotify.com/v1'
        headers = getHeaders()
        params = {
            'id': f'{id}'
        }
        # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
        response = requests.get(f'{URL}/artists/{id}/related-artists', headers=headers, params=params)
        # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해 json 타입의 데이터를 파이썬의 자료형으로 변환한다.
        response = response.json().get('artists')

        related_artists = [each['name'] for each in response]

        return related_artists

    except : 
        return None




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_related_artists("NewJeans"))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists("OldShirts"))
    # None
