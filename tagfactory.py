###########################
# reads from a csv file with 3 columns: 
#   BRAND NAME, ITEM NAME, PRICE
# the brand must be from this list:
#   atomic, burton, full tilt, head, jones, k2, line, look, marker, ride, rossignol, salomon, tyrolia
# there will be 8 tags a sheet. 3 tags for each item. 
#  
#   
###########################
from __future__ import print_function
import os, sys, csv
from PIL import Image, ImageDraw, ImageFont

## need to open all the logo files for use
im = Image.open("full tag.png")
settemplate = Image.open("setof8.png")

burton = Image.open("logo/burtonlogo.png")
jones = Image.open("logo/jones logo.png")
k2 = Image.open("logo/k2logo.png")
atomic = Image.open("logo/atomiclogo.png")
fulltilt = Image.open("logo/ftlogo.png")
head = Image.open("logo/headlogo.png")
line = Image.open("logo/line logo.png")
look = Image.open("logo/look logo.png")
marker = Image.open("logo/marker logo.png")
ride = Image.open("logo/ridelogo.png")
rossi = Image.open("logo/rossilogo.png")
salomon = Image.open("logo/salomonlogo.png")
tyrolia = Image.open("logo/tyrolia logo.png")
logolist = [[burton,"BURTON"], [jones, "JONES"], [k2,"K2"], [atomic,"ATOMIC"], [fulltilt,"FULL TILT"], [head,"HEAD"],[line,"LINE"],[look,"LOOK"],[marker,"MARKER"],[ride,"RIDE"],[rossi,"ROSSIGNOL"],[salomon,"SALOMON"],[tyrolia,"TYROLIA"]]
logobox = (0,0,480,555)
tagbox = (0,0,1200,555)
fontsize = 150
positioncounter = 0
sheetcounter = 0
## tag positions
## |-------|
## | 0  1  |
## | 2  3  |
## | 4  5  |
## | 6  7  |
## |-------|

positions = [(0,0,1200,555),(1200,0,2400,555),
             (0,555,1200,1110),(1200,555,2400,1110),
             (0,1110,1200,1665),(1200,1110,2400,1665),
             (0,1665,1200,2220),(1200,1665,2400,2220)]

fontname = 'SairaCondensed-Regular.ttf'
fnt = ImageFont.truetype(fontname,fontsize)


with open("testbook.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
            
        brand = row[0].upper()
        item = row[1].upper()
        price = row[2].upper()

        # handling the logo based off what the brand category is
        for company in logolist:
            if company[1] == brand:
                region = company[0].crop(logobox)  
        im.paste(region,logobox)

        # handling the item name
        itemname = ImageDraw.Draw(im)
        fontsize = 140
        ycoord = 60

        # handling if the item name overflows off the tag
        while itemname.textsize(item,font=fnt)[0] > 650: 
            fontsize = fontsize - 1
            fnt = ImageFont.truetype(fontname,fontsize)
            ycoord = ycoord + 0.5
        itemname.text((518,ycoord),item,font=fnt)
        # reset font in case we messedwith it to fix sizing!
        fnt = ImageFont.truetype(fontname,185)
        

        # handling the item price
        itemprice = ImageDraw.Draw(im)
        itemprice.text((518,240),price,font=fnt)

        # save the new tag
        im.save(brand+" "+item+".png","PNG")

        ## crop the tag and paste it onto a sheet 3 times
        region = im.crop(tagbox)
        for i in range(3):
            settemplate.paste(region,positions[positioncounter])
            positioncounter = positioncounter + 1

            ## if the postion is past the end of the sheet, we have to save the current sheet
            ## reset the position counter, and increase the sheet counter.
            if positioncounter == 8:
                settemplate.save("sheet" + str(sheetcounter) + ".png","PNG")
                settemplate = Image.open("setof8.png")
                sheetcounter = sheetcounter+1
                positioncounter = 0
                

        ## save the sheet and reopen the image fresh for new tag creation
        
        im = Image.open("full tag.png")

if positioncounter != 0:
    settemplate.save("sheet" + str(sheetcounter) + ".png","PNG")
     