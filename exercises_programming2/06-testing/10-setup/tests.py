from calendars import *
from tasks import *
import pytest
from datetime import date, timedelta

def setup_function():
    global today, tomorrow, future_date, past_date, calendar, sut
    today = date(1998,5,14)
    tomorrow = today + timedelta(days=1)
    future_date = today + timedelta(days=7)
    past_date = today - timedelta(days=7)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)


def test_creation():    
    # assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_task_becomes_overdue():
    # arrange
    task = Task('a description', tomorrow)
    sut.add_task(task)

    # act
    calendar.today = future_date

    # assert
    assert [task] == sut.overdue_tasks

def test_adding_task_with_due_day_in_future():
    # arrange
    task = Task('some description', future_date)

    # act
    sut.add_task(task)

    # assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    # arrange
    task = Task('some description', past_date)

    # act, arrange
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)

def test_task_becomes_finished():
    # arrange
    task = Task('description', tomorrow)

    # first act and assert
    sut.add_task(task)
    assert 1 == len(sut)
    assert [task] == sut.due_tasks
    assert [] == sut.finished_tasks

    # second act and assert
    task.finished = True
    assert 1 == len(sut)
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks