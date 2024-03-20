import csv
import random
import string
from random import choice

#AUTHOR
chars = string.digits
a =  ''.join(choice(chars) for _ in range(4)) + "-" + ''.join(choice(chars) for _ in range(4)) + "-" \
        + ''.join(choice(chars) for _ in range(4)) + "-" + ''.join(choice(chars) for _ in range(4))

file = open("output_author_original.csv")
file = file.read()
file = file.split('\n')
newfile = []
newfile.append("ID;author;orcid\n")

#add a random orcid
for i in range(1,int(len(file)/10)): #reduce the dataset
    newfile.append(file[i] + ";" + ''.join(choice(chars) for _ in range(4)) + "-" + ''.join(choice(chars) for _ in range(4)) + "-" \
        + ''.join(choice(chars) for _ in range(4)) + "-" + ''.join(choice(chars) for _ in range(4)) + "\n")

f = open('output_author.csv', 'w')
f.writelines(newfile)
f.close()



#BOOK
file = open("output_book_original.csv")
file = file.read()
file = file.split('\n')
newfile = []
newfile.append("ID;author;author-bibtex;author-orcid;booktitle;cdrom;cite;cite-label;crossref;editor;editor-orcid;ee;ee-type;i;isbn;isbn-type;key;mdate;month;note;note-type;pages;publisher;publisher-href;publtype;school;series;series-href;sub;sup;title;url;volume;year\n")

for i in range(1,int(len(file)/10)): #reduce the dataset
    newfile.append(file[i] + '\n')

f = open('output_book.csv', 'w')
f.writelines(newfile)
f.close()



#INCOLLECTION
file = open("output_incollection_original.csv")
file = file.read()
file = file.split('\n')
newfile = []
newfile.append("ID;author;author-orcid;booktitle;cdrom;chapter;cite;cite-label;crossref;ee;ee-type;i;key;mdate;note;number;pages;publisher;publisher-href;publtype;sub;sup;title;url;year\n")

for i in range(1,int(len(file)/10)): #reduce the dataset
    newfile.append(file[i] + '\n')

f = open('output_incollection.csv', 'w')
f.writelines(newfile)
f.close()
