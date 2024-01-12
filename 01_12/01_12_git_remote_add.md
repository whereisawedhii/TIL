# 로컬 & 원격 저장소 - 연결

- git remote : 로컬 저장소에 원격 저장소 추가

git remote -v  : 연결된 연결 저장소가 있으면 보여줌 - 처음엔 안보이는게 정상수

git remote add origin “remote_repo_url” : remote 저장소 추가(add) 

origin : origin 이라는 이름으로 추가하기 때문에 default 값임 (관례적으로 - but 반드시 origin 이라고 넣을 필요는 없다)

```jsx
SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git remote -v

SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git remote add origin https://github.com/whereisawedhii/first-repo.git

SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git remote -v
origin  https://github.com/whereisawedhii/first-repo.git (fetch)
origin  https://github.com/whereisawedhii/first-repo.git (push)
```

git remote remove : 잘못된 연결 끊을 때 

- github 연결방법
    
    **…or create a new repository on the command line**
    
    ```jsx
    echo "# first-repo" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M master
    git remote add origin https://github.com/whereisawedhii/first-repo.git
    git push -u origin master
    ```
    
    **…or push an existing repository from the command line**
    
    ```jsx
    git remote add origin https://github.com/whereisawedhii/first-repo.git
    git branch -M master
    git push -u origin master
    ```
    

> push / pull or clone
> 

> 리모트 저장소를  pull 하거나 fetch 하기
> 
- git fetch : 가져와 !

`git fetch` 명령은 리모트 저장소의 데이터를 모두 로컬로 가져오지만, 자동으로 Merge 하지 않는다. 그래서 당신이 로컬에서 하던 작업을 정리하고 나서 수동으로 Merge 해야 한다.

a - 원격저장소에도 a

파일명 같음 , 내용 같으면 문제 안되는데 내용이 다르다면? 

fetch 가져올 뿐만 아니라 합쳐야 함 - Merge

그냥 쉽게 `git pull` 명령으로 리모트 저장소 브랜치에서 데이터를 가져올 뿐만 아니라 자동으로 로컬 브랜치와 Merge 시킬 수 있다

- git push

git push -**u** origin master : origin 저장소의 master 브랜치 

프로젝트를 공유하고 싶을 때 **Upstream** 저장소에 Push 할 수 있다. 이 명령은 `git push <리모트 저장소 이름> <브랜치 이름>` 으로 단순하다.

원격 저장소의 commit 목록을 업로드 

최초  push 할 때에는 github로부터 인증서 git credential 발급이 필요 - 권한 확인 

```jsx
SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git push -u origin master
info: please complete authentication in your browser...
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (8/8), 642 bytes | 321.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/whereisawedhii/first-repo.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```

```jsx
SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice (master)
$ git log --oneline
5b313f6 (HEAD -> master, origin/master) update a.txt
1217362 add b.txt
fa80ae4 add a.txt
```


push 결과 : git bash - GitHub 커밋 내역과 축약 해시값이 동일한지 확인할 수 있다 

commit이 없으면 push 할 수 없다 

commit 내역 클릭시 세부 변경사항을 확인할 수 있다 

- git pull : 변경사항을 받아와서 merge - 업데이트까지 시키는 것

로컬에 나의 git 저장소가 있어야 함 

pull은 받아오는 것 

`git pull <원격 저장소 명> <branch 명>`

git pull origin master 

- git clone : 원격 저장소 전체를 다운로드 하는 것

git clone “remote_repo_url”

복제하다 - 세상에 없는 것을 만들어 낸다는 것 (어원적 의미)

로컬에 나의 git 저장소가 없을 때 하는 것 - 원격에만 만들어짐 

clone은 해오는 것

ex. 협업할 때 1명이 먼저 로컬 만들고 push함 - 다른 사람들은 clone 하면 됨 

나랑 똑같은 환경이 만들어짐 (git init, git add, … )

→ git init을 내 로컬에서 할 필요가 없음 

A 로컬 : git_practice → 원격 : first-repo → B - clone : first-repo

A 추가적으로 로컬 commit → 원격에 push → B - pull : commit 받아옴 

```jsx
SSAFY@2□□PC93 MINGW64 ~/Desktop/git_practice2
$ git clone https://github.com/whereisawedhii/first-repo.git
Cloning into 'first-repo'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (8/8), done.
```

Clone 받아온 이후에 로컬에서 폴더명 변경해서 관리 가능 

1. 로컬 pc A - git_practice - a.txt, b.txt 

→ git init 

→ git add .

→ git commit -m “first” 

.git 폴더 안에 커밋 변경 내용들 ⇒ 로컬 pc A에 저장됨

2. 원격 저장소  “first-repo”를 만들어서 B와 협업하기로 함

→ remote repo : https://github.com/whereisawedhii/first-repo

→ git remote add -u origin https://github.com/whereisawedhii/first-repo.git

→ git push -u origin master

A가 원격 저장소에 푸시 - 업로드 완료

3. B가 remote repo에서 clone해와야 함 

→ git clone https://github.com/whereisawedhii/first-repo.git

→ 폴더 이름은 “first-repo”로 생성됨 

→ 폴더 이름을 “git_advanced” 로 바꿔 관리해도 잘 작동하는 것을 확인할 수 있음 

→ 커밋은 .git 폴더에서 관리하기 때문

→ 새로 파일을 변경하거나 새로운 파일을 만들어서 commit 

→ git push nickname origin master 

A가 owner기 때문에 commit - push 권한을 협업자한테 주어야 함