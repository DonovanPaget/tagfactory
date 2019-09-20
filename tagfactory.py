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
burton = Image.open("logo/burtonlogo.png")
jones = Image.open("logo/jones logo.png")
k2 = Image.open("logo/k2logo.png")
green = Image.open("testgreen.png")
blue = Image.open("testblue.png")
pink = Image.open("testpink.png")
logolist = [[burton,"burton"], [jones, "jones"], [k2,"k2"], [green,"green"], [blue,"blue"], [pink,"pink"]]
logobox = (0,0,480,555)
fontsize = 160
fontname = 'SairaCondensed-Regular.ttf'
fnt = ImageFont.truetype(fontname,fontsize)


with open("testbook.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        brand = row[0]
        item = row[1]
        price = row[2]
        item = item.upper()

        # handling the logo based off what the brand category is
        for company in logolist:
            if company[1] == brand:
                region = company[0].crop(logobox)  
        im.paste(region,logobox)

        # handling the item name
        itemname = ImageDraw.Draw(im)
        fontsize = 165
        ycoord = 60

        # handling if the item name overflows off the tag
        while itemname.textsize(item,font=fnt)[0] > 650: 
            fontsize = fontsize - 1
            fnt = ImageFont.truetype(fontname,fontsize)
            ycoord = ycoord + 0.5
        itemname.text((518,ycoord),item,font=fnt)
        # reset font in case we messed with it to fix sizing!
        fnt = ImageFont.truetype(fontname,165)
        

        # handling the item price
        itemprice = ImageDraw.Draw(im)
        itemprice.text((518,280),price,font=fnt)

        # save the new tag
        im.save(brand+item+".png","PNG")
        im = Image.open("full tag.png")
