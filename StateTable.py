class StateTable:
    def __init__(self):
        self.__next_states = []
        self.__output = []

    def add(self, next_state: list, output: list):
        self.__next_states.append(next_state)
        self.__output.append(output)

    def get_next_states(self, state) -> list:
        return self.__next_states[state]

    def get_output(self, state) -> list:
        return self.__output[state]
