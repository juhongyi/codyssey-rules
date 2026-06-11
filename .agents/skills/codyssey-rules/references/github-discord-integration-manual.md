# GitHub Discord Integration Manual

Source: `github-discord-integration-manual.pdf`

## Page 1

GitHub 연동하기

## Page 2

Contents
A) GitHub이란?
B) GitHub 사용법
C) Codyssey와 연결하기
D) Discord 연결하기

## Page 3

A) GitHub이란?
A) GitHub이란?
: 소프트웨어 개발자들이 가장 많이 사용하는
형상 관리(변경 사항을 추적, 제어하는 과정) 플랫폼 중 하나
GitHub 기본 기능
1. 원격 코드 저장소
2. 이슈 트래킹
3. 프로젝트 진행 추적 관리
4. 코드 변경 이력 관리
5. 개발자 동시 작업에 유용
출처 : https://aonee.tistory.com/15

## Page 4

A) GitHub이란?
GitHub 왜 사용하나요?
전 세계 수백만 명의 개발자들이 코드를 호스팅하고 공유하고, 프로젝트에서 협업하는 데 사용.
버전 관리, 버그 추적, 프로젝트 관리 등 개발자가 코드를 관리하고 추적하는 데 도움을 주는 기능과 도구를 제공.
GitHub Repository
프로그램 소스 코드를 저장하게 하고 개발자가 사용하는
GitHub 대표적 서비스.
GitHub Actions
지속적 통합(continuous integration, CI) 그리고 지속적 배포
(continuous delivery, CD)를 사용해서 빌드, 테스트, 배포를
가능하게 하는 데브옵스(DevOps) 파이프라인 자동화 툴.
GitHub Packages
Docker 컨테이너 혹은 프로그램 패키지(NPM, NuGet, Gem,
Maven/Gradle)를 저장할 수 있는 이미지 레지스트리 개념
의 서비스.
GitHub Advanced Security (GHAS)
코드 패키지에 있는 취약점을 찾아주는 Dependabot 그리고
소스 코드에 있는 문제점들을 찾는 것 등등 다양한 보안 기
능을 제공하는 서비스.
GitHub Projects
Atlassian JIRA같이 프로젝트를 관리하게 도와줄 수 있는
서비스.
GitHub Discussions
Stack Overflow나 Quora 같이 질문을 물어보고 대답하는
형식을 제공하는 커뮤니티 서비스.
GitHub Copilot
머신 러닝을 사용해서 자동으로 개발자가 코드를 적는
내용을 파악하고 자동으로 나머지를 대신해서 적어주는
생성형 인공지능 서비스.
GitHub Codespace
GitHub Repository 안에서 별도의 다운로드나 설치 없이 웹
브라우저에서 개발 가능한 인터넷 내장 코드 에디터 IDE.
GitHub 서비스

## Page 5

A) GitHub이란?
출처 : https://aonee.tistory.com/15
GitHub 사용법 동영상
https://www.youtube.com/watch?v=Fley6IFhlC8https://www.youtube.com/watch?v=FXDjmsiv8fI&t=212s
※ GitHub는 회원가입을 해야 사용할 수 있습니다. ※
회원가입을 진행해 보세요.

## Page 6

B) GitHub 사용법
B) GitHub 사용법
1) 레파지토리 생성 방법 1 https://github.com으로 먼저 이동
합니다.
학습자 개인의 GitHub 계정으로
로그인 후 오른쪽 상단의 [+] 드롭
다운 버튼을 클릭합니다.
1
2
2 [new repository]를 클릭합니다.

## Page 7

B) GitHub 사용법
B) GitHub 사용법
1) 레파지토리 생성 방법 1 Repository의 이름을 작성해 주세
요.
1
2
3
2 어떤 Repository인지 설명하는 작
성란 입니다.(선택사항)
3 Repository를 다른 사용자에게 공
개 여부를 설정할 수 있습니다.
“Codyssey 플랫폼을 사용하기 위
해서는" [Public]으로 선택해야 합
니다.
4 모든 설정이 끝났다면
[Create repository] 버튼 클릭 시
Repository를 최종 생성합니다.
4
Repository의 기타 정보를
설정하는 구간입니다.
직접 공부해 보세요.

## Page 8

B) GitHub 사용법
B) GitHub 사용법
1) 레파지토리 생성 방법 1 생성한 Repository를 확인할 수 있
습니다.
1

## Page 9

C) Codyssey와 연결하기
C) Codyssey와 연결하기
1) Codyssey와 GitHub를 연동하기 위한 토큰을 발급 받으실 수 있습니다.
1 https://github.com으로 먼저 이동
합니다.
학습자 개인의 GitHub 계정으로
로그인 후 오른쪽 상단의 프로필
을 클릭합니다.
2 [Settings] 버튼을 클릭합니다.
클릭 시 그림과 같은 화면으로 이
동합니다.
3 화면의 가장 하단에 있는
[Developer settings] 버튼을 클
릭합니다.
2
3
1

## Page 10

