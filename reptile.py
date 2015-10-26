#import sys
#reload(sys)
import datetime
import time
import re
import os
#import HTMLParser
#sys.setdefaultencoding("utf-8")
from ghost import Ghost

furl = open('C:\\Users\\Frank\\Desktop\\url.txt','w+')
ftitle = open('C:\\Users\\Frank\\Desktop\\title.txt','w+')
fimg = open('C:\\Users\\Frank\\Desktop\\img.txt','w+')

def reptile(url):
	
	ghost = Ghost(wait_timeout=20)
	page,resources = ghost.open(url)
	result, resources = ghost.wait_for_selector("#wxmore a")
	
	from bs4 import BeautifulSoup
	c=0
	
	while True:
	    if c>=1:
	        break
	 
	    soup = BeautifulSoup(ghost.content)
	 
	    for wx in soup.find_all("h4"):
	        links = re.findall('"((http|ftp)s?://.*?)"', str(wx))
	        try:
	            #print links[0][0]
	            furl.write(links[0][0])
	            furl.write('\n')
	            furl.write('\n')
	        except:
	            pass
	        titles = re.findall('">.*?<\/a', str(wx))
	        try:
	            #print titles[0][2:-3].decode("utf-8")
	            ftitle.write(titles[0][2:-3])
	            ftitle.write('\n')
	            ftitle.write('\n')
	        except:
	            pass
	
	    for img in soup.find_all("img"):
	        imgs = re.findall('c="http://img01\.st.*" s', str(img))
	        try:
	            #print imgs[0][3:-3].replace('amp;','')
	            fimg.write(imgs[0][3:-3].replace('amp;',''))
	            fimg.write('\n')
	            fimg.write('\n')
	        except:
	            pass
	 
	    page, resources = ghost.evaluate(
	        """
	        var div1 = document.getElementById("wxbox");
	        div1.innerHTML = '';
	        """)
	    ghost.click("#wxmore a")
	    result, resources = ghost.wait_for_selector(".wx-rb3")
	 
	    c=c+1
	    pass
	pass

fff=os.listdir('C:\\Users\\Frank\\Desktop\\all')

for ff in fff:
	with open('C:\\Users\\Frank\\Desktop\\all\\'+ff,'r') as f:
		a=f.read()
		urls=a.split()
		for url in urls:
			reptile(url)
furl.close()
ftitle.close()
fimg.close()

print "finish"
