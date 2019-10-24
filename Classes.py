from decimal import Decimal


class Teacher:
    index = 0

    def __init__(self, name, courses, schedule, seniority):
        self.index = Teacher.index
        self.name = name
        self.courses = courses
        self.schedule = schedule
        self.seniority = seniority
        Teacher.index = Teacher.index + 1


class Course:
    index = 0

    def __init__(self, name, credits, year, hoursPerWeek):
        self.index = Course.index
        self.name = name
        self.credits = credits
        self.year = int(year)
        self.hoursPerWeek = float(hoursPerWeek)
        Course.index = Course.index + 1

