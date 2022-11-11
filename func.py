import os
from time import sleep
import collections
import natsort
from pdf2image import convert_from_path
from PIL import Image
import pdfkit
import pytesseract
import numpy as np

def counting():
    c = 0
    while c != 20:
        c += 1
        print(c)
        sleep(1)
        continue


def img_con_pdf(src, dest):
    # print(src, dest)
    img_in = (natsort.natsorted(os.listdir(src)))
    try:
        for f in img_in:
            image_1 = Image.open(src+f)
            im_1 = image_1.convert('RGB')
            im_1.save(dest+f.split('.')[-2]+'.pdf')
            continue
    except:
        print(Exception)

def pdf_con_img(src_path, dest_path):
    pages = convert_from_path(src_path, 350)
    i = 1
    try:
        for page in pages:
            image_name = "Page_" + str(i) + ".jpg"  
            page.save(dest_path+image_name, "JPEG")
            i = i+1  
    except:
        print(Exception)


def pdf_con_txt():
    print('')

def www_to_pdf(src_page):
    pdfkit.from_url(src_page, 'out.pdf')

def img_to_txt(src_path):
    img_lst = (natsort.natsorted(os.listdir(src_path)))
    for i in img_lst:# tesseract converting images to plain txt format image by image to create one text file
        text = pytesseract.image_to_string(np.array(Image.open(src_path+i)))
        txt_name = f'{src_path}text.txt'     #.split (".")[-2]                   
        with open(txt_name, 'a+', encoding='utf-8') as f:
            f.write(text)
            f.close()



def text_count(src_path,):
    try:
        # Create an empty dictionary
        d = dict()

        # Loop through each line of the file
        for line in open(src_path, "r"):
            # Remove the leading spaces and newline character
            # line = line.strip(line.lower(line.split(" ")))
            line = line.strip()

            # Convert the characters in line to
            # lowercase to avoid case mismatch
            line = line.lower()

            # Split the line into words
            words = line.split(" ")
                                

            # Iterate over each word in line
            for word in words:
                # Check if the word is already in dictionary
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1

        # Print the contents of dictionary
        for key in sorted(d.keys()):
            list1 = d[key], ":", key
            print(list1)
            # print(sorted(list1))

        # print(d)
    except Exception as Error:
        print(Error)
