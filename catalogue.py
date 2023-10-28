# CS1026A: Assignment 4 "Country Classes"
# Student Name: Hala Abudaqqa
# Student No.: 251245967
# Email: habudaqq@uwo.ca

from country import *


# creating a CountryCatalogue class
class CountryCatalogue:             # reads a file, imports the content of a file and modify the information and then save them to a file
    countryCat = {}                 # a dictionary

    def __init__(self, countryFile):       # creates objects of the country catalogue class
        self.countryCat = {}
        fileLine = countryFile.readlines()[1:]    # read each line except the header which is the first line, make a new country object
        for line in fileLine:
            line = line.strip()
            countryInfo = line.split("|")  # split the string on the vertical bar character
            name = countryInfo[0]
            pop = countryInfo[2]
            area = countryInfo[3]
            continent = countryInfo[1]
            country = Country(name, pop, area, continent)
            self.countryCat[name] = country

    def setPopulationOfCountry(self, countryName, pop):
        if countryName in self.countryCat:                    # if the country exists, the population will be changed
            self.countryCat[countryName].setPopulation(pop)   # adds the new country object to the dictionary

    def setAreaOfCountry(self, countryName, area):
        if countryName in self.countryCat:                    # if the country exists, the area will be changed
            self.countryCat[countryName].setArea(area)        # adds the new country object to the dictionary

    def setContinentOfCountry(self, countryName,continent):
        if countryName in self.countryCat:                           # if the country exists, the continent will be changed
            self.countryCat[countryName].setContinent(continent)     # adds the new country object to the dictionary

    def findCountry(self,country):        # checks if that country object object is in countryCat
        if country in self.countryCat:
            return country
        else:
            return None                    # returns None if the country is not in countryCat

    def addCountry(self, countryName, pop, area, cont):   # adds a new country to the countryCat
        country = Country(countryName, pop, area, cont)   # creates a new country object with the given information
        if self.findCountry(country) is None:             # if the new country object does not exist
            self.countryCat[countryName] = country        # country object is added
            return True                                   # it should be added if the country does not exist
        return False

    def printCountryCatalogue(self):     # prints a list of the countries and their information
        values = self.countryCat.values()
        for v in values:
            print(v)

    def saveCountryCatalogue(self, fname):   # all the country information in the catalogue to be saved to a file
        try:
            file = open(fname, "w")
            file.write("Country|Continent|Population|Area\n")
            count = 0
            self.countryCat = dict(sorted(self.countryCat.items()))   # countries sorted alphabetically
            for i in self.countryCat:
                countryInfo = self.countryCat[i].getName() + "|" + self.countryCat[i].getContinent() + "|" + self.countryCat[i].getPopulation() + "|" + self.countryCat[i].getArea()
                file.write(countryInfo + "\n")
                count += 1
            file.close()
            return count                                   # if the operation is successful
        except:
            return -1                                      # if the operation is not successful it returns -1
