# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta
from os import environ


class Transaction(object):
    def __init__(self):
        try:
            # TODO: you should export envs before execute!
            self.residentnumber = environ['RESIDENTNUMBER']
            self.bankid = environ['BANKID']
            self.password = environ['BANKPW']
            self.accountnumber = environ['ACCOUNTNUMBER']
        except KeyError:
            print("TODO: you should export envs before execute!")

    @property
    def check_transactions(self):
        url = 'https://obank1.kbstar.com/quics?page=C025255&cc=b028364:b028702'
        payload = dict(
            KEYPAD_TYPE_139833834814='3',
            
            
            고객ID= self.bankid.upper(), #인터넷 뱅킹 ID
            비밀번=self.password, #계좌 비밀번호
            조회시작년='2016',
            조회시작월='12',
            조회시작일='03',
            조회끝년='2016',
            조회끝월='12',
            조회끝일='04',
            검색구분='1',
            빠른조회='Y',
            조회구분='2',
            응답방법='2',
            #startday= (date.today()-timedelta(1)).strftime("%Y%m%d"), #조회시작일/어제
            #endday= date.today().strftime("%Y%m%d"), #조회마감일/오늘
            조회계좌=self.accountnumber #계좌번호
        )
        with requests.Session() as s:
            res = s.post(url, data=payload)
            if res == '':
                raise Exception('반환받은 결과가 없음')
            html = res.text
            print(html)
            soup = bs(html, 'html.parser')
            infos = soup.select('tr[align:center] > td')
            item_quantitys = int(len(infos)) / 9
            item_seq = 0
            transactions = []
            while item_seq < item_quantitys:
                transaction = []
                seq = infos[item_seq*9:item_seq*9+8]
                for i in seq:
                    transaction.append(i.text.strip())
                transactions.append(transaction)
                item_seq += 1
            return transactions

    @property
    def get_transact_dic(self):
        results = self.check_transactions
        result_dics = []
        for info in results:
            transact_date = info[0].strip()[:10]
            transact_time = info[0].strip()[10:]
            transact_by = info[2].strip()
            if info[4] != '0':
                transact_amount = "-" + info[4].strip()
            else:
                transact_amount = "+" + info[5].strip()
            print("거래일시: {}\n거래시각: {}\n​거래처: {}\n거래금액: {}".format(
                transact_date, transact_time, transact_by, transact_amount
            ))
            result_dics.append({
                'date': transact_date,
                'time': transact_time,
                'by': transact_by,
                'amount': transact_amount
            })
        return result_dics

if __name__=='__main__':
    tr = Transaction()
    print(tr.check_transactions)
