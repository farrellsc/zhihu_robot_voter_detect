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
            'Answers': {}
            }
class Answer(Question):
    def __init__(self):
        self.data={
            'ID': None,
            'Name': None,
            'Publish':None,
            'Edited':None,
            'Text': None
            }
    def printa(self):
        print 'ID',self.data['ID']
        print 'Name',self.data['Name']
        print 'Text',self.data['Text']
        print 'Publish',self.data['Publish']
        print 'Edited',self.data['Edited']
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
        url='https://www.zhihu.com/question/22722259/answer/'+i
        driver.get(url)
        answer=Answer()
        answer.data['ID']=i
        answer.data['Name']=driver.find_element_by_class_name('author-link').text
        answer.data['Text']=driver.find_element_by_css_selector('div[class=\"zm-editable-content clearfix\"]').text
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
        #answer-date-link-wrap date
    return question
    
    #div class="zh-summary summary clearfix" 回答内容
    #a class="answer-date-link last_updated meta-item" 回答编辑日期， 用正则
    #h3 data-num="793" id="zh-question-answer-num">793 个回答
    #<span class="count">522</span>赞同
    #a class="author-link" 回答作者
    return answer
    
