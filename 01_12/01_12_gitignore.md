# gitignore

### git 에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일 

프로젝트에 따라 공유하지 않아야 하는 것들도 존재하기 때문

프로젝트가 돌아가도록 환경을 셋업하는 파일들 - 오히려 협업에 방해가 됨 

- **ex.**

윈도우에서 일하는 사람 <-> 맥에서 일하는 사람 <-> 리눅스 서버에서 일하는 사람

path 설정하는 방법이 전부 다름 

프로젝트를 하다 보면 민감한 개인정보나 보안정보를 다루는 파일들은 협업하는 사람들 사이에서도 공유되지 않는 경우가 있음 

API 토큰 - 과금해야 하는 경우 : 본인 API 키만 사용하자 

1. ".gitignore" 파일 생성 : 파일명 앞에 . 입력, 확장자 없음 
2. a 와 b 이름을 가진 텍스트 파일 생성 
3. gitignore에 a.txt 작성
4. git init 
5. git status 


```
SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ touch x.txt

SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ touch y.txt

SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ touch .gitignore

SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git log--oneline
git: 'log--oneline' is not a git command. See 'git --help'.

SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git log --oneline
5b313f6 (HEAD -> master, origin/master) update a.txt
1217362 add b.txt
fa80ae4 add a.txt

SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        y.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

특정 파일군들이나 폴더도 관리 가능 
```
x.txt
*.txt
/test
```
### 한번이라도 git이 track을 시작한 파일이나 디렉토리는 나중에 gitignore 작성해도 적용되지 않음

- gitignore 설정 서비스 

운영체제, 프레임워크, 프로그래밍 언어 등 개발 환경에 따라 gitignore 목록을 만들어주는 사이트
https://www.toptal.com/developers/gitignore/

-> 협업을 할 때 도움이 되지 않는 파일이라고 검증이 된 목록 
-> .gitignore 에 추가해야 함 
ex. Python, VS Code, Windows, PyCharm, Django, Vue
누적해서 쓸 수 있음 


# GitHub 활용 
1. 프로젝트 협업
2. 개인 포트폴리오

## 포트폴리오 
- TIL을 통해 내가 학습하는 것을 기록 
    - Today I Learned 
    - GitHub에 Repository name : "TIL" 에 올림 
    - 과목별로 만들거나 날짜별로 만들거나 ~~
    - 매일 내가 배운것을 마크다운으로 정리해서 문서화 하는 것 
    배운것을 필기 하는게 아니
    



- 개인, 팀 프로젝트 코드를 공유

    - 개발 면접 지원 시 본인의 github 주소를 공유해 어떤 프로젝트들을 진행했고, 어떤 코드를 작성했는지 공유하고 평가 받기 위해 사용

- 오픈 소스 프로젝트에 기여
    - push를 한다고 바로 반영되지 않고 pullrequest - 평가 이후 사용 - contributor
    - 영문 매뉴얼 한글화 - open source contributor (요즘은 잘 안쳐줌)


## 문서화의 중요성 : 신입 개발자에게 요구되는 가장 중요한 덕목
꾸준히 스스로 학습해 성장할 수 있고 문서화를 통해 내 생각을 정리하고 팀에게 공유할 수 있는 능력 

레벨0 : 가이드 문서를 줘도 잘 못씀

레벨1 : 알려주거나 같은 팀에서 만든 가이드 문서에 있는 만큼만 쓸 수 있음

*레벨2* : 
- *개발도구의 공식 레퍼런스를 보고 사용법을 스스로 익힐 수 있음* 
- *자신이 경험한 사용법을 문서화해서 팀 내에 전파할 수 있음*

레벨3 : 
- 여러 개발도구를 비교 분석해서 상황에 적합한 도구를 선택할 수 있음
- 공식 레퍼런스 문서에서 부족한 부분을 수정해서 기여할 수 있음 

레벨4 : 
개발도구의 문제를 소스 코드를 수정해서 Fork/패치해서 사용할 수 있음

실습 1 
TIL 이라는 이름의 GitHub Repository 생성
로컬 저장소 설정 (init)
README.md 생성 및 지금까지의 수업 내용을 정리하고 commit 
TIL 원격 저장소 추가
commit 목록을 push 

