# OOP Calculator

## Description

This project is a command-line calculator built with Python and object-oriented programming principles. It supports addition, subtraction, calculation history, removing calculations, help, and exiting the application.

The project demonstrates abstraction, inheritance, polymorphism, encapsulation, error handling, automated testing, and continuous integration.

## Installation

This project requires Python 3.11 or newer.

Check your installed Python version with:

```bash
python --version
```

On systems where `python` is not available, use:

```bash
python3 --version
```

Clone the repository and enter the project directory:

```bash
git clone https://github.com/jmb26243/my-oop-calculator.git
cd my-oop-calculator
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Calculator

Start the calculator with:

```bash
python -m calculator
```

The available commands are:

- `add` — Add two numbers
- `subtract` — Subtract the second number from the first
- `history` — Display calculations from the current session
- `remove` — Remove a calculation from history
- `help` — Display the available commands
- `exit` — Exit the calculator

The calculator keeps history only for the current session.

## Running the Tests

Run the complete test suite with:

```bash
python -m pytest
```

The test configuration enforces both 100% line coverage and 100% branch coverage.

The tests also verify error handling, including invalid numbers, nonfinite numbers, invalid history removal, empty history, unknown commands, and interrupted input.

## Project Design

### Calculation Abstraction

The `Calculation` class provides a common abstract contract for calculations. `Add` and `Subtract` inherit from `Calculation` and implement the `get_result()` method.

This allows the calculator to work with different calculation types through the same interface.

### Polymorphism

The calculator can call:

```python
calculation.get_result()
```

without needing to check whether the calculation is an `Add` or `Subtract` object.

Each subclass provides its own implementation of `get_result()`.

### Encapsulation

The `History` class owns the collection of calculations. The internal list is protected through `_calculations`, while methods such as `add()`, `get_history()`, and `remove()` control how the collection is accessed and changed.

`get_history()` returns a copy of the collection so callers cannot directly modify the internal list.

### Separation of Responsibilities

The calculation classes are responsible for performing calculations. `History` is responsible for storing calculation objects. The CLI is responsible for interacting with the user.

Keeping these responsibilities separate means changes to one part of the application do not require unrelated parts to be rewritten.

## Continuous Integration

The project uses GitHub Actions to automatically run the test suite.

The workflow tests the project on:

- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

Each job creates a fresh Ubuntu environment, installs the dependencies, and runs:

```bash
python -m pytest
```

The pytest configuration enforces 100% line and branch coverage.

## Stage 6 Reflection

### Adding Multiply

A `Multiply` operation would belong alongside `Add` and `Subtract` as another subclass of `Calculation`.

The structure would become:

```text
Calculation
├── Add
├── Subtract
└── Multiply
```

The `Multiply` class would implement `get_result()` by multiplying its two operands.

The CLI would need to import `Multiply` and register it in the `operations` dictionary. The help text would also need to include the new `multiply` command. Tests would need to verify multiplication results and the corresponding CLI behavior.

The `History` class would not need any multiplication-specific logic. History stores `Calculation` objects rather than performing the calculations itself. Because `Multiply` follows the same `Calculation` contract, it can be stored and displayed using the existing history functionality.

### Notification Objects

Email and text-message notification objects could share a common contract with a `send()` method.

For example:

```text
Notification
├── EmailNotification
└── TextNotification
```

Both objects could implement `send()`, while each class would handle its own method of delivering the message.

Code using the notification would only need to call `send()` and would not need to know whether the notification is an email or a text message. This is similar to the calculator using `get_result()` without needing to know which calculation subclass it received.

### Transferring the Design to Another Language

The main design concepts transfer to other programming languages. Abstraction, encapsulation, inheritance, polymorphism, separation of responsibilities, and testing are not limited to Python.

However, the syntax and runtime rules would still need to be learned for another language. For example, a language such as Java has different syntax, static typing, interfaces, package organization, and testing tools.

The design principles can transfer between languages, but their implementation depends on the language.

## Independent README Usability Test

To test the README, I followed the instructions from a fresh clone in a separate directory with a new virtual environment.

The project was successfully cloned, the virtual environment was created and activated, the dependencies were installed, the calculator was run, and the test suite passed.

One potentially confusing instruction is the Python version requirement because different systems may use different commands for Python. The README was improved by explaining how to check the installed Python version and noting that `python3` may need to be used instead of `python`.

## Investigating a Coverage Failure

If all tests pass but the coverage requirement fails, I would first examine the coverage report and look at the `Missing` column.

I would identify the uncovered line or branch and determine which execution path is not being tested. I would then add a focused test for that missing path and run the test suite again.

For example, during this project the coverage initially reached 98.33% and later 99.17%. The coverage report identified an uncovered line in `calculation.py` and an uncovered branch in `__main__.py`. I added tests for those paths and eventually reached 100% line and branch coverage.

The important distinction is that passing tests and complete coverage are separate checks. A test suite can pass while still failing to execute part of the application.

## Stage 6 Self-Check

### 1. Why must CI install packages if the application uses only the standard library?

The calculator itself uses Python's standard library, but the project also depends on external development tools such as pytest and pytest-cov. A fresh CI runner does not automatically have those project dependencies installed. Installing the requirements ensures that CI has the same testing tools needed to run the complete test suite and enforce the coverage requirement.

### 2. How can the CI log distinguish an assertion failure from an installation failure?

The location of the failure in the workflow provides the first clue. If the dependency installation step fails, the problem occurred before the tests could run. If the installation succeeds but the test step reports a failed test with an assertion message, the problem is with application behavior or a test expectation. The first useful error message in the failed step is more informative than the final exit code alone.

### 3. Does a shared design vocabulary imply identical grammar across languages?

No. Programming languages can use similar design concepts while having different syntax and rules. Concepts such as abstraction, encapsulation, inheritance, and polymorphism can transfer between languages, but the syntax, type systems, interfaces, package systems, and runtime behavior can be different.

## Conclusion

This project demonstrates how object-oriented design can separate responsibilities while allowing related objects to share common behavior. Automated tests and continuous integration provide additional confidence that the design continues to work across different Python versions.
