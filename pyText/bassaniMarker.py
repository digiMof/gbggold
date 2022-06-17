def parser(filePath):
    f = open(filePath, 'r')
    rawText = f.read()
    listBook = rawText.split("\n\n\n") 
    listChap = []
    for chapt in listBook:
        chaptParsed = chapt.split("\n\n")
        listChap.append(chaptParsed)
    return listChap

def marker(listOfChap):
    taggedBookList = []
    for chap in listOfChap:
        taggedChapList = ["<div>"]
        for par in chap:
            par = "<p>" + par + "</p>"
            taggedChapList.append(par)
        taggedChapList.append("</div>")
        taggedChapStr = '\n'.join(taggedChapList)
        taggedBookList.append(taggedChapStr)
    taggedBookStr = '\n\n'.join(taggedBookList)
    with open('pyText/taggedBassani.txt', 'w', encoding='utf-8') as f:
        for chap in taggedBookList:
            f.write(chap)
            f.write('\n')
    return taggedBookStr

basssaniPath = 'pyText/occhialiOro.txt'
parsed = (parser(basssaniPath))
print(marker(parsed))