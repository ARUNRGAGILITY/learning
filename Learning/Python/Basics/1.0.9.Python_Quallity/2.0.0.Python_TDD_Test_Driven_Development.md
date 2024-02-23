# Test Driven Development (TDD)

Test-Driven Development (TDD) is a software development approach where tests are written before writing the functional code. It follows a cycle of writing a test, ensuring it fails (since the functionality isn't implemented yet), writing the minimal code to pass the test, and then refactoring the code. Here's a step-by-step guide to TDD in Python, using a simple example:

The TDD cycle, or Test-Driven Development cycle, is a software development approach where tests are written before the actual code. It's based on a simple, repetitive cycle called "Red-Green-Refactor." Here's a breakdown of each step:

1. **Write a Test**: Start by writing a test for a new function or feature. This test will initially fail, as the functionality it tests does not yet exist. This is the "Red" phase, indicating that tests are failing.

2. **Write the Minimum Amount of Code to Pass the Test**: Write just enough code to make the test pass. This is the "Green" phase, where the focus is on getting a passing test, which validates that the new functionality works as expected.

3. **Refactor the Code**: Now that the test is passing, look at the code and consider how it can be improved without changing its behavior. This might involve removing duplication, improving readability, or applying design patterns. Refactoring ensures that the codebase is clean and maintainable.

4. **Repeat**: Go back to step 1 and start the cycle again with a new test.

The key benefits of TDD include:

- **Early bug detection**: Since tests are written first, issues are identified early in the development process.
- **Improved Code Quality**: Regular refactoring helps maintain a high standard of code.
- **Better Design**: TDD encourages developers to think about the design and structure of their code, often leading to more modular and flexible code.
- **Documentation**: Tests serve as a form of documentation that describes what the code is supposed to do.

TDD is a core practice in Agile methodologies and is widely used in various forms of software development.
![image](https://github.com/ARUNRGAGILITY/learning_python/assets/96728746/8202f60c-317e-407b-881e-d9bf5af6f5df)

### 1. Set Up Your Environment

Make sure you have Python installed. Also, install `pytest`, a popular testing framework in Python.

```bash
pip install pytest
```

### 2. Decide on a Simple Functionality to Implement

Let's say we are building a function `add` that adds two numbers. We'll start by writing a test for this function.

### 3. Write the First Test

Create a file `test_calculator.py` for your tests.

```python
# test_calculator.py

def test_add():
    assert add(2, 3) == 5
```

This test checks if the `add` function correctly adds 2 and 3.

### 4. Run the Test and See it Fail

Running the test now should fail because `add` isn't defined yet.

```bash
pytest test_calculator.py
```

### 5. Write the Minimal Code to Pass the Test

Create a file `calculator.py` with the minimal implementation.

```python
# calculator.py

def add(x, y):
    return x + y
```

### 6. Run the Test Again

Now, when you run the test, it should pass.

### 7. Refactor if Necessary

Refactor the code for better readability or efficiency if needed, but this is optional for our simple example.

### 8. Repeat for More Functionality

For each new functionality, repeat steps 3 to 7. For example, if you want to add a `subtract` function, start by writing a test for it.

### Example: Adding a New Functionality with TDD

Suppose we now want to add a `multiply` function.

#### Write the Test First

In `test_calculator.py`, add:

```python
def test_multiply():
    assert multiply(3, 4) == 12
```

#### Run the Test and Watch it Fail

```bash
pytest test_calculator.py
```

#### Implement the Function

In `calculator.py`, add:

```python
def multiply(x, y):
    return x * y
```

#### Method to run the tdd code

### `calculator.py`
This file contains the implementation of the calculator functions.

```python
# calculator.py

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y
```

### `test_calculator.py`
This file contains the tests for the calculator functions.

```python
# test_calculator.py
from calculator import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(3, 4) == 12
```

### Instructions for Running the Tests
1. Save these two files (`calculator.py` and `test_calculator.py`) in the same directory.
2. Run the tests using `pytest` from the command line in that directory:

   ```bash
   pytest test_calculator.py
   ```

This will execute the tests defined in `test_calculator.py`, testing the functionality implemented in `calculator.py`. 
If everything is correct, `pytest` should indicate that all tests have passed. 
This approach ensures that your implementation meets the expected requirements as defined by your tests.


#### Run the Test Again and Ensure it Passes

### Conclusion

This cycle of Red (write a failing test), Green (make the test pass), and Refactor is the essence of TDD. It ensures that your code has tests from the very beginning and can help in minimizing bugs and improving code quality.

As your project grows, your test suite will become more comprehensive, and you'll be more confident in the robustness of your code.
