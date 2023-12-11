class Statement:
    def __init__(self, state: bool or set = False):
        """
        Initialize a Statement object.

        Parameters:
        - state (bool or set): The initial state of the statement. Default is False for boolean state.
                              If a set is provided, it represents a custom condition.

        Note:
        - The default state is set to False for boolean values.
        - If a set is provided, it is considered as a custom condition.

        """
        self.state = state

    def set_true(self):
        """
        Set the statement to True.

        This method sets the state of the statement to True.

        """
        self.state = True

    def set_false(self):
        """
        Set the statement to False.

        This method sets the state of the statement to False.

        """
        self.state = False

    def set_condition(self, condition: set):
        """
        Set a custom condition for the statement.

        Parameters:
        - condition (set): A set representing a custom condition.

        Note:
        - The statement's state will be set to the provided condition.

        """
        self.state = condition

    def get_state(self):
        """
        Get the current state of the statement.

        Returns:
        - The current state of the statement.

        """
        return self.state

    def equals(self, other_statement) -> bool:
        """
        Check if two Statement objects are equal.

        Parameters:
        - other_statement (Statement): Another Statement object to compare.

        Returns:
        - True if the two statements are equal, False otherwise.

        """
        return self.state == other_statement.get_state()

    def __str__(self):
        """
        Provide a string representation of the Statement object.

        Returns:
        - A string representation of the current state.

        """
        return str(self.state)
