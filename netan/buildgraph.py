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
    word_lst = re.split('\s(?!(\w+\-?\w+\"\>)?(\s?\w+\s?\w+){1,2}\<)',item)   # Split the paragraph in a list of words (str)
        # '\s(?!(\w+\<))'
        # \s(?!(\w+\s?+\w+\s?\w+\<))
        # \s(?!(\w+\s?\w+\s?\w+\s?\w+\<))
        # \s(?!(\w+\s?\w+){1,2}\<)
        # \s(?!(\s?\w+\s?\w+){1,2}\<)
        # \s(?!(\w+\-?\w+\"\>)?(\s?\w+\s?\w+){1,2}\<)

    word_lst = list(filter(None,word_lst))   #Clean the word-list from None elements
    node_lst = list()   # List of all the nodes contained in the paragraph item (from now on considered as a word-list word_lst)
    for word in word_lst:
        if "pers-name" in word or "place-name" in word: # If the word contains one of these strings it is a character/place
            node = re.search('(?<=\"\>)\w+\s?\w+(\s?\w+(\s?\w+)?)?',word)
            node_lst.append(node.group(0))
            # We then add the word in the different 'communities'
            if "pers-name" in word:
                char_list.add(node.group(0))
                if "primary" in word:
                    primary_char.add(node.group(0))  # The character is either Fadigati, Deliliers or the narrator
                elif "family" in word:    # The character belongs to the narrator's family
                    family_char.add(node.group(0))
                elif "student" in word: # The character belongs to the group of young students
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

    # Update the list of lists
    tot_lst.append(node_lst)

# ==== CREATING THE EDGES SHEET ====
# 2) Create tuples associating the items of each list together
    # Add attributes

tpl_lst1 = list()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        tpl1 = tuple((paragraph[0],paragraph[i]))
        tpl_lst1.append(tpl1)

# 3) Create the csv file from the tuples
    # !!! If we add stuff on the previous point, here we will need to add the necessary column(s)

with open('netan/edgesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Source","Target"])
    for item in tpl_lst1:
        writer.writerow(item)
    
# ==== CREATING THE NODES SHEET ====
tpl_lst2 = list()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        if paragraph[i] in place_list:
            if paragraph[i] in ferrara_pl:
                tpl2 = tuple((paragraph[i],paragraph[i],"Place","Ferrara's Locations"))
            elif paragraph[i] in bologna_pl:
                tpl2 = tuple((paragraph[i],paragraph[i],"Place","Bologna's Locations"))
            elif paragraph[i] in adriatic_pl:
                tpl2 = tuple((paragraph[i],paragraph[i],"Place","Adriatic Region's Locations"))
            else:
                tpl2 = tuple((paragraph[i],paragraph[i],"Place","Others"))
            tpl_lst2.append(tpl2)
        elif paragraph[i] in char_list:
            if paragraph[i] in primary_char:
                tpl2 = tuple((paragraph[i],paragraph[i],"Character","Primary Character"))
            elif paragraph[i] in family_char:
                tpl2 = tuple((paragraph[i],paragraph[i],"Character","Family Character"))
            elif paragraph[i] in students_char:
                tpl2 = tuple((paragraph[i],paragraph[i],"Character","Student Character"))
            elif paragraph[i] in borg_char:
                tpl2 = tuple((paragraph[i],paragraph[i],"Character","Bourgeoisie Character"))
            elif paragraph[i] in historical_char:
                tpl2 = tuple((paragraph[i],paragraph[i],"Character","Historical Character"))
            elif paragraph[i] in cultural_char:
                tpl2 = tuple((paragraph[i],paragraph[i],"Character","Cultural Character"))
            else:
                tpl2 = tuple((paragraph[i],paragraph[i],"Character","Others"))
            tpl_lst2.append(tpl2)

with open('netan/nodesSheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id","Label","Type","Class"])
    for item in tpl_lst2:
        writer.writerow(item)





### CHECK TXT

# PRIMARY CHARACTERS: NARRATOR, FADIGATI, ERALDO DELILIERS ---- DONE
# SECUNDARY CHARACTERS: MOTHER, FATHER, FANNY, ERNESTO, ELISA ---- DONE
# BOURGEOISIE CHARACTERS: LAVEZZOLIS ---- DONE
# YOUNG STUDENTS: BIANCA SGARBI, NINO BOTTECCHIARI, VITTORIO MOLON, SERGIO PAVANI, OTELLO FORTI, GIOVANNINO PIAZZA, ENRICO SANGIULIANO ---- DONE
# HISTORICAL: MUSSOLINI, DOLLFUSS, CIANO, FRANCO, HITLER ---- DONE
# CULTURAL: BENEDETTO CROCE, PADRE GEMELLI, OMERO, ORAZIO, PASCOLI, BACH, BEETHOVEN, MOZARD, SCHUBERT, WAGNER, CASORATI, DE CHIRICO, DE PISIS, MELOZZO DA FORLI, AURELIANO PERTILE, RIDOLINI, BRUNO WALTER, ---- DONE

# FERRARA---- DONE
# BOLOGNA---- DONE
# ADRIATIC---- DONE












































