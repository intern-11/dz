class User:
    def __init__(self, user_id: int, name: str):
        self._id = user_id
        self._name = name
        self._access_level = "user"

    # Геттеры
    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_access_level(self) -> str:
        return self._access_level

    # Сеттеры
    def set_name(self, name: str):
        self._name = name

    def __repr__(self):
        return f"User(id={self._id}, name='{self._name}', access='{self._access_level}')"


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self._access_level = "admin"

    def add_user(self, user_list: list, user: User):
        if user not in user_list:
            user_list.append(user)

    def remove_user(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                return

    def __repr__(self):
        return f"Admin(id={self._id}, name='{self._name}', access='{self._access_level}')"

users = []

admin = Admin(1, "Алексей")
user1 = User(2, "Мария")
user2 = User(3, "Иван")

admin.add_user(users, user1)
admin.add_user(users, user2)

print(users)
# [User(id=2, name='Мария', access='user'), User(id=3, name='Иван', access='user')]

admin.remove_user(users, 2)

print(users)
# [User(id=3, name='Иван', access='user')]
