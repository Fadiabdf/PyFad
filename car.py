class Car:
    wheels = 4 #class variable :default value for all objects that u can change it lately for a specific object
    def __init__(self,make,model,year,color):# constructer
        # attributs of car object
        self.make = make # instance variable
        self.model = model # instance variable
        self.year = year # instance variable
        self.color = color # instance variable
'''
    #methods
    def drive(self):
        print("this "+self.model+" is driving")

    def stop(self):
        print("this "+self.model+" is stopped")
'''