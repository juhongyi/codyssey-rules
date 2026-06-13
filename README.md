# Codyssey Rules Skill

Codyssey 공식 참조 문서를 근거로 학칙, 장학금, 동료 평가, GitHub/Discord 연동, iMac 설정, Neito 기능 질문에 답하기 위한 Codex skill입니다. 답변은 번들된 `references/` 문서를 먼저 확인하고, 확인 가능한 범위 안에서 근거와 함께 한국어로 제공합니다.

## 스킬 사용법

Codex나 Claude Code 같은 에이전트에서 `/codyssey-rules` 뒤에 궁금한 내용을 자연어로 붙여 질문합니다.

```text
/codyssey-rules 이번 달 장학금 언제 들어와요?
/codyssey-rules 동료평가 디코로 해도 되나요?
/codyssey-rules 아이맥에서 한글 입력이 안 돼요
```

## 활용 문서

| 문서 | 주요 내용 | 활용되는 질문 |
| --- | --- | --- |
| `codyssey-regulations.md` | 운영 학칙, 학사/학습 관리, 장학금, 시설 사용, 징계 기준 | 장학금 지급 조건, 수료, 출석/출입, 시설 이용, 규정 위반 |
| `codyssey-peer-evaluation-rules.md` | 동료 평가 절차, 대면 평가 원칙, 금지 행위, 피드백 기준, Q&A | 동료 평가 진행 방식, 원격 평가, 노쇼, FAIL, 피드백 작성 |
| `neito-now-supports-image-video-and-voice-tts-generation.md` | Neito 이미지·영상·음성 생성 기능, 토큰 차감, 보존/다운로드 정책 | Neito 미디어 생성, 토큰 사용량, 파일 다운로드와 보존 기간 |
| `github-discord-integration-manual.md` | GitHub 기본 사용법, Codyssey 코드저장소 연동, Discord 연결 | GitHub 계정/토큰 연동, 레포지토리 공개 설정, Discord 인증 |
| `imac-macos-sequoia-korean-input-guide.md` | iMac macOS Sequoia 한글 입력 설정, 구름 입력기, 한/영 전환 | iMac 한글 입력, 구름 입력기 활성화, 단축키 충돌 해결 |
| `password-change-guide.md` | iMac 비밀번호 변경, 비밀번호 정책, 키체인 주의사항 | 임시 비밀번호, `passwd` 명령, 비밀번호 복잡도, 키체인 업데이트 |

## 예시 질의응답

| 질의 | 응답 | 근거 |
| --- | --- | --- |
| 이번 달 장학금 언제 들어와요? | 월별 장학금 지급 요건을 충족하면 익월 중 교육생 지급 계좌로 지급됩니다. | `codyssey-regulations.md` Page 8, 제13조 ①: "익월 중에 교육생 지급 계좌로 장학금을 지급한다." |
| 80시간 못 찍었는데 장학금 아예 못 받나요? | 아예 못 받는다고 단정할 수는 없습니다. 본과정과 AI네이티브에는 40시간 이상 80시간 미만 50만원 구간이 있지만, 활동 및 동료평가 기준 등 모든 지급 조건을 충족해야 합니다. | `codyssey-regulations.md` Page 9, 장학금 지급 기준: "50만원 40시간 이상~80시간 미만", "모든 지급 조건을 충족해야 함" |
| 프리랜서나 알바 중이어도 장학금 받을 수 있어요? | 프리랜서 등 소득이 있는 경우는 장학금 지급 대상에서 제외됩니다. 알바는 문서에 별도 용어로 명시되어 있지 않으므로, 공식 문서 기준으로는 4대 보험 가입 재직자 또는 소득이 있는 경우에 해당하는지 확인해야 합니다. | `codyssey-regulations.md` Page 9, 제13조 ⑧ 2호: "재직자 등 4대 보험 가입자와 자영업자·프리랜서 등 소득이 있는 경우... 장학금 지급 대상에서 제외한다." |
| 동료평가 디코로 하면 안 돼요? | 안 됩니다. 동료평가는 캐빈에서 대면으로 진행해야 하며 원격 평가는 금지됩니다. Discord는 평가 시작 전 시간 조율에 활용할 수 있는 수단으로만 확인됩니다. | `codyssey-peer-evaluation-rules.md` 1. 평가 진행 기본 원칙, 2. 평가 시퀀스: "반드시 캐빈에서 대면으로 진행", "원격 평가는 금지", "Discord 등을 활용한 상호 소통" |
| 평가 상대가 안 오는데 이거 어떻게 해요? | 평가자가 오지 않으면 평가 시작 시간부터 15분이 지난 뒤 피평가자가 취소할 수 있습니다. 반대로 피평가자가 연락 두절이면 평가자가 해당 프로젝트를 FAIL 처리할 수 있습니다. | `codyssey-peer-evaluation-rules.md` 2. 평가 시퀀스, 노쇼 처리 기준: "15분 경과 후 피평가자가 평가를 취소", "피평가자가 연락 두절인 경우... FAIL 처리" |
