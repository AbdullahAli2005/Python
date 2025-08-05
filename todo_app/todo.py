import json
import os

FILENAME = 'todo.json'

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task.get('completed', False) else "✗"
        print(f"{idx}. [{status}] {task['title']} - {task.get('description', '')}")
    
def save_task(title, description):
    tasks = load_tasks()
    new_task = {
        'title': title,
        'description': description,
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")
    
def mark_task_completed(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{deleted['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    
def main():
    while True:
        print("\nTodo List")
        print("1. Show tasks")
        print('2. Add task')
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            tasks = load_tasks()
            show_tasks(tasks)  
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            save_task(title, description)
        elif choice == '3':
            mark_task_completed(load_tasks())
        elif choice == '4':
            delete_task(load_tasks())
        elif choice == '5':
            print("Exiting the todo list application.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()