class StateTable:
    def __init__(self):
        self.__present_states = []
        self.__next_states = []
        self.__output = []

    def add(self, next_state: list, output: list):
        self.__present_states.append(len(self.__present_states))
        self.__next_states.append(next_state)
        self.__output.append(output)

    def get_next_states(self, state) -> list:
        return self.__next_states[state]

    def get_output(self, state) -> list:
        return self.__output[state]

    def row_match(self) -> None:
        matches = {0: 0}

        # Repeat the following steps as long as there's still possible matches
        while len(matches) != 0:
            matches = dict()

            # Search for matching rows and populate dict 'matches'
            for i in range(len(self.__next_states) - 1):
                for j in range(i + 1, len(self.__next_states)):
                    if self.__next_states[i] == self.__next_states[j] and self.__output[i] == self.__output[j]:
                        if matches.get(j) is None:
                            matches[j] = i

            repeated_states = sorted(list(matches.keys()), reverse=True)

            # Cross the repeated row
            for state in repeated_states:
                self.__present_states.pop(state)
                self.__next_states.pop(state)
                self.__output.pop(state)

            # Substitute with the original state
            for next_states in self.__next_states:
                for i in range(len(next_states)):
                    if next_states[i] in repeated_states:
                        next_states[i] = matches[next_states[i]]

    def print_table(self):
        for i in range(len(self.__next_states)):
            row = [chr(ord('a') + self.__present_states[i]), [chr(ord('a') + x) for x in self.__next_states[i]],
                   self.__output[i]]

            print(row[0], end="")
            print(" | ", end="")

            for x in row[1]:
                print(f"{x} ", end="")
            print("| ", end="")

            for x in row[2]:
                print(f"{x} ", end="")
            print()


class ImplicationTable:
    def __init__(self):
        self.table = dict()

    def set_condition(self, state: set, condition: set):
        self.table[state] = condition

    def get_condition(self, state: set) -> set:
        return self.table[state]
