from person import Person


class Staff(Person):
    def __init__(self, name, age, gender, staff_id):
        super().__init__(name, age, gender)
        self.staff_id = staff_id

    def get_details(self):
        return f"Staff: {self.name}, Age: {self.age}, ID: {self.staff_id}"


class Team(Staff):
    def __init__(self, name, age, gender, staff_id, team_name):
        super().__init__(name, age, gender, staff_id)
        self.team_name = team_name

    def get_details(self):
        return f"Team: {self.team_name}, {super().get_details()}"
