from collections import deque
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request
import urllib.parse


url="https://juejin.cn/post/7119764025210044423#heading-19"

local_domain = urlparse(url).netloc
#ParseResult(scheme='https', netloc='juejin.cn', path='/post/7119764025210044423', params='', query='', fragment='heading-19')

"""
# url2 = "https://juejin.cn/search?query=gpts&fromSeo=0&fromHistory=0&fromSuggest=0"

#ParseResult(scheme='https', netloc='juejin.cn', path='/search', params='', query='query=gpts&fromSeo=0&fromHistory=0&fromSuggest=0', fragment='')
# local_domain2 = urlparse(url2)
# print(local_domain2)
"""

print(local_domain)

queue = deque([url])

while queue:
    url = queue.pop()
    # print(url)

if not os.path.exists('debug/'):
    os.mkdir('debug/')

if not os.path.exists("debug/"+local_domain+"/"):
        os.mkdir("debug/" + local_domain + "/")
# try:
#     with open('debug/' + local_domain + '/' + url[8:].replace("/","-") + ".txt","w",encoding="utf-8") as f



# BeautifulSoup 使用

"""

soup = BeautifulSoup(requests.get(url).text, "html.parser")

# 查找标题标签
text = soup.text
print("text:", text)
# 查找标题标签
title_tag = soup.title
print("标题标签:", title_tag)

# 查找第一个 div 标签的内容
div_content = soup.find('div', class_='content')
print("div 标签内容:", div_content)

# 查找所有段落标签
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print("段落内容:", paragraph.text)

# 查找和遍历列表项
list_items = soup.find('ul').find_all('li')
for item in list_items:
    print("列表项:", item.text)
"""
try:
    # Open the URL and read the HTML
    with urllib.request.urlopen(url) as response:
        # If the response is not HTML, return an empty list
        if  response.info().get('Content-Type').startswith("text/html"):
            # Decode the HTML
            html = response.read().decode('utf-8')
            print(html)
except Exception as e:
    print(e)

        