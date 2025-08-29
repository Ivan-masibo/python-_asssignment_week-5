# 1a). Activity Base class

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"{self.model} is calling {number}... 📞")

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"{self.model} charged to {self.battery}% 🔋")

    def info(self):
        print(f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%")

 # c) Child class with inheritance
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_quality):
        super().__init__(brand, model, storage, battery)
        self.camera_quality = camera_quality
# d) Polymorphism: overriding a method 
    def info(self):
        print(f"{self.brand} {self.model} Pro | Storage: {self.storage}GB | Battery: {self.battery}% | Camera: {self.camera_quality}MP 📷")

    def take_photo(self):
        print(f"{self.model} takes a {self.camera_quality}MP photo! 📸")

# e) Creating objects 
phone1 = Smartphone("Evanray", "eVAN 14", 64, 50)
phone2 = SmartphonePro("Evanray", "eVAN 2", 256, 80, 48)

# f) Using methods
phone1.info()
phone1.call("0700932014")
phone1.charge(30)

print()  # space

phone2.info()
phone2.take_photo()
phone2.call("0700932014")
