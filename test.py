from bs4 import BeautifulSoup as bs
import csv
import os
from os import listdir

def list_files(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))

content = []

dires = [a for a in os.listdir() if os.path.isdir(a)]
dires=sorted(dires)
#list directory in given directory
with open('gt.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    for key,dire in enumerate(dires):
        frame=key+1
        xml_file=(list(list_files(dire,"xml"))[0])

        with open("./"+dire+"/"+xml_file, "r") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.readlines()
            # Combine the lines in the list into a string
            content = "".join(content)
            bs_content = bs(content, "lxml")
            result = bs_content.find_all("object")

            val_x = bs_content.find_all("x")
            val_y = bs_content.find_all("y")        
            print(len(result))
            for i in range(len(result)):
                temp_name=(result[i].find("name").getText())
                
                points = []
                points=(frame,val_x[4*i].getText(), val_y[4*i].getText(), val_x[4*i+2].getText(), val_y[4*i+2].getText(),1,1,1)
                points=list(points)
                points.insert(1,temp_name)
                print((points))
                writer.writerow(points)

