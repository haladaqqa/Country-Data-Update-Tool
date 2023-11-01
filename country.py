# creating a Country class
class Country:                                    # holds information about a single country
    def __init__(self,name,pop,area,continent):   # creating the Country object with the instance variables
        # initializing instance variables
        self.name = name
        self.pop = pop
        self.area = area
        self.continent = continent

    def getName(self):                            # getter method for name of country
        return self.name

    def getPopulation(self):                      # getter method for population of country
        return self.pop

    def setPopulation(self, pop):                 # setter method to set population of country
        self.pop = pop

    def getArea(self):                            # getter method for area of country
        return self.area

    def setArea(self, area):                      # setter method to set area of country
        self.area = area

    def getContinent(self):                       # getter method for continent of country
        return self.continent

    def setContinent(self, continent):            # setter method to set continent of country
        self.continent = continent

    def __repr__(self):                         # generates a string representation for class objects
        n = (str(self.name) + " (pop: " + str(self.pop) + ", size: " + str(self.area) + ") in " + str(self.continent))
        return n
