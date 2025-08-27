class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        
    def describe_car(self):
        print("Year",self.year)
        print("Make",self.make)
        print("Model",self.model)
        return
    

myCar=Car("Toyota","Corolla","2020")
print(myCar.describe_car())
