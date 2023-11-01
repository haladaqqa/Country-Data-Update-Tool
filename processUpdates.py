from catalogue import *


def processUpdates(cntryFileName,updateFileName,badUpdateFile):        # processes the updates and returns tuple of whether updates were successful or not
    file = open(badUpdateFile,"w")                             # opens and writes in the bad update file
    # utilize the try_open method to keep trying to open the file until its successful or the user quits
    countryData = try_open(cntryFileName)                      # open the country file and checks if it exists using the method try_open
    updateData = try_open(updateFileName)                      # open the update file and checks if it exists using the method try_open

    if countryData is False or updateData is False:            # if try_open returned False for either files
        return (False, None)

    catlog = CountryCatalogue(countryData)                    # initiates country catalogue using CountryCatalogue class
    fileLine = updateData.readlines()
    for line in fileLine:
        newline = line.strip()                                # strip spaces
        newline = newline.replace(" ","")                     # remove spaces
        updateInfo = newline.split(";")                       # split the data at semicolon
        if len(updateInfo) > 4:                               # the semicolons separating the country name should be less than 4
            file.write(line)                                  # writes in the bad update file
            continue
        country = updateInfo[0]
        cntry_obj = Country(country,"","","")
        countryEntry = catlog.findCountry(country)          # find country for existence
        if countryEntry is None:                                # checks if the country name is valid
            for u in updateInfo[1:]:                            # check update
                if u[0] == "P":
                    cntry_obj.setPopulation(u[2:])
                elif u[0] == "A":
                    cntry_obj.setArea(u[2:])
                elif u[0] == "C":
                    cntry_obj.setContinent(u[2:])
            catlog.addCountry(cntry_obj.getName(),cntry_obj.getPopulation(),cntry_obj.getArea(),cntry_obj.getContinent())

        if check_capital(country) and country != "":                 # check if the country name is in a specific format and is not blank
            found_P = False
            found_A = False
            found_C = False
            for u in updateInfo[1:]:
                uInfo = u.split("=")
                if uInfo[0] == "P" and found_P is False:
                    if check_num(uInfo[1]):      # population has to be in a specific format
                        catlog.setPopulationOfCountry(country,uInfo[1])   # update population
                        found_P = True
                    else:

                        file.write(line)
                        continue
                elif uInfo[0] == "A" and found_A is False:
                    if check_num(uInfo[1]):
                        catlog.setAreaOfCountry(country,uInfo[1])
                        found_A = True
                    else:
                        file.write(line)
                        continue
                elif uInfo[0] == "C" and found_C is False:
                    validContinent = ["Africa","Antarctica","Arctic","Asia","Europe","North_America","South_America"]
                    if uInfo[1] in validContinent:
                        catlog.setContinentOfCountry(country,uInfo[1])
                        found_C = True
                    else:
                        file.write(line)                                       # writes in the bad update file
                        continue
                else:
                    file.write(line)                                           # writes in the bad update file
                    continue

            catlog.saveCountryCatalogue("output.txt")                          # writes the updated country catalogue to an output file
        else:
            file.write(line)                                                   # writes in the bad update file
            continue

    return (True,catlog)


def try_open(filename):                                              # checks if the file exists or not, opens file repeatedly until it is done successfully
    while True:                                                      # run the loop until the user enters correct file name or quits
        try:
            open_Data = open(filename,"r")                           # open file and check status
            return open_Data                                         # returns the file if it exists
        except:                                                      # if the file does not exist
            value = input("Do you want to quit? (Y/N)")              # prompt the user to quit or not (yes or no)
            if value == "N":                                         # if N prompt for filename
                filename = input("What is the new valid filename?")
            else:                                                    # if y,(user wants to quit) to output file update unsuccessful then return false
                newFile = open("output.txt", "w")
                newFile.write("Update Unsuccessful \n")
                return False


def check_capital(string):                                           # checks if the string consists of underscores beginning with a capital letter
    word = string.split("_")
    for w in word:
        if w != w.capitalize():
            return False
    return True


def check_num(num):                                                  # checks if the string of digits consists of commas separating groups of 3
    reverse = num[::-1]
    for i in range(len(reverse)):
        if i % 4 == 3:
            if reverse[i] != ",":
                return False
        else:
            if reverse[i] == ",":
                return False
    return True
