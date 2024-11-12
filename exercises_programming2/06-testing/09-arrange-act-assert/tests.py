from calendars import *
from tasks import *
import pytest
from datetime import date, timedelta

def test_task_becomes_overdue():
    # arrange
    today = date(2005,5,14)
    tomorrow = date(2005,5,15)
    next_week = date(2005,5,21)
    calendar = CalendarStub(today)
    task = Task('a description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # act
    calendar.today = next_week

    # assert
    assert [task] == sut.overdue_tasks

def test_creation():
    # arrange
    today = date(2015,12,16)
    calendar = CalendarStub(today)
    
    # act
    sut = TaskList(calendar)

    # assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_day_in_future():
    # arrange
    today_calendar = CalendarStub(date(2015,12,16))
    sut = TaskList(today_calendar)
    future_date = date(2015,12,18)
    task = Task('some description', future_date)

    # act
    sut.add_task(task)

    # assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    # arrange
    today_calendar = CalendarStub(date(2015,12,16))
    sut = TaskList(today_calendar)
    past_date = date(2015,12,12)
    task = Task('some description', past_date)

    # act, arrange
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)

def test_task_becomes_finished():
    # arrange
    today = date(2020,3,8)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    tomorrow = today + timedelta(days=1)
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