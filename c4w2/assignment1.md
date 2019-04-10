# Our First Database
## Instructions
If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":
```html
CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
```
Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:
```html
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Thais', 19);
INSERT INTO Ages (name, age) VALUES ('Rodrigo', 23);
INSERT INTO Ages (name, age) VALUES ('Rhianna', 14);
INSERT INTO Ages (name, age) VALUES ('Elisha', 15);
```
Once the inserts are done, run the following SQL command:
```html
SELECT hex(name || age) AS X FROM Ages ORDER BY X
```
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.  

Note: This assignment must be done using SQLite - in particular, the SELECT query above will not work in any other database. So you cannot use MySQL or Oracle for this assignment.
