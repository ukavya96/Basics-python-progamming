class Animal:
    def __init__(self,name,sound):
        self.animal_name=name
        self.animal_sound=sound
        
    def Sound(self):
        print(f"{self.animal_name} is makes {self.animal_sound} sound")
        
Dog=Animal("dog","bow")
Cat=Animal("cat","meow")



Dog.Sound()
Cat.Sound()
      
        