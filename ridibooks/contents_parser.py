# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


def get_content(user_id, user_pw, booknumber):
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
        driver.get(url)
        sleep(1)
        try:
            html = driver.find_element_by_id('ridi_c1')
        except:
            try:
                driver.get(url)
                sleep(2)
                html = driver.find_element_by_id('ridi_c1')
            except:
                input('계속')
                driver.get(url)
                sleep(5)
                html = driver.find_element_by_id('ridi_c1')
        html = html.text
        f.write(html+'\n{}\n'.format('-'*10))

    f.close()

    print('end')


if __name__ == "__main__":
    user_id = input('Input your RIDI ID: ')
    user_pw = input('Input your RIDI PW: ')
    booknumber = input('Input booknumber: ')
    get_content(user_id, user_pw, booknumber)
    print("ENDED")
