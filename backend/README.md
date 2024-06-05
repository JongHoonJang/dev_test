# dev_test

backend : Django

DB : PostgreSql

### 1. 시작하기

1. 가상환경 생성

    python -m venv 가상환경이름

2. 가상환경 활성화

   source 가상환경이름/Scripts/activate

3. pip intall

   pip install -r requirements.txt

4. db 생성

   python manage.py makemigrations

   python manage.py migrate

5. 실행

   python manage.py runserver

### 2. 기능

#### 1. accounts

        1. User db 스키마 (장고 내장 스키마 사용)

        id : PK(기본키)

        name : 유저이름

        username : 유저아이디

        password : 유저 비밀번호

        

        2. URL

         localhost:8000/accounts/user : 회원 탈퇴

         localhost:8000/accounts/user/login/ : 로그인

         localhost:8000/accounts/user/reissue/ : JWT 토큰 재발급

         localhost:8000/accounts/user/logout/ : 로그아웃

         localhost:8000/accounts/user/signup/ : 회원탈퇴

#### 2. Boards

        1-1. Board db 스키마

        id : PK(기본키)

        user_id : FK(외래키)

        title : 제목

        content : 내용

        group_order : 부모 게시글 id

        order_id : 댓글 순서

        depth : 계층

        created_at : 등록시간

        counting : 조회수

        1-2. Counting db 스키마

        id : PK(기본키)

        ip : 유저 또는 ip

        2. URL

        localhost:8000/boards/<<int:board_id>>/ : 게시판상세정보 및 수정 및 삭제

        localhost:8000/boards/list/ :게시글 리스트

        localhost:8000/boards/create/ : 게시글 작성

        localhost:8000/boards/counting/<<int:board_id>>/ : 조회수

# 