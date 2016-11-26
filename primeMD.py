# parsing primeMD

import requests
from bs4 import BeautifulSoup as bs


def get_html(info):
    print('start requests')
    # javascript:viewAction('view', '2017', '20', '1001', '3008', 'kim24682468', 'thankeun', '5388');
    # viewAction('view', '2017', '20',     '1001',     '3148',   'cindy567', 'thankeun', '5390');
    # viewAction(cmd, ent_year, test_type, apply_div, univ_code, user_id,   session_id, sid)
    payload = {
        'bid': 'interview',
        'cmd': 'view',
        'menuid': '',
        'gubun_apply_div': '',
        'ent_year': info[1],
        'test_type': info[2],
        'apply_div': '',
        'univ_code': info[4],
        'user_id': info[5],
        'keyw2': '',
        'keyh': '',
        'sid': ''
    }

    with requests.Session() as s:
        res = s.post('http://www.pmd.co.kr/pmd/postscript', data=payload)
        html = res.text
        print(html)

        soup = bs(html, 'html.parser')
        texts = soup.select(
            'table.view_cont_tbl'
        )
        print(texts)
        f = open('some.html', 'w+')
        for i in texts:
            f.write(str(i))
        f.close()



    print('end requests')


if __name__ == '__main__':
    info = input('링크복붙: ')
    info = str(info.replace("javascript:viewAction('view'","").replace(");","")).strip().split(',')
    list = []
    for i in info:
        list.append(i.strip().replace("'",''))
    print(list)
    
    get_html(list)