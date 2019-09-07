import requests
from bs4 import BeautifulSoup
import pandas as pd

url_prefix = "http://www.pbc.gov.cn/zhengwugongkai/127924/128041/2951606/1923625/1923629/d6d180ae/index"
url_appendix = ".html"

title_list = []
count = 0

url_list = []
for i in range(1, 13,1):
    url = url_prefix + str(i) + url_appendix
    url_list.append(url)

#get html
#cookie refresh in 1 min
headers = {
    'Cookie':"wzws_cid=d3cb5dffc034e514e7b6a2a0fae614de29378f514c7b0957d7b1623d3f20a7b415856735d4a7c6bfa4b0e9f8f879b359",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
}

for url_element in url_list:
    response = requests.get(url_element,headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    # print(type(html))
    soup = BeautifulSoup(html,"html.parser")
    # parse html
    for element in soup.select('td.hei12jj'):
        title_father = element.select('font.hei12')
        # print(title_father)
        if len(title_father) > 0:
            title = title_father[0].text
            title_list.append(title)
            count += 1
            print(count)


ALL_TITLES = pd.Series(title_list)
ALL_TITLES.to_excel("pbc_all_titles.xlsx")