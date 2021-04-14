class C32:  # Implements final Mele's automaton
    state = None

    # Initializes fields of class
    def __init__(self):
        self.state = 'A'

    def race(self):
        """
        Returns integer value and sets new character to field 'state'
        :exception RuntimeError
        :return: Integer value
        """
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'B':
            self.state = 'G'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise RuntimeError

    def sit(self):
        """
        Returns integer value and sets new character to field 'state'
        :exception RuntimeError
        :return: Integer value
        """
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'B'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise RuntimeError

    def group(self):
        """
        Returns integer value and sets new character to field 'state'
        :exception RuntimeError
        :return: Integer value
        """
        if self.state == 'B':
            self.state = 'D'
            return 4
        elif self.state == 'C':
            self.state = 'D'
            return 5
        else:
            raise RuntimeError
