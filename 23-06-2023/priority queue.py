'''append elements(key,value),
key:priority
value:element in queue
and sort the list every time an element is appended.'''
students_grade=[]
students_grade.append((1,"rakesh"))
students_grade.append((4,"valli"))
students_grade.sort(reverse=True)
print("yes")
print(students_grade)
students_grade.append((3,"jeevana"))
students_grade.sort(reverse=True)
students_grade.append((2,"nandhini"))
students_grade.sort(reverse=True)
print("priority wise sorted")
print(students_grade)
print("original queue")
while students_grade:
    print(students_grade.pop())
