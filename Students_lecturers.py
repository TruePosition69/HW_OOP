class Student:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      self.grades_avg = 1

  def rate_lecturer(self, student, mark, course, lecturer):
      if isinstance(lecturer,Lecturer) and isinstance(student, Student) and \
              course in student.courses_in_progress and \
              course in lecturer.courses_attached and \
              (1 <= mark <= 10):
          if course in lecturer.marks:
              lecturer.marks[course] += [mark]
          else:
              lecturer.marks[course] = [mark]
      else:
          return 'Ошибка'

  def average(self):
      all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
      if all_grades:
          avg_grade = sum(all_grades) / len (all_grades)
          return avg_grade
      else:
          return 0

  def get_courses_in_progress(self):
      delimiter = ', '
      courses_in_progress_str = delimiter.join(self.courses_in_progress)
      return courses_in_progress_str

  def get_finished_courses(self):
      return ', '.join(self.finished_courses)

  def __str__(self) -> str:
      return f'Имя: {self.name}\
             \nФамилия: {self.surname}\
             \nСредняя оценка за домашние задания: {self.average():.1f}\
             \nКурсы в процессе изучения: {self.get_courses_in_progress()}\
             \nЗавершенные курсы: {self.get_finished_courses()}'

  def __gt__(self, other_student):
      return self.average() > other_student.average()

  def __lt__(self, other_student):
      return self.average() < other_student.average()

  def __eq__(self, other_student):
      return self.average() == other_student.average()

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

  def __str__(self) -> str:
      return f'Имя: {self.name}\
             \nФамилия: {self.surname}'

class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.marks = {}

  def average(self):
      marks_list = [mark for self.marks in self.marks.values() for mark in self.marks]
      self.marks_avg = sum(marks_list) / len(marks_list)
      return self.marks_avg

  def __str__(self) -> str:
      return f'Имя: {self.name}\
             \nФамилия: {self.surname}\
             \nСредняя оценка за лекции: {round(self.marks_avg,1)}'
  
  def __gt__(self, other_lecturers):
      return self.average() > other_lecturers.average()

  def __lt__(self, other_lecturers):
      return self.average() < other_lecturers.average()

  def __eq__(self, other_lecturers):
      return self.average() == other_lecturers.average()

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and \
            course in self.courses_attached and \
            course in student.courses_in_progress and \
            (1 <= grade <= 10):
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self) -> str:
      return f'Имя: {self.name}\
             \nФамилия: {self.surname}'
  
student1 = Student('Some', 'Buddy')
student1.finished_courses = ['Введение в программирование']
student1.courses_in_progress = ['Python', 'Git']
student1.grades = {'Python' : [10, 9, 8, 7], 'Git' : [10, 9]}

student2 = Student('Some_2', 'Buddy_2')
student2.finished_courses = ['Введение в программирование']
student2.courses_in_progress = ['Python', 'Git']
student2.grades = {'Python' : [10, 9, 8, 7], 'Git' : [10, 9]}

def avg_grade_by_course(students, course_name):
    total_grade = 0
    num_students = 0
    for student in students:
        if course_name in student.courses_in_progress or course_name in student.finished_courses:
            total_grade += student.grades[course_name]
            num_students += 1
    if num_students == 0:
        return 0
    return total_grade / num_students

def avg_marks_by_lecterer(lecturers, course_name):
    total_grade = 0
    num_lecturers = 0
    for lecterer in lecturers:
        if course_name in lecterer.courses_in_progress or course_name in lecterer.finished_courses:
            total_grade += lecterer.marks[course_name]
            num_lecturers += 1
    if num_lecturers == 0:
        return 0
    return total_grade / num_lecturers

print(student2)