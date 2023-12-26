from user import User

class Student(User):
    # def __init__(self, first_name, last_name):
    #     super().__init__(first_name, last_name)
        self.knowledge = []  # Initializing self.knowledge as an empty list for each student

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)  # Adding the new knowledge (string) to the self.knowledge list
