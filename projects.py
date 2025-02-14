tasks = []
class Task:
    def __init__(self, task_name, date, status = 'Not completed'):
        self.task_name = task_name
        self.date = date
        self.status = status
    
    def mark_complete(self):
        self.status = 'complete'
    
def add_task(task_name, date):
    task = Task(task_name, date)
    tasks.append(task)

def view_tasks():
    if not tasks:
        print('there is no task to do')
    else:
        print('\nTo-Do List')
        for index, task in enumerate(tasks, start= 1):
            print(f'{index} - {task.task_name} - {task.date}')

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1].mark_complete()
        print(f"Task '{tasks[task_index - 1].task_name}' marked as complete.")
    else:
        print('invalid task number')

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f'task {removed_task.task_name} removed successfully!')
    else:
        print('invalid task number')

while True:
    print('\nTo-Do List menu:')
    print('1. Add task')
    print('2. view tasks')
    print('3. mark task as complete')
    print('4. remove task')
    print('5. Exit')

    choice = int(input('enter your choice:'))
    if choice == 1:
        task_name = input('enter the task name: ')
        date = input('enter the date: ')
        add_task(task_name, date)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        view_tasks()
        task_index = int(input('which task should mark as read: '))
        complete_task(task_index)
    elif choice == 4:
        view_tasks()
        task_index = int(input('enter the number of task that you want to delete: '))
        remove_task(task_index)
    elif choice == 5:
        print('Good Bye!')
        break
    else:
        print('invaild number, please try again')