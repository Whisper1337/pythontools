class task: #without this there is no object structure
    def __init__(self, title, priority): #creates the ttile and priority when we make a task
        self.title = title
        self.priority = priority

    def display(self):
        return f"{self.title} (priority {self.priority})"


class emergencytask(task): #need this so we dont lose the subcalss feature
    def __init__(self, title, priority):
        super().__init__(title, priority)

    def display(self):
        return f"{self.title} (emergency priority {self.priority})"


tasks = [] #stores all tasks
undo_stack = [] #allows us to undo work


def save_to_file():
    try:
        file = open("tasks.txt", "w") #cannot load saved tasks without this
        for t in tasks:
            line = type(t).__name__ + "," + t.title + "," + str(t.priority) + "\n"
            file.write(line)
        file.close()
        print("saved.")
    except:
        print("error saving file.")


def load_from_file():
    try:
        file = open("tasks.txt", "r")
        tasks.clear()

        for line in file:
            parts = line.strip().split(",")

            if parts[0] == "task":
                tasks.append(task(parts[1], int(parts[2])))
            elif parts[0] == "emergencytask":
                tasks.append(emergencytask(parts[1], int(parts[2])))

        file.close()
        print("loaded.")
    except:
        print("error loading file.")


def add_task():
    title = input("enter title: ")
    priority = int(input("enter priority number: "))
    kind = input("is this emergency? yes or no: ")

    if kind == "yes":
        t = emergencytask(title, priority)
    else:
        t = task(title, priority)

    tasks.append(t) #you HAVE to have this so taskss are stored
    undo_stack.append(("add", t))


def remove_task():
    title = input("enter title to remove: ")

    for t in tasks:
        if t.title == title:
            tasks.remove(t) #allows a "delete" feature
            undo_stack.append(("remove", t))
            print("removed.")
            return

    print("not found.")


def undo():
    if len(undo_stack) == 0:
        print("nothing to undo.")
        return

    action, t = undo_stack.pop() #think of last in first out. need the "pop" for the "undo" to work correctly

    if action == "add":
        tasks.remove(t)
    elif action == "remove":
        tasks.append(t)

    print("undone.")


def search_task():
    title = input("enter title to search: ")

    for t in tasks:
        if t.title == title:
            print(t.display())
            return

    print("not found.")


def sort_tasks():
    tasks.sort(key=lambda x: x.priority) #this makes the sorting very happy
    print("sorted by priority.")


def view_tasks():
    if len(tasks) == 0:
        print("no tasks.")
        return

    for t in tasks:
        print(t.display())


while True: #without this vital loop, the program would just run once and exit right after
    print("\n1 add task")
    print("2 remove task")
    print("3 view tasks")
    print("4 search task")
    print("5 sort tasks")
    print("6 undo")
    print("7 save")
    print("8 load")
    print("9 exit")

    choice = input("choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        search_task()
    elif choice == "5":
        sort_tasks()
    elif choice == "6":
        undo()
    elif choice == "7":
        save_to_file()
    elif choice == "8":
        load_from_file()
    elif choice == "9":
        break #need this to avoid an infinite loop
    else:
        print("invalid choice.")