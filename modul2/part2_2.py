# string format

# method format

my_str = "text {}"
print(my_str.format('''example'''))
my_str = "text {}"
print(my_str.format(2))
my_str = "text {1} {0} {1}"
print(my_str.format('example1', 'example2'))
my_str = "text {ex1} {ex2}"
print(my_str.format(ex1='example1', ex2='example2'))

print (80 * '#')

# formatted string
ex1 = 'example1'
ex2 = 'example2'
print(f"text2 {ex1}")
print(f"text2 {2}")
print(f"text2 {ex1} {ex2} {ex1}")