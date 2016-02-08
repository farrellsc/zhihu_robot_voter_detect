# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import re
import time
import login_hahaha
import get_question
#https://www.zhihu.com/question/20899988/
#https://www.zhihu.com/answer/6224783/voters_profile?total=563&offset=0
#input....
        
class Question:
    def __init__(self):
        self.data={
            'Text':None,
            'Answernum':None,
            'Followernum':0,
            'Publish':None,#昨天
            'Updated':'Never Updated',
            'Reviewed':0,
            'Answers': {}
            }
    def printq(self):
        print 'Text',self.data['Text']
        print 'Answernum',self.data['Answernum']
        print 'Followernum',self.data['Followernum']
        print 'Publish',self.data['Publish']
        print 'Updated',self.data['Updated']
        print 'Reviewed',self.data['Reviewed']
class Answer:
    def __init__(self):
        self.data={
            'ID': 'None',
            'Name': 'None',
            'Agree':'0',
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
        print 'Reviews',self.data['Reviews']
        print 'done'
def get_answers(driver,question):
    author_name=driver.find_elements_by_class_name('author-link')
    content=driver.page_source
    pattern_answer_ID=re.compile('data-atoken=\".{,15}\"')
    answer_ID_raw=pattern_answer_ID.findall(content)
    answer_ID=[]
    for i in answer_ID_raw:
        answer_ID.append(i[13:-1])
    for i in answer_ID:
        url='https://www.zhihu.com/question/40175228/answer/'+i
        driver.get(url)
        answer=Answer()
        answer.data['ID']=i
        answer.data['Name']=driver.find_element_by_class_name('author-link').text
        answer.data['Text']=driver.find_element_by_css_selector('div[class=\"zm-editable-content clearfix\"]').text
        '''review_button=driver.find_elements_by_name('addcomment')
        review_button[1].click()
        reviews=driver.find_elements_by_name('addcomment')
        answer.data['Reviews']=reviews[1].text[0:2]''' #bug
        answer.data['Agree']=driver.find_element_by_class_name('count').text
        content=driver.page_source.split('\n')
        for line in content:
            if 'answer-date-link ' in line:
                if 'data-tip' in line:
                    pattern_pub=re.compile(r'data-tip=.{22}')
                    pub_date=pattern_pub.findall(line)
                    answer.data['Publish']=pub_date[0][18:-3]
                    answer.data['Edited']=line[-14:-4]
                else:
                    answer.data['Edited']='Never Edited'
                    answer.data['Publish']=line[-14:-4]
                break
        question.data['Answers'].setdefault(answer.data['ID'],answer)
    return question
    

    #h3 data-num="793" id="zh-question-answer-num">793 个回答
    #<span class="count">522</span>赞同

    
