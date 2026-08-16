# 💜 Python Beginner Notes

<span style="color:#9B6A8F;"><strong>A simple cheat sheet for the Python basics learned so far</strong></span>

---

## 🌸 1. Variables

A **variable** stores a value so you can use it later.

```python
model_name = "GPT-4"
accuracy = 94.7
is_deployed = True
version = 4
```

Unlike Java, Python does not require you to write the data type before the variable name.

**Java**
```java
int version = 4;
```

**Python**
```python
version = 4
```

> **Note:** Python decides the type from the value you assign.

---

## 🌷 2. Identifiers

An **identifier** is the name you give to a variable.

Valid examples:

```python
model_name = "GPT-4"
accuracy = 94.7
_version = 4
```

Invalid examples:

```python
2model = "GPT-4"      # starts with a number
model name = "GPT-4"  # contains a space
class = "GPT-4"       # class is a reserved word
```

> **Important:** An identifier can start with a letter or `_`, but not with a number.

Python commonly uses **snake_case**:

```python
model_name
version_number
is_deployed
```

---

## ✨ 3. Basic Data Types

| Type | Meaning | Example |
|---|---|---|
| `str` | text | `"GPT-4"` |
| `int` | whole number | `10` |
| `float` | decimal number | `94.7` |
| `bool` | true/false value | `True` |

Example:

```python
name = "GPT-4"
epochs = 10
accuracy = 94.7
deployed = True
```

> **Common Mistake:** `"10"` is a `str`, but `10` is an `int`.

---

## 📝 4. `type()`

`type()` tells you what data type Python thinks a value has.

```python
x = 10
print(type(x))
```

Output:

```text
<class 'int'>
```

Another example:

```python
name = "GPT-4"
accuracy = 94.7

print(type(name))
print(type(accuracy))
```

Output:

```text
<class 'str'>
<class 'float'>
```

---

## 🌸 5. Type Conversion

Sometimes a number arrives as text.

```python
raw_accuracy = "94.7"
raw_epochs = "10"
```

Convert them using:

```python
accuracy = float(raw_accuracy)
epochs = int(raw_epochs)
```

Now:

```python
print(type(accuracy))
print(type(epochs))
```

Output:

```text
<class 'float'>
<class 'int'>
```

> **Important:** `input()` and many file values arrive as strings, so conversion is often necessary.

---

## 💜 6. f-Strings

An **f-string** lets you place variables directly inside a sentence.

```python
name = "GPT-4"
accuracy = 94.7

print(f"{name} has an accuracy of {accuracy}")
```

Output:

```text
GPT-4 has an accuracy of 94.7
```

The `f` before the string is important:

```python
f"Hello {name}"
```

---

## 🌷 7. Arithmetic Operators

Given:

```python
x = 17
y = 5
```

| Operator | Meaning | Result |
|---|---|---|
| `+` | addition | `22` |
| `-` | subtraction | `12` |
| `*` | multiplication | `85` |
| `/` | normal division | `3.4` |
| `%` | remainder | `2` |
| `**` | power | `1419857` |
| `//` | whole-number division | `3` |

Example:

```python
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
```

### `/` vs `//` vs `%`

```python
17 / 5
```

Result:

```text
3.4
```

```python
17 // 5
```

Result:

```text
3
```

```python
17 % 5
```

Result:

```text
2
```

Think of it as:

```text
17 = (5 × 3) + 2
          ↑     ↑
         //     %
```

---

## ✨ 8. Assignment Operators

These operators update the current value of a variable.

```python
total = 0

total += 10
print(total)

total -= 3
print(total)

total *= 2
print(total)
```

Output:

```text
10
7
14
```

These are shortcuts:

```python
x += 3
```

means:

```python
x = x + 3
```

Similarly:

```python
x -= 3
x *= 3
```

---

# 💜 Strings

## 🌸 9. Strings

A **string** is text written inside quotes.

