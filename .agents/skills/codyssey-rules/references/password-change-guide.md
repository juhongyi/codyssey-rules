# Password Change Guide

Source: `password-change-guide.pdf`

## Page 1

비밀번호 변경 가이드
iMac 로그인
첫 로그인 시 , 교육생 계정 및 임시 패스워드 입력
최초 임시 패스워드의 경우 휴대폰 번호 11 자리
터미널 실행 (Terminal) 하여 패스워드 변경
# 패스워드 변경 명령어 실행 : passwd
💡이미지 예시 )
# 이미지에서의 ‘WARNINGʼ 은 하기 주의사항 내용 확인
패스워드 정책
최소 길이 : 8 자 이상
복잡도 : 4 종류 혼합 필수
대문자 , 소문자 , 숫자 , 특수문자를 각각 최소 1 개씩 모두 포함
예시 ) Codyssey12#
비 밀 번 호 변 경 가 이 드
1

## Page 2

* 주의 사항 ( 필수 )
💡터미널로 비밀번호를 바꾸는 경우 macOS 의 키체인 (Keychain) 비밀번호는 자
동으로 바뀌지 않기 때문에 다음과 같은 현상이 발생합니다 .
** ' 로그인 키체인 ' 업데이트 문제 (macOS 특성 )
현상: 로그인하였던 iMac 재부팅 또는 재로그인 시 , " 시스템이 로그인 키체인에 접근하
려고 합니다 " 라는 팝업 발생
The systme was unable to unlock your login keychain.
* Update Keychain Password 클릭
조치: [Update Keychain Password] 클릭 후 패스워드 입력창이 뜨면 , 이전 비밀번호
( 변경 전 )를 입력하여 키체인을 수동으로 업데이트 합니다 .
( 예시 ) 첫 비밀번호 변경 시 : 임시 비밀번호 ( 전화번호 11 자리 ) 입력
* 유의 사항
[ 시스템 설정 System Settings] – [ 로그인 암호 Login Password]에서 패스워드 변
경 불가
터미널에서 passwd 명령어로 변경해 주세요 .
비 밀 번 호 변 경 가 이 드
2
