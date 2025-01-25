# t.py - Titanium Display Manager
# Version - 0.1-alpha

# Global Variables (can be used for any occasions)
resX = 0
resY = 0
posX = 0
posY = 0
cdepth = 8
csend = '\n '

print("""
----------------------------------------
 T.py - Titanium Display Manager
 Version - 0.1-alpha
----------------------------------------
""",end=" ")

print("Importing Turtle...",end="")
import turtle as tl # importing the module with the name "tl"
print("done",end=csend)
# initializing the canvas
# all the functions in this section are self-explanatory, so there's no need to explain
# about them
tl.speed(0)
print(f"Turtle Speed: {tl.speed()} (infinity)",end=csend)
tl.delay(0)
print(f"Turtle Delay: {tl.delay()} (zero delay)",end=csend)
tl.bgcolor(0,0,0)
print(f"Background color: {tl.bgcolor()}",end=csend)
tl.hideturtle()
print(f"Turtle: Hidden")
print("----------------------------------------")

# The Color Palette function serves the final color that can be used in a given pixel.
# Because the whole color system functions in floating values by default, we need to
# ensure the color system works in fixed absolute states instead of fluid ones.
#print("ColorPalette(self,cdepth)")
#def ColorPalette(self,cdepth):
#    if self <= cdepth:
#        print(self/cdepth
#    else:
#        print("Fault: value of ColorPalette is greater than color depth")

# the filler command for the else keyword
def fillerC():
    while True:
        break

# the fill command in a program like a display manager AND a WINDOW MANAGER!!!
# ohhhhhhhhhhh... man!!! i keep forgetting it's a displyay manager fr, i can't
# take it anymore. i'm done. It was supposed to be a display manager, not a
# window manager. the only reason why i didn't make the window manager a separate
# program was because the program had NO file support. or at least, i don't even
# know how to put it in action in Python. Like, Python is weird. There are some
# programming languages such as C, C++, Ruby and Java, that actually do it much
# better than Python, but the trouble is they don't look like Python at all.
# Even C++, the one I thought was hard to learn, actually looked a bit similar
# to Python, but I didn't learn it because it was confusing. it used accent marks
# to have something pumped into the standard output, like a terminal, like
# "std::cout << "help me"" like what even is this? It's like it's a programming
# language that murdered a Linux shell and is now wearing its skin.

# the fill command that puts a rectangle.
def Fill(X,Y,Xend,Yend,r,g,b):
    while Y > Yend:
        tl.pendown()
        tl.setx(X)
        tl.setx(Xend)
        tl.penup()
        tl.setx(X)
        tl.sety(Y)
        tl.color(r,g,b)
        print("x = "+str(X)+", "+"y = "+str(Y)+", "+"r = "+str(r)+", " + "g = "+str(g)+", " + "b = "+str(b),end="            \r ")
        Y -= 1

