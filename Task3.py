from gfxhat import lcd
from gfxhat import backlight

def generateDictionary(charToShow):
    font3In = open("font3.txt", "r")
    for line in font3In:
        fullLine = line.split(",")
        charAndReturn = fullLine[1]
        character = charAndReturn[0]
        if character == charToShow:
            break
        
    if character != charToShow:
        print("This character cannot be displayed.")
        return "N/A"

    hexCode = int(fullLine[0], 16)
        
    binNumber = f'{hexCode:0>64b}'
    listOfBin = list(binNumber)
    obj = []
    for i in range(0,8):
        listToAdd = []
        for j in range(0,8):
            elementId = (i*8) + j
            intOfBin = int(listOfBin[elementId])
            listToAdd.append(intOfBin)
        obj.append(listToAdd)

    return obj


def displayObject(obj, x, y):
    positionx = x
    positiony = y
    for i in obj:
        for j in i:
            if j == 1:
                lcd.set_pixel(positionx, positiony, 1)
            positionx += 1
        positiony += 1
        positionx = x
    lcd.show()


backlight.set_all(190,190,190)
backlight.show()
print("This program will display a character of your choice on the GFX Hat.")
print("Please write the character you want to display. Write ONLY ONE character, or it will not work.")
print("Enter 'exit' to end the program")
print("")
while True:
    charInput = input(str("Write the character you want to display."))
    lcd.clear()
    lcd.show()
    if charInput == "exit":
        break
    else:
        obj = generateDictionary(charInput)
        if obj == "N/A":
            continue
        displayObject(obj,60,30)
    
backlight.set_all(0,0,0)
backlight.show()