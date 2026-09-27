from calculator.calculation import Add, Subtract
from calculator.history import History


def run():
    history = History()

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        if command == "add":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            calculation = Add(a, b)
            history.add(calculation)
            print(calculation.get_result())

        elif command == "subtract":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            calculation = Subtract(a, b)
            history.add(calculation)
            print(calculation.get_result())

        elif command == "history":
            for index, calculation in enumerate(history.get_all()):
                print(f"{index}: {calculation.get_result()}")

        elif command == "remove":
            index = int(input("Enter calculation number: "))
            history.remove(index)
            print("Calculation removed.")
