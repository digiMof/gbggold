from email.errors import FirstHeaderLineIsContinuationDefect
import re
import csv

from numpy import char, place

# ------------------------------------ CSV CREATION FOR GRAPH BUILDING IN GEPHI -------------------------------------------------------
# To create the WHOLE GRAPH for the whole literary text, use the starting .txt file "fulltext.txt"
    # Output files: edgesSheet.csv, nodesSheet.csv
# To create the FADIGATI GRAPH (FIRST CORPORA), use the starting .txt file "corpora1.txt"
    # Output files: F1_edgesSheet.csv, F1_nodesSheet.csv
# To create the FADIGATI GRAPH (SECOND CORPORA), use the starting .txt file "corpora2.txt"
    # Output files: F2_edgesSheet.csv, F2_nodesSheet.csv


# Read the txt file as a string
with open("netan/corpora2.txt", encoding="UTF-8") as f:
    corpora = f.read()

# Clean the corpora-string from excessive spaces, tabs and newline
re.sub('\s{2,}', ' ', corpora)
re.sub('\t+', ' ', corpora)
re.sub('\n+', '', corpora)

# Split the corpora in a list of paragraphs (delimiter: \n)
txt = re.split('\n', corpora)

# Now build the graph
# 1) Gather the 'pers-name' and 'place-name' in each paragraph and save the string associated to these (= the name of the character or the place) in a list

# List of lists (each second layer list represents a paragraph) -> List of paragraphs
tot_lst = list()
place_list = set()
char_list = set()

# Sets for distinguish between characters' communities
primary_char = set()
family_char = set()
students_char = set()
borg_char = set()
historical_char = set()
cultural_char = set()

# Sets for distinguish between places' communities
ferrara_pl = set()
bologna_pl = set()
adriatic_pl = set()

for item in txt:
    # Split the paragraph in a list of words (str)
    word_lst = re.split('\s(?!(\w+\-?\w+\"\>)?(\s?\w+\s?\w+){1,2}\<)', item)

    # Clean the word-list from None elements
    word_lst = list(filter(None, word_lst))
    node_lst = list()   # List of all the nodes contained in the paragraph item (from now on considered as a word-list word_lst)
    for word in word_lst:
        # If the word contains one of these strings it is a character/place
        if "pers-name" in word or "place-name" in word:
            node = re.search('(?<=\"\>)\w+\s?\w+(\s?\w+(\s?\w+)?)?', word)
            node_lst.append(node.group(0))
            # We then add the word in the different 'communities'
            if "pers-name" in word:
                char_list.add(node.group(0))
                if "primary" in word:   # The character is either Fadigati, Deliliers or the narrator
                    primary_char.add(node.group(0))
                elif "family" in word:    # The character belongs to the narrator's family
                    family_char.add(node.group(0))
                elif "student" in word:  # The character belongs to the group of young students
                    students_char.add(node.group(0))
                elif "borg" in word:    # The character belongs to the bourgeoisie class (e.g. Lavezzoli family)
                    borg_char.add(node.group(0))
                elif "historical" in word:  # The character is historical (Mussolini, Hitler, Dolfuss...)
                    historical_char.add(node.group(0))
                elif "cultural" in word:    # The character is cultural (composer, artist...)
                    cultural_char.add(node.group(0))
            elif "place-name" in word:
                place_list.add(node.group(0))
                if "ferrara-loc" in word:
                    ferrara_pl.add(node.group(0))
                elif "bologna-loc" in word:
                    bologna_pl.add(node.group(0))
                elif "adriatic-loc" in word:
                    adriatic_pl.add(node.group(0))

    # Update the list of lists
    tot_lst.append(node_lst)


# ==== CREATING THE EDGES SHEET ====
# 2) Create tuples associating the items of each list together
    # Add attributes

tpl_lst1 = list()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        tpl1 = tuple((paragraph[0], paragraph[i]))
        tpl_lst1.append(tpl1)

