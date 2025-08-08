import csv
import os

class ToDoList:
    def __init__(self, filename='todo_list.csv'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the CSV file."""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]

    def save_tasks(self):
        """Save tasks to the CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task])

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{task}" added to the list.')

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f'Task "{removed_task}" removed from the list.')
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
