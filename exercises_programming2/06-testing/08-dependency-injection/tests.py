from calendars import *
from tasks import *
import pytest
from datetime import date, timedelta

def test_task_becomes_overdue():
    tasks = TaskList(Calendar()) #tasklist with accurate today's date
    tomorrow = date.today() + timedelta(days=2)
    task = Task('something', tomorrow) #task due to tomorrow
    tasks.add_task(task)

    five_days_from_now = date.today() + timedelta(days=5)
    tasks.calendar = CalendarStub(five_days_from_now) #put tasklist object into the future

    assert [task] == tasks.overdue_tasks