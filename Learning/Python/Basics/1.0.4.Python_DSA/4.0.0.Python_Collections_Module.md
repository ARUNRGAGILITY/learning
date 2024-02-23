# Python Builtin Collections Module/Classes

Python `collections` module:

1. Counters
2. DefaultDict
3. OrderedDict
4. ChainMap
5. NamedTuple
6. DeQue
7. UserList
8. UserString
9. UserDict

Here we go through each one of them in details...

1. **Counter**
   - **Purpose**: Counting occurrences of elements.
   - **Practical Use Case**: Analyzing the frequency of items in a list can be useful for statistics, such as finding the most common words in a document.

   ```python
   # Find the three most common words in a text
   words = "apple banana apple strawberry banana lemon apple banana".split()
   word_counts = Counter(words)
   most_common_three = word_counts.most_common(3)
   print(most_common_three)  # Output: [('apple', 3), ('banana', 3), ('strawberry', 1)]
   ```

2. **defaultdict**
   - **Purpose**: Assigning default values to keys that do not exist.
   - **Practical Use Case**: Grouping items without having to initialize a list for new keys, such as categorizing a list of tuples into a dictionary.

   ```python
   # Group animals by their type
   animal_list = [('dog', 'Fido'), ('cat', 'Whiskers'), ('dog', 'Clifford'), ('parrot', 'Polly')]
   animal_dict = defaultdict(list)
   for animal, name in animal_list:
       animal_dict[animal].append(name)
   print(animal_dict)  # Output: defaultdict(<class 'list'>, {'dog': ['Fido', 'Clifford'], 'cat': ['Whiskers'], 'parrot': ['Polly']})
   ```

3. **OrderedDict**
   - **Purpose**: Maintaining the order of keys.
   - **Practical Use Case**: When the order of entries is critical, such as in an ordered configuration file where parameters have a specific sequence.

   ```python
   # Remember the order of tasks completed
   tasks_completed = OrderedDict()
   tasks_completed['wake up'] = '7am'
   tasks_completed['breakfast'] = '8am'
   tasks_completed['work'] = '9am'
   for task, time in tasks_completed.items():
       print(f"Task: {task}, Time: {time}")
   ```

4. **ChainMap**
   - **Purpose**: Searching through multiple dictionaries as one.
   - **Practical Use Case**: For an application with multiple configuration settings, `ChainMap` can be used to define a priority: user settings override defaults.

   ```python
   # Application settings: defaults and overrides
   default_settings = {'color': 'blue', 'font': 'Arial'}
   user_settings = {'font': 'Tahoma'}
   settings = ChainMap(user_settings, default_settings)
   print(settings['color'], settings['font'])  # Output: blue Tahoma
   ```

5. **namedtuple**
   - **Purpose**: Lightweight, immutable data structures with named fields.
   - **Practical Use Case**: Reading a CSV file where each row represents a record with fields, and accessing the fields by name improves code readability.

   ```python
   # Employee records
   Employee = namedtuple('Employee', 'name, age, department')
   emp1 = Employee('John Doe', 30, 'Finance')
   print(emp1)  # Output: Employee(name='John Doe', age=30, department='Finance')
   ```

6. **deque**
   - **Purpose**: Efficient appends and pops from either end.
   - **Practical Use Case**: Implementing a queue for tasks in a multi-threaded environment since it’s thread-safe.

   ```python
   # Maintaining a fixed-size queue of the latest N items
   recent_items = deque(maxlen=5)
   for i in range(10):
       recent_items.append(i)
       print(f"New item: {i}, Recent 5: {list(recent_items)}")
   ```

7. **UserList**
   - **Purpose**: Easier list subclassing.
   - **Practical Use Case**: Creating a custom list type that has certain constraints, like a typed array or a list that does not allow duplicates.

   ```python
   # A list that only accepts integers and no duplicates
   class IntegerSet(UserList):
       def append(self, item):
           if not isinstance(item, int):
               raise TypeError("Only integers are allowed")
           if item not in self.data:
               super().append(item)
   ```

8. **UserString**
   - **Purpose**: Easier string subclassing.
   - **Practical Use Case**: Extending string functionality, such as adding methods for specific kinds of parsing or formatting.

   ```python
   # A custom string class that adds a method to reverse the string
   class MyString(UserString):
       def reverse(self):
           return self.data[::-1]
   ```

9. **UserDict**
   - **Purpose**: Easier dict subclassing.


   - **Practical Use Case**: Extending the dictionary to provide additional methods or to enforce certain rules on keys or values.

   ```python
   # A dictionary that never allows deletion of items
   class PersistentDict(UserDict):
       def __delitem__(self, key):
           raise NotImplementedError("Item deletion not allowed")
   ```

These examples show how each class can be used in a meaningful context, demonstrating their practical applications in various programming scenarios.


