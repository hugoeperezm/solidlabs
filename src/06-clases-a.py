class Person():

    def __init__(self, name, gender, birthdate) -> None:
        self.name = name
        self.gender = gender
        self.birthdate = birthdate


class User(Person):

    def __init__(self, name, gender, birthdate, email, role, lastAccess) -> None:
        super().__init__(name, gender, birthdate)
        self.email = email
        self.role = role
        self.lastAccess = lastAccess

    def checkCredentials(self):
        return True
    
class UserSettings(User):
    def __init__(self, name, gender, birthdate, email, role, lastAccess, workingDirectory, lastOpenFolder) -> None:
        super().__init__(name, gender, birthdate, email, role, lastAccess)
        self.workingDirectory = workingDirectory
        self.lastOpenFolder = lastOpenFolder

if __name__ == "__main__":
    userSettings = UserSettings("Marco", "M", "1968-06-18", "hugoeperezm@gmail.com", "Lead", "2023-03-24", "usr/home", "/home")
    print(userSettings.__dict__, "AreCredentialsValid:", userSettings.checkCredentials())

    person = Person('Hugo', 'M', '1968-06-18')
    print(person.__dict__)