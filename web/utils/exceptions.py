class AppExceptions(Exception):
    pass

class InvalidInput(AppExceptions):
    def __init__(self, msg="Invalid Input") -> None:
        if msg != "Invalid Input":
            self.msg = f"Invalid Input: {msg}"
        self.msg = msg
        super().__init__(self.msg)

class NonExistentValue(AppExceptions):
    def __init__(self, msg="Non existent value") -> None:
        if msg != "Non existent value":
            self.msg = f"Non existent value: {msg}"
        self.msg = msg
        super().__init__(self.msg)
