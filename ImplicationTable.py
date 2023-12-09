class ImplicationTable:
    def __init__(self):
        self.table = dict()

    def set_condition(self, state: set, condition: set):
        self.table[state] = condition

    def get_condition(self, state: set) -> set:
        return self.table[state]
