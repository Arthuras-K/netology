class Student:
    items = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.items.append(self)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_from:
                lecturer.grades_from[course] += [grade]
            else:
                lecturer.grades_from[course] = [grade]
        else:
            print('Ошибка!') 
    def _average_hw(self):
        if self.grades == {}:
            return 'Нет оценок'        
        list_grade = []
        for grade in self.grades.values():
            list_grade += grade
        return round(sum(list_grade)/len(list_grade), 2)
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за домашние задания: {self._average_hw()}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: {", ".join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    items = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from = {}
        Lecturer.items.append(self)
    def _average_rating(self):
        if self.grades_from == {}:
            return 'Нет оценок'
        list_grade = []
        for grade in self.grades_from.values():
            list_grade += grade
        return round(sum(list_grade)/len(list_grade), 2)
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за лекции: {self._average_rating()}'
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'        
        return self._average_rating() < other._average_hw()
    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self._average_rating() > other._average_hw() 

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка!') 
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'           


# Создание функций
def average_grade_hw(list_stud, course):
    all_grades = []
    for stud in list_stud:
        if course in stud.courses_in_progress: 
            all_grades += stud.grades[course]
    if all_grades == []:
        return 'На этот курс никто не записан или нет еще оценок'
    aver_grades = sum(all_grades)/len(all_grades)
    return  round(aver_grades, 2)

def average_grade_lect(list_lect, course):
    all_grades = []
    for lect in list_lect:
        if course in lect.grades_from: 
            all_grades += lect.grades_from[course]
    if all_grades == []:
        return 'Никто не ведет данный курс или еще не проставлены оценки'
    aver_grades = sum(all_grades)/len(all_grades)
    return  round(aver_grades, 2)


# Определение студентов
gr_1_1 = Student('Guido', 'van Rossum', 'man')
gr_1_1.courses_in_progress += ['Python']
gr_1_1.finished_courses += ['Музыка', 'Литература']

gr_1_2 = Student('Bjarne', 'Stroustrup', 'man')
gr_1_2.courses_in_progress += ['С++']
gr_1_2.finished_courses += ['Музыка']

gr_1_3 = Student('Brendan', 'Eich', 'man')
gr_1_3.courses_in_progress += ['JavaScript']
gr_1_3.finished_courses += ['Музыка', 'Литература']

gr_1_4 = Student('Ada', 'Lovelace', 'woman')
gr_1_4.courses_in_progress += ['Python']
gr_1_4.courses_in_progress += ['JavaScript']
gr_1_4.courses_in_progress += ['С++']
gr_1_4.finished_courses += ['Музыка', 'Литература']



# Определение учителей
lect_1 = Lecturer('Oleg', 'Bulygin')
lect_1.courses_attached += ['Python']
lect_1.courses_attached += ['С++']

lect_2 = Lecturer('Sergey', 'Dmitriev')
lect_2.courses_attached += ['JavaScript']

rev_1 = Reviewer('Mark', 'Zuckerberg')

rev_2 = Reviewer('Pavel', 'Durov')


# Выставление оценок учителям
gr_1_1.rate_lect(lect_1, 'Python', 10)
gr_1_2.rate_lect(lect_1, 'С++', 10)
gr_1_3.rate_lect(lect_2, 'JavaScript', 7)
gr_1_4.rate_lect(lect_1, 'Python', 6)
gr_1_4.rate_lect(lect_1, 'С++', 8)
gr_1_4.rate_lect(lect_2, 'JavaScript', 2)



# Выставление оценок ученикам
rev_1.rate_hw(gr_1_1, 'Python', 9)
rev_1.rate_hw(gr_1_1, 'Python', 8)
rev_1.rate_hw(gr_1_1, 'Python', 10)
rev_1.rate_hw(gr_1_1, 'Python', 10)
rev_1.rate_hw(gr_1_2, 'С++', 10)
rev_1.rate_hw(gr_1_2, 'С++', 9)
rev_1.rate_hw(gr_1_4, 'С++', 5)
rev_1.rate_hw(gr_1_4, 'С++', 9)
rev_1.rate_hw(gr_1_4, 'С++', 2)
rev_1.rate_hw(gr_1_4, 'Python', 9)
rev_1.rate_hw(gr_1_4, 'Python', 6)
rev_2.rate_hw(gr_1_3, 'JavaScript', 10)
rev_2.rate_hw(gr_1_3, 'JavaScript', 10)
rev_2.rate_hw(gr_1_3, 'JavaScript', 9)
rev_2.rate_hw(gr_1_4, 'JavaScript', 9)
rev_2.rate_hw(gr_1_4, 'JavaScript', 7)



# Вывод на экран
print('-'*50)

# Задание №3
print(rev_1, lect_1, gr_1_1, sep='\n\n')
print()
print(lect_1 > gr_1_1)
print(lect_1 < gr_1_1)
print()

# Задание №4
print('Средняя оценка всех студентов в рамках данного курса:', average_grade_hw(Student.items, 'JavaScript'))
print('Средняя оценка всех лекторов в рамках данного курса:', average_grade_lect(Lecturer.items, 'JavaScript'))

print('-'*50)