```python
model_name = "GPT-4"
```

Strings are **immutable**.

This means you cannot directly change one character inside a string.

```python
name = "GPT"
# name[0] = "B"   # Error
```

Instead, string methods create a **new string**.

---

## 🌷 10. String Methods

### `.strip()`

Removes extra whitespace from the beginning and end.

```python
name = " GPT-4 "
clean_name = name.strip()

print(clean_name)
```

Output:

```text
GPT-4
```

### `.upper()`

Makes letters uppercase.

```python
name = "gpt-4"
print(name.upper())
```

Output:

```text
GPT-4
```

### `.replace(old, new)`

Replaces part of a string.

```python
name = "GPT-4"
new_name = name.replace("-", "_")

print(new_name)
```

Output:

```text
GPT_4
```

You can also combine methods:

```python
model_name = " GPT-4 "
cleaned_name = model_name.strip().upper().replace("-", "_")
```

> **Important:** `.strip()`, `.upper()`, and `.replace()` return a new string. They do not change the original string by themselves.

---

## ✨ 11. `len()`

`len()` returns the number of characters in a string.

```python
name = "GPT_4"

print(len(name))
```

Output:

```text
5
```

`len()` also works with lists and tuples.

---

## 📝 12. Indexing

Python indexing starts from `0`.

```python
word = "Python"
```

```text
Index:  0 1 2 3 4 5
        P y t h o n
```

Examples:

```python
print(word[0])
print(word[1])
```

Output:

```text
P
y
```

---

## 🌸 13. Negative Indexing

Negative indexing counts from the end.

```python
word = "Python"
```

```text
Index:  -6 -5 -4 -3 -2 -1
         P  y  t  h  o  n
```

```python
print(word[-1])
```

Output:

```text
n
```

> **Remember:** `-1` means the last item.

---

## 🌷 14. String Slicing

Slicing extracts part of a string.

Syntax:

```python
s[start:end]
```

The `end` index is **not included**.

Example:

```python
s = "Python"

print(s[0:3])
```

Output:

```text
Pyt
```

It takes indexes:

```text
0, 1, 2
```

but stops before `3`.

### Reverse a String

```python
s = "Python"

print(s[::-1])
```

Output:

```text
nohtyP
```

The general slicing form is:

```python
s[start:end:step]
```

`-1` as the step means move backwards.

---

# 💜 Lists

## 🌸 15. Lists

A **list** stores multiple values in order.

```python
scores = [0.71, 0.85, 0.63, 0.90, 0.78]
```

Lists are **mutable**, so their contents can be changed.

---

## 🌷 16. `.append()`

`.append(value)` adds a new item to the end of a list.

```python
scores = [0.71, 0.85, 0.63]

scores.append(0.90)

print(scores)
```

Output:

```text
[0.71, 0.85, 0.63, 0.9]
```

---

## ✨ 17. Editing a List Item

Because lists are mutable, you can change an item using its index.

```python
scores = [0.71, 0.85, 0.63]

scores[0] = 0.75

print(scores)
```

Output:

```text
[0.75, 0.85, 0.63]
```

---

## 📝 18. List Indexing and Negative Indexing

```python
scores = [0.71, 0.85, 0.63, 0.90]
```

```python
print(scores[0])
```

Output:

```text
0.71
```

```python
print(scores[-1])
```

Output:

```text
0.9
```

`-1` means the last item.

---

## 🌸 19. List Slicing

Slicing works with lists too.

```python
scores = [0.71, 0.85, 0.63, 0.90, 0.78]
```

Get the last three items:

```python
print(scores[-3:])
```

Output:

```text
[0.63, 0.9, 0.78]
```

`-3:` means:

> Start from the third item from the end and continue to the end.

---

## 🌷 20. List Length

Use `len()` to count the items.

```python
scores = [0.71, 0.85, 0.63]

print(len(scores))
```

Output:

```text
3
```

---

# 💜 Tuples

