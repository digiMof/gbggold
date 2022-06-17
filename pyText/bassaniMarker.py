def parser(filePath):
    f = open(filePath, 'r')
    rawText = f.read()
    listBook = rawText.split("\n\n\n") 
    listBook = listBook[:2] #Da rimuovere
    listChap = []
    for chapt in listBook:
        chaptParsed = chapt.split("\n\n")
        listChap.append(chaptParsed)
    return listChap

def marker(listOfChap):
    taggedBookList = []
    for chap in sample:
        taggedChapList = ["<div>"]
        for par in chap:
            par = "<p>" + par + "</p>"
            taggedChapList.append(par)
        taggedChapList.append("</div>")
        taggedChapStr = '\n'.join(taggedChapList)
        taggedBookList.append(taggedChapStr)
    taggedBookStr = '\n\n'.join(taggedBookList)
    return taggedBookStr

basssaniPath = 'occhialiOro.txt'
parsed = (parser(basssaniPath))
print(marker(parsed))