# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
tasks = []
class Task():
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    def on_status(self):
        self.status = True

def add_task(description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

def complete_task(description):
    for task in tasks:
        if task.description == description:
            task.on_status()
            return
    print("Задача не найдена")

def show_tasks():
    print("Текущие задачи:")
    for task in tasks:
        if not task.status:
            print(task.description, "-", task.deadline)

#доп задание

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}


    def add_item(self, item_name, price):
        self.items[item_name] = price


    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]


    def get_price(self, item_name):
        return self.items.get(item_name)


    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# создаём магазины
store1 = Store("Фруктовый рай", "ул. Ленина, 10")
store2 = Store("Продукты 24", "пр. Мира, 5")
store3 = Store("ЭкоМаркет", "ул. Садовая, 3")

# добавляем товары в первый магазин
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store1.add_item("oranges", 0.6)

# добавляем товары во второй магазин
store2.add_item("milk", 1.2)
store2.add_item("bread", 0.8)
store2.add_item("eggs", 2.5)

# добавляем товары в третий магазин
store3.add_item("eco apples", 1.0)
store3.add_item("eco honey", 5.5)
store3.add_item("eco tea", 3.2)

# проверка
print(store1.items)
print(store2.items)
print(store3.items)