# Python Built-in Classes explaination

 `collections` classes with an explanation and example:

1. **Counter**
   - A `Counter` is a `dict` subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

   ```python
   from collections import Counter

   # Count the frequency of each character in a string
   c = Counter('hello world')
   print(c)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
   ```

2. **defaultdict**
   - The `defaultdict` is a `dict` subclass that calls a factory function to supply missing values.

   ```python
   from collections import defaultdict

   # Function that returns a default value for the missing keys
   def default_value():
       return "Not Present"
   
   d = defaultdict(default_value)
   d['a'] = 1
   d['b'] = 2
   print(d['a'])  # Output: 1
   print(d['c'])  # Output: Not Present
   ```

3. **OrderedDict**
   - An `OrderedDict` is a `dict` subclass that remembers the order that keys were first inserted.

   ```python
   from collections import OrderedDict

   # Remember the order the keys are added to the dictionary
   od = OrderedDict()
   od['a'] = 1
   od['b'] = 2
   od['c'] = 3
   for key in od:
       print(key, od[key])
   ```

4. **ChainMap**
   - A `ChainMap` groups multiple dictionaries into a single view.

   ```python
   from collections import ChainMap

   # Combine two dictionaries for a single view
   dict1 = {'a': 1, 'b': 2}
   dict2 = {'b': 3, 'c': 4}
   cm = ChainMap(dict1, dict2)
   print(cm['b'])  # Output: 2 (values from the first dictionary have precedence)
   ```

5. **namedtuple**
   - `namedtuple` creates tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable.

   ```python
   from collections import namedtuple

   # Create a namedtuple to represent a point in 2D space
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(11, y=22)
   print(p[0] + p[1])  # Output: 33
   print(p.x + p.y)    # Output: 33
   ```

6. **deque**
   - A `deque` is a list optimized for inserting and removing items.

   ```python
   from collections import deque

   # Initialize a deque with three items
   d = deque('abc')
   d.append('d')         # add to the right
   d.appendleft('z')     # add to the left
   print(d)  # Output: deque(['z', 'a', 'b', 'c', 'd'])
   ```

7. **UserList**
   - `UserList` is a wrapper around list objects for easier list subclassing.

   ```python
   from collections import UserList

   # Create a subclass of UserList
   class MyList(UserList):
       def append(self, item):
           if not isinstance(item, int):
               raise ValueError("Only integers are allowed")
           super().append(item)
   
   ml = MyList([1, 2, 3])
   ml.append(4)
   print(ml)  # Output: [1, 2, 3, 4]
   ```

8. **UserString**
   - `UserString` is a wrapper around string objects for easier string subclassing.

   ```python
   from collections import UserString

   # Create a subclass of UserString
   class MyString(UserString):
       def append(self, s):
           self.data += s
   
   ms = MyString("Python")
   ms.append("3.8")
   print(ms)  # Output: Python3.8
   ```

9. **UserDict**
   - `UserDict` is a wrapper around dictionary objects for easier dict subclassing.

   ```python
   from collections import UserDict

   # Create a subclass of UserDict
   class MyDict(UserDict):
       def pop(self, key):
           raise NotImplementedError("Pop is not allowed for MyDict")
   
   md = MyDict({'a': 1, 'b': 2})
   print(md)  # Output: {'a': 1, 'b': 2}


# Python Built-in Collections with more examples

Let's go over four practical examples for each of the nine `collections` classes.

### 1. Counter

**Example 1**: Counting the number of occurrences of each character in a string.
```python
Counter("abracadabra")
```

**Example 2**: Counting the number of occurrences of each word in a sentence.
```python
Counter("the quick brown fox jumps over the lazy dog".split())
```

**Example 3**: Finding the most common elements in a list.
```python
nums = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1, 2, 9]
Counter(nums).most_common(3)
```

**Example 4**: Updating the count of elements from an iterable.
```python
c = Counter()
c.update("abcdaab")
c.update({'a': 1, 'd': 5})
```

### 2. defaultdict

**Example 1**: Grouping items by a certain attribute.
```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
```

**Example 2**: Counting items in a list.
```python
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
```

**Example 3**: Building a multidimensional array.
```python
dd = defaultdict(lambda: defaultdict(int))
dd[0][1] = 1
```

**Example 4**: Caching results of a function.
```python
def retrieve_user(id):
    return f"User{id}"

cache = defaultdict(retrieve_user)
cache[10]
cache[23]
```

### 3. OrderedDict

**Example 1**: Remembering the order of items added to a dictionary.
```python
d = OrderedDict()
d['foo'] = 100
d['bar'] = 200
d['baz'] = 300
```

**Example 2**: Reordering dictionary items.
```python
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
```

**Example 3**: Reverse iteration.
```python
for key in reversed(d):
    print(key, d[key])
