# dailyparser
- 생활에 필요한 WebParser들을 Apache라이센스로 공개합니다.
- 자세한 라이센스는 LICENSE파일을 참고하세요.
- 소스를 받아 사용함에 있어서 따르는 제약은 컨텐츠 제공업체의 표준계약에 따르며,
  사용 지역에 따른 법률을 준수하시길 권장합니다.
- 본 소스는 정식 구매자의 오프라인 독서를 위해 제작되었습니다.
- 본 프로그램을 통해 혹은 여타 방법으로 만든 텍스트 파일의 저작권은 작가와 출판사에 귀속되며,
  배포시 사적복제의 영역을 넘어가므로 저작권 관련 법률에 의거 법적 처벌을 받을 수 있습니다.
- 기본적으로 Python3에서 작동합니다.

## Ridibooks (리디북스)
### 개요
- Request, BeautifulSoup, Selenium을 사용합니다.
- Firefox가 구동 시스템에 설치되어있어야 합니다. (크롬으로도 가능하지만 권장하지 않습니다.)
- 리디북스의 연재 책을 텍스트 파일로 만들 수 있습니다.
- 유의 사항은 다음과 같습니다.
  1. 책의 고유 번호(연재 리스트에 들어간 경우 주소창에 뜨는 10자리 숫자를 확인하면 됩니다.
    (http://ridibooks.com/v2/Detail?id=0000000000 의 경우 제일 0000000000)
  2. 구매한/대여한 책(단, 연재본의 경우 대여시스템이 없으므로 현재는 구매한 책)만 받을 수 있습니다.
  3. 파이어폭스의 최신버전이 설치되어있어야 합니다.
  4. Python3.4 / 3.5 이상의 버전(혹은 2.7)이 설치되어있어야 합니다.
    (단, 2.7에서는 unicode error가 발생할 수 있습니다.)
  5. OS X El Capitan에서 정상 작동합니다.
  6. Windows의 경우 시스템 설정에 따라 Unicode Error가 발생할 수 있습니다.
- pip모듈은 requirements.txt로 설치가 가능합니다.
- booklist\_parser.py 파일 실행 후 contents\_parser.py를 실행합니다.
- booklist\_parser.py 파일은 로그인이 필요하지 않으며, contents\_parser.py는 로그인이 필요합니다.
- 전반적인 사용 방법입니다.
```
    $ git clone https://github.com/Beomi/dailyparser.git
      (git을 사용하지 않는 경우에는 소스를 압축파일로 받으시면 됩니다.)
    $ cd dailyparser
    $ pip install -r requirements.txt
    (virtualenv / pyvenv 사용을 추천합니다.)
    $ cd ridibooks
    $ python booklist_parser.py
      책의 고유번호를 입력해주세요: (10자리 책 번호를 입력해주세요)
      연재본의 링크가 들어있는 txt파일이 생성됩니다.
    $ python contents_parser.py
      Input your RIDI ID: (리디북스 아이디 입력)
      Input your RIDI PW: (리디북스 비밀번호 입력)
      Input booknumber: (책 번호 입력)
      자동적으로 Firefox가 실행되며 파싱을 시작합니다.
```
- Known-Issues
  1. 윈도우에서 Unicode Error문제 가능성
  2. 리디북스 연재본의 다음 링크로 넘어갈 때 불규칙적으로 로그인이 풀리는 문제
    현재 이 경우, 콘솔(shell / terminal / cmd ..)에 '계속' 문구 출력 후 대기.
    로그인시 '로그인 유지' 선택할 경우 더이상 로그인 풀리지 않음.

## Joara (조아라)
### 개요
- Request와 BeautifulSoup을 사용합니다.
- 조아라의 연재도서들을 텍스트 파일로 만들 수 있습니다.
### 구현기능
- 조아라 책의 고유 번호와 아이디, 비밀번호를 입력하면 자동으로 받아서 한 텍스트 파일로 합쳐줍니다.
### 사용법
```
    $ git clone https://github.com/Beomi/dailyparser.git
      (git을 사용하지 않는 경우에는 소스를 압축파일로 받으시면 됩니다.)
    $ cd dailyparser
    $ pip install -r requirements.txt
    (virtualenv / pyvenv 사용을 추천합니다.)
    $ cd joara
    $ python parsing.py
      JOARA ID: (조아라 아이디 입력)
      JOARA PW: (조아라 비밀번호 입력)
      JOARA BOOKNUM : (책 번호 입력)

      퍼센트가 올라가며 파싱이 완료됩니다.
```

## KBDepositCheck (국민은행 빠른조회)
### 구현기능
1. KB은행 간편조회에 등록된 계좌에 한해 사용가능
2. 사용자가 일정의 재설정 가능
3. python3으로 이용가능
4. 환경변수로 접근해서 사용하게 됨
  /etc/bash.bashrc 파일에
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
source /etc/bash.bashrc
```
  명령어로 사용 가능.

### 추가예정기능
1. Django ORM에 Celery를 통해 비동기 방식(스케쥴러)으로 동작
  Payment가 이루어진 경우에는 django db인스턴스 객체 생성 후 db에 반영함.
  사용 조건은 다음과 같음
  * 무통장 입금 기한은 실행 시간부터 24시간 이내로 할 것
  * 무통장 계좌 번호와 금액 안내가 사용자 휴대폰으로 안내됨.
  * 등록된 유저가 마이페이지에서 결제 페이지로 들어갈 경우에 결제정보를 볼 수 있어야 함.
