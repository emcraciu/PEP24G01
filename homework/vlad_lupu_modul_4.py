# 1.
def calculate_x_and_y():
    for i in range(10, 20):
        y = 3 * i
        x = (3 * (i ** 2)) - (4 * y) + 4
        print(f"""============= X = {i} ==================
Rezultatul functiei: {x}""")


print(calculate_x_and_y())

# 2.
num_of_books = int(input("How many books do you want to add in your library? "))
library = []
keys = ("name", "author", "year")

for i in range(num_of_books):
    book_info = {}
    print(f"===== Book {i + 1} =====")

    for key in keys:
        book_info[key] = input(f"What is the {key} of the book? ")

    library.append(book_info)

print("Your books are: ")
for book in library:
    print(book)

# 3.
input_year = int(input("Type a publication year: "))

for book in library:
    if input_year < int(book["year"]):
        print(f"{book["name"]} was published after the {input_year}.")