def Font_CharacterSans(self):
    CapitalA = "0001000000101000010001001000001011111110100000101000001000000000"
    CapitalB = "1111110010000010100000101111110010000010100000101111110000000000"
    CapitalC = "0111110010000010100000001000000010000000100000100111110000000000"
    CapitalD = "1111110010000010100000101000001010000010100000101111110000000000"
    CapitalE = "1111111010000000100000001111000010000000100000001111111000000000"
    CapitalF = "1111111010000000100000001111000010000000100000001000000000000000"
    CapitalG = "0111110010000010100000001001111010000010100000100111110000000000"
    CapitalH = "1000001010000010100000101111111010000010100000101000001000000000"
    CapitalI = "1111111000010000000100000001000000010000000100001111111000000000"
    CapitalJ = "1111111000000010000000100000001010000010100000100111110000000000"
    CapitalK = "1000001010000100100010001001000010101000110001001000001000000000"
    CapitalL = "1000000010000000100000001000000010000000100000001111111000000000"
    CapitalM = "1000001011000110101010101001001010000010100000101000001000000000"
    CapitalN = "1000001011000010101000101001001010001010100001101000001000000000"
    CapitalO = "0111110010000010100000101000001010000010100000100111110000000000"
    CapitalP = "1111110010000010100000101111110010000000100000001000000000000000"
    CapitalQ = "0111110010000010100000101000001010001010100001000111101000000000"
    CapitalR = "1111110010000010100000101111110010010000100010001000011000000000"
    CapitalS = "0111111010000000100000000111110000000010000000101111110000000000"
    CapitalT = "1111111000010000000100000001000000010000000100000001000000000000"
    CapitalU = "1000001010000010100000101000001010000010100000100111110000000000"
    CapitalV = "1000001010000010100000101000001001000100001010000001000000000000"
    CapitalW = "1000001010000010100000101001001010101010110001101000001000000000"
    CapitalX = "1000001001000100001010000001000000101000010001001000001000000000"
    CapitalY = "1000001001000100001010000001000000010000000100000001000000000000"
    CapitalZ = "1111111000000100000010000001000000100000010000001111111000000000"
    # Introducing mini versions of the above letters right now...
    # Starting with letter A.
    SimpleA = "0000000000000000001110000000010000111100010001000011110000000000"
    SimpleB = "0100000001000000011110000100010001000100010001000111100000000000"
    SimpleC = "0000000000000000001110000100010001000000010001000011100000000000"
    SimpleD = "0000010000000100001111000100010001000100010001000011110000000000"
    SimpleE = "0000000000000000001110000100010001111100010000000011110000000000"
    SimpleF = "0000110000010000011111000001000000010000000100000001000000000000"
    SimpleG = "0000000000000000001111100100010000111100000001000011100000000000"
    SimpleH = "0100000001000000011110000100010001000100010001000100010000000000"
    SimpleI = "0001000000000000000100000001000000010000000100000001000000000000"
    SimpleJ = "0000010000000000000001000000010000000100010001000011100000000000"
    SimpleK = "0100000001000000010010000101000001100000010100000100100000000000"
    SimpleL = "0001000000010000000100000001000000010000000100000001000000000000"
    SimpleM = "0000000000000000000000001110110011010010100100101001001000000000"
    SimpleN = "0000000000000000000000000101100001100100010001000100010000000000"
    SimpleO = "0000000000000000001110000100010001000100010001000011100000000000"
    SimpleP = "0000000000000000011100000100100001001000011100000100000001000000"
    SimpleQ = "0000000000000000001110000100100001001000001110100000110000001000"
    SimpleR = "0000000000000000010110000110010001000000010000000100000000000000"
    SimpleS = "0000000000000000001110000100000000111000000001000011100000000000"
    SimpleT = "0000000000100000001000000010000011111000001000000010010000011000"
    SimpleU = "0000000000000000000000000100100001001000010010000011100000000000"
    SimpleV = "0000000000000000000000000100010001000100001010000001000000000000"
    SimpleW = "0000000000000000010001000100010001010100011011000100010000000000"
    SimpleX = "0000000000000000010001000010100000010000001010000100010000000000"
    SimpleY = "0000000000000000010001000100010001000100001111000000010001111000"
    SimpleZ = "0000000000000000011111000000100000010000001000000111110000000000"
    # Symbols and punctuation marks for definition of the sentences...
    Space               =   "0000000000000000000000000000000000000000000000000000000000000000"
    Period              =   "0000000000000000000000000000000000000000001100000011000000000000"
    Comma               =   "0000000000000000000000000000000000000000001100000001000000100000"
    At                  =   "0111110010000010100110101010101010011110100000000111110000000000"
    Hash                =   "0100010011111110010001000100010001000100111111100100010000000000"
    Dollar              =   "0011110001010000010100000011100000010100000101000111100000010000"
    Percent             =   "0110001010010100100110000111110000110010010100101000110000000000"
    Caret               =   "0000000000010000001010000000000000000000000000000000000000000000"
    ExclamationMark     =   "0000000000010000000100000001000000010000000000000001000000000000"
    Ampersand           =   "0010000001010000001000000101001010001100100011000111001000000000"
    Single_Quote        =   "0000000000010000000100000000000000000000000000000000000000000000"
    Double_Quote        =   "0000000000101000001010000010100000000000000000000000000000000000"

    if self == 'A':
        return CapitalA # wait, we cannot define a variable in the function definition to extract the value from it
    elif self == 'B':   # so how can we accomplish the master challenge of turning letters to character bitmaps?
        return CapitalB # let's use the return command and see if it does anything
    elif self == 'C':   # nice! it worked. i love it!
        return CapitalC
    elif self == 'D':
        return CapitalD
    elif self == 'E':
        return CapitalE
    elif self == 'F':
        return CapitalF
    elif self == 'G':
        return CapitalG
    elif self == 'H':
        return CapitalH
    elif self == 'I':
        return CapitalI
    elif self == 'J':
        return CapitalJ
    elif self == 'K':
        return CapitalK
    elif self == 'L':
        return CapitalL
    elif self == 'M':
        return CapitalM
    elif self == 'N':
        return CapitalN
    elif self == 'O':
        return CapitalO
    elif self == 'P':
        return CapitalP
    elif self == 'Q':
        return CapitalQ
    elif self == 'R':
        return CapitalR
    elif self == 'S':
        return CapitalS
    elif self == 'T':
        return CapitalT
    elif self == 'U':
        return CapitalU
    elif self == 'V':
        return CapitalV
    elif self == 'W':
        return CapitalW
    elif self == 'X':
        return CapitalX
    elif self == 'Y':
        return CapitalY
    elif self == 'Z':
        return CapitalZ
    elif self == 'a':
        return SimpleA
    elif self == 'b':
        return SimpleB
    elif self == 'c':
        return SimpleC
    elif self == 'd':
        return SimpleD
    elif self == 'e':
        return SimpleE
    elif self == 'f':
        return SimpleF
    elif self == 'g':
        return SimpleG
    elif self == 'h':
        return SimpleH
    elif self == 'i':
        return SimpleI
    elif self == 'j':
        return SimpleJ
    elif self == 'k':
        return SimpleK
    elif self == 'l':
        return SimpleL
    elif self == 'm':
        return SimpleM
    elif self == 'n':
        return SimpleN
    elif self == 'o':
        return SimpleO
    elif self == 'p':
        return SimpleP
    elif self == 'q':
        return SimpleQ
    elif self == 'r':
        return SimpleR
    elif self == 's':
        return SimpleS
    elif self == 't':
        return SimpleT
    elif self == 'u':
        return SimpleU
    elif self == 'v':
        return SimpleV
    elif self == 'w':
        return SimpleW
    elif self == 'x':
        return SimpleX
    elif self == 'y':
        return SimpleY
    elif self == 'z':
        return SimpleZ
    elif self == ' ':
        return Space
    elif self == '.':
        return Period
    elif self == ',':
        return Comma
    elif self == '!':
        return ExclamationMark
    elif self == '@':
        return At
    elif self == '$':
        return Dollar
    elif self == '%':
        return Percent
    elif self == '^':
        return Caret
    elif self == '&':
        return Ampersand
    elif self == '\'':
        return Single_Quote
    elif self == '\"':
        return Double_Quote
    else:
        return ""

