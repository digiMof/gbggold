import re
import csv

# Since we want to distinguish between the two networks of Fadigati before and after the discovery of his sexuality, we need to split the full text into two different corpora (the before and after corpora): two txt files (NO tags except for the pers-name and place-name)

# Starting corpora -> corpora1.txt, corpora2.txt
# Open the two corpora and retrieve the text as a string
with open("netan/corpora1.txt", encoding="UTF-8") as f:
    corpora_1 = f.read()

with open("netan/corpora2.txt", encoding="UTF-8") as f:
    corpora_2 = f.read()

# Strip the strings from the newlines \n
# Also strip it from the excessive spaces
corpora_1.replace("\n"," ")
corpora_2.replace("\n"," ")
#print("STRIP FROM NEWLINE",corpora_1)

# Split the corpora in sentences (using multiple delimiters with regular expressions) --> # Now you will have a list of sentences/strings
txt_1 = re.split("\.\s|\.\n|\?\s|\?\n|\!\s|!\n",corpora_1)
    # Maybe the actual sentence-ending period would be this one \.\s+[A-Z]
txt_2 = re.split("\.\s|\.\n|\?\s|\?\n|\!\s|!\n",corpora_2)

print(txt_1)

tpl_list1 = list()  # Create an empty list for the tuples that I will need for the csv (2 columns: source (node) and target (node))
for item in txt_1:  # We scroll through the list of sentences(:str)
    print("ITEM\n",item)
    counter = 0     
    words = item.split("\s[^\>\w*\s?\w*\<]")  # We split the sentence in words -> words is a list of strings
    # Here we cannot use just the blank space cause otherwise it will split in two different sentences also the name inside the pers-name tag, which is the one we are interested in!
    print("This is the list of strings\n",words)
    '''
    for wrd in words:        # For every word in the list of words
        if "pers-name" in wrd:  # If that word contains "pers-name" THEN it IS a character!
            counter += 1
            name_char = re.match("\>(.*)\<",wrd)    #\s?("\>\w*\s?\w*\<?)\s? -> this is the correct one, it will match whatever is inside the tags (just remember to clean it removing the <> afterwards (NOT BEFORE because they are important characters to identify this specific part of the strings))
            print(name_char)
            tpl = ()
'''
# Iterate over the txt_1, list of sentences of corpora_1



tpl_list2 = list()











# Create the csv file to be imported to Gephi for visualisation
with open('simplenetwork.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["source", "target"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
