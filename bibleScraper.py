import bs4 as bs
import json as json
import os
from os import path
from urllib.request import Request, urlopen


def oldTest():
    chapters = []
    chapterNum = []
    booksAndNums = {}
    req = Request('file:///Users/1kooko/Desktop/bibleWebScraper/ChaptersOT.html')
    source = urlopen(req).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    with open('./ChaptersDump.txt', "w") as text:
        for span in soup.find_all(name='a', attrs={"colspan": "1"}):
            chapters.append(str(span.text))
        for span in soup.find_all(name='td', attrs={"colspan": "2"}):
            chapterNum.append(str(span.text))
            if((len(chapters) == 39) and len(chapterNum) == 39):
                for i in range(39):
                    booksAndNums[chapters[i]] = chapterNum[i]

        text.write(json.dumps(booksAndNums))


def newTest():
    chapters = []
    chapterNum = []
    booksAndNums = {}
    req = Request(
        'file:///Users/1kooko/Desktop/bibleWebscraper/ChaptersNT.html')
    source = urlopen(req).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    with open('./ChaptersDump.txt', "w") as text:
        for span in soup.find_all(name='a', attrs={"colspan": "1"}):
            # print(span.text)
            chapters.append(str(span.text))
        for span in soup.find_all(name='td', attrs={"colspan": "2"}):
            # print(span.text)
            chapterNum.append(span.text)
        for i in range(len(chapterNum)):
            booksAndNums[chapters[i]] = chapterNum[i]

        text.write(json.dumps(booksAndNums))


def initOTChapters():
    OT = {}
    with open("./CAndV_OT.json") as OT_file:
        OT_raw = OT_file.read()
        OT = json.loads(OT_raw)
    return OT[0]


def initNTChapters():
    NT = {}
    with open("./CAndV_NT.json") as NT_file:
        NT_raw = NT_file.read()
        NT = json.loads(NT_raw)

    return NT[0]


# newTest()


def makeTwiBible():
    OT = initOTChapters()
    initChapt = 1
    
    for x, y in OT.items():

        currChaptPath = "./BibleChapters/Old_Testament/" + x
        if(not path.exists(currChaptPath)):
            os.mkdir(currChaptPath)

        for i in range(1, (int(y) +1)):
            currBook = x[:3]
            url = 'https://www.bible.com/bible/1461/' + \
                currBook + '.' + str(i) + '.ASWDC'
            
            currfileName = 'BibleChapters/Old_Testament/' + \
                str(x) + '/' + str(x) + ' ' + str(i)+'.txt'
            currBibleChapter = str(x) + ' ' + str(i)
            req = Request(url,
                          headers={'User-Agent': 'Mozilla/5.0'})
            source = urlopen(req).read()
            soup = bs.BeautifulSoup(source, 'lxml')
            currChapt = str(x) + " " + str(i) + ".txt"
            versesRaw = soup.find_all(name='span', attrs={'class': 'content'})
            print("Writing Old Testament. Here is " + x + ' ' + str(i))
            with open(currfileName, "w+") as bookChapt:
                bookChapt.write(currBibleChapter + '\n\n')

            for verses in versesRaw:
                with open(currfileName, "a+") as bookChapt:
                    bookChapt.write(verses.text + '\n')
                    bookChapt.close()
    
    
    
    NT = initNTChapters()
    initChapt = 1
    
    for x, y in NT.items():
    
        currChaptPath = "./BibleChapters/New_Testament/" + x
        if(not path.exists(currChaptPath)):
            os.mkdir(currChaptPath)

        for i in range(1, (int(y) + 1)):
            currBook = x[:3]
            url = 'https://www.bible.com/bible/1461/' + \
                currBook + '.' + str(i) + '.ASWDC'
            print("Writing New Testament. Here is " + x + ' ' + str(i))
            currfileName = 'BibleChapters/New_Testament/' + \
                str(x) + '/' + str(x) + ' ' + str(i)+'.txt'
            currBibleChapter = str(x) + ' ' + str(i)
            req = Request(url,
                            headers={'User-Agent': 'Mozilla/5.0'})
            source = urlopen(req).read()
            soup = bs.BeautifulSoup(source, 'lxml')
            currChapt = str(x) + " " + str(i) + ".txt"
            versesRaw = soup.find_all(name='span', attrs={'class': 'content'})

            with open(currfileName, "w+") as bookChapt:
                bookChapt.write(currBibleChapter + '\n\n')

            for verses in versesRaw:
                with open(currfileName, "a+") as bookChapt:
                    bookChapt.write(verses.text + '\n')
                    bookChapt.close()


makeTwiBible()

#Do a Switch for Unique Cases of 1 samuel and co