# 3) Create the csv file from the tuples

with open('netan/csv/F2_edgesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Target"])
    for item in tpl_lst1:
        writer.writerow(item)

# ==== CREATING THE NODES SHEET ====
# This is a set because the repetitions are not meaningful for what concerns nodes
tpl_lst2 = set()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        if paragraph[i] in place_list:
            if paragraph[i] in ferrara_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Ferrara's Locations"))
            elif paragraph[i] in bologna_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Bologna's Locations"))
            elif paragraph[i] in adriatic_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Adriatic Region's Locations"))
            else:
                tpl2 = tuple((paragraph[i], paragraph[i], "Place", "Others"))
            tpl_lst2.add(tpl2)
        elif paragraph[i] in char_list:
            if paragraph[i] in primary_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Primary Character"))
            elif paragraph[i] in family_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Family Character"))
            elif paragraph[i] in students_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Student Character"))
            elif paragraph[i] in borg_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Bourgeoisie Character"))
            elif paragraph[i] in historical_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Historical Character"))
            elif paragraph[i] in cultural_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Cultural Character"))
            else:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Others"))
            tpl_lst2.add(tpl2)

with open('netan/csv/F2_nodesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "Label", "Type", "Class"])
    for item in tpl_lst2:
        writer.writerow(item)


''' This code was built to create the different Fadigati's network but it gives some problems: as it doesn't change it is easier to use the functioning one
# ------------------------------------- CREATE FADIGATI'S NETWORK -----------------------------------------------------------------------

# >>>>>> FIRST CORPORA <<<<<<

with open("netan/corpora1.txt", encoding="UTF-8") as f:
    corpora1 = f.read()

re.sub('\s{2,}', ' ', corpora1)
re.sub('\t+', ' ', corpora1)
re.sub('\n+', '', corpora1)

txt1 = re.split('\n', corpora1)

f1_tot_lst = list()  # List of paragraphs
for item in txt1:
    word_lst = re.split('\s(?!(\w+\-?\w+\"\>)?(\s?\w+\s?\w+){1,2}\<)', item)
    word_lst = list(filter(None, word_lst))
    node_lst = list()
    for word in word_lst:
        if "pers-name" in word or "place-name" in word:
            node = re.search('(?<=\"\>)\w+\s?\w+(\s?\w+(\s?\w+)?)?', word)
            node_lst.append(node.group(0))
            if "pers-name" in word:
                char_list.add(node.group(0))
                if "primary" in word:
                    primary_char.add(node.group(0))
                elif "family" in word:
                    family_char.add(node.group(0))
                elif "student" in word:
                    students_char.add(node.group(0))
                elif "borg" in word:
                    borg_char.add(node.group(0))
                elif "historical" in word:
                    historical_char.add(node.group(0))
                elif "cultural" in word:
                    cultural_char.add(node.group(0))
            elif "place-name" in word:
                place_list.add(node.group(0))
                if "ferrara-loc" in word:
                    ferrara_pl.add(node.group(0))
                elif "bologna-loc" in word:
                    bologna_pl.add(node.group(0))
                elif "adriatic-loc" in word:
                    adriatic_pl.add(node.group(0))
    f1_tot_lst.append(node_lst)

# ===
# ==== EDGES SHEET ====
# ===
tpl_lstF11 = list()
for paragraph in f1_tot_lst:
    for i in range(len(paragraph)):
        tpl = tuple((paragraph[0], paragraph[i]))
        tpl_lstF11.append(tpl)

with open('netan/csv/F1_edgesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Target"])
    for item in tpl_lstF11:
        writer.writerow(item)

# ===
# ==== NODES SHEET ====
# ===
tpl_lstF12 = set()
for paragraph in f1_tot_lst:
    for i in range(len(paragraph)):
        if paragraph[i] in place_list:
            if paragraph[i] in ferrara_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Ferrara's Locations"))
            elif paragraph[i] in bologna_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Bologna's Locations"))
            elif paragraph[i] in adriatic_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Adriatic Region's Locations"))
            else:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Others"))
            tpl_lstF12.add(tpl2)
        elif paragraph[i] in char_list:
            if paragraph[i] in primary_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Primary Character"))
            elif paragraph[i] in family_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Family Character"))
            elif paragraph[i] in students_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Student Character"))
            elif paragraph[i] in borg_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Bourgeoisie Character"))
            elif paragraph[i] in historical_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Historical Character"))
            elif paragraph[i] in cultural_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Cultural Character"))
            else:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Others"))
            tpl_lstF12.add(tpl2)

with open('netan/csv/F1_nodesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "Label", "Type", "Class"])
    for item in tpl_lstF12:
        writer.writerow(item)





# >>>>>> SECOND CORPORA <<<<<<

with open("netan/corpora2.txt", encoding="UTF-8") as f:
    corpora2 = f.read()
    
re.sub('\s{2,}', ' ', corpora2)
re.sub('\t+', ' ', corpora2)
re.sub('\n+', '', corpora2)

txt2 = re.split('\n', corpora2)

f2_tot_lst = list()
for item in txt2:
    word_lst = re.split('\s(?!(\w+\-?\w+\"\>)?(\s?\w+\s?\w+){1,2}\<)', item)
    word_lst = list(filter(None, word_lst))
    node_lst = list()
    for word in word_lst:
        if "pers-name" in word or "place-name" in word:
            node = re.search('(?<=\"\>)\w+\s?\w+(\s?\w+(\s?\w+)?)?', word)
            node_lst.append(node.group(0))
            if "pers-name" in word:
                char_list.add(node.group(0))
                if "primary" in word:
                    primary_char.add(node.group(0))
                elif "family" in word:
                    family_char.add(node.group(0))
                elif "student" in word:
                    students_char.add(node.group(0))
                elif "borg" in word:
                    borg_char.add(node.group(0))
                elif "historical" in word:
                    historical_char.add(node.group(0))
                elif "cultural" in word:
                    cultural_char.add(node.group(0))
            elif "place-name" in word:
                place_list.add(node.group(0))
                if "ferrara-loc" in word:
                    ferrara_pl.add(node.group(0))
                elif "bologna-loc" in word:
                    bologna_pl.add(node.group(0))
                elif "adriatic-loc" in word:
                    adriatic_pl.add(node.group(0))
    f2_tot_lst.append(node_lst)
print(f2_tot_lst)

# ==== EDGES SHEET ====
tpl_lstF21 = list()
for paragraph in f2_tot_lst:
    for i in range(len(paragraph)):
        tpl = tuple((paragraph[0], paragraph[i]))
        tpl_lstF21.append(tpl)

with open('netan/csv/F2_edgesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Target"])
    for item in tpl_lstF21:
        writer.writerow(item)

# ==== NODES SHEET ====
tpl_lstF22 = set()
for paragraph in f2_tot_lst:
    for i in range(len(paragraph)):
        if paragraph[i] in place_list:
            if paragraph[i] in ferrara_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Ferrara's Locations"))
            elif paragraph[i] in bologna_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Bologna's Locations"))
            elif paragraph[i] in adriatic_pl:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Adriatic Region's Locations"))
            else:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Place", "Others"))
            tpl_lstF22.add(tpl2)
        elif paragraph[i] in char_list:
            if paragraph[i] in primary_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Primary Character"))
            elif paragraph[i] in family_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Family Character"))
            elif paragraph[i] in students_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Student Character"))
            elif paragraph[i] in borg_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Bourgeoisie Character"))
            elif paragraph[i] in historical_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Historical Character"))
            elif paragraph[i] in cultural_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Cultural Character"))
            else:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Others"))
            tpl_lstF22.add(tpl2)

with open('netan/csv/F2_nodesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "Label", "Type", "Class"])
    for item in tpl_lstF22:
        writer.writerow(item)
'''