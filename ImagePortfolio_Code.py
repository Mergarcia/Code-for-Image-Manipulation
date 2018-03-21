#Mercedes Garcia

def roseColoredGlasses():

  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
   
    b = getBlue(p)
    setBlue(p, b *0.7)
    g = getGreen(p)
    setGreen(p, g * 0.7)
  repaint(pic)
  writePictureTo(pic, "/Users/mercedesgarcia/CS/CSUMB/CST205/Lab#3/roseColoredGlasses.jpg")

#Negative
def makeNegative():

 filename = pickAFile()
 pic = makePicture(filename)
 pixels = getPixels(pic)
 for pix in getPixels(pic):
   red = getRed(pix)
   green = getGreen(pix)
   blue = getBlue(pix)
   negativeColor = makeColor(255-red, 255-green, 255-blue)
   setColor(pix,negativeColor)
 repaint(pic)
 writePictureTo(pic, "/Users/mercedesgarcia/CS/CSUMB/CST205/Lab#3/makeNegative.jpg")
#Black and White
def betterBnW():

  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  
  for pix in pixels:
    red = getRed(pix)
    green = getGreen(pix)
    blue = getBlue(pix)
    
    betterBnW = makeColor((red*0.299) + (green*0.587) + (blue*0.114))
    setColor(pix,betterBnW)
  repaint(pic)
  writePictureTo(pic, "/Users/mercedesgarcia/CS/CSUMB/CST205/Lab#3/betterBnW.jpg")
#Manipulates photo "Bottom to Top" Mirror
def bottomToTopMirror():
    picFile = getMediaPath("CatPic.jpg")
    pic = makePicture(picFile)
    width = getWidth(pic)
    height = getHeight(pic)
    canvas = makeEmptyPicture(width, height)
    for x in range(0,width):
        for y in range(0,height):
            color = getColor(getPixel(pic, x, y))
            setColor(getPixel(canvas,x,y),color)
            setColor(getPixel(canvas,x,height-y-1),color)
    show(pic)
    show(canvas)
    writePictureTo(canvas,"/Users/mercedesgarcia/CS/CSUMB/CST205/Lab#4/bottomToTopCat.jpg")
#Shrink Function
def shrink():
    source  = quadrupleMirror()
    srcW = getWidth(source)
    srcH= getHeight(source)
    tarW = getWidth(source)/2
    tarH = getHeight(source)/2
    target = makeEmptyPicture(tarW,tarH)

    targetX = 0
        for srcX in range(0,srcW,2):
            targetY = 0
            for srcY in range(0,srcH,2):
                color = getColor(getPixel(source,srcX,srcY))
                setColor(getPixel(target,targetX,targetY),color)
                targetY += 1
            targetX += 1
        
        show(target)
        writePictureTo(target,"/Users/mercedesgarcia/CS/CSUMB/CST205/Lab#4/shrinkCat.jpg")
#Collage Functions

def get_pic():
    filename = pickAFile()
    return makePicture(filename)

def noBlue():
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)
    for p in pixels:
        b = getBlue(p)
        setBlue(p, b * 0)
    return pic


def roseColoredGlasses():
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)
    for p in pixels:
        b = getBlue(p)
        setBlue(p, b *0.7)
        g = getGreen(p)
        setGreen(p, g * 0.7)
    repaint(pic)
    return pic

def lightenUp():
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)
    for p in pixels:
        oldColor = getColor(p)
        newColor = makeLighter(oldColor)
        lightenUp = makeColor(newColor)
        setColor(p,lightenUp)
    return pic

def makeNegative():
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)
    for pix in getPixels(pic):
        red = getRed(pix)
        green = getGreen(pix)
        blue = getBlue(pix)
        negativeColor = makeColor(255-red, 255-green, 255-blue)
        setColor(pix,negativeColor)
    repaint(pic)
    return pic

def BnW():
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)
    for pix in pixels:
        red = getRed(pix)
        green = getGreen(pix)
        blue = getBlue(pix)
    
    BnW = makeColor((red + green + blue) / 3)
        setColor(pix,BnW)
    show(pic)
    return pic

def verticalMirror():
    pic = get_pic()
    width = getWidth(pic)
    height = getHeight(pic)
    canvas = makeEmptyPicture(width, height)
    for x in range(0, width/2):
        for y in range(0, height):
            color = getColor(getPixel(pic, x, y))
            setColor(getPixel(canvas,x,y),color)
            setColor(getPixel(canvas,width- x - 1,y),color)
    show(canvas)
    return canvas

def bottomToTopMirror():
    pic = get_pic()
    width = getWidth(pic)
    height = getHeight(pic)
    canvas = makeEmptyPicture(width, height)
    for x in range(0,width):
        for y in range(0,height):
            color = getColor(getPixel(pic, x, y))
            setColor(getPixel(canvas,x,y),color)
            setColor(getPixel(canvas,x,height-y-1),color)
    show(canvas)
    return canvas