# The Charater Printer!!! One of the sigmas in this app! This is crazy! :D
def CharacterPrinter(self,X,Y,r,g,b):
    posX = int(X)
    posY = int(Y)
    resX = 8
    resY = 8
    posXend = posX + resX
    posYend = posY - resY
    fred = r/cdepth
    fgreen = g/cdepth
    fblue = b/cdepth
    self_position = 0
    while posY > posYend:
        tl.sety(posY)
        posX = int(X)
        while posX < posXend:
            tl.setx(posX)
            tl.color(fred,fgreen,fblue)
            if self[self_position] == '0':
                tl.penup()
            elif self[self_position] == '1':
                tl.pendown()
            else:
                print("bit corrupted...")
            print(f"x = {posX}, y = {posY}, z = {self_position}", end = "\r")
            self_position += 1
            posX += 1
        posY -= 1

# ----- written on November 1st 2024, one day after Halloween -----
# find me in the woods with this text writer that has a built-in font and can write
# text like your standard average typewriter.
def TextPrinter(X,Y,text,r,g,b):
    posX = int(X)
    posY = int(Y)
    character_spacing = 8
    for text_position in range(0,len(text)):
        letter_bitmap_buffer = Font_CharacterSans(text[text_position])
        CharacterPrinter(letter_bitmap_buffer,posX,posY,r,g,b)
        posX += character_spacing

