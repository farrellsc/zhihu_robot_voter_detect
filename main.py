from selenium import webdriver
import re
import xlwt
#https://www.zhihu.com/question/20777862/answer/27221618
#https://www.zhihu.com/answer/6224783/voters_profile?total=563&offset=0
que_id=raw_input('input the question id:')
ans_id=raw_input('input the answer id:')
post_id=raw_input('enter the responding url caught by firebug:')
#input....
#I could not really figure out how to automatically catch the id for 'more voters' because it seems the id was randomly patched by the host with no significant order.

driver=webdriver.Firefox()
url='https://www.zhihu.com/question/'+que_id+'/answer/'+ans_id
driver.get(url)
driver.find_element_by_class_name('more').click()
author_name=driver.find_element_by_class_name('author-link').text
voter_num=int(driver.find_element_by_class_name('count').text)
voter_name=[]
for i in range(0,voter_num,10):
    url='https://www.zhihu.com/answer/'+post_id+'/voters_profile?total='+\
         str(voter_num)+'&offset='+str(i)
    driver.get(url)
    content=driver.page_source
    pat='data-tip=.{,30}class='
    list_ori=re.findall(pat,content)
    list_fin=[]
    for i in list_ori:
        name=i[15:-10]
        list_fin.append(name)
    voter_name.extend(list_fin)
print 'Caught '+str(len(voter_name))+' voters among '+str(voter_num)+' voters.'
print 'Creating profile...'
#patch all the names into a list.For I did not log in,a few voters were hidden by the host.

could_be_script=[]
count=0
for i in voter_name:
    count+=1
    print count,i
    url='https://www.zhihu.com/people/' + i
    driver.get(url)
    vote_for_IDs=driver.find_elements_by_class_name('author-link')
    name=[]
    for r in vote_for_IDs:
        name.append(r.text)
    try:
        if name.count(name[0])!=len(name):
            continue
    except:
        pass
    #does this voter only vote for the author of our original answer?
    voter_profile=driver.find_elements_by_class_name('num')
    num=[]
    for r in voter_profile:
        num.append(r.text)
    if num.count('0')==len(num):
        could_be_script.append(i)
    #does this voter offered zero personal information?
    #if yes,add it to the list

print 'I think '+str(len(could_be_script))+' out of '+str(len(voter_name))+\
      ' voters ('+ str(voter_num-len(voter_name))+' voters are not included due to tech reasons) '+\
      'could be scripts.'
print 'the list is as follows:'
print could_be_script
