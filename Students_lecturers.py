class Student:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

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

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.marks = {}

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