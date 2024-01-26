import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def ranking():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': 'genres:"k-pop"',  # 필수 파라미터
        'type': 'track',  # 필수 파라미터
        'market': 'KR',
        'limit': 20,
    }

    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해 json 타입의 데이터를 파이썬의 자료형으로 변환한다.
    response = response.json()
    # response 구조는 위의 공식 문서에서 확인할 수 있다.
    result = response.get('tracks').get('items')

    track_list = [each['name'] for each in result]
    release_date_list = [each['album']['release_date'] for each in result]
    release_date_list.sort(reverse=True)

    return release_date_list[:5]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    ['2023-06-09', '2023-05-22', '2023-05-12', '2023-05-08', '2023-05-01']
    """
