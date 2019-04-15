## Many-to-Many Relationships and Python
1.How do we model a many-to-many relationship between two database tables?  
Answer: We add a table with two foreign keys  

2.In Python, what is a database "cursor" most like?
Answer: A file handle

3.What method do you call in an SQLIte cursor object in Python to run an SQL command?
Answer: execute()

4.In the following SQL,
```html
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
```
what is the purpose of the "?"?
Answer: It is a placeholder for the contents of the "org" variable

5.In the following Python code sequence (assuming cur is a SQLite cursor object),
```html
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
row = cur.fetchone()
```
Answer: None

6.What does the LIMIT clause in the following SQL accomplish?  
```html
SELECT org, count FROM Counts
   ORDER BY count DESC LIMIT 10
```
Answer: It only retrieves the first 10 rows from the table

7.What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?
Answer: It allows multiple SQL statements separated by semicolons

8.What is the purpose of "OR IGNORE" in the following SQL:  
```html
INSERT OR IGNORE INTO Course (title) VALUES ( ? )
```
Answer: It makes sure that if a particular title is already in the table, there are no duplicate rows inserted

9.What do we generally avoid in a many-to-many junction table?
Answer: An AUTOINCREMENT primary key column and A logical key

10.For the following Python code to work, what must be added to the title column in the CREATE TABLE statement for the Course table:
```html
cur.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES ( ? )''', ( title, ) )
cur.execute('SELECT id FROM Course WHERE title = ? ',
    (title, ))
course_id = cur.fetchone()[0]
```
Answer: A UNIQUE constraint
