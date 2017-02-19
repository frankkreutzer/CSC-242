class Animal():

    def __init__(self, species = "default", language = "default", age = 0):
        self.species = species
        self.lang = language
        self.age = age 

    def __repr__(self):
        return( "Animal('{}','{}',{})".format(self.species, self.lang, self.age) )
        
    def setSpecies(self, species):
        self.species = species
        
    def setLanguage(self, language):
        self.lang = language
        
    def setAge(self, age):
        self.age = age

    def speak(self):
        print( "I am a {} year-old {} and I {}.".format(self.age, self.species, self.lang) )



def processAnimals(filename):
    with open(filename, 'r') as f:
        animalList = []
        for line in f:
            newAnimal = Animal(*(line.strip().split(',')))
            animalList.append(newAnimal)
            newAnimal.speak()
        return(animalList)



if __name__=='__main__':
    import doctest
    print(doctest.testfile('lab2TEST.py'))
