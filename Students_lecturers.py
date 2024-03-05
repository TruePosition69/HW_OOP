class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, student, mark, course, lecturer):
        if isinstance(lecturer,Lecturer) and isinstance(student, Student) and course in student.courses_in_progress and course in lecturer.courses_attached and (1 <= mark <= 10):
            if course in lecturer.marks:
                lecturer.marks[course] += [mark]
            else:
                lecturer.marks[course] = [mark]
        else:
            return 'Ошибка'
        
    def average(self):
        grades_list = list(self.grades.values())
        self.grades_avg = sum(grades_list) / len(grades_list)

    def courses_in_prgrs(self):
        delimiter = ','
        courses_in_progress_str = delimiter.join(self.courses_in_progress)
        return courses_in_progress_str
    
    def finished_courses(self):
        delimiter = ','
        finished_courses_str = delimiter.join(self.finished_courses)
        return finished_courses_str

    def __str__(self) -> str:
        return f'Имя: {self.name}\
               \nФамилия: {self.surname}\
               \nСредняя оценка за домашние задания: {round(self.grades_avg,1)}\
               \nКурсы в процессе изучения: {self.courses_in_prgrs}\
               \nЗавершенные курсы: {self.finished_courses}'
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self) -> str:
        return f'Имя: {self.name}\
               \nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self):
        self.marks = {}

    def average(self):
        self.marks_list = list(self.marks.values())
        self.sum_marks = sum(self.marks_list)
        self.marks_avg = self.sum_marks/len(self.marks_list)

    def __str__(self) -> str:
        return f'Имя: {self.name}\
               \nФамилия: {self.surname}\
               \nСредняя оценка за лекции: {round(self.marks_avg,1)}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and (1 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self) -> str:
        return f'Имя: {self.name}\
               \nФамилия: {self.surname}'