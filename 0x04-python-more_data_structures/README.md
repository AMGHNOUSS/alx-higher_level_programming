0x04. Python - More Data Structures: Set, Dictionary
=============================================

-   By Guillaume

Resources
---------

**Read or watch**:

-   [Data structures](https://intranet.alxswe.com/rltoken/GmgoSUtBbHBW8suWkws51g")
-   [Lambda, filter,reduceand map](https://intranet.alxswe.com/rltoken/53f4kKVT0-jyzrJstOSJWg")
-   [Learn to Program 12 : Lambda map Filter Reduce](https://intranet.alxswe.com/rltoken/v9eyFryhkYmxDI13iTx2VA")

**man or help:**
-   [python3]

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/qZrNhvUqi5zcqE4cMFGU6Q "explain to anyone"), **without the help of Google**:

### General

-   Why Python programming is awesome
-   What are sets and how to use them
-   What are the most common methods of set and how to use them
-   When to use sets versus lists
-   How to iterate into a set
-   What are dictionaries and how to use them
-   When to use dictionaries versus lists or sets
-   What is a key in a dictionary
-   How to iterate over a dictionary
-   What is a lambda function
-   What are the map, reduce and filter functions

Copyright - Plagiarism
----------------------
-   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
-   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
-   You are not allowed to publish any content of this project.
-   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version 2.7.*)
-   All your files must be executable
-   The length of your files will be tested using `wc`

Tasks
-----

### 0\. Squared simple

mandatory

Write a function that computes the square value of all integers of a matrix.
-   Prototype: `def square_matrix_simple(matrix=[]):`
-   `matrix` is a 2 dimensional array
-   Returns a new matrix:
    -   Same size as `matrix`
    -   Each value should be the square of the value of the input
-   Initial matrix should not be modified
-   You are not allowed to import any module
-   You are allowed to use regular loops, `map`, etc.

```
ume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x03-python-more_data_structures`
-   File: `0-square_matrix_simple.py`
