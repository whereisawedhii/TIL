# 관통 project day 03
### 02_movies 주제를 선택한 이유
- 2번 주제의 영화들이 전부 명작이어서 매우 관심이 갔고, 원하는 페이지 레이아웃과 디자인이 명확하여 선택하였습니다.
- 이번 1번 주제는 포트폴리오를 만드는 프로젝트였는데, 포트폴리오에 기재할 컨텐츠가 아직 부족하고, <br> 상대적으로 자유도가 더 높은 작업이기 때문에 2번 주제를 선택하게 되었습니다.

## 이번 project 통해 학습한 내용 
- html의 header, footer, article, aside 등의 시맨틱 태그와, form 태그 등 기능적 태그를 사용
- Bootstrap의 여러 클래스들과 컴포넌트를 사용하여 웹 페이지 레이아웃을 구현
- css를 통해 Bootstrap에서 가져온 항목들을 커스터마이징하여 웹 페이지 레이아웃을 완성

## 구현 기능 

### Navbar
1. 화면을 스크롤 하더라도 항상 화면 상단에 고정되도록 해야 함 
    - css 를 이용한 구현 
```css
    nav {
        position: sticky;
        top: 0;
    }
    
    ```
    - Bootstrap 클래스를 이용한 구현 (선택한 구현 방식)
    ```html
    <nav class="sticky-top">
```
2. 네비게이션 메뉴 중 Home, Community 클릭 시 각각 다른 html 파일의 페이지로 이동
    - a 태그의 네비게이션 링크를 각 html로 할당함
```html
    <li class="nav-item">            
              <a class="nav-link" href="01-home.html">Home</a>        
            </li>        
            <li class="nav-item">            
              <a class="nav-link" href="02-community.html">Community</a>        
            </li> 
```
3. 네비게이션 메뉴의 Login을 클릭시 Login 화면을 팝업 
![Login 팝업 화면](result.image1.png)
    - Bootstrap의 Modal 컴포넌트를 활용해 팝업창 구현
    - Modal body에서 html form 태그와 button을 활용해 로그인 화면을 구현
```html
    ...
    <li class="nav-item">            
              <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#Login">Login</a>
            </li>
    ...
    <div class="modal fade" id="Login" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">Login</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">ID</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your ID with anyone else.</div>
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </div>
</div>

```

### 메인 페이지 - Header
- Bootstrap Carousel 컴포넌트를 활용
- 자동으로 slide 되도록 구현
- media 쿼리를 사용하여 반응형으로 구현

### 메인 페이지 - Section 
- Bootstrap Grid Card 컴포넌트를 활용
- 카드의 높이를 모두 같게 하기 위해 card는 h-100, img는 h-75의 클래스를 줌
- row-col 클래스를 통해 각각의 viewport 너비 당 표시되는 열의 개수를 조절 

### 커뮤니티 페이지 - Aside, Section
- viewport의 크기당 Aside와 Section의 반응형 구현을 위해 부모 div를 flew row 의 클래스 를 줌 
- Aside 와 Section별 breakpoint를 lg를 기준으로 반응형으로 구현하기 위해 col-*-# 클래스를 활용
- Section은 breakpoint를 기준으로 Bootstrap Table 컴포넌트가 나타나야 하기 때문에,  d-*-none 을 활용해 2가지 Section을 구현 

### 커뮤니티 페이지 - Pagination
- Bootstrap Pagination 컴포넌트로 구성하고, 수평 중앙 정렬을 위해 justify-content-center, align-content-center 을 활용