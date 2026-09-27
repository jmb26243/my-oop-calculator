class History:
    def __init__(self):
        self._calculations = []

    def add(self, calculation):
        self._calculations.append(calculation)

    def get_all(self):
        return list(self._calculations)

    def remove(self, index):
        if index < 0 or index >= len(self._calculations):
            raise IndexError("Calculation index out of range")

        return self._calculations.pop(index)

    def clear(self):
        self._calculations.clear()
