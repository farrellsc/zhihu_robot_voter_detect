from selenium import webdriver
import re
import login_hahaha
import get_question
import get_answers
import get_voters
import mkdir
import os
import time
#https://www.zhihu.com/question/22722259
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
        
driver=login_hahaha.login()
url='https://www.zhihu.com/question/22722259' 
driver.get(url)
'driver=get_question.process_question_page(driver)'
question=Question()
question=get_question.get_question(driver)
question=get_answers.get_answers(driver,question)
for i in question.data['Answers']:
    print question.data['Answers'][i].printa()
'''
question=get_voters.get_voter_id(driver.question)
mkdir.mkdir(question)
'''