```

**Example 4**: Creating a Last Recently Used (LRU) cache.
```python
class LRU(OrderedDict):
    def __init__(self, maxsize=128, *args, **kwds):
        super().__init__(*args, **kwds)
        self.maxsize = maxsize

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value
```

### 4. ChainMap

**Example 1**: Searching through multiple scopes (like variable scopes in functions).
```python
local_scope = {'x': 1}
global_scope = {'x': 2, 'y': 3}
chain = ChainMap(local_scope, global_scope)
```

**Example 2**: Command-line argument parsing fallbacks.
```python
defaults = {'color': 'red', 'user': 'guest'}
parsed_args = {'user': 'admin', 'password': 'admin'}
config = ChainMap(parsed_args, defaults)
```

**Example 3**: Context switching (such as between different configuration settings).
```python
contexts = ChainMap()
contexts['development'] = {'mode': 'dev', 'debug': True}
contexts['production'] = {'mode': 'prod', 'debug': False}
```

**Example 4**: Merging dictionaries for configurations.
```python
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'berry': 3, 'orange': 4, 'apple': 0}
merged = ChainMap(dict1, dict2)
```

### 5. namedtuple

**Example 1**: Representing a point in a 2D coordinate system.
```python
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
p2 = Point(30, 40)
```

**Example 2**: Storing data from a CSV file.
```python
Employee = namedtuple('Employee', 'name, age, department')
emp1 = Employee('John Doe', 30, 'Marketing')
```

**Example 3**: As a return type for a function instead of a dictionary.
```python
def get_dimensions():
    Dimension = namedtuple('Dimension', 'width height')
    return Dimension(1024, 768)
```

**Example 4**: Using as a more readable alternative to tuples.
```python
Color = namedtuple('Color', 'red green blue')
color =

 Color(55, 155, 255)
```

### 6. deque

**Example 1**: Implementing a queue.
```python
q = deque()
q.append('eat')
q.append('sleep')
q.append('code')
```

**Example 2**: Implementing a stack.
```python
stack = deque()
stack.appendleft('eat')
stack.appendleft('sleep')
stack.appendleft('code')
```

**Example 3**: Keeping a list of last seen items.
```python
history = deque(maxlen=5)
for i in range(10):
    history.append(i)
```

**Example 4**: Rotating elements.
```python
d = deque(range(5))
d.rotate(2)  # Rotates the deque by n steps to the right
```

### 7. UserList

**Example 1**: Creating a list that can only store integers.
```python
class IntegerList(UserList):
    def append(self, item):
        if not isinstance(item, int):
            raise TypeError("Only integers are allowed")
        super().append(item)
```

**Example 2**: A list with logging on item addition.
```python
class LoggingList(UserList):
    def append(self, item):
        print(f"Adding item {item}")
        super().append(item)
```

**Example 3**: A list where duplicate values are not allowed.
```python
class UniqueList(UserList):
    def append(self, item):
        if item not in self.data:
            super().append(item)
```

**Example 4**: A list with a custom method for computing the sum.
```python
class SummableList(UserList):
    def get_sum(self):
        return sum(self.data)
```

### 8. UserString

**Example 1**: A string that can't be modified.
```python
class ImmutableString(UserString):
    def __setitem__(self, key, value):
        raise TypeError("This string is immutable")
```

**Example 2**: A string with a method for removing vowels.
```python
class NoVowelsString(UserString):
    def remove_vowels(self):
        for vowel in 'aeiouAEIOU':
            self.data = self.data.replace(vowel, '')
```

**Example 3**: A string that tracks how many times it has been modified.
```python
class CountedString(UserString):
    def __init__(self, seq):
        super().__init__(seq)
        self.modifications = 0
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.modifications += 1
```

**Example 4**: A string that converts to uppercase when accessed.
```python
class LoudString(UserString):
    def __getitem__(self, key):
        return super().__getitem__(key).upper()
```

### 9. UserDict

**Example 1**: A dictionary that doesn't allow deletion.
```python
class NonDeletableDict(UserDict):
    def __delitem__(self, key):
        raise TypeError("Deletion not allowed")
```

**Example 2**: A dictionary with keys always stored as lowercase.
```python
class LowercaseDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
```

**Example 3**: A dictionary that logs accesses to its items.
```python
class LoggingDict(UserDict):
    def __getitem__(self, key):
        print(f"Accessing {key}")
        return super().__getitem__(key)
```

**Example 4**: A dictionary that automatically initializes missing keys.
```python
class AutoInitDict(UserDict):
    def __missing__(self, key):
        self[key] = AutoInitDict()
        return self[key]
```

These examples demonstrate various ways you can use the specialized collection classes from Python's `collections` module to simplify your code and implement functionality efficiently.
