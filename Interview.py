from psycopg2 import Error
import psycopg2
import re  # import regular expression module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# create a list for the baby names
mylist = []
# iterate line by line in the file
for line in open('python_class_question.html', 'rt'):
    line = line.strip()  # eliminate whitespaces
    # implement regex findall
    # print(line)
    xi = re.findall(r'<td>(.+)</td>', line)
    # print(xi)
    if len(xi) > 0:
        # print(xi)
        list0 = xi[0].split(', ')
        mylist.append(list0)  # append concatenated names to the list

# print(mylist[1])
an_list = []
for i in range(len(mylist)):
    if i % 2 != 0:
        for j in mylist[i]:
            an_list.append(j)

df = pd.DataFrame(an_list, columns=['Colors'])
# print(df.head())
unik = df.Colors.unique()
# print(unik)
each = [an_list.count(i) for i in unik]
# print(each)
for_crud = list(zip(unik, each))
print(for_crud)
df2 = pd.DataFrame({'Colors': unik, 'Count': each})
# print(df2)
total = df2.Count.sum()
red_count = int(df2[df2.Colors == 'RED'].Count.values)
red_prob = red_count/total
print('The Probability that the color is red is {}'.format(round(red_prob, 3)))

# Number 1: The mean color of shirts cannot be interpreted as 'Color' is a nominal categorical feature
# Number 2: The blue color, with a frequency of 30(+1, given BLEW == BLUE), is mostly worn throughout the week
# Number 3: The median color cannot be interpreted
# Number 4: The variance cannot be easily interpreted as well
# Number 5: The Probability that the color is red is 0.095

print('Number 1: The mean color of shirts cannot be interpreted as "Color" is a nominal categorical feature')
print('Number 2: The blue color, with a frequency of 30(+1, given BLEW == BLUE), is mostly worn throughout the week')
print('The median color cannot be interpreted')
print('The variance cannot be easily interpreted as well')
print('The Probability that the color is red is 0.095')

# Number 6


try:
    conn = psycopg2.connect(
        user='postgres',
        password='Akokite1',
        host='127.0.0.1',
        port=5432,
        database='ToDoList'
    )

    cursor = conn.cursor()

    my_query = '''CREATE TABLE Colors (
        Color varchar(100) NOT NULL,
        Frequency integer);'''

    cursor.execute(my_query)
    conn.commit()
    print('New Table successfully created!')
except (Exception, Error) as error:
    print('Error while connecting to PostgreSQL', error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print('PostgreSQL operation closed!')


def bulk_insert(list_of_tuples):
    try:
        conn = psycopg2.connect(
            user='postgres',
            password='Akokite1',
            host='127.0.0.1',
            port=5432,
            database='ToDoList'
        )

        cursor = conn.cursor()

        insertion_query = '''INSERT INTO Colors (Color, Frequency)
                            VALUES (%s, %s);
                            '''

        cursor.executemany(insertion_query, list_of_tuples)
        conn.commit()
        print(cursor.rowcount, 'records inserted successfully into table')

        # Fetch results
        cursor.execute("SELECT * FROM Colors")
        record = cursor.fetchall()
        print('Result: \n', record)
    except (Exception, Error) as error:
        print('Error while connecting to PostgreSQL', error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print('PostgreSQL operation closed!')


bulk_insert(for_crud)

# Number 7 program


def recSearch(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recSearch(arr, l+1, r-1, x)


arr = [12, 34, 54, 2, 3]
n = len(arr)
x = 3
index = recSearch(arr, 0, n-1, x)
if index != -1:
    print('Element', x, 'is present at index', index)
else:
    print('Element', x, 'is not present')

# Number 8 program


def bin4_to_dec():
    import random

    mine = ''
    for i in range(4):
        n = random.randint(0, 1)
        mine += str(n)
    return int(mine, 2)


print(bin4_to_dec())

# Number 9 program


def sum_first_fib(n):
    """A Function  thhat somes the first n terms of a fibonacci sequence, starting from 1"""
    a, b, counter = 0, 1, 0
    summer = 0
    while True:
        if counter > n-1:
            break
        a, b = b, a + b
        summer += a
        counter += 1
    return summer


print(sum_first_fib(5))