C) Codyssey와 연결하기
C) Codyssey와 연결하기
2) GitHub과 연동하기 위한 토큰을 발급 받으실 수 있습니다.
1 [Personal access tokens]을 클
릭합니다.
2 [Tokens (classic)]을 클릭합니다
.
3 [Generate new token]을
클릭하여 드롭다운 버튼을 열어줍
니다.
1
2
4
3
4 [Generate new token(classic)]을
클릭 시 GitHub 토큰을 발급하는
페이지로 이동합니다.

## Page 11

C) Codyssey와 연결하기
C) Codyssey와 연결하기
2) GitHub과 연동하기 위한 토큰을 발급 받으실 수 있습니다.
1
1 [Note]에 토큰에 대한 제목을 작
성해 주세요.
Ex) Codyssey-GitHub 연동 토큰
2 [Expiration]은 토큰에 대한 만료일
을 설정하는 칸입니다.
만료일을 No Expiration(만료 없음)
으로 설정합니다.
3 [repo] 체크박스를 선택을 한 뒤
페이지 맨 아래로 이동하세요.3
만료일에 제한이 있다면
Codyssey 플랫폼을 사용하실
때 불이익이 있을 수 있습니다.
2

## Page 12

C) Codyssey와 연결하기
C) Codyssey와 연결하기
2) GitHub과 연동하기 위한 토큰을 발급 받으실 수 있습니다.
1
1 페이지 맨 아래로 이동 후
[Generate token] 버튼을 눌러 토
큰을 발급받으세요.

## Page 13

C) Codyssey와 연결하기
C) Codyssey와 연결하기
2) GitHub과 연동하기 위한 토큰을 발급 받으실 수 있습니다.
1
1 [토큰]을 복사한 뒤
Codyssey 플랫폼으로 이동하세
요.
발급된 토큰은 단 한 번만 보여
지기 때문에 메모를 해두시거
나 바로 설정하는 것이 좋습니
다.

## Page 14

C) Codyssey와 연결하기
C) Codyssey와 연결하기
3) 로그인 후, 우측 상단 MY - [코드저장소]에서 GitHub 연동을 확인 할 수 있습니다.
1
1 MY > 코드저장소로 이동합니다.

## Page 15

[GitHub 연동] 버튼을 누르면 학
습자 개인의 GitHub 계정과 연동
할 수 있습니다.
버튼 클릭 시 GitHub을 연동할 수
있는 팝업창이 나옵니다.
C) Codyssey와 연결하기
C) Codyssey와 연결하기
3) [코드저장소]에서 GitHub 연동 및 레파지토리를 확인 할 수 있습니다.
1
1

## Page 16

C) Codyssey와 연결하기
C) Codyssey와 연결하기
3) [코드저장소]에서 GitHub 연동 및 레파지토리를 확인 할 수 있습니다.
1 학습자 개인의 GitHub 아이디를
입력해 주세요.
2 GitHub에서 복사한 [토큰]을 입력
해 주세요.
GitHub 연동 시 참고사항
✔GitHub 아이디는
학습자 자신의 계정이어야
합니다.
✔GitHub 주소는 학습자 포탈
[코드저장소] 에서 확인할 수
있습니다.
3 [등록/수정하기] 버튼을 클릭하면
GitHub 연동하실 수 있습니다.
1
2
3

## Page 17

C) Codyssey와 연결하기
C) Codyssey와 연결하기
4) 나의 Git 저장소 목록을 볼 수 있습니다.
1 [저장소 가기] 버튼 클릭 시 학습
자 개인의 GitHub로 이동할 수 있
습니다.
2 [GitHub 레파지토리]의 목록을 확
인하실 수 있습니다.
1
2

## Page 18

D) Discord 연결하기
D) Discord 연결하기
: 디스코드(Discord)는 다양한 커뮤니티와 팀들이 사용하는 무료 음성, 영상, 텍스트 커뮤니케이션 플랫폼 중 하나로
코디세이와 연동하여 평가 알림등의 기능을 사용 할 수 있습니다.

## Page 19

D) Discord 연결하기
D) Discord 연결하기
1)Discord와 연결하기 위한 아이디를 확인할 수 있습니다.
1 Discord 화면 왼쪽 하단의 닉네임
을 클락하면 왼쪽의 화면이 나옵
니다.
2 열린 화면에서 닉네임 밑의 아이
디를 연동을 위해 복사 합니다.
1
Discord ID
Discord 2
Discord

## Page 20

D) Discord 연결하기
D) Discord 연결하기
2)Discord와 코디세이를 연결하기 위해 내정보로 들어 갑니다.
1 코디세이 오른쪽 상단의 내정보를
클릭하여 내 정보 화면으로 이동
합니다.
2 열린 화면에서 알림 방식의
Discord를 체크 하면 디스코드 id
를 입력할 수 있는 부분이 활성화
됩니다.
3 앞에서 확인한 아이디를 입력하고
‘인증번호전송’ 버튼을 클릭하면
Discord를 통하여 인증번호가 전
송됩니다.
4 인증이 완료 되었다면 마지막으로
수정하기 버튼을 눌러 저장하여
연동을 완료합니다.
1
2
3
4

## Page 21

THANK YOU
Code your Journey
