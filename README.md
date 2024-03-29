# django_allauth
음식점 리뷰 블로그 입니다.

## 사용한 기술스택
---
- python
- Django
- Django-allauht
- HTML
  
## 구현기능
---
- 계정관련
  - 로그인, 로그아웃, 회원가입
  - 비밀번호 찾기
  - 프로필 수정
  - 팔로우. 팔로워
- 유효성 검사
  - 닉네임은 특수문자를 사용 할 수 없다.
  - 이메일은 중복이 불가능하다.
  - 비밀번호는 8자 이상의 영문 대/소문자, 숫자, 특수문자를 포함해야 한다.
- 이메일 인증
  - 콘솔로 보내게 만들었습니다.
  ![image](https://user-images.githubusercontent.com/67260228/206126771-e4dd6e25-47ef-4a1b-bca3-7ad092068b99.png)
- 간단한 CRUD
- 댓글/대댓글
- 프로필 
- 검색기능

## 이미지
- 홈화면
  ![image](https://user-images.githubusercontent.com/67260228/206125876-ba65f040-fc10-4bb8-aa7d-c8c7d0e77a0a.png)
  - 로그인이 되었다면 팔로우 게시글 보이게 설정

  ![image](https://user-images.githubusercontent.com/67260228/206126144-c24ad765-00c0-48ba-9121-31a694c2c392.png)

- 검색기능
 ![image](https://user-images.githubusercontent.com/67260228/206126381-7da40176-2f70-4bea-ad04-c67b67992427.png)

- 프로필
  - 프로필 수정
  - 팔로우, 팔로워 리스트 확인
  
  ![image](https://user-images.githubusercontent.com/67260228/206126546-15962820-7084-408c-8cda-991f144e8b27.png)

- 게시글 작성
  - 주소를 직접 입력해야함(추후 카카오 api로 수정할 예정)
  
  ![image](https://user-images.githubusercontent.com/67260228/206127052-62e0ab3a-e6f9-4c46-9a59-af4e412f17d7.png)

- 디테일페이지
  - 댓글기능
  - 수정 및 삭제
  - 유저를 누르면 그 유저 프로필로 이동
  - 위치보기 클릭시 위치 표시기능
  
  ![image](https://user-images.githubusercontent.com/67260228/206127245-73747d8f-0b8f-4825-ba43-ce6080099a36.png)