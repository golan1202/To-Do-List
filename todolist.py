from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import calendar

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Nothing to do!')
    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task


class DB:
    def __init__(self):
        self.engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)


class TodoApp:
    def __init__(self):
        self.db = DB()
        self.session = self.db.Session()

    def menu(self):
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")

    def todays_tasks(self):
        today = datetime.today().date()
        print(f"{calendar.day_name[today.weekday()]} {today.day} {today.strftime('%b')}")
        to_do_list = self.session.query(Table).filter(today == Table.deadline).order_by(Table.deadline).all()
        if len(to_do_list) != 0:
            for count, item in enumerate(to_do_list, 1):
                print(f"{count}) {item.task}")
        else:
            print("Nothing to do!")

    def weeks_tasks(self):
        today = datetime.today().date()
        for i in range(7):
            to_do_list = self.session.query(Table).filter(today == Table.deadline).order_by(Table.deadline).all()
            print(f"{calendar.day_name[today.weekday()]} {today.day} {today.strftime('%b')}")
            if len(to_do_list) != 0:
                for count, item in enumerate(to_do_list, 1):
                    print(f"{count}) {item.task}\n")
            else:
                print("Nothing to do!\n")
            today += timedelta(days=1)

    def all_tasks(self):
        print("All tasks:")
        to_do_list = self.session.query(Table).order_by(Table.deadline).all()
        if len(to_do_list) != 0:
            for count, item in enumerate(to_do_list, 1):
                print(f"{count}) {item.task}. {item.deadline.day} {item.deadline.strftime('%b')}")
        else:
            print("Nothing to do!")

    def add_task(self):
        my_task = input("Enter task\n")
        my_deadline = list(map(int, input("Enter deadline\n").split("-")))
        my_deadline = datetime(my_deadline[0], my_deadline[1], my_deadline[2]).date()
        new_row = Table(task=my_task, deadline=my_deadline)
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!")

    def missed_tasks(self):
        print("Missed tasks:")
        to_do_list_past = self.session.query(Table).filter(Table.deadline < datetime.today().date()).all()
        if len(to_do_list_past) != 0:
            for count, item in enumerate(to_do_list_past, 1):
                print(f"{count}) {item.task}. {item.deadline.day} {item.deadline.strftime('%b')}")
        else:
            print("Nothing to do!")

    def delete_tasks(self):
        print("Choose the number of the task you want to delete:")
        self.all_tasks()
        delete_task = int(input()) - 1
        to_do_list = self.session.query(Table).order_by(Table.deadline).all()
        if len(to_do_list) != 0 and delete_task in range(0, len(to_do_list)):
            self.session.delete(to_do_list[delete_task])
            self.session.commit()
        else:
            print('Nothing to delete')

    def run(self):
        while True:
            self.menu()
            choice = int(input())
            if choice == 0:
                print("Bye!")
                break
            elif choice == 1:
                self.todays_tasks()
            elif choice == 2:
                self.weeks_tasks()
            elif choice == 3:
                self.all_tasks()
            elif choice == 4:
                self.missed_tasks()
            elif choice == 5:
                self.add_task()
            elif choice == 6:
                self.delete_tasks()
            print()


app = TodoApp()
app.run()