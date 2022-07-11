import csv

# Clean the newly .html 
    # Remove all <p> tags
    # Remove all </p> tags
    # Remove all <h5> tags
    # Remove all </h5> tags
    # Remove all the html-related tags (<head></head>, <body></body>)




# Starting corpora -> corpora1.txt, corpora2.txt
corpora_1 = "corpora1.txt"
corpora_2 = "corpora2.txt"




# Split corpora_1 in sentences (use the period .)

# Now you will have a list of sentences




# Split corpora_2 in sentences (use the period .)

# Now you will have a list of sentences




# Iterate over the list
    # Create empty tuple


# Create the csv file to be imported to Gephi for visualisation
with open('simplenetwork.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["source", "target"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
