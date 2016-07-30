# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


def get_content(user_id, user_pw, booknumber):
    #func get_htmls : get rendered html from firefox, retries 2 times for slow networks.
    def get_htmls(url, max_try_times):
        try_time = 1
        def get_html_raw(url, try_time):
            if try_time <= max_try_times:
                try:
                    driver.get(url)
                    sleep(try_time)
                    driver.find_element_by_id('ridi_c1')  # check if texts are loaded or not
                    htmls = driver.find_elements_by_tag_name('article')
                    return htmls
                except:
                    htmls = get_html_raw(url=url,try_time=try_time+1)
                    return htmls
            else:
                input('Plz login again (or) Buy books')
        htmls = get_html_raw(url, try_time)
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

    #input max_retry_times
    max_try_times = 3

    for book in book_list:
        url = str(book).replace('\n','')
        htmls = get_htmls(url, max_try_times)
        for html in htmls:
            f.write(html.text + '\n{}\n'.format('-' * 10))


    f.close()

    print('end')


if __name__ == "__main__":
    user_id = input('Input your RIDI ID: ')
    user_pw = input('Input your RIDI PW: ')
    booknumber = input('Input booknumber: ')
    get_content(user_id, user_pw, booknumber)
