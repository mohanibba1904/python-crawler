import bs4
import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *
workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Numbers')
table.write(0, 1, 'NAMES')
# table.write(0, 2, 'movie_name')
# table.write(0, 3, 'movie_introduction')
line = 1
url = "https://www.mcxindia.in/"
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
# }
f = requests.get(url)

movies_lst = []
soup = BeautifulSoup(f.content, 'lxml')

mcx = soup.find_all('table',{
  'class': 'home-table'
})
num = 1
names = []
for items in mcx:
  # if items.text.strip() != '':
  #   names.append((items.text.strip()))
  names.append(items.td.h2.text)
  
for i in names:  
  table.write(line, 0, num)
  table.write(line, 1, i)
  line += 1
  num += 1
  workbook.save('MCX.xls') 

  
spanvalues = soup.find_all('span',{
  'class': 'indexprice'
})  

for spn in spanvalues:
  print(spn.text)
# values = soup.find_all('td',{
#   'class': 'index-price'
# })
# valueslist = []
# for vl in values:
#   print(vl) 
# # soup = bs4(f.text, 'html.parser')
# movies = soup.find('div',{
#   'class': 'col-sm-12 col-md-4 col-lg-4 graph-md3'
# }).find_all('div')

# for i in movies:
#   print(i)


# lists = []
# for i in movies:
#   values = i.find('div', class_ = "bgs")
#   print(values.div)
# for anchor in movies:
#     urls = 'https://www.rottentomatoes.com' + anchor['href']
#     movies_lst.append(urls)
#     num += 1
#     movie_url = urls
#     movie_f = requests.get(movie_url, headers = headers)
#     movie_soup = BeautifulSoup(movie_f.content, 'lxml')
#     movie_content = movie_soup.find('div', {
#     'class': 'movie_synopsis clamp clamp-6 js-clamp'
#     })
#     print(num, urls, '\n', 'Movie:' + anchor.string.strip())
#     print('Movie info:' + movie_content.string.strip())
#     table.write(line, 0, num)
#     table.write(line, 1, urls)
#     table.write(line, 2, anchor.string.strip())
#     table.write(line, 3, movie_content.string.strip())
#     line += 1
#     workbook.save('movies_top100.xls')