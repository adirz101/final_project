import xlrd
import Classes
import copy


def ret_courses_from_sheet_one():
    result_data = []
    file_name = 'Workbook1.xlsx'
    workbook = xlrd.open_workbook(file_name)
    for sheet in workbook.sheets():
        if sheet.name != 'courses':
            break
        num_rows = sheet.nrows  # Number of Rows
        num_cols = sheet.ncols  # Number of Columns
        for curr_row in range(0, num_rows):
            row_data = []
            for curr_col in range(0, num_cols):
                data = sheet.cell_value(curr_row, curr_col)  # Read the data in the current cell
                row_data.append(data)
            result_data.append(row_data)

    return parse_courses_names(result_data)


def ret_teachers_list(Courses):
    result_data = []
    file_name = 'Workbook1.xlsx'
    workbook = xlrd.open_workbook(file_name)
    for sheet in workbook.sheets():
        if sheet.name == 'courses':
            continue
        schedule = ret_schedule_of_teacher(sheet)
        courses_str = ret_all_courses_by_teacher(sheet)
        t_courses = find_courses_obj_by_str(Courses, courses_str)
        seniority = int(sheet.cell_value(1, 6))
        result_data.append(Classes.Teacher(sheet.name,t_courses,schedule,seniority))
    return result_data


def ret_schedule_of_teacher(sheet):
    result = []
    num_rows = 10  # Number of Rows
    num_cols = 5  # Number of Columns
    for curr_col in range(0, num_cols):
        for curr_rows in range(0, num_rows):
            data = sheet.cell_value(curr_rows, curr_col)  # Read the data in the current cell
            result.append((int)(data))
    return result


def ret_all_courses_by_teacher(sheet):
    course_by_t = []
    num_rows = sheet.nrows
    col = 5
    for i in range(0,num_rows):
        data = sheet.cell_value(i, col)
        if data == "" :
            break
        course_by_t.append(data)
    return course_by_t


def parse_courses_names(list):
    courses = []
    for course in list:
        name = str(course[0]).strip("'")
        credits = str(course[1]).strip("'")
        year = str(int(course[2])).strip("'")
        hoursPerWeek = credits
        courses.append(Classes.Course(name, credits, year, hoursPerWeek))
    return courses


def find_courses_obj_by_str(Courses, c_name):
    c = []
    for i in c_name:
        for j in Courses:
            if i == j.name:
                c.append(copy.copy(j))
                break
    return c

def ret_total_hours(Course):
    total = 0
    for i in Course:
        total = total + i.hoursPerWeek
    return total