# found the issue. even though the environment background function worked just fine,
# the only reason why the window background function doesn't work is because the
# function itself has no defined absolute start points. sure, i would save time just
# by doing things the professional way, but i didn't know how to make the resolution
# variable apply to every function on the program. it's time to make a new adaptation
# of the background function and hope it works.
def Background(XSize,YSize,r,g,b):
    # setting up the resolution
    resX = XSize
    resY = YSize
    # the first position to start with. Whichever moves first is gay.
    posX = int((resX/2)-resX)
    posY = int(resY/2)
    # the last position to end with. English or Spanish, French would win.
    posXend = int(resX/2)
    posYend = int((resY/2)-resY)
    # checking if each values are greater than the depth of each color
    # if the values are greater than cdepth, set the ceiling for them
    if r > cdepth:
        r = cdepth
        if g > cdepth:
            g = cdepth
            if b > cdepth:
                b = cdepth
            else:
                fillerC()
        else:
            fillerC()
    else:
        fillerC()
    # the color palette system. I need the colors to assert dominance
    # in a monotonous world full of shades of gray.
    fred = r/cdepth
    fgreen = g/cdepth
    fblue = b/cdepth
    Fill(posX,posY,posXend,posYend,fred,fgreen,fblue)

class Window():
    # there we go, did some fixes to the resolution variable and the position
    # variable
    def Background(X,Y,XSize,YSize,r,g,b):
        # setting up the resolution
        resX = XSize
        resY = YSize
        # the first position to start with. Whichever moves first is gay.
        posX = 0 - X
        posY = Y
        # the last position to end with. English or Spanish, French would win.
        posXend = posX + resX
        posYend = 0 - posY + resY
        # checking if each values are greater than the depth of each color
        # if the values are greater than cdepth, set the ceiling for them
        if r > cdepth:
            r = cdepth
            if g > cdepth:
                g = cdepth
                if b > cdepth:
                    b = cdepth
                else:
                    fillerC()
            else:
                fillerC()
        else:
            fillerC()
        # the color palette system. I need the colors to assert dominance
        # in a monotonous world full of shades of gray.
        fred = r/cdepth
        fgreen = g/cdepth
        fblue = b/cdepth
        Fill(posX,posY,posXend,posYend,fred,fgreen,fblue)

    def TitleBar(X,Y,scaleX,thickness,r,g,b):
        # setting up the resolution
        resX = scaleX
        resY = thickness
        # the first position to start with. Whichever moves first is gay.
        posX = 0 - X
        posY = Y
        # the last position to end with. English or Spanish, French would win.
        posXend = posX + resX
        posYend = posY - resY
        # checking if each values are greater than the depth of each color
        # if the values are greater than cdepth, set the ceiling for them
        if r > cdepth:
            r = cdepth
            if g > cdepth:
                g = cdepth
                if b > cdepth:
                    b = cdepth
                else:
                    fillerC()
            else:
                fillerC()
        else:
            fillerC()
        # the color palette system. I need the colors to assert dominance
        # in a monotonous world full of shades of gray.
        fred = r/cdepth
        fgreen = g/cdepth
        fblue = b/cdepth
        Fill(posX,posY,posXend,posYend,fred,fgreen,fblue)

# themes
# not yet implemented, but will be implemented in the future

#test program
#Background(640,480,10,10,10)
#Window.Background(200,200,200,300,5,7,8)
#Window.TitleBar(200,200,200,15,1,2,3)
TextPrinter(-200,0,"don\'t mind me, just here to troubleshoot the text feature",4,0,8)

tl.done()
