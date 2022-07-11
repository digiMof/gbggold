import re
import csv

# Clean the newly .html 
    # Remove all <p> tags
    # Remove all </p> tags
    # Remove all <h5> tags
    # Remove all </h5> tags
    # Remove all the html-related tags (<head></head>, <body></body>)

# Since we want to distinguish between the two networks of Fadigati before and after the discovery of his sexuality, we need to split the full text into two different corpora (the before and after corpora)


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

# Split corpora_1 in sentences (use the period .) --> # Now you will have a list of sentences
#txt_1 = nltk.tokenize.sent_tokenize(corpora_1)

#Split list based on multiple delimiters
txt_1 = re.split("\."|"?"|"!",corpora_1)
print("Divided text\n",txt_1)

# txt_2 = nltk.tokenize.sent_tokenize(corpora_2)

# Create an empty list for the tuples that I will need for the csv
tpl_list1 = list()
for item in txt_1:
    tpl = tuple()

# Iterate over the txt_1, list of sentences of corpora_1



tpl_list2 = list()











# Create the csv file to be imported to Gephi for visualisation
with open('simplenetwork.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["source", "target"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
