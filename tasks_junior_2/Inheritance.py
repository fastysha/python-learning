from abc import ABC, abstractmethod

class Product():
    def __init__(self,brand,name,price):
        self.name_brand=brand
        self.name_product=name
        self.price=price

    def general_brand_name(self):
        print("We have: ",self.name_brand,self.name_product)

    def get_all_props(self):
        return self.name_brand, self.name_product, self.price


class Phone(Product):
    def __init__(self,brand,name,price,memory,camera):
        super().__init__(brand,name,price)
        self.memory=memory
        self.camera=camera

    def print_availability(self):
        print("Now in stock: ", super().get_all_props(), self.memory, self.camera)

class TV(Product):
    def __init__(self,brand,name,price,diagonal,screen):
        super().__init__(brand,name,price)
        self.diagonal=diagonal
        self.screen=screen

    def print_availability(self):
        print("Now in stock: ", super().get_all_props(), self.diagonal,self.screen)

p=Phone("Iphone","11 Pro max",40000,"560 gb","14.0")
p1=Phone("Iphone","12 Pro max",60000,"240 gb","18.0")
t=TV("Samsung","X5",23450,"30x50","HD")
t1=TV("Lenovo","A10",30500,"50x80","Full HD")


p.print_availability()
t.print_availability()

