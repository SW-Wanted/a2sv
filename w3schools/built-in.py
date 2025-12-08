numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f'doubled\t\t-> {doubled}')

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f'odd_numbers\t-> {odd_numbers}')

students = [("Emanuel", 25), ("Carneiro", 22), ("Santos", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(f'sorted_students\t-> {sorted_students}')