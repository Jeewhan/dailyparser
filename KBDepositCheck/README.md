# KBDepositCheck
## 구현기능
1. KB은행 간편조회에 등록된 계좌에 한해 사용가능
2. 사용자가 일정의 재설정 가능
3. python3에 구현 맞춰져 있음
4. 환경변수로 접근해서 사용하게 됨
  ~/.bashrc 파일에 (zsh 의경우 ~/.zshrc 파)
```
#ENV for BANK PY
export RESIDENTNUMBER=주민번호 뒤7자리
export BANKID=국민은행ID
export BANKPW=계좌비밀번호4자리
export ACCOUNTNUMBER=계좌번호
```
  이같은 형식으로 입력후 사용 가능
  bash를 재실행 하지 않고 적용하기 위해서라면
```
$source ~/.bashrc (혹은 $source ~./.zshrc)
```
  명령어로 바로 로딩이 가능합니다.
5. 외부 라이브러리로서 사용할 때
```
from KBDepositCheck.CheckBalance import Transaction

#사용할경우
Transaction.
```


## 추가예정기능
1. Django ORM에 Celery를 통해 비동기 방식(스케쥴러)으로 동작
  Payment가 이루어진 경우에는 django db인스턴스 객체 생성 후 db에 반영함.
  사용 조건은 다음과 같음
  * 무통장 입금 기한은 실행 시간부터 24시간 이내로 할 것
  * 무통장 계좌 번호와 금액 안내가 사용자 휴대폰으로 안내됨.
  * 등록된 유저가 마이페이지에서 결제 페이지로 들어갈 경우에 결제정보를 볼 수 있어야 함.
