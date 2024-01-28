# 관통 project day02
### 02_movies 주제를 선택한 이유
- 저번 day01에도 선택한 이유와 동일함
- 파이썬 라이브러리를 사용한 데이터 분석 및 데이터 사이언스 입문보다는 <br> 기존에 api에 관심이 있었기 때문에 더 흥미로운 과제라고 생각했음 

## 이번 project 통해 학습한 내용 
- 코드 진행 중 Error가 발생할 수 밖에 없는 값이 있을 때 <br> 이를 확인하고 `try-except` 로 대처할 수 있음 
- api 공식 문서에서 요구하는 키값을 변경하며 데이터를 송신하여 원하는 데이터를 받아올 수 있음 

### 문제 A
#### 요약 
- 스포티파이 api 를 사용하여 한국 시장의 k-pop 장르 곡 20개를 응답받아와 이름을 리스트로 출력
#### 구현 
```python
def get_tracks():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    # 케이팝 장르 검색을 위한 파라미터값 수정 
    params = {
        'q': 'genres:"k-pop"',  # 필수 파라미터
        'type': 'track',  # 필수 파라미터
        'market': 'KR',
        'limit': 20,
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    result = response.get('tracks').get('items')

    # 요청받은 트랙의 이름을 저장 후 반환
    track_list = []
    track_list = [each.get('name') for each in result]

    return track_list
```

#### 막혔던 부분 및 해결 
- Spotify API 공식문서에도, 프로젝트에도 없었던 genres 값을 넣어야 했음 
- genre가 아니라 genres였고, 값에는 단순 문자열이 아니라 "k-pop"과 같이 넣어줘야 정상적으로 작동했음 
- 동작을 안하는 것이 아니라 해당 쿼리값을 제외하고 검색한 결과를 불러와 맞는 결과인지 예측하기가 힘들었음 
- 결국 이전 project day01 의 JSON 파일에서 사례를 탐색하며, 여러 가지 a,b 로 테스트함 

### 문제 B
#### 요약
- 이전 응답받은 값에서 인기도가 90 이상인 트랙만 선별하여 따로 이름을 출력
- 인기도가 90 이상인 항목이 없어 60 이상으로 조건을 걸어야 2개 이상의 값이 출력되었음
#### 구현
```python
    # 중략 
    track_list = []
    popularity = []
    # 응답받은 결과들에서 각 트랙별 이름과 인기도만 따로 리스트에 저장 
    track_list = [each.get('name') for each in result]
    popularity = [each.get('popularity') for each in result]
    
    # popularity 90 이상인 항목이 없어 빈 리스트가 출력됨 - 60으로 변경하여 6가지 항목이 출력되도록 설정함
    popular_tracks = [track_list[i] for i in range(len(track_list)) if popularity[i] > 60]

    return popular_tracks
```
#### 막혔던 부분 및 해결 
- 90 이상의 값으로 조건을 걸었더니 출력받은 값이 없어 코드를 잘못 짰나 당황했음 
- 인기도를 80, 70, 60 으로 내리며 정상출력되는 것을 확인함 

### 문제 C
#### 요약
- 이전 응답받은 값에서 앨범의 발매일이 최신인 5개의 값만 출력
#### 구현
```py
    # 
    track_list = [each['name'] for each in result]
    release_date_list = [each['album']['release_date'] for each in result]
    release_date_list.sort(reverse=True)

    return release_date_list[:5]

```
#### 막혔던 부분 및 해결 
- 조건이 간단하여 슬라이싱으로 출력함
- 2023년으로 조건을 건다거나 하는 다른 문제의 구현도 혼자 생각해보았음

### 문제 D
#### 요약
- NewJeans와 OldShirts 라는 아티스트의 이름으로 조건을 걸어 spotify api에 요청 
- 이후 아티스트의 고유 id값으로 related-artists를 재검색함 
- OldShirts의 경우 결과값이 없기 때문에 2번째 검색시 결과가 없어 최종 리턴시 에러가 발생함
- try-except를 사용하여 에러가 발생할 경우 None을 리턴하도록 구현
#### 구현
```python
    params = {
        'q': f'artist:{name}',  # 필수 파라미터
        'type': 'artist',  # 필수 파라미터
        'market': 'KR',
        'limit': 1,
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    result = response.get('artists').get('items')

    try : 
        id = result[0]['id']
        
        URL = f'https://api.spotify.com/v1'
        headers = getHeaders()
        # artist 검색에 맞는 필수 파라미터 값으로 수정함
        params = {
            'id': f'{id}'
        }
        # related artists의 결과값을 가져오도록 요청 URL을 수정 
        response = requests.get(f'{URL}/artists/{id}/related-artists', headers=headers, params=params)
        response = response.json().get('artists')

        # 결과값에서 아티스트의 이름만 출력하도록 함 
        related_artists = [each['name'] for each in response]

        return related_artists

    except : 
        # 결과값이 없는 경우 에러가 아닌 None을 리턴하도록 수정 
        return None
```
#### 막혔던 부분 및 해결 
- URL 수정하는 부분을 놓쳐서 결과값이 제대로 나오지 않았는데 찾아서 수정함 

### 문제 E
#### 요약
- 트랙 1개, 아티스트 1팀 을 api를 통해 검색해 각각 고유 트랙id, 아티스트id를 추출
- 고유 트랙id, 아티스트id 그리고 장르값을 새로운 param값에 넣어 추천 곡들의 목록을 받아와 이름을 리턴
#### 구현
```python
    # 아티스트 검색하여 고유 id값을 할당
    params = {
        'q': f'artist:{artist}',  # 필수 파라미터
        'type': 'artist',  # 필수 파라미터
        'market': 'KR',
        'limit': 1,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    artist_id = response.json().get('artists').get('items')[0].get('id')
    
    # 트랙 검색하여 고유 id값을 할당
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

    # 아티스트id, 트랙id, 장르값을 활용해 recommendation 요청 후 추천 트랙들의 이름을 리턴
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'seed_artists': {artist_id},
        'seed_genres': {genre},
        'seed_tracks': {track_id},
        'market': 'KR',
        'limit': 5,
    }
    response = requests.get(f'{URL}/recommendations', headers=headers, params=params)
    recommended_raw = response.json().get('tracks')

    recommended_tracks = [each.get('name') for each in recommended_raw]

    return recommended_tracks
```
#### 막혔던 부분 및 해결 
- 장르값으로 헤맸기 때문에 걱정되었으나 다행히 무리없이 한번에 결과값을 받아올 수 있었음 
- 그러나 해당 param 값에서 `{genre}` 가 아닌 `f"{genre}"` 로 바꿀 경우 다른 결과값이 나오는 것을 확인함 
- response 내에는 장르를 직접 확인할 수 없어 결과값이 맞는지 바로 검증할 수 없는 것이 아쉬웠음 

## 후기 
- 이전 프로젝트 내용과 달리 직접 api를 통해 요청, 응답을 받을 수 있는 것이 좋았음 
- 역시 spotify 같은 기업에서도 공식 api 문서는 불친절하고, 전부 알아내기 힘들어 응답값을 직접 보고 알아내야 하는 부분이 많았음 
- 코드 작성에 큰 무리가 없었고, 이전보다 실력이 향상되어감을 느낄 수 있어 좋았음 
