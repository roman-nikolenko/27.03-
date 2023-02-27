import sqlite3
con = sqlite3.connect('school.sqlite')
cur = con.cursor()

que_create = '''
CREATE TABLE IF NOT EXISTS class(
    id INTEGER PRIMARY KEY,
    name TEXT, 
    surname TEXT, 
    mark INTEGER
)
'''

cur.execute(que_create)
con.commit()

con.close()

----------------------------------------------- 1

import sqlite3

con = sqlite3.connect('school.sqlite')
cur = con.cursor()

que_insert = '''
INSERT INTO class (name, surname, mark) 
VALUES
    ('Василийй', 'Пупкин', 3),
    ('Денис', 'Синицин', 4),
    ('Ангелина', 'Соколова', 5),
    ('Саша', 'Петров', 2)
'''
cur.execute(que_insert)
con.commit()
con.close()
------------------------------------------------- 2

import sqlite3
from random import choice
con = sqlite3.connect('school.sqlite')
cur = con.cursor()
que_insert = '''INSERT INTO class (name, surname, mark) VALUES
    ('{}', '{}', {})
'''
pool_name = ('Василий', 'Денис', 'Костя', 'Саша')
pool_surname = ('Синицын', 'Соколов', 'Петров', 'Крылов')
pool_nums = tuple(range(2, 6))
for i in range(5):
    name_insert = choice(pool_name)
    surname_insert = choice(pool_surname)
    nums_insert = choice(pool_nums)
    cur.execute((que_insert.format(name_insert, surname_insert, nums_insert)))
con.commit()
con.close()

--------------------------------------------------------- 3
