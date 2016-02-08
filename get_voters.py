# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import re
import time
import login_hahaha
#https://www.zhihu.com/question/20899988/
#https://www.zhihu.com/answer/6224783/voters_profile?total=563&offset=0
#input....

class Voter:
    def __init__(self):
        self.data={
            'ID':None,
            'Name':'Not Edited',
            'location':'Not Edited',
            'thanks':0,
            'agree':0,
            'asks':0,
            'answers':0,
            'followers':0,
            'followees':0
            }
    def printv(self):
        print 'ID',self.data['ID']
        print 'Name',self.data['Name']
        print 'location',self.data['location']
        print 'thanks',self.data['thanks']
        print 'agree',self.data['agree']
        print 'asks',self.data['asks']
        print 'answers',self.data['answers']
        print 'followers',self.data['followers']
        print 'followees',self.data['followees']
class Answer:
    def __init__(self):
        self.data={
            'ID': 'None',
            'Name': 'None',
            'Publish':'None',
            'Edited':'None',
            'Text': 'None',
            'Reviews':'0',
            'Voters':{}
            }
    def printa(self):
        print 'ID',self.data['ID']
        print 'Name',self.data['Name']
        print 'Text',self.data['Text']
        print 'Publish',self.data['Publish']
        print 'Edited',self.data['Edited']
        print 'done'
def get_voter_id(driver,answer):
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
        id_list_ori=re.findall(pat,content)
        for i in id_list_ori:
            voter=Voter()
            voter.data['ID']=i[15:-10]
            voter_url='https://www.zhihu.com/people/'+voter.data['ID']
            driver.get(voter_url)
            try:
                names=driver.find_elements_by_class_name('name')
                voter.data['Name']=names[1].text
            except:pass
            try:
                voter.data['location']=driver.find_element_by_css_selector('span[class=\"location item\"]').text
            except:pass
            voter.data['thanks']=driver.find_element_by_class_name('zm-profile-header-user-thanks').text[:-2]
            voter.data['agree']=driver.find_element_by_class_name('zm-profile-header-user-agree').text[:-2]
            nums=driver.find_elements_by_class_name('num')
            voter.data['asks']=nums[0].text
            voter.data['answers']=nums[1].text
            follow=driver.find_elements_by_css_selector('a[class=\"item\"]')
            voter.data['followers']=follow[1].text[4:-1]
            voter.data['followees']=follow[0].text[4:-1]
            answer.data['Voters'].setdefault(voter.data['ID'],voter)
            voter.printv()
    return answer
