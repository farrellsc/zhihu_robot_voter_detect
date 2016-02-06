# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import re
import time
import login_hahaha
#https://www.zhihu.com/question/20899988/
#https://www.zhihu.com/answer/6224783/voters_profile?total=563&offset=0
#input....

def get_voter_id(driver):
    content=driver.page_source
    voter_links=[] #stores all the voter post links
    answer_post_pattern=re.compile(u'data-aid=\".{,10}\"')
    voter_links_original=answer_post_pattern.findall(content)
    for i in voter_links_original:
        voter_links.append(i[10:-1])
    author_name=driver.find_element_by_class_name('author-link').text
    voter_num=int(driver.find_element_by_class_name('count').text)
    voter_id=[]
    for i in range(0,voter_num,10):
        url='https://www.zhihu.com/answer/'+voter_links[0]+'/voters_profile?total='+\
             str(voter_num)+'&offset='+str(i)
        driver.get(url)
        content=driver.page_source
        pat='data-tip=.{,30}class='
        list_ori=re.findall(pat,content)
        list_fin=[]
        for i in list_ori:
            name=i[15:-10]
            list_fin.append(name)
        voter_id.extend(list_fin)
    print 'Caught '+str(len(voter_id))+' voters among '+str(voter_num)+' voters.'
    print 'stored voter ID to voter_id'
    return voter_id
