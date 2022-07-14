import re
import csv

from numpy import char, place

# ======== WHOLE GRAPH ========

# Read the txt file as a string
with open("netan/fulltext.txt", encoding="UTF-8") as f:
    corpora = f.read()

# Clean the corpora-string from excessive spaces, tabs and newline
re.sub('\s{2,}',' ',corpora)
re.sub('\t+',' ',corpora)
re.sub('\n+','',corpora)

# Split the corpora in a list of paragraphs (delimiter: \n)
txt = re.split('\n',corpora)

# Now build the graph
# 1) Gather the 'pers-name' and 'place-name' in each paragraph and save the string associated to these (= the name of the character or the place) in a list

tot_lst = list()    # List of lists (each second layer list represents a paragraph)
place_list = set()
char_list = set()
for item in txt:
    word_lst = re.split('\s(?!(\s?\w+\s?\w+){1,2}\<)',item)   # Split the paragraph in a list of words (str)
        # '\s(?!(\w+\<))'
        # \s(?!(\w+\s?+\w+\s?\w+\<))
        # \s(?!(\w+\s?\w+\s?\w+\s?\w+\<))
        # \s(?!(\w+\s?\w+){1,2}\<)

    word_lst = list(filter(None,word_lst))   #Clean the word-list from None elements

    node_lst = list()   # List of all the nodes contained in the paragraph item (from now on considered as a word-list word_lst)

    for word in word_lst:
        if "pers-name" in word or "place-name" in word: # If the word contains one of these strings it is a character/place
            node = re.search('(?<=\"\>)\w+\s?\w+(\s?\w+(\s?\w+)?)?',word)
            node_lst.append(node.group(0))
            if "pers-name" in word:
                char_list.add(node.group(0))
            elif "place-name" in word:
                place_list.add(node.group(0))
    
    # Update the list of lists
    tot_lst.append(node_lst)

# 2) Create tuples associating the items of each list together
    # !!! Here we may want to add something to the tuple to specify the kind of relation, or the community to which the characters belong... or do it on Gephi

tpl_lst = list()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        if paragraph[0] in place_list:
            tpl = tuple((paragraph[0],paragraph[i],"Place"))
        elif paragraph[0] in char_list:
            tpl = tuple((paragraph[0],paragraph[i],"Character"))
        #match paragraph[0]:
        #    case 
        #tpl = tuple((paragraph[0],paragraph[i]))
        tpl_lst.append(tpl)

# 3) Create the csv file from the tuples
    # !!! If we add stuff on the previous point, here we will need to add the necessary column(s)

with open('netan/NEW_fulltext.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Source","Target","Type"])
    for item in tpl_lst:
        writer.writerow(item)

























































