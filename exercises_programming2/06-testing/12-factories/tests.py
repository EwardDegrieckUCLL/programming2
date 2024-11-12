from calendars import *
from tasks import *
import pytest
from datetime import date, timedelta

def create_today_date():
    return date(1998,5,14)

def create_tomorrow():
    return create_today_date() + timedelta(days=1)

def create_future_date():
    return create_today_date() + timedelta(days=7)

def create_past_date():
    return create_today_date() - timedelta(days=7)

def create_calendar(*, date=None):
    date = date or create_today_date()
    return CalendarStub(date)

def create_task(*, description='some description', due_date=None, finished=False):
    due_date = due_date or create_tomorrow()
    task = Task(description, due_date)
    if finished:
        task.finished = True
    return task

def create_tasklist(*, calendar=None):
    calendar = calendar or create_calendar()
    return TaskList(calendar)

def test_creation():    
    # arrange
    sut = create_tasklist()
    
    # assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_task_becomes_overdue():
    # arrange
    task = create_task(due_date=create_tomorrow())
    calendar = create_calendar()
    sut = create_tasklist(calendar=calendar)
    sut.add_task(task)

    # act
    calendar.today = create_future_date()

    # assert
    assert [task] == sut.overdue_tasks

def test_adding_task_with_due_day_in_future():
    # arrange
    task = create_task(due_date=create_future_date())
    sut = create_tasklist()

    # act
    sut.add_task(task)

    # assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    # arrange
    task = create_task(due_date=create_past_date())
    sut = create_tasklist()

    # act, arrange
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)

def test_task_becomes_finished():
    # arrange
    task = create_task(due_date=create_tomorrow())
    sut = create_tasklist()

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

# it is overkill to use ALL these factory functions, but it was the exercise