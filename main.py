import Keywords
from docplex.mp.model import Model

from decimal import Decimal

Courses = Keywords.ret_courses_from_sheet_one()
Teachers = Keywords.ret_teachers_list(Courses)

th = Keywords.ret_total_hours(Courses)
X = [(i,j,k.index) for i in range(len(Teachers)) for j in range(50) for k in Teachers[i].courses]
mdl = Model('AN')
A = mdl.binary_var_dict(X,name='A')
mdl.minimize(mdl.sum(mdl.sum(mdl.sum(A[i,j,k.index]*(int)(Teachers[i].schedule[j])*Teachers[i].seniority for k in Teachers[i].courses)for j in range(50))for i in range(len(Teachers))))
for i in range(len(Teachers)):
    for j in range(50):
        mdl.add_constraint(mdl.sum(A[i,j,k.index] for k in Teachers[i].courses)<=1)
# for i in range(len(Teachers)):
#     for j in range(50):
#         mdl.add_constraint(mdl.sum(A[i, j, k.index] for k in Teachers[i].courses) == Courses[k.index].hoursPerWeek)
# mdl.add_constraint(mdl.sum(mdl.sum(mdl.sum(A[i, j, k.index] for k in Teachers[i].courses)for j in range(50))for i in range(len(Teachers))) == Courses[k.index].hoursPerWeek)
for i in range(len(Teachers)):
    for k in Teachers[i].courses:
        print(k.name)
        mdl.add_constraint(mdl.sum(A[i, j, k.index] for j in range(50)) == Courses[k.index].hoursPerWeek)
for j in range(50):
    mdl.add_constraint(mdl.sum(mdl.sum(A[i, j, k.index] for k in Teachers[i].courses if k.year == 1)for i in range(len(Teachers))) <= 1)
    mdl.add_constraint(mdl.sum(mdl.sum(A[i, j, k.index] for k in Teachers[i].courses if k.year == 2)for i in range(len(Teachers))) <= 1)
    mdl.add_constraint(mdl.sum(mdl.sum(A[i, j, k.index] for k in Teachers[i].courses if k.year == 3)for i in range(len(Teachers))) <= 1)

for i in range(len(Teachers)):
    for d in range(5):
        for k in Teachers[i].courses:
            mdl.add_constraint(mdl.sum(A[i, (d*10+h), k.index]+A[i, (d*10+h+1), k.index] for h in range(9)) <= 2);


solution = mdl.solve(log_output=True)
sol = [a for a in X if A[a].solution_value == 1.0]
print(sol)
Keywords.createExelTableForStudents(Courses, Teachers, sol)
Keywords.createExelTableForteachers(Courses, Teachers, sol)