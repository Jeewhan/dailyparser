# parsing primeMD

import requests
from bs4 import BeautifulSoup as bs


def get_list():
    with requests.Session() as s:
        print('get urls')
        for pagenum in range(1,5):
            res = s.get('http://www.pmd.co.kr/pmd/postscript?page={}&bid=interview&cmd=list&keyh=title&keyw2=%B0%E6%BA%CF%B4%EB'.format(pagenum))
            html = res.text
            soup = bs(html, 'html.parser')
            ss = soup.select(
                'td.subject > a'
            )
            for i in ss:
                info = (i['href'])
                get_html(info)


def get_html(info):
    infos = str(info.replace("javascript:viewAction('view'", "").replace(");", "")).strip().split(',')
    lists = []
    for i in infos:
        lists.append(i.strip().replace("'", ''))
    print(lists)
    print('start requests')
    # javascript:viewAction('view', '2017', '20', '1001', '3008', 'kim24682468', 'thankeun', '5388');
    # viewAction('view', '2017', '20',     '1001',     '3148',   'cindy567', 'thankeun', '5390');
    # viewAction(cmd, ent_year, test_type, apply_div, univ_code, user_id,   session_id, sid)
    payload = {
        'bid': 'interview',
        'cmd': 'view',
        'menuid': '',
        'gubun_apply_div': '',
        'ent_year': lists[1],
        'test_type': lists[2],
        'apply_div': '',
        'univ_code': lists[4],
        'user_id': lists[5],
        'keyw2': '',
        'keyh': '',
        'sid': ''
    }

    with requests.Session() as s2:
        res = s2.post('http://www.pmd.co.kr/pmd/postscript', data=payload)
        html = res.text
        print(html)
        soup = bs(html, 'html.parser')
        texts = soup.select(
            'table.view_cont_tbl'
        )
        print(texts)
        f = open('temp/{}.html'.format(lists[5]), 'w+')
        for i in texts:
            f.write(str(i))
        f.close()



    print('end requests')


if __name__ == '__main__':

    
    get_list()