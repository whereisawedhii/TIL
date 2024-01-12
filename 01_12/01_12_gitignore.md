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
