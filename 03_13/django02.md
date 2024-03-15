### Django 프로젝트, 앱 생성 루틴
- 가상환경 생성 : `python -m venv venv`
- 가상환경 활성화 : `source venv/Scripts/activate`
- 가상환경 비활성화 : `deactivate`
- Django 설치 : `pip install django`
- 의존성 패키지 목록 생성(패키지 새로 설치 시마다 진행) : `pip freeze > requirements.txt`
- 의존성 패키지 목록을 통해 패키지 받아오기 (동기화) : `pip install -r requirements.txt`

- 프로젝트 만들기 : `django-admin startproject firstpjt .`
    - 뒤에 한칸 띄고 `.`을 찍어줘야 해당 경로에 바로 manage.py 파일이 생성됨, 
    - 그렇지 않을 경우 디렉토리가 한 depth 더 들어가기 때문에 서버 실행을 위해서는 경로를 바꿔야 함 - 번거로울 수 있음 
- django 서버 실행 : `python manage.py runserver` (manage.py와 동일한 경로에서 진행)
- 서버 종료 : `ctrl + c` (manage.py와 동일한 경로에서 진행)

- ***반드시 앱을 생성한 후에 등록해야 함***
- 앱 생성 : `python manage.py startapp articles`
- 앱 등록 : 프로젝트 폴더 내의 settings.py - INSTALLED APPS 리스트 안에 `'application이름',`으로 등록해야함

## Django Template System
- 데이터 표현을 제어하면서 표현과 관련된 부분을 담당 

### HTML 의 콘텐츠를 변수 값에 따라 바꾸고 싶다면?

### Django Template Language (DTL)
- Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

### DTL Syntex
1. Variable
- render 함수의 세번째 인자로 딕셔너리 데이터를 사용
- 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨 
- `.` 를 사용하여 변수 속성에 접근할 수 있음 (딕셔너리 안 하위값 속성 추가 접근)
- `{{variable}}`, `{{variable.attribute}}`

2. Filters
- 표시할 변수를 수정할 때 사용 (변수 + `|` + 필터)
- chained (연결)이 가능하며 일부 필터는 인자를 받기도 함 
- 약 60개의 built-in template filter를 제공 
- `{{variable|filter}}` , `{{name|trucatewords|30}}`

3. Tags
- 반복 또는 논리를 수행하여 제어 흐름을 만듦
- 일부 태그는 시작과 종료 태그가 필요
- 약 24개의 built-in template tag를 제공 
- `{% tag %}`, `{% if %} {% endif %}`

4. Comments
- DTL 에서의 주석 
- `{# comments #}`
- 주석 태그 활용
```django
{% comment %}

{% endcomment %}
```

- URL -> View -> Template (데이터의 흐름)

## 템플릿 상속 Template inheritance
- 페이지의 공통요소를 포함하고
- 하위 템플릿이 재정의 할 수 있는 공간을 정의하는
- 기본 skeleton 템플릿을 작성하여 상속 구조를 구축

### 기본 템플릿 구조의 한계
- 만약 모든 템플릿에 bootstrap을 적용하려면?
- 부모 템플릿을 만들어두고, 상속을 주면 자식 템플릿들은 이미 모두 CDN 작성되어 있음

### extends tag
- `{% extends "articles/base.html" %}`
- 다른 어떤 태그보다 위에 있어야 함 (템플릿 최상단)

### block tag
- ` {% block content %}
    {% endblock content %}`
- 상위 템플릿에 작성
- 하위 템플릿에서 재정의 할 수 있는 블록을 정의
- 블락 여러개 작성시 이름 다르게 해서 정의하면 됨 

## HTML form 요청과 응답
### 데이터를 보내고 가져오기 Sending and Retrieving form data
- HTML 'form' element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기 
- 서버와 함께할 때 의미있음 
- HTML 'form'은 HTTP 요청을 서버에 보내는 가장 편리한 방법 
- ex. 로그인 작업 

### 'form' element
- 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러 방식
- text, password, checkbox 등 

## 핵심 속성 'action' & 'method'
- 'action' 
    - 입력 데이터가 전송될 URL을 지정 (목적지)
    - 속성을 지정하지 않으면 현재 form이 있는 페이지의 URL로 보내짐
