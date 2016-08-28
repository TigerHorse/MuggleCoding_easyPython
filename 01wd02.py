from bs4 import BeautifulSoup

finPath = "./week1/1_2/\
1_2answer_of_homework/\
1_2_homework_required/index.html"

# Read and Analyse
with open(finPath, 'r') as fin:
    Soup = BeautifulSoup(fin.read(), 'lxml')
    itemTitle = Soup.select('body > div.container > div.row > div.col-md-9 > \
div.row > div > div > div.caption > h4:nth-of-type(2) > a')
    itemPicSrc = Soup.select('body > div.container > div.row > div.col-md-9 > \
div.row > div > div > img')
    itemPrice = Soup.select('body > div.container > div.row > div.col-md-9 > \
div.row > div > div > div.caption > h4.pull-right')
    itemComment = Soup.select('body > div.container > div.row > div.col-md-9 > \
div.row > div > div > div.ratings > p.pull-right')
    itemStar = Soup.select('body > div.container > div.row > div.col-md-9 > \
div.row > div > div > div.ratings > p:nth-of-type(2)')


# Save Result
dataSet = []
for iTitle, iPic, iPrice, iComment, iStar in zip(itemTitle, itemPicSrc, itemPrice, itemComment, itemStar):
    info = {
        'iTitle': iTitle.get_text(),
        'iPic': iPic.get('src'),
        'iPrice': iPrice.get_text(),
        'iComment': iComment.get_text(),
        'iStar': len(iStar.find_all("span", class_="glyphicon glyphicon-star"))
    }
    dataSet.append(info)

# See Result
for info in dataSet:
    print(info)