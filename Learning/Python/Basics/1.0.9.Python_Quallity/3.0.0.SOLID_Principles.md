# SOLID Principles

The SOLID principles are a set of guidelines for object-oriented design and programming that improve the maintainability, scalability, and robustness of software. They were introduced by Robert C. Martin and are widely regarded as best practices in software development. Here's a brief overview of each principle:

1. **Single Responsibility Principle (SRP)**: This principle states that a class should have only one reason to change, meaning it should have only one job or responsibility. By ensuring a class is focused on a single aspect of the system, it becomes easier to understand, test, and maintain.

2. **Open/Closed Principle (OCP)**: According to this principle, software entities (like classes, modules, functions, etc.) should be open for extension but closed for modification. This means you should be able to add new functionality to an existing class without changing its existing code, typically by using interfaces or abstract classes.

3. **Liskov Substitution Principle (LSP)**: This principle extends the notion of inheritance in object-oriented programming. It states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In simpler terms, subclasses should adhere to the behavior expected by the clients of the superclass.

4. **Interface Segregation Principle (ISP)**: The Interface Segregation Principle advises that no client should be forced to depend on methods it does not use. It's better to have many specific interfaces than one general-purpose interface. This keeps class interfaces lean and relevant to their users.

5. **Dependency Inversion Principle (DIP)**: This principle suggests that high-level modules should not depend on low-level modules but should depend on abstractions. Similarly, abstractions should not depend on details; details should depend on abstractions. This principle encourages the design of systems that are loosely coupled and hence more flexible and maintainable.

Applying these principles can lead to more reusable, flexible, and maintainable code. 
They are especially beneficial in large and complex software systems where the cost of change and the risk of introducing bugs are high. 

### Examples of SOLID Principles


### Single Responsibility Principle (SRP)

**Violation Example:**
```python
class User:
    def __init__(self, name: str):
        self.name = name

    def get_user_data(self):
        pass  # Fetch user data from database

    def save_user_data(self):
        pass  # Save user data to database
```

**Refactored Example:**
```python
class User:
    def __init__(self, name: str):
        self.name = name

class UserDataBase:
    @staticmethod
    def get_user_data(user: User):
        pass  # Fetch user data

    @staticmethod
    def save_user_data(user: User):
        pass  # Save user data
```

**Violation:**
In the original `User` class, the class has two responsibilities: managing user data and interacting with the database. This violates SRP as the class is responsible for more than one operation.

**Resolution:**
In the refactored code, the responsibilities are separated into two classes. The `User` class is responsible for user-related data, and the `UserDataBase` class handles database operations. This separation ensures that each class has only one reason to change, adhering to the SRP.

### Open/Closed Principle (OCP)

**Violation Example:**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def calculate_area(shapes):
    total_area = 0
    for shape in shapes:
        if isinstance(shape, Rectangle):
            total_area += shape.width * shape.height
    return total_area
```

**Refactored Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_area(shapes):
    return sum(shape.area() for shape in shapes)
```

**Violation:**
The `calculate_area` function violates OCP because it needs to be modified every time a new shape is added. This is evident from the `if isinstance(shape, Rectangle)` check, which is not scalable for multiple shapes.

**Resolution:**
By introducing an abstract class `Shape` with an `area` method, the `calculate_area` function can now operate on any shape that implements the `Shape` interface. This means new shapes can be added without modifying the existing code, keeping it open for extension but closed for modification.

### Liskov Substitution Principle (LSP)

**Violation Example:**
```python
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches cannot fly")
```

**Refactored Example:**
```python
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "I can fly!"

class Ostrich(Bird):
    def move(self):
        return "I can run!"
```

**Violation:**
The original example violates LSP because `Ostrich`, a subclass of `Bird`, cannot be used interchangeably with its superclass, as ostriches cannot fly. This breaks the contract established by the superclass.

**Resolution:**
The refactored code introduces an abstract method `move` in the base class `Bird` and differentiates between flying and non-flying birds. This way, subclasses like `FlyingBird` and `Ostrich` can provide their own implementations of movement, ensuring they can be used interchangeably without breaking the functionality.

### Interface Segregation Principle (ISP)

**Violation Example:**
```python
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Human(Worker):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating lunch")
```

**Refactored Example:**
```python
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating lunch")
```

**Violation:**
The original `Worker` interface forces the `Human` class to implement both `work` and `eat` methods. This is a violation of ISP because not all workers may need the `eat` method.

**Resolution:**
The refactored code separates the responsibilities into two interfaces: `Workable` and `Eatable`. The `Human` class implements both interfaces, but other classes can choose to implement only the interfaces they need, thus adhering to ISP.
### Dependency Inversion Principle (DIP)

**Violation Example:**
```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class ElectricPowerSwitch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb
        self.on = False

    def press(self):
        if self.on:
            self.bulb.turn_off()
            self.on = False
        else:
            self.bulb.turn_on()
            self.on = True
```

**Refactored Example:**
```python
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class ElectricPowerSwitch:
    def __init__(self, device: Switchable):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True
```


**Violation:**
The original `ElectricPowerSwitch` class is directly dependent on the `LightBulb` class. This high-level module is dependent on a low-level module, which goes against DIP.

**Resolution:**
In the refactored code, both `ElectricPowerSwitch` and `LightBulb` depend on the `Switchable` abstraction. This decouples the high-level module (the switch) from the low-level module (the light bulb), adhering to DIP. The switch class is no longer dependent on the light bulb class but on the `Switchable` interface, allowing for greater flexibility and easier testing.


Each example demonstrates a specific SOLID principle in a Pythonic context. 
While these are simple illustrations, the principles can be applied to more complex and real-world scenarios.