- 'method'
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP request method를 지정
    - 'GET' : 검색어가 URL에 노출됨
    - 'POST' : 검색어가 URL에 노출하지 않아야 할 때 로그인 등

### 'input' element
- 사용자의 데이터를 입력 받을 수 있는 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음 

### input의 핵심 속성 'name' attribute
- 입력한 데이터에 붙이는 이름 (key)
- 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근 

### Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
- 문자열은 앰퍼샌드('&')로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표('?')로 구분됨

```html
{% extends "articles/base.html" %}

{% block content %}
    {% comment %} 데이터를 어디로 보낼 것인지 {% endcomment %}
    {% comment %} HTTP request method : POST, GET {% endcomment %}
    <form action="https://search.naver.com/search.naver">
        <label for="message">검색 : </label>
        {% comment %} 무슨 데이터를 보낼 것인지 {% endcomment %}
        {% comment %} input의 id 값은 labal의 for와 동일하게  {% endcomment %}
        {% comment %} input의 name값을 key로, 실제 input은 value로 하여 데이터를 보내게 됨 {% endcomment %}
        <input type="text" id="message" name="query">
        <input type="submit">
    </form>
{% endblock content %}

```

### 추가 템플릿 경로 지정
- settings.py에서 TEMPLATES의 DIRS 부분을 바꿀 것
```python
TEMPLATES = [
    {
        # 이 부분 지정할 것
        'DIRS': [BASE_DIR/ 'templates'],
```
- templates 에 base.html -> 새로운 템플릿 커스텀 경로 생성 
- 이후 extends 경로 수정하면 됨 
- BASE_DIR : settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정해놓은 변수
- `BASE_DIR = Path(__file__).resolve().parent.parent`
    - 리눅스 계열 OS : // // 
    - 윈도우 경로 : \\ \\ 

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

### DTL 주의사항
- python 처럼 일부 프로그래밍 구조를 사용할 수 있지만 
    python 코드로 실행되는 것이 아니며 python과는 관련 없음
- 표현을 위한 것임을 명시
- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것 

### 요청과 응답에서 Django URLs의 역할 
- URL dispatcher : 운항 관리자, 분배기 
- URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)
- URL 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까?

## Variable Routng 
- URL 일부에 변수를 포함시키는 것 
- 변수는 view 함수의 인자로 전달할 수 있음 
- `<path_converter:variable_name>`
```python
path('articles/<int:num)
```

## Trailing Slashes
- Django는 URL 끝에 '/'가 없다면 자동으로 붙임 
- 기술적인 측면에서, foo.com/bar와 foo.com/bar/는 서로 다른 URL임
    - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 서로 다른 페이지로 봄
- Django는 검색 엔진이 혼동하지 않게 무조건 붙임
    - http 200 : /가 잘 붙은걸 나타냄 
    - http 301 : /가 없는 경우 /를 붙여서 요청함
- 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님. 주의할 것

# 기욱쌤 보충 
- foo.com/bar와 foo.com/bar/는 서로 다른 URL임 -> 왜일까?
- 예전? 완성된 페이지를 구축해놓고 파일 자체를 보여줌 (정적)
    - / <- 이 경로 까지임을 나타냄 

- 레거시 : 버릴 필요까지는 없음 
- 경로라는 기준점은 가지고 가되, 파일을 보내주는 건 맘대로 해보자 
- 완성된 페이지가 아니라 view에 정의한 함수가 결정지음 -> 정적인 파일이 아니라 동적인 파일을 보여준다는 차이 

#### dry 원칙
- do not repeat yourself
- 중복으로 작성되는 코드를 피하고, 재활용 가능하도록 작성
- 시간과 노력이 절약되고, 유지 관리가 쉬우며 버그 가능성도 줄어든다

### 추가 템플릿 경로 지정
- settings.py에서 TEMPLATES의 DIRS 부분을 바꿀 것
```python
TEMPLATES = [
    {
        # 이 부분 지정할 것
        'DIRS': [BASE_DIR/ 'templates'],
```
- 생성하는 프로젝트들은 여러개의 앱을 묶는 단위임
- 앱을 여러개 만들 때, 어떤 경로를 기준으로 가져올 건지 템플릿의 기준 경로를 지정