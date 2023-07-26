from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
url = 'https://www.vancouverislandfreedaily.com/business/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req)

html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
# base_url = 'https://www.vancouverislandfreedaily.com/business/page/'
# for page_num in range(2,10):
#     cur_url = base_url + str(page_num)
#     page = urlopen(cur_url)
#     html = page.read().decode('utf-8')

articles_name = soup.find_all('h4')

print(articles_name)
