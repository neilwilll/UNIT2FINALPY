class cupcake:
    def __init__(self, name, price, flavor, frosting, filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = sprinkles

my_cupcake = Cupcake("Red Velvet", 2.99, "Choclate", "Cherry", "Vanilla", True)

my_cupcake.frosting = "Chocolate"
my_cupcake.filling = "Chocolate"
my_cupcake.name = "Triple Chocolate"

my_cupcake.is_miniature = False
print(my_cupcake.is_miniature)

class Cupcake:
    def __init__(self, name, price, flavor, frosting, filling, sprinkles):
     self.name = name
     self.price = price
     self.flavor = flavor
     self.frosting = frosting
     self.filling = filling
     self.sprinkles = sprinkles
 
    def my_method(self):
        pass
    
class Cupcake:
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

        def add_sprinkles(self):
            pass
    
class Cupcake:
        def __init__(self, name, price, flavor, frosting, filling):
            self.name = name
            self.price = price
            self.flavor = flavor
            self.frosting = frosting
            self.filling = filling
            self.sprinkles = []

        def add_sprinkles(self, *args):
            for sprinkle in args:
             self.sprinkles.append(sprinkle)


        my_cupcake = Cupcake("Cookies and Cream", 2.99, "Chocolate", "Oreo", "Vanilla")

        my_cupcake.add_sprinkles("Oreo crumbs", "Chocolate", "Vanilla")

        print(my_cupcake.sprinkles)


  #pt 2 
class Cupcake:
          size = "regular"
          def __init__(self, name, price, flavor, frosting, filling):
            self.name = name
            self.price = price
            self.flavor = flavor
            self.frosting = frosting
            self.filling = filling
            self.sprinkles = []
        
class Cupcake:
        size = "regular"
        def __init__(self, name, price, flavor, frosting, filling):
            self.name = name
            self.price = price
            self.flavor = flavor
            self.frosting = frosting
            self.filling = filling
            self.sprinkles = []

        def add_sprinkles(self, *args):
            for sprinkle in args:
                self.sprinkles.append(sprinkle)

        def calculate_price(self, quantity):
            return quantity * self.price 
            class Mini(Cupcake):
            size = "mini"
            my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")
            print(my_cupcake_mini.name)
            print(my_cupcake_mini.price)
            print(my_cupcake_mini.size)

            class Mini(Cupcake):
            size = "mini"

        def __init__(self, name, price, flavor, frosting):
            self.name = name
            self.price = price
            self.flavor = flavor
            self.frosting = frosting
            self.sprinkles = []

            from abc import ABC

    #class Vehicle(ABC):#
    #pass

    #pt 3


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
     fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    cupcake1 = regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
    cupcake1.add_sprinkles("Red", "White", "Blue", "Chocolate")
    cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
    cupcake2.add_sprinkles("Oreo pieces")
    cupcake3 = LookupErrorarge("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)
    cupcake4 = Regular("TripleChocolate", 2.99, "Chocolate", "Chocolate", None)
    cupcake5 = Regular("Strawberry", 2.99, "Strawberry"","Vanilla", None)

    cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
    cupcake4
    cupcake5
    ]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
    fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for cupcake in cupcakes:
    if hasattr(cupcake, "filling"):
    writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
    else:
    writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


    write_new_csv("sample.csv", cupcake_list)

                       
                       
    #pt4
                  
        from flask import Flask 
        app = Flask(__name__)

        @app.route("/endpoint")
    def home():
            return "Hello World!"
        if __name__ == "__main__":
            app.run()

        if __name__ == "__main__":
        app.env = "development"
        app.run(debug = True, port = 8000, host = "localhost")
            #pt5                   
    def find_cupcake(file, name):
        for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
            return None

    def add_cupcake_dictionary(file, cupcake):
        with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)                   
    