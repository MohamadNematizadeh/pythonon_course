class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f"{self.name} is speaking.")

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def study(self, subject):
        print(f"{self.name} is studying {subject}.")
        
class Assistant(Student):
    def __init__(self, name, age, student_id, assistant_id):
        super().__init__(name, age, student_id)
        self.assistant_id = assistant_id
        
    def assist_professor(self, task):
        print(f"{self.name} (Assistant) is assisting with {task}.")


human = Human("Mohmmad", 16)
student = Student("Ali", 20, "A12")
assistant = Assistant("Sajad", 25, "A12", "A79")

human.speak()
student.speak()
student.study("Math")
assistant.speak()
assistant.study("Computer Science")
assistant.assist_professor("grading papers")
