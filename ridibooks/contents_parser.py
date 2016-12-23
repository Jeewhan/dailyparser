# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import json


def get_content(user_id, user_pw, booknumber):
    #func get_htmls : get rendered html from firefox, retries 2 times for slow networks.
    def get_htmls(url, max_try_times):
        try_time = 1
        def get_html_raw(url, try_time):
            try:
                driver.get(url)
                driver.implicitly_wait(15)
                driver.find_element_by_id('ridi_c1')  # check if texts are loaded or not
                htmls = driver.find_elements_by_tag_name('article')
                return htmls
            except:
                sleep(2)
                driver.get(base_url + "account/login")
                driver.find_element_by_name("user_id").clear()
                driver.find_element_by_name("user_id").send_keys(user_id) #str type, input RIDI ID
                driver.find_element_by_name("passwd").clear()
                driver.find_element_by_name("passwd").send_keys(user_pw) #str type, input RIDI PW
                driver.find_element_by_css_selector("button.blue_button.submit_button").click()

                sleep(2)
                htmls = get_html_raw(url, try_time)
                return htmls

        htmls = get_html_raw(url, try_time)
        return htmls

    
        

    driver = webdriver.PhantomJS('phantomjs')
    driver.implicitly_wait(3)
    base_url = "https://ridibooks.com/"
    #driver = webdriver.Chrome('chromedriver')
    driver.get(base_url + "account/login")
    driver.find_element_by_name("user_id").clear()
    driver.find_element_by_name("user_id").send_keys(user_id) #str type, input RIDI ID
    driver.find_element_by_name("passwd").clear()
    driver.find_element_by_name("passwd").send_keys(user_pw) #str type, input RIDI PW
    driver.find_element_by_css_selector("button.blue_button.submit_button").click()

    sleep(2)


    #get lists
    book_list = open('book_list_{}.txt'.format(booknumber),'r').readlines()

    f = open('book_{}.txt'.format(booknumber), 'w+')

    #input max_retry_times
    max_try_times = 3

    book_length = len(book_list)

    for idx, book in enumerate(book_list):
        url = str(book).replace('\n','')
        htmls = get_htmls(url, max_try_times)
        for html in htmls:
            f.write(html.text + '\n{}\n'.format('-' * 10))
        print('({}%) {}/{}'.format(str(((idx+1)/book_length)*100)[:4], idx+1, book_length))


    f.close()

    print('end')


if __name__ == "__main__":
    env = open('envs.json')
    env_json = json.load(env)
    print(env_json)
    user_id = env_json['ridi_id']
    user_pw = env_json['ridi_pw']
    booknumber = env_json['book_num']
    get_content(user_id, user_pw, booknumber)
