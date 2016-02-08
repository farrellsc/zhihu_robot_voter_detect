# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import re
import time
import login_hahaha
#https://www.zhihu.com/question/20899988/
#https://www.zhihu.com/answer/6224783/voters_profile?total=563&offset=0
#input....
class Question:
    def __init__(self):
        self.data={
            'Text':None,
            'Answernum':None,
            'Followernum':0,
            'Publish':None,
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

def process_question_page(driver):
    for i in range(1,200):
        try:
            button=driver.find_element_by_css_selector("a[class=\"zg-btn-white zu-button-more\"]")
            button.click()
            time.sleep(2)
        except:
            break
    return driver

def get_question(driver,question_id):
    question=Question()
    question.data['Text']=driver.find_element_by_css_selector("h2[class=\"zm-item-title zm-editable-content\"]").text[:-2]
    question.data['Answernum']=driver.find_element_by_css_selector("h3[id=\"zh-question-answer-num\"]").text[:-3]
    question.data['Followernum']=driver.find_element_by_css_selector('a[href=\"/question/'+question_id+'/followers\"]').text
    gray=driver.find_elements_by_css_selector('div[class=\"zg-gray-normal\"]')
    #line=question.data['Reviewed']=gray[2].text
    #line=line.split('，')[0]
    #question.data['Reviewed']=line.split(' ')[1]   review not done
    question.data['Updated']=driver.find_element_by_class_name('time').text
    question.data['Publish']=driver.find_element_by_css_selector('a[class=\"answer-date-link meta-item\"]').text[4:]
    return question






    

