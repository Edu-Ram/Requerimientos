class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def register_user(self, username, password):
        self.user_service.register(username, password)


class UserService:
    def register(self, username, password):
        print(f"Usuario '{username}' registrado exitosamente")


user_service = UserService()
user_controller = UserController(user_service)
user_controller.register_user("john_doe", "password123")
