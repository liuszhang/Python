import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#my_url="http://www.cricbuzz.com/"
my_url="http://top.baidu.com/?fr=tph_right"
Client=uReq(my_url)

html_page=Client.read()
Client.close()


soup_page=soup(html_page,"html.parser")


#score_box=soup_page.findAll("div",{"class":"cb-col cb-col-25 cb-mtch-blk"})
score_box=soup_page.findAll("a",{"class":"list-title"})
l = len(score_box)
print(l)
for i in range(l):
	#print(score_box[i].a["title"])
	print(score_box[i].text)
	print()
