# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:55:43 2020

@author: Annie
"""

food = []
def get_name(url):
    _DELAY = 1.5  # 確認網頁有LOAD好 再進行爬蟲 如未載好 相隔_DELAY再爬
    _STATUS = 0
    while (_STATUS==0):
        try:
            elements = driver.find_elements_by_tag_name('img')
            if len(elements) > 0:
                for prod in elements:
                    if len(prod.get_attribute('alt')) > 0:
                        food.append(prod.get_attribute('alt'))
                        #if len(elements.get_attribute('alt')) > 0:
                        #    food.append(elements.get_attribute('alt'))
                    # 找到了, 網頁應已經載入成功
                    #    _STATUS = 1
                    #break
            else:
                time.sleep(_DELAY)
        except:
            pass
        
        #time.sleep(_DELAY)
    return 1

# 抓
page = 1 # 追蹤第幾頁有問題
n = 5 # 跳頁秒數
for url in url_1[3:15]:
    driver.get(url)
    get_yahoo_name(url)
    print('This is page: '+ str(page))
    #food.append('This is page: '+ str(page))
    time.sleep(n)
    #n += 0.5
    page += 1

# 去除抓到重複的
food_check  = sorted(set(food),key = food.index)
# save
with open('0429UDN_sweet.txt','w',encoding='UTF-8') as file:
    for prod in food_check:
        file.write(prod + '\n')