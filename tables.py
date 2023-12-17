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
        self.state_table = s_table
        self.states_count = s_table.get_states_count()
        self.table = [[[] for _ in range(self.states_count)] for _ in range(self.states_count)]
        self.populate()

    def set_condition(self, state: set, condition: set or bool):
        row = max(state)
        col = min(state)

        self.table[row][col].append(condition)

    def reset_condition(self, state: set, condition: set or bool):
        row = max(state)
        col = min(state)

        self.table[row][col] = [condition]

    def get_conditions(self, state: set) -> list[bool or set]:
        row = max(state)
        col = min(state)

        return self.table[row][col]

    def get_remaining_states(self) -> list:
        remaining_states = []

        for i in range(self.states_count):
            for j in range(self.states_count):
                if i > j and self.table[i][j][0] != False:
                    remaining_states.append({i, j})

        return remaining_states

    def print_table(self):
        for i in range(self.states_count):
            if i > 0:
                print(chr(ord('A') + i), end="\t\t\t")

            for j in range(self.states_count):
                if i > j:
                    conditions = self.get_conditions({i, j})

                    count = 0
                    for condition in conditions:
                        if isinstance(condition, bool):
                            print(f"{condition}", end=" ")
                        else:
                            count += 1
                            print(f"{chr(ord('A') + max(condition))}-{chr(ord('A') + min(condition))}", end=" ")

                    if count == 2:
                        print("\t\t", end="")
                    else:
                        print("\t\t\t", end="")

            print("\n")

        print("\t\t\t", end="")
        for i in range(self.states_count - 1):
            print(chr(ord('A') + i), end="\t\t\t\t")

        print("\n")

    def populate(self):
        for i in range(self.states_count - 1):
            for j in range(i + 1, self.states_count):
                i_next_states = self.state_table.get_next_states(i)
                j_next_states = self.state_table.get_next_states(j)

                i_outputs = self.state_table.get_output(i)
                j_outputs = self.state_table.get_output(j)

                state = {i, j}
                conditions = []

                # If the 2 states have different o/p, then they're not equivalent
                if i_outputs != j_outputs:
                    condition = False
                    conditions.append(condition)
                else:
                    # If the 2 states have the same next states, then they're equivalent
                    if i_next_states == j_next_states:
                        condition = True
                        conditions.append(condition)
                    # If the 2 states have different next states, then add the condition
                    else:
                        for state1, state2 in zip(i_next_states, j_next_states):
                            if state1 != state2:
                                condition = {state1, state2}

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
            for state in self.get_remaining_states():
                for condition in self.get_conditions(state):
                    if isinstance(condition, set):
                        transitive_conditions = self.get_conditions(condition)

                        if len(transitive_conditions) == 1 and \
                                transitive_conditions[0] == False:

                            self.reset_condition(state, False)
                            reduced = True
                            break
