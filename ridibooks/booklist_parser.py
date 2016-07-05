# coding: utf-8

import requests
from bs4 import BeautifulSoup


def get_book(booknumber):
    html = requests.get('http://ridibooks.com/v2/Detail?id={}'.format(booknumber)) #input your books origin number
    soup = BeautifulSoup(html.text, 'html.parser')
    urls = soup.select(
        'div.book_list_wrapper'
    )

    lists = []
    for url in urls:
        real_url = url['data-book-id'].strip()
        lists.append(real_url)

    return lists


if __name__ == '__main__':
    booknumber = input('책의 고유번호를 입력해주세요: ')
    f = open('book_list_{}.txt'.format(booknumber),'w+')
    booklist = get_book(booknumber)
    for i in booklist:
        f.write(
            'https://view.ridibooks.com/books/'+i+'\n'
        )
    f.close()
