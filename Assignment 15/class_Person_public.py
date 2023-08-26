class Person:
    def __init__(self, name):
        self.name = name          # public
        self._age = None          # protected
        self.__address = None     # private
    
    def set_age(self, age):
        if age > 0:
            self._age = age
    
    def set_address(self, address):
        self.__address = address
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Address: {self.__address}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        
    def display_student_info(self):
        print(f"Student ID: {self.student_id}")

student = Student("Alice", "S123")
student.set_age(20)          
student.set_address("123 Street")  

student.display_info()        
student.display_student_info() 

print(student.name)        
print(student._age)        
print(student._Person__address)  
