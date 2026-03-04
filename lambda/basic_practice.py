#map() function

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = list(map(lambda x: x * 2, nums))
print(doubled)

#filter() function
words = ['hi', 'hello', 'sun', 'amazing', 'cat']

long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)

#sorting with lambda
students = [('Alice', 88), ('Bob', 72), ('Charlie', 95)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)