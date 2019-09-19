###########################
# current requirements:
#   logo needs to be 50x50
#   the tag size is 200x50
# 
#   need to get the tags from work computer
#   and edit the values and how it interacts
#   to be like the current tags
###########################
from __future__ import print_function
import os, sys, csv
from PIL import Image, ImageDraw, ImageFont
im = Image.open("full tag.png")
redlogo = Image.open("testred.png")
orangelogo = Image.open("testorange.png")
yellowlogo = Image.open("testyellow.png")
greenlogo = Image.open("testgreen.png")
bluelogo = Image.open("testblue.png")
pinklogo = Image.open("testpink.png")
logobox = (0,0,50,50)
fontsize = 26
fnt = ImageFont.truetype('arial.ttf',fontsize)
with open("testbook.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        brand = row[0]
        item = row[1]
        price = row[2]

        # handling the logo based off what the brand category is
        if brand == "red":
            region = redlogo.crop(logobox)
        if brand == "orange":
            region = orangelogo.crop(logobox)
        if brand == "yellow":
            region = yellowlogo.crop(logobox)
        if brand == "green":
            region = greenlogo.crop(logobox)
        if brand == "blue":
            region = bluelogo.crop(logobox)
        if brand == "pink":
            region = pinklogo.crop(logobox)    
        im.paste(region,logobox)

        # handling the item name
        
        itemname = ImageDraw.Draw(im)
        # handling if the item name overflows off the tag
        while itemname.textsize(item,font=fnt)[0] > 145: 
            fontsize = fontsize - 1
            fnt = ImageFont.truetype('arial.ttf',fontsize)
        itemname.text((55,0),item,font=fnt)
        # reset font in case we messed with it to fix sizing!
        fnt = ImageFont.truetype('arial.ttf',20)

        # handling the item price
        itemprice = ImageDraw.Draw(im)
        itemprice.text((55,22),price,font=fnt)

        fnt = ImageFont.truetype('arial.ttf',26)
        im.save(brand+item+".png","PNG")
        im = Image.open("full tag.png")
