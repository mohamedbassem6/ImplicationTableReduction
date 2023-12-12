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

    def get_states_count(self) -> int:
        return len(self.__present_states)

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
    def __init__(self, s_table):
        self.table = dict()
        self.populate(s_table)

    def set_condition(self, state: frozenset, condition: frozenset or bool):
        if self.table.get(state) is None:
            self.table[state] = [condition]
        else:
            self.table[state].append(condition)

    def reset_condition(self, state: frozenset, condition: frozenset or bool):
        self.table[state] = [condition]

    def get_condition(self, state: frozenset) -> list[frozenset]:
        return self.table.get(state)

    def print_table(self):
        for key, values in self.table.items():
            print("{ ", end="")
            for x in key:
                print(chr(ord('a') + x) + " ", end="")
            print("} -> ", end="")

            for value in values:
                if isinstance(value, frozenset):
                    print("{ ", end="")
                    for x in value:
                        print(chr(ord('a') + x) + " ", end="")
                    print("}", end="")
                else:
                    print(f"{value} ", end="")

            print()

    def populate(self, s_table: StateTable):
        states_count = s_table.get_states_count()

        for i in range(states_count - 1):
            for j in range(i + 1, states_count):
                i_next_states = s_table.get_next_states(i)
                j_next_states = s_table.get_next_states(j)

                i_outputs = s_table.get_output(i)
                j_outputs = s_table.get_output(j)

                state = frozenset({i, j})
                conditions = []

                if i_outputs != j_outputs:
                    condition = False
                    conditions.append(condition)
                else:
                    if i_next_states == j_next_states:
                        condition = True
                        conditions.append(condition)
                    else:
                        for state1, state2 in zip(i_next_states, j_next_states):
                            if state1 != state2:
                                condition = frozenset({state1, state2})

                                if condition != state:
                                    conditions.append(condition)

                if len(conditions) == 0:
                    self.set_condition(state, True)
                else:
                    for condition in conditions:
                        self.set_condition(state, condition)

    def imply(self):
        reduced = True

        while reduced:
            reduced = False
            for state, conditions in self.table.items():
                for condition in conditions:
                    if isinstance(condition, frozenset):
                        transitive_conditions = self.get_condition(condition)

                        if transitive_conditions is not None and \
                            len(transitive_conditions) == 1 and \
                                transitive_conditions[0] == False:

                            self.reset_condition(state, False)
                            reduced = True
                            break
