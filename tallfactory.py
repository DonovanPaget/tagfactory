###########################
# reads from a csv file with 3 columns: 
#   BRAND NAME, ITEM NAME, PRICE
# the brand must be from this list:
#   atomic, burton, full tilt, head, jones, k2, line, look, marker, ride, rossignol, salomon, tyrolia
# there will be 8 tags a sheet. 3 tags for each item. 
#  
#   TODO: binding and ski tags (skinny and long)
#   TODO: fix short item names being low on the tag
#   TODO: test with large price book
###########################
from __future__ import print_function
import os, sys, csv
from PIL import Image, ImageDraw, ImageFont

## need to open all the logo files for use
im = Image.open("resources/tall tag.png").convert("RGBA")
settemplate = Image.open("resources/tallsetof8.png").convert("RGBA")


burton = Image.open("resources/logo/burtonlogo.png").convert("RGBA")
jones = Image.open("resources/logo/jones logo.png").convert("RGBA")
k2 = Image.open("resources/logo/k2logo.png").convert("RGBA")
atomic = Image.open("resources/logo/atomiclogo.png").convert("RGBA")
fulltilt = Image.open("resources/logo/ftlogo.png").convert("RGBA")
head = Image.open("resources/logo/headlogo.png").convert("RGBA")
line = Image.open("resources/logo/line logo.png").convert("RGBA")
look = Image.open("resources/logo/look logo.png").convert("RGBA")
marker = Image.open("resources/logo/marker logo.png").convert("RGBA")
ride = Image.open("resources/logo/ridelogo.png").convert("RGBA")
rossi = Image.open("resources/logo/rossilogo.png").convert("RGBA")
salomon = Image.open("resources/logo/salomonlogo.png").convert("RGBA")
tyrolia = Image.open("resources/logo/tyrolia logo.png").convert("RGBA")
fischer = Image.open("resources/logo/fischer logo.png").convert("RGBA")
dynastar = Image.open("resources/logo/dynastar logo.png").convert("RGBA")
armada = Image.open("resources/logo/armada logo.png").convert("RGBA")
smith = Image.open("resources/logo/smith logo.png").convert("RGBA")
giro = Image.open("resources/logo/giro logo.png").convert("RGBA")
poc = Image.open("resources/logo/poc logo.png").convert("RGBA")
logolist = [[poc,"POC"],[giro,"GIRO"],[smith,"SMITH"],[armada,"ARMADA"],[dynastar,"DYNASTAR"],[burton,"BURTON"], [jones, "JONES"], [k2,"K2"], [atomic,"ATOMIC"], [fulltilt,"FULL TILT"], [head,"HEAD"],[line,"LINE"],[look,"LOOK"],[marker,"MARKER"],[ride,"RIDE"],[rossi,"ROSSIGNOL"],[salomon,"SALOMON"],[tyrolia,"TYROLIA"],[fischer,"FISCHER"]]
logobox = (0,0,480,555)
tagbox = (0,0,480,950)
fontsize = 140
positioncounter = 0
sheetcounter = 0
## tag positions
## |-----------|
## | 0  1  2  3|
## | 4  5  6  7|
## |-----------|

positions = [(0,0,480,950),(480,0,960,950),
             (960,0,1440,950),(1440,0,1920,950),
             (0,950,480,1900),(480,950,960,1900),
             (960,950,1440,1900),(1440,950,1920,1900)]

fontname = 'SairaCondensed-Regular.ttf'
fnt = ImageFont.truetype(fontname,fontsize)


with open("resources/pricebook.csv") as csv_file:
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
        fontsize = 90
        ycoord = 565

        # handling if the item name overflows off the tag
        while itemname.textsize(item,font=fnt)[0] > 400: 
            fontsize = fontsize - 1
            fnt = ImageFont.truetype(fontname,fontsize)
            ycoord = ycoord + 1
        itemname.text((45,ycoord),item,font=fnt)
        # reset font in case we messedwith it to fix sizing!
        fnt = ImageFont.truetype(fontname,140)
        

        # handling the item price
        itemprice = ImageDraw.Draw(im)
        itemprice.text((36,700),price,font=fnt)

        # save the new tag
        im.save("tags/"+brand+" "+item+".png","PNG")

        ## crop the tag and paste it onto a sheet 3 times
        region = im.crop(tagbox)
        for i in range(3):
            settemplate.paste(region,positions[positioncounter])
            positioncounter = positioncounter + 1

            ## if the postion is past the end of the sheet, we have to save the current sheet
            ## reset the position counter, and increase the sheet counter.
            if positioncounter == 8:
                settemplate.save("tags/sheets/" + "sheet" + str(sheetcounter) + ".png","PNG")
                settemplate = Image.open("resources/tallsetof8.png").convert("RGBA")
                sheetcounter = sheetcounter+1
                positioncounter = 0
                

        ## save the sheet and reopen the image fresh for new tag creation
        
        im = Image.open("resources/tall tag.png").convert("RGBA")

if positioncounter != 0:
    settemplate.save("sheet" + str(sheetcounter) + ".png","PNG")
     