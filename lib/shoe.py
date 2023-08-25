#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

if __name__ == "__main__":
    # Test the Shoe class
    stan_smith = Shoe("Adidas", 9)
    print(stan_smith.size)  
    stan_smith.size = "not an integer"  
    print(stan_smith.size)  
    stan_smith.cobble()  
