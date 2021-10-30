from datetime import date


class Student:

    def __init__(self):
        self.__name = None
        self.__student_id = None
        self.__surname = None
        self.__patronymic = None
        self.__adress = None
        self.__telephone_number = None
        self.__faculty = None
        self.__birthday = None

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print('incorrect Name')

    def get_name(self):
        return self.__name

    def set_student_id(self, student_id):
        if isinstance(student_id, int) and student_id >= 0:
            self.__student_id = student_id
        else:
            print('incorrect student_id')

    def get_student_id(self):
        return self.__student_id

    def set_surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            print('incorrect surname')

    def get_surname(self):
        return self.__surname

    def set_patronymic(self, patronymic):
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            print('incorrect patronymic')

    def get_patronymic(self):
        return self.__patronymic

    def set_adress(self, adress):
        if isinstance(adress, str):
            self.__adress = adress
        else:
            print('incorrect adress')

    def get_adress(self):
        return self.__adress

    def set_telephone_number(self, telephone_number):
        if isinstance(telephone_number, int) and telephone_number >= 0:
            self.__telephone_number = telephone_number
        else:
            print('incorrect telephone_number')

    def get_telephone_number(self):
        return self.__telephone_number

    def set_faculty(self, faculty):
        if isinstance(faculty, str):
            self.__faculty = faculty
        else:
            print('incorrect faculty')

    def get_faculty(self):
        return self.__faculty

    def set_birthday(self, year, month, day):
        if isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
            self.__birthday = date(year, month, day)

    def get_birthday(self):
        return self.__birthday

    def get_age(self):
        now = date.today()

        if self.__birthday is None:
            print('student birthday was not set')
            return

        age = now.year - self.__birthday.year
        if now.month < self.__birthday.month:
            age -= 1
        elif now.month == self.__birthday.month:
            if now.day < self.__birthday.day:
                age -= 1
        return age


s1 = Student()
s1.set_name('Vlad')
s1.set_student_id(66)
s1.set_surname('Novik')
s1.set_patronymic('Viktorovich')
s1.set_adress('Minsk')
s1.set_faculty('ftug')
s1.set_birthday(1991, 12, 19)
print(s1.get_age())
