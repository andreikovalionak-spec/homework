
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.2f}")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
            course in self.courses_attached and
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
            return None
        return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
            1 <= grade <= 10 and
            course in self.courses_in_progress and
            course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
            return None
        return 'Ошибка'

    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count > 0 else 0


    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.2f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

def average_student_grade_by_course(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grades / total_count if total_count > 0 else 0

def average_lecturer_grade_by_course(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return total_grades / total_count if total_count > 0 else 0

  # Задание №1
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True
print(lecturer.courses_attached)     # []
print(reviewer.courses_attached)    # []

    #Задание №2
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# Тесты
print(student.rate_lecture(lecturer, 'Python', 7))   
print(student.rate_lecture(lecturer, 'Java', 8))     
print(student.rate_lecture(lecturer, 'C++', 8))    
print(student.rate_lecture(reviewer, 'Python', 6))  

print(lecturer.grades)  # {'Python': [7]}

   # Задание №3
lecturer = Lecturer('Some', 'Buddy')
reviewer = Reviewer('Some', 'Buddy')
student = Student('Ruoy', 'Eman', 'М')

# Настройка данных для демонстрации
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
student.grades = {'Python': [9, 10, 10], 'Git': [9, 9]}

lecturer.courses_attached += ['Python']
lecturer.grades = {'Python': [9, 10, 10]}
print(lecturer)
print(reviewer)
print(student)


    #Задание№4
# Создаём по 2 экземпляра каждого класса
student1 = Student('Надежда', 'Юрьева', 'Ж')
student2 = Student('Андрей', 'Сидоров', 'М')

lecturer1 = Lecturer('Алексей', 'Смирнов')
lecturer2 = Lecturer('Мария', 'Кречетова')

reviewer1 = Reviewer('Евгений', 'Коваленок')
reviewer2 = Reviewer('Ирина ', 'Вчерашнева')
    # Курсы
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']


student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Основы алгоритмов']

lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Java', 'Python']

reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['Java', 'Python']

# Вызов всех методов
print(" ВЫСТАВЛЕНИЕ ОЦЕНОК ")
print(reviewer1.rate_hw(student1, 'Python', 8))  
print(reviewer1.rate_hw(student1, 'Git', 6))     
print(reviewer1.rate_hw(student2, 'Python', 7))   
print(reviewer2.rate_hw(student2, 'Java', 9))    
print(reviewer1.rate_hw(student1, 'Java', 5))    

print(" ОЦЕНКИ ЗА ЛЕКЦИИ ")
print(student1.rate_lecture(lecturer1, 'Python', 19))  
print(student1.rate_lecture(lecturer1, 'Git', 9))       
print(student2.rate_lecture(lecturer2, 'Python', 8))  
print(student2.rate_lecture(lecturer2, 'Java', 7))      
print(student1.rate_lecture(lecturer2, 'C++', 7))       

print(" ИНФОРМАЦИЯ ОБ ОБЪЕКТАХ ")
print(" Студент 1 ")
print(student1)
print(" Студент 2 ")
print(student2)
print(" Лектор 1 ")
print(lecturer1)
print(" Лектор 2 ")
print(lecturer2)
print(" Ревьюер 1 ")
print(reviewer1)
print(" Ревьюер 2 ")
print(reviewer2)

print("СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ")
# Для студентов
python_avg_students = average_student_grade_by_course([student1, student2], 'Python')
git_avg_students = average_student_grade_by_course([student1], 'Git')
java_avg_students = average_student_grade_by_course([student2], 'Java')


print(f"Средняя оценка студентов по курсу Python: {python_avg_students:.2f}")
print(f"Средняя оценка студентов по курсу Git: {git_avg_students:.2f}")
print(f"Средняя оценка студентов по курсу Java: {java_avg_students:.2f}")

# Для лекторов
python_avg_lecturers = average_lecturer_grade_by_course([lecturer1, lecturer2], 'Python')
git_avg_lecturers = average_lecturer_grade_by_course([lecturer1], 'Git')
java_avg_lecturers = average_lecturer_grade_by_course([lecturer2], 'Java')

print(f"Средняя оценка лекторов по курсу Python: {python_avg_lecturers:.2f}")
print(f"Средняя оценка лекторов по курсу Git: {git_avg_lecturers:.2f}")
print(f"Средняя оценка лекторов по курсу Java: {java_avg_lecturers:.2f}")
