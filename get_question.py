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
            'Answers': {}
            }

def process_question_page(driver):
    for i in range(1,200):
        try:
            button=driver.find_element_by_css_selector("a[class=\"zg-btn-white zu-button-more\"]")
            button.click()
            time.sleep(2)
        except:
            break
    return driver

def get_question(driver):
    question=Question()
    question.data['Text']=driver.find_element_by_css_selector("h2[class=\"zm-item-title zm-editable-content\"]").text[:-2]
    question.data['Answernum']=driver.find_element_by_css_selector("h3[id=\"zh-question-answer-num\"]").text[:-3]
    question.data['Followernum']=driver.find_element_by_css_selector('a[href=\"/question/22722259/followers\"]').text
    return question






    

