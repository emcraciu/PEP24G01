from modul4.app2 import medie


nume = input('Introdueti numele elevului:')
note = input('Introduceti notele elevului separate prin virgula:')
# print(note.split(','))

grades = []
for number in note.split(','):
    try:
        grades.append(float(number))
    except ValueError:
        print(f'{number} is not a grade')

assert grades, 'No grades were provided'
print(grades)

if medie(grades) < 5:
    print(f'{nume} failed the class')
else:
    print(f'{nume} passed the class')