# -*- coding: utf-8 -*-
from selenium import webdriver
import re
import login_hahaha
import get_question
import get_answers
import get_voters
import mkdir
import os
import time
#https://www.zhihu.com/question/40175228
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
class Answer(Question):
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
        print 'Reviews',self.data['Reviews']
        print 'done'

question_id=raw_input('input question id:')
driver=login_hahaha.login()
url='https://www.zhihu.com/question/'+question_id 
driver.get(url)
'driver=get_question.process_question_page(driver)'
question=Question()
question=get_question.get_question(driver,question_id)
print ' '
question=get_answers.get_answers(driver,question,question_id)
for i in question.data['Answers']:
    answer_url=url+'/answer/'+question.data['Answers'][i].data['ID']
    driver.get(answer_url)
    i=get_voters.get_voter_id(driver,question.data['Answers'][i])
'''
mkdir.mkdir(question)
'''
