class Session:
    def __init__(self, term, number_of_exams):
        self.__term = 0
        self.__number_of_credits = 0
        self.__number_of_exams = 0
        self.set_term(term)
        self.set_number_of_credits()
        self.set_number_of_exams(number_of_exams)

    def get_term(self):
        return self.__term

    def get_number_of_credits(self):
        return self.__number_of_credits

    def get_number_of_exams(self):
        return self.__number_of_exams

    def set_term(self, term):
        if term >= 1 and term <= 8:
            self.__term = term
        else:
            self.__term = 1
        self.set_number_of_credits()

    def set_number_of_credits(self):
        if self.__term == 3 or self.__term == 7:
            self.__number_of_credits = 3
        elif self.__term == 5 or self.__term == 6:
            self.__number_of_credits = 4
        else:
            self.__number_of_credits = 5

    def set_number_of_exams(self, number_of_exams):
        if number_of_exams > 4:
            self.__number_of_exams = 4
        else:
            self.__number_of_exams = number_of_exams

    def get_all(self):
        return str(self.__term) + " " + str(self.__number_of_credits) + " " + str(self.__number_of_exams) + " "



session1 = Session(1, 3)
session2 = Session(5, 7)
print(session1.get_all())
print(session2.get_all())
