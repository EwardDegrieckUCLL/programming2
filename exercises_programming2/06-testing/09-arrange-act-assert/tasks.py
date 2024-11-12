from datetime import date, timedelta

class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.finished = False

    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
        
class TaskList:
    def __init__(self, calendar):
        self.__list = []
        self.calendar = calendar

    @property
    def list(self):
        return self.__list
    
    def add_task(self, task):
        if task.due_date >= self.calendar.today:
            self.__list.append(task)
        else:
            raise RuntimeError("task due date can't be in the past")
        
    def __len__(self):
        return len(self.list)
    
    @property
    def finished_tasks(self):
        return [task for task in self.list if task.finished]
    
    @property
    def due_tasks(self):
        return [task for task in self.list if not task.finished]
    
    @property
    def overdue_tasks(self):
        return [
            task for task in self.due_tasks 
            if task.due_date < self.calendar.today
            ]