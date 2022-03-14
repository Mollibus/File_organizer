#!/usr/bin/env python
# coding: utf-8

# In[3]:


import argparse 
import sys
import shutil
import os
import csv

def main(): #creo un parser e passo come unico argomento il nome del file 
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="what is the file to move? (file.ext)")
    args = parser.parse_args() 
    sys.stdout.write(move(args)) # l'output generato è una stringa in cui viene riportato il messaggio della funzione move()

directory = os.path.join(os.getcwd(),"files")
filenames = os.listdir(directory)

dic = {} 
dic[".mp3"] = "audio"
dic[".odt"] = "docs"
dic[".txt"] = "docs"
dic[".jpg"] = "images" 
dic[".jpeg"]= "images"
dic[".png"] = "images"



def move(args): #utilizzo la stessa logica del notebook FileOrganizer, aggiungendo una variabile messaggio che riporti l'esito della funzione
    if args.file in filenames: 
        ext = os.path.splitext(args.file)[1]
        if not os.path.isdir(os.path.join(directory,dic[ext])):
            os.makedirs(os.path.join(directory, dic[ext]))
        message = "{} has been moved to {} folder".format(args.file,dic[ext])
        with open((os.path.join(directory,"recap.csv")),"a") as recap:  #per ogni file scrive un recap
            writer = csv.writer(recap)  #creo un file di recap
            writer.writerow([os.path.basename(os.path.join(directory, args.file)).split(".")[0], dic[ext], 
                             os.path.getsize(os.path.join(directory,args.file))])
        shutil.move(os.path.join(directory,args.file),os.path.join(directory,dic[ext]))
        
    else: message = "file does not exist"
    return message
if __name__== "__main__":
    main()

