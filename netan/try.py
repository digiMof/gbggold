from codecs import charmap_build
import re
import csv


# ====== I HAVE TO USE PARAGRAPHS, NOT SENTENCES =====




# Since we want to distinguish between the two networks of Fadigati before and after the discovery of his sexuality, we need to split the full text into two different corpora (the before and after corpora): two txt files (NO tags except for the pers-name and place-name)

# Starting corpora -> corpora1.txt, corpora2.txt
# Open the two corpora and retrieve the text as a string
with open("netan/corpora1.txt", encoding="UTF-8") as f:
    corpora_1 = f.read()

with open("netan/corpora2.txt", encoding="UTF-8") as f:
    corpora_2 = f.read()

# Clean the corpora-string
re.sub('\s{2,}',' ',corpora_1) # Remove excessive spaces \s{2,} (from 2 to more occurrences of \s)
re.sub('\t+',' ',corpora_1) # Remove tabs \t+ (one or more occurrences of \t)
re.sub('\n+','',corpora_1)  # Remove excessive newline \n+ (one or more occurrences of \n)

re.sub('\s{2,}',' ',corpora_2)
re.sub('\t+',' ',corpora_2)
re.sub('\n+','',corpora_2)

''' OLD CODE
corpora_1.replace("\n"," ")
corpora_2.replace("\n"," ")
#print("STRIP FROM NEWLINE",corpora_1)
'''
''' NEW OLD CODE
# Split the corpora-string into a list of sentences -> sentences delimiters: . (period), ?, !
    # . (period) -> RegEx \.\s[A-Z]
    # ! -> RegEx \!\s[A-Z]
    # ? -> RegEx \?\s[A-Z]

# The problem of re.split is that it removes the delimiter (the pattern we pass as one of the input parameters) -> so we cannot use \.\s+[A-Z]
txt1 = re.split('\.\s+|\?\s+|\!\s+',corpora_1)
txt2 = re.split('\.\s+|\?\s+|\!\s+',corpora_2)
'''

# Split the corpor-string in a list of paragraphs -> paragraph delimiter: \n
txt1 = re.split('\n',corpora_1)
txt2 = re.split('\n',corpora_2)

''' OLD CODE
# Split the corpora in sentences (using multiple delimiters with regular expressions) --> # Now you will have a list of sentences/strings
txt_1 = re.split("\.\s|\.\n|\?\s|\?\n|\!\s|!\n",corpora_1)
    # Maybe the actual sentence-ending period would be this one \.\s+[A-Z]
txt_2 = re.split("\.\s|\.\n|\?\s|\?\n|\!\s|!\n",corpora_2)
print(txt_1)
'''

# In each paragraphs I will gather the various pers-name (as I have decided that the presence of two characters in the same sentence defines a connection between them)
# In order to correctly build a csv file, I will need to save these pers-name in tuples (let's say a list of tuples)

tot_lst = list()

# Scroll through the list of paragraphs
for item in txt2:
    #print("\n THIS IS A paragraph",item)
    # ++++++++++++++++++++ print("\nThis is my paragraph\n",item)

    # Split the paragraph into a list of words-strings
    word_lst = re.split('\s(?!(\w+\<))',item) # The \s(?!(\w+\<)) matches every space character (\s) but not those followed by \w+\< (any alphanumeric character followed by an open <)
        # === PROBLEM: I get a list of words BUT there are None elements
    # ++++++++++++++++++++ print("\nThis is my word_list\n",word_lst)
    word_lst = list(filter(None,word_lst))  # Clean the list of words of all the None elements
    # ++++++++++++++++++++ print("\nThis is the word list cleaned of all the None\n",word_lst)

    person_lst = list()
    # For each word in the list, I need to check if it contains the string "pers-name"
    for word in word_lst:
        if "pers-name" in word:
            # The word is a character
            # I save the name of the character (what is follows the pers-name"> sequence of characters)
                # (?<="\>)\w+\s?\w+ -> Matches the \w+\s?\w+ that is only preceeded by (?<="\>)
            #print("\nTHIS IS THE WORD\n",word)
            char = re.search('(?<=\"\>)\w+\s?\w+',word)
            #print("This is the char\n",char)
            #print(type(char))
            person_lst.append(char.group(0))
            #print("THIS IS THE CHARACTER\n",char)

    tot_lst.append(person_lst)  # Append list to external list
print(tot_lst)  # The empty lists will be the paragraphs in which there is no pers-name


# Out of the snt_lst we will create the tuples for the csv file
    # For sentence in snt_lst:
        # Create tuples
        # All the elements inside this paragraph will be linked to eachother so I need to create tuples with all of them 

tpl_lst = list()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        tpl = tuple((paragraph[0],paragraph[i]))
        #print(tpl)
        tpl_lst.append(tpl)
    #print("SINGLE TPL_LIST",tpl_lst)
#print(tpl_lst)

''' OLD CODE
tpl_list1 = list()  # Create an empty list for the tuples that I will need for the csv (2 columns: source (node) and target (node))
for item in txt_1:  # We scroll through the list of sentences(:str)
    print("ITEM\n",item)
    counter = 0     
    words = item.split("\s[^\>\w*\s?\w*\<]")  # We split the sentence in words -> words is a list of strings
    # Here we cannot use just the blank space cause otherwise it will split in two different sentences also the name inside the pers-name tag, which is the one we are interested in!
    print("This is the list of strings\n",words)

    for wrd in words:        # For every word in the list of words
        if "pers-name" in wrd:  # If that word contains "pers-name" THEN it IS a character!
            counter += 1
            name_char = re.match("\>(.*)\<",wrd)    #\s?("\>\w*\s?\w*\<?)\s? -> this is the correct one, it will match whatever is inside the tags (just remember to clean it removing the <> afterwards (NOT BEFORE because they are important characters to identify this specific part of the strings))
            print(name_char)
            tpl = ()
# Iterate over the txt_1, list of sentences of corpora_1



tpl_list2 = list()







'''

# Create the csv file to be imported to Gephi for visualisation
with open('netan/corpora2.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["source", "target"])
    for item in tpl_lst:
        writer.writerow(item)
