import requests
from bs4 import BeautifulSoup as bs


def _get_content_how_many(booknum):
    html = requests.get(
        'http://www.joara.com/premium_new/book_intro.html?book_code={}'.format(
            booknum)
        )
    soup = bs(html.text, 'html.parser')
    urls = soup.select(
        'div.work_view > span.select'
    )
    if len(urls) > 1:
        raise Exception("There's more info in page!")
    else:
        how_many = int(urls[0].text.strip().replace('편',''))
    return how_many


def make_txt(booknum, payload):
    whole_book = []
    how_many = _get_content_how_many(booknum)
    with requests.Session() as s:
        def _get_texts(booknum, inning_num):
            html = s.get(
                'http://mw.joara.com/web_viewer/book_view.html?book_code={booknum}&sortno={inning_num}'.format(
                    booknum = booknum,
                    inning_num = inning_num
                )
            )
            #print(html.text)
            soup = bs(html.text, 'html.parser')
            texts = soup.select(
                'article'
            )
            real_texts_list = []

            for text in texts:
                real_texts_list.append(
                    text.text.replace(
                        '\xa0','').replace(
                        '\n\n','\n').replace(
                        '\u3000','')
                    )
            real_texts = ''.join(real_texts_list)
            return real_texts

        auth = s.post('https://www.joara.com/loginExe.html', data=payload)
        text = []
        for i in range(1, how_many+1):
            text.append(_get_texts(booknum, i) + '\n')
            print('({}%) {}/{} downloaded'.format(int(i/how_many*100), i, how_many))
        return text


# make file if it is work by own
if __name__=='__main__':
    joara_id = input('JOARA ID: ')
    joara_pw = input('JOARA PW: ')
    payload = {
    'member_id': joara_id,
    'passwd': joara_pw
    }
    booknum = input('JOARA BOOKNUM: ')
    text = make_txt(booknum, payload)
    f = open('book_{}.txt'.format(booknum),'w+')
    for i in text:
        f.write(i)
    f.close()
    f = open('book_{}.txt'.format(booknum),'r')
    rd = f.readlines()
    f.close()

    for i in rd:
        if i != '\n':
            f.write(i)
    f.close()