def quadrupleMirror():
    filename = pickAFile()
    pic = makePicture(filename)
    width = getWidth(pic)
    height = getHeight(pic)
    canvas = makeEmptyPicture(width, height)
    for x in range(0,width/2):
        for y in range(0,height/2):
            color = getColor(getPixel(pic, x, y))
            setColor(getPixel(canvas,x,y),color)
            setColor(getPixel(canvas,width-x-1,y),color)
            setColor(getPixel(canvas,x,height-y-1),color)
            setColor(getPixel(canvas,width-x-1,height-y-1),color)
                
    show(pic)
    show(canvas)
    return canvas


def pyCopy(source,target, targetX, targetY):
    width = getWidth(source)
    height = getHeight(source)
    
    for x in range(0,width):
        for y in range(0,height):
            color = getColor(getPixel(source,x,y))
            setColor(getPixel(target, x + targetX , y + targetY),color)
                
    return target

#Collage Function
def makeCollage():
    
    collage = makeEmptyPicture(2550,3300)

    p1 = verticalMirror()
    p2 = makeNegative()
    p3 = roseColoredGlasses()
    p4 = get_pic()
    p5 = get_pic()
    p6 = noBlue()
    p7 = get_pic()
    p8 = quadrupleMirror()
    p9 = roseColoredGlasses()
    p10 = bottomToTopMirror()
    p11 = roseColoredGlasses()
    p12 = lightenUp()
    p13 = get_pic ()
    p14 = quadrupleMirror()
    p15 = BnW()
    p16= lightenUp()


    pyCopy(p1,collage,875,1250)
    pyCopy(p2, collage, 0,0)
    pyCopy(p3, collage, 0, 700)
    pyCopy(p4, collage, 1850,1050)
    pyCopy(p5,collage, 1700, 1250)
    pyCopy(p6, collage, 0, 1290)
    pyCopy(p7,collage, 0, 2245)
    pyCopy(p8,collage, 0, 2880)
    pyCopy(p9,collage, 1900, 0)
    pyCopy(p10, collage, 880, 0)
    pyCopy(p11, collage, 1700, 2100)
    pyCopy(p12, collage, 1300, 550)
    pyCopy(p13, collage, 1330, 0)
    pyCopy(p14, collage, 800, 800)
    pyCopy(p15, collage, 850, 2000)
    pyCopy(p16, collage,2000,500)
            
            
    repaint(collage)
    writePictureTo(collage,"/Users/mercedesgarcia/CS/CSUMB/CST205/Lab#5/collage.jpg")

def removeRedEye():
    filename = pickAFile()
    pic = makePicture(filename)
    newRed = makeColor(210,50,58)
    brown = makeColor(119,101,54)
    for p in getPixels(pic):
        color = getColor(p)
        if distance(color, newRed) < 50.0:
            setColor(p, brown)
    repaint(pic)

#Luminance function
def Artify():
    
    filename = pickAFile()
    pic = makePicture(filename)
    pixels = getPixels(pic)

    for p in pixels:

red = getRed(p)
green = getGreen(p)
blue = getBlue(p)

    if red < 64:
        setRed(p,31)
    elif 63<red<128:
        setRed(p,95)
    elif 127<red<192:
        setRed(p,159)
    elif 191<red<256:
        setRed(p,223)

    elif green <64:
        setGreen(p, 31)
    elif 63<green<128:
        setGreen(p,95)
    elif 127<green<192:
        setGreen(p,159)
    elif 191<green<256:
        setGreen(p,223)
    
    elif blue < 64:
        setBlue(p,31)
    elif 63<blue<128:
        setBlue(p,95)
    elif 127<blue<192:
        setBlue(p,159)
    elif 191<blue<256:
        setBlue(p,223)

    repaint(pic)
#Green screen function
def chromakey(source,bg):
    for x in range(1,source.getWidth()):
        for y in range(1,source.getHeight()):
            p = getPixel(source,x,y)
            if((getRed(p) + getBlue(p)) < getGreen(p)):
                setColor(p,getColor(getPixel(bg,x,y)))
    repaint(source)
    return(source)

#Line Drawing Function with supplemental fucntions
def get_pic():
    filename = pickAFile()
    return makePicture(filename)

def betterBnW(pic):
    
    pixels = getPixels(pic)

    for pix in pixels:
    red = getRed(pix)
    green = getGreen(pix)
    blue = getBlue(pix)
    
    betterBnW = makeColor((red*0.299) + (green*0.587) + (blue*0.114))
        setColor(pix,betterBnW)
    return(pic)


def lineDraw(pic):
    
    pixels = getPixels(pic)
    betterBnW(pic)

    for x in range(0, getWidth(pic)-1):
        for y in range(0, getHeight(pic)-1):
            p = getPixel(pic, x, y)
            pBelow = getPixel(pic, x, y+1)
            pRight = getPixel(pic, x+1, y)
            picValue = getRed(p)
            valBelow = getRed(pBelow)
            valRight = getRed(pRight)
            if abs(picValue - valBelow) > 2 and abs(picValue - valRight) > 2:
                setColor(p, black)
            else:
                setColor(p, white)
    show(pic)
    return(pic)











