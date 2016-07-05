# dailyparser

## Ridibooks (리디북스)
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
    $ python booklist\_parser.py
      책의 고유번호를 입력해주세요: (10자리 책 번호를 입력해주세요)
      연재본의 링크가 들어있는 txt파일이 생성됩니다.
    $ python contents\_parser.py
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
      
