class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def add_finished_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avrg_rate(self):
        if len(self.grades) > 0:
            sum_rate = 0
            for course in self.grades:
                sum_rate += sum(self.grades[course]) / len(self.grades[course])
            return round(sum_rate / len(self.grades), 2)
        return 0

    def __str__(self):
        res_0 = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        if self._avrg_rate():
            res_1 = f'Средняя оценка за домашкие задания: {self._avrg_rate()}\n'
        else:
            res_1 = 'Нет оценок\n'
        res_2 = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res_0 + res_1 + res_2

    def __lt__(self, other):
        return self._avrg_rate() < other._avrg_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course_attached(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}

    def _avrg_rate(self):
        if len(self.lectures_grades) > 0:
            sum_rate = 0
            for course in self.lectures_grades:
                sum_rate += sum(self.lectures_grades[course]) / len(self.lectures_grades[course])
            return round(sum_rate / len(self.lectures_grades), 2)
        return 0

    def __str__(self):
        res_0 = f'Имя: {self.name}\nФамилия: {self.surname}'
        if self._avrg_rate():
            res_1 = f'\nСредняя оценка за лекции: {self._avrg_rate()}'
        else:
            res_1 = 'Нет оценок за лекции'
        return res_0 + res_1

    def __lt__(self, other):
        return self._avrg_rate() < other._avrg_rate()


class Rewiever(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('John', 'Daw', 'm')
student_2 = Student('Jake', 'Morris', 'm')

lecturer_1 = Lecturer('Hank', 'Mose')
lecturer_2 = Lecturer('Eva', 'Holmes')

rewiever_1 = Rewiever('Frank', 'Osborne')
rewiever_2 = Rewiever('Chloe', 'Grimes')

student_1.add_course_in_progress('Python')
student_1.add_course_in_progress('JavaScript')
student_1.add_finished_course('HTML')
student_1.add_finished_course('Git')

student_2.add_course_in_progress('Python')
student_2.add_course_in_progress('Git')
student_2.add_finished_course('JavaScript')

lecturer_1.add_course_attached('Python')
lecturer_1.add_course_attached('JavaScript')

lecturer_2.add_course_attached('Python')
lecturer_2.add_course_attached('Git')

rewiever_1.add_course_attached('Python')
rewiever_1.add_course_attached('JavaScript')
rewiever_1.add_course_attached('Git')
rewiever_2.add_course_attached('Python')
rewiever_2.add_course_attached('JavaScript')

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'JavaScript', 6)
student_1.rate_lecture(lecturer_1, 'JavaScript', 10)
student_1.rate_lecture(lecturer_2, 'Python', 6)
student_1.rate_lecture(lecturer_2, 'Python', 8)

student_2.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_1, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'Git', 10)

rewiever_1.rate_hw(student_1, 'Python', 10)
rewiever_1.rate_hw(student_1, 'Python', 9)
rewiever_1.rate_hw(student_1, 'Python', 5)
rewiever_1.rate_hw(student_1, 'JavaScript', 6)
rewiever_1.rate_hw(student_1, 'Python', 10)
rewiever_2.rate_hw(student_1, 'Python', 9)
rewiever_2.rate_hw(student_1, 'Python', 9)

rewiever_1.rate_hw(student_2, 'Git', 10)
rewiever_1.rate_hw(student_2, 'Python', 7)
rewiever_2.rate_hw(student_2, 'Python', 6)
rewiever_2.rate_hw(student_2, 'Python', 10)

print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(rewiever_1)
print()
print(rewiever_2)
print()
print(student_1 < student_2)
print(lecturer_1 > lecturer_2)