## ✨ 21. Tuples

A **tuple** is similar to a list, but it cannot be changed after creation.

```python
scores = (0.71, 0.85, 0.63)
```

A tuple uses:

```text
( )
```

A list uses:

```text
[ ]
```

---

## 📝 22. Lists vs Tuples

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable? | Yes | No |
| Can change an item? | Yes | No |

List:

```python
numbers = [1, 2, 3]
numbers[0] = 10
```

This works.

Tuple:

```python
numbers = (1, 2, 3)
# numbers[0] = 10
```

This gives an error.

> **Important:** Tuples are **immutable**.

---

## 🌸 23. Converting Between Lists and Tuples

### List → Tuple

```python
numbers = [1, 2, 3]

numbers_tuple = tuple(numbers)

print(numbers_tuple)
```

Output:

```text
(1, 2, 3)
```

### Tuple → List

```python
numbers = (1, 2, 3)

numbers_list = list(numbers)

print(numbers_list)
```

Output:

```text
[1, 2, 3]
```

---

# 💜 Dictionaries

## 🌷 24. Basic Dictionary Usage

A **dictionary** stores values using **keys**.

```python
model = {
    "name": "GPT-4",
    "accuracy": 94.7
}
```

Here:

```text
"name"      → key
"GPT-4"     → value

"accuracy"  → key
94.7        → value
```

---

## ✨ 25. Add or Update a Dictionary Item

Add a new key:

```python
model["version"] = 4
```

Now:

```python
print(model)
```

Output:

```text
{'name': 'GPT-4', 'accuracy': 94.7, 'version': 4}
```

If the key already exists:

```python
model["accuracy"] = 96.2
```

Python updates its value.

> **Remember:**  
> New key → add  
> Existing key → update

---

# 💜 Other Useful Basics

## 🌸 26. Swapping Variables

Python can swap two variables without a temporary variable.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

In Java, you would normally use a temporary variable. Python makes the swap shorter.

---

# 💜 Quick Revision

```python
# Variables
name = "GPT-4"
accuracy = 94.7
version = 4
deployed = True

# Type checking
type(name)

# Type conversion
int("10")
float("94.7")

# f-string
f"Hello {name}"

# Arithmetic
x + y
x - y
x * y
x / y
x % y
x ** y
x // y

# Assignment operators
x += 3
x -= 3
x *= 3

# String methods
s.strip()
s.upper()
s.replace("-", "_")

# Length
len(s)

# Indexing
s[0]
s[-1]

# Slicing
s[0:3]
s[::-1]

# Lists
scores.append(0.90)
scores[0] = 0.75
scores[-1]
scores[-3:]

# List and tuple conversion
tuple(my_list)
list(my_tuple)

# Dictionary
d["key"] = value

# Swap
a, b = b, a
```

### 💜 Remember These

| Concept | Key Idea |
|---|---|
| `"10"` | string |
| `10` | integer |
| `94.7` | float |
| `True` | boolean |
| Index `0` | first item |
| Index `-1` | last item |
| `s[0:3]` | indexes 0, 1, 2 |
| `/` | normal division |
| `//` | whole-number division |
| `%` | remainder |
| String | immutable |
| List | mutable |
| Tuple | immutable |

---

# 🌸 Mini Practice

1. Create variables for a model name, accuracy, version, and deployment status. Print each value with its type.

2. Convert `"88.5"` to a float and `"15"` to an integer, then print them in one f-string sentence.

3. Create the string `" Python-Model "`, remove the spaces, make it uppercase, replace `-` with `_`, and print the first six characters.

4. Create a list containing five scores, append one new score, change the first score, and print the last three scores.

5. Create a list of three numbers, convert it to a tuple, convert it back to a list, then create a dictionary and add one new key-value pair.

---

<span style="color:#9B6A8F;"><strong>💜 Keep practicing small examples — Python gets easier very quickly when the syntax becomes familiar.</strong></span>
