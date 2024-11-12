from calendars import *
from tasks import *
import pytest
from datetime import date, timedelta

@pytest.fixture
def today():
    return date(1998,5,14)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def future_date(today):
    return today + timedelta(days=7)

@pytest.fixture
def past_date(today):
    return today - timedelta(days=7)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)

def test_creation(sut):    
    # assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_task_becomes_overdue(tomorrow, sut, calendar, future_date):
    # arrange
    task = Task('a description', tomorrow)
    sut.add_task(task)

    # act
    calendar.today = future_date

    # assert
    assert [task] == sut.overdue_tasks

def test_adding_task_with_due_day_in_future(future_date, sut):
    # arrange
    task = Task('some description', future_date)

    # act
    sut.add_task(task)

    # assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past(past_date, sut):
    # arrange
    task = Task('some description', past_date)

    # act, arrange
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)

def test_task_becomes_finished(tomorrow, sut):
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