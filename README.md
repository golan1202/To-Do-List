# To-Do-List
To-Do list that will help you manage your tasks. You will practice using loops, conditions and statement branches.
And also you will learn the basics of SQLAlchemy to manage SQLite database on python! This project is a part of the following track.

## Work on project. Stage 1/4: Plan it
#### Objectives
To begin with, develop a simple list of 4 tasks. Your program must print exactly the same list as given in the example.

#### Example
**Output:**
```Today:
1) Do yoga
2) Make breakfast
3) Learn basics of SQL
4) Learn what is ORM 
```
## Work on project. Stage 2/4: I am an Alchemist!
#### Objectives
Let's store the data about our tasks in the database. Here's what you need to do:

- Create a database file. Its name should be ```todo.db```.
- Create a table in this database. The table name should be ```task```.
The table ```task``` should have the following columns:

- Integer column named ```id```. It should be the ```primary key```.
- String column named ```task```.
- Date column named ```deadline```. It should have the date when the task was created by default. You can use ```datetime.today``` method.
Also, you need to implement a menu that will make your program more convenient. The menu should have the following items:

**Today's tasks**. Prints all tasks for today.
**Add task**. Asks for task description and saves it in the database.
**Exit**.

## Work on project. Stage 3/4: Deadlines are scary
#### Objectives
Add the following items to your menu:

- **Week's tasks**: prints all tasks for 7 days from today.
- **All tasks**: prints all tasks sorted by deadline.
Now **Add task** item should ask for the deadline of the task. Users should input the deadline in this format: **YYYY-MM-DD**.

Also, **Today's tasks** item should print today's date.

See the format of the output in the example.

## Work on project. Stage 4/4: Bye, completed tasks
#### Objectives

Add the following items into your menu:

- **Missed tasks**: prints all tasks whose deadline was missed, that is, tasks whose deadline date is earlier than today's date.
- **Delete task**: deletes the chosen task. Print 'Nothing to delete' if the tasks list is empty.
**Missed tasks** should print the tasks ordered by the deadline date.

**Delete task** should print all the tasks sorted by the deadline date and ask to enter the number of the task to delete.

See in the example what your program should look like.
