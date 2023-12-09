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

    def print_table(self):
        for i in range(len(self.__next_states)):
            row = [chr(ord('a') + i), [chr(ord('a') + x) for x in self.__next_states[i]], self.__output[i]]

            print(row[0], end="")
            print(" | ", end="")

            for x in row[1]:
                print(f"{x} ", end="")
            print("| ", end="")

            for x in row[2]:
                print(f"{x} ")
