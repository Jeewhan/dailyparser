# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


def get_content(user_id, user_pw, booknumber):
    #func get_htmls : get rendered html from firefox, retries 2 times for slow networks.
    def get_htmls(url):
        try:
            driver.get(url)
            sleep(1)  # give time to browser for rendering texts.
            driver.find_element_by_id('ridi_c1')  # check if texts are loaded or not
            htmls = driver.find_elements_by_class_name('chapter')
        except: #if texts aren't loaded yet.
            try:
                driver.get(url)
                sleep(2)
                driver.find_element_by_id('ridi_c1')  # check if texts are loaded or not
                htmls = driver.find_elements_by_class_name('chapter')
            except:
                input('로그인이 풀렸거나 구매하지 않은 책입니다. 계속하시려면 Return을 누르세요')
                driver.get(url)
                sleep(2)
                driver.find_element_by_id('ridi_c1')  # check if texts are loaded or not
                htmls = driver.find_elements_by_class_name('chapter')
        return htmls


    #driver open with Firefox
    driver = webdriver.Firefox()
    base_url = "http://ridibooks.com/"

    #login
    driver.get(base_url + "account/login")
    driver.find_element_by_name("user_id").clear()
    driver.find_element_by_name("user_id").send_keys(user_id) #str type, input RIDI ID
    driver.find_element_by_name("passwd").clear()
    driver.find_element_by_name("passwd").send_keys(user_pw) #str type, input RIDI PW
    driver.find_element_by_id('remember_login').click()
    driver.find_element_by_css_selector("button.blue_button.submit_button").click()

    #get lists
    book_list = open('book_list_{}.txt'.format(booknumber),'r').readlines()

    f = open('book_{}.txt'.format(booknumber), 'w+')

    for book in book_list:
        url = str(book).replace('\n','')
        htmls = get_htmls(url)
        for html in htmls:
            f.write(html.text + '\n{}\n'.format('-' * 10))


    f.close()

    print('end')


if __name__ == "__main__":
    user_id = input('Input your RIDI ID: ')
    user_pw = input('Input your RIDI PW: ')
    booknumber = input('Input booknumber: ')
    get_content(user_id, user_pw, booknumber)
