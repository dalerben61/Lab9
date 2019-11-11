boysNamesIn = open("2000_BoysNames.txt", "r")
boysNamesOut = open("2000_BoysNames.csv", "w")
line1 = '"First Name","Count" \n'
boysNamesOut.write(line1)
for line in boysNamesIn:
    fullLine = line.split()
    firstName = fullLine[0]
    nameCount = fullLine[1]
    lineToJoin = '"', firstName, '","', nameCount, '" \n'
    lineToWrite = ''.join(lineToJoin)
    boysNamesOut.write(lineToWrite)
boysNamesIn.close
boysNamesOut.close

girlsNamesIn = open("2000_GirlsNames.txt", "r")
girlsNameOut = open("2000_GirlsNames.csv", "w")
line2 = '"First Name","Count" \n'
girlsNameOut.write(line1)
for line in girlsNamesIn:
    fullLine2 = line.split()
    firstName2 = fullLine2[0]
    nameCount2 = fullLine2[1]
    lineToJoin2 = '"', firstName2, '","', nameCount2, '" \n'
    lineToWrite2 = ''.join(lineToJoin2)
    girlsNameOut.write(lineToWrite2)
girlsNamesIn.close
girlsNameOut.close