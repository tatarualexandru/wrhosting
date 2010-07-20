#!/usr/bin/python

import urllib
import re
import string
import os
import databaseManager

#Ar trebui sa verifice o pagina si sa puna in baza de date informatiile despre ea
#si apoi sa apeleze recursiv crawl pe toate linkurile pe care le gaseste in pagina
#cred totusi ca ar mai trebui si un fork() pe aici pe undeva

urlFeed = [];

def remove(self, chars):
    s = self
    for c in chars:
        s = s.replace(c, '')
    return(s)

def crawl(url):
    urlFeed.append(url)
    while len(urlFeed) > 0:
        try:
            url = urlFeed.pop()
            web_page = urllib.urlopen(url)
            titlu, descriere = extractinfo(web_page)
            #print(url)
            #print(titlu)
            #print(descriere)
            databaseManager.insertpage(remove(url, "\""), titlu, descriere[5:-5])
            getlinks(url)
            print("Pagini indexate pana acum: "+str(len(urlFeed)))
            web_page.close()
        except:
            pass
    

def extractinfo(web_page):
    for line in web_page:
        line = line.strip()
        x = str(line)
        parsed_line1 = re.match('(.*)(<title>)(.*)(</title>)(.*)', x)
        if parsed_line1:
            title = parsed_line1.group(3)
        parsed_line1 = re.match('(.*)(<meta name=\"description\" content=)(.*)(/>)(.*)', x)
        if parsed_line1:
            description = parsed_line1.group(3)
    return title, description
            
def getlinks(url):
    page=urllib.urlopen(url)
    tag="<a href=\""
    endtag="\">"
    for item in page:
        x = str(item)
        if "<a href" in x:
            try:
                ind = x.index(tag)
                x=x[ind+len(tag):]
                end=x.index(endtag)
            except: pass
            else:
                firstpass = x[:end]
                if "http:" in firstpass:
                    vector = firstpass.split("target=")
                    urlFeed.append(vector[0])


#Testarea functiei de extragere a titlului
#web_page = urllib.request.urlopen("http://searchenginewatch.com/2167931")
#titlu, descriere = extractinfo(web_page)
#print("Titul paginii este: "+titlu)
#print("Descrierea paginii este: "+descriere);
#web_page.close()
crawl("http://www.amazon.com")
