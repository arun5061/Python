import pickle
class person:
    def setNames(self,firstName,lastName): #Member function - Set Names
        self.firstName=firstName #Passing Attributes
        self.lastName=lastName #Passing Attributes
    def printName(self): #Member function - Print Names
        print (self.firstName,self.lastName)

personName=person() #Instance of a class or Object
personName.setNames("Arun",'Kumar') #Passing attributes to the class
personName.printName() #To print output
obj=personName
obj.printName()


#self -> points to the instance of the class i.e self = person

#input_raw("/n/n press enter")
