#self -> points to the instance of the class i.e self = personName
#Person - Name of class
class person:
    def __init__(self,personId): #It is like initialization for a class instance
        self.personId = personId
        print ("In initialization part - Constructor")
    def __del__(self) : #It deletes Class instance when ever control is out of scope - End of usage of class instance
        print ("Deletes class instance - Destructor")
    def setNames(self,firstName,lastName): #Member function - Set Names
        self.firstName=firstName #Passing Attributes
        self.lastName=lastName #Passing Attributes
    def printName(self): #Member function - Print Names
        print (self.firstName,self.lastName,self.personId)

personName=person(5061) #Instance of a class or Object
personName.setNames("Arun",'Kumar') #Passing attributes to the class
print(personName.__dict__) #Dictionary of a Instance object - It gives all info on Instance variables and its present values
personName.printName() #To print output
personName.firstName = "Vishnu","Kiran" #To Redefine Names in Instance
personName.personId = 5091
personName.printName() #To print output
personName1=person(5087)
personName1.setNames("Shashank",'Merugu')
personName1.printName()
personName.__del__()
print(personName1.__dict__)
