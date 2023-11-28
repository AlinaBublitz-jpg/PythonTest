# Python Project

## 1. TASK DEFINITION

The following task is available for the term paper.
The starting point for the term paper is the study script, the contents of which represent the basic knowledge
required for the in-depth consideration of the following question. It is expected that further literature
sources on this question will be researched and processed in the term paper.

**1.1 The task**
You will receive:

1. A) 4 training data sets
2. B) a test data set
3. C) a data set that describes 50 ideal functions

All data consists of x-y pairs. The structure in the CSV files is as follows:

| x   | y   |
| --- | --- |
| x1  | y   |
| ... | ... |
| xn  | yn  |

Your task is to write a Python program that uses the four training data sets (A) to find the four best fits from
the data set of 50 ideal functions (C). The following criteria should be observed:

1. The criterion for selecting ideal functions for the training data set is the minimization of the sum of
   all quadratic y-deviations (least square).
2. Your program must use the test data set B to validate the selection. For each x-y pair in the test data set,
   the program should check whether the values match the four ideal functions.
   a. Use a criterion which ensures that the maximum deviation between the previously determined
   ideal function and the test values does not exceed the maximum deviation between the training
   data (A) and the four ideal functions from (C) by more than the factor _root of two_ (sqrt(2)).
   b. If the test data can be adapted to the four functions you have found, save the corresponding
   deviations for each test data set.
3. All data should be visualized logically.
4. Write unit tests wherever possible.
   In order to demonstrate the skills you have learned in the course, you must fulfill the criteria outlined in the
   following chapter (details).

**1.2 Details database and tables**

- You will receive four training data sets in the form of CSV files. Your Python program must be able to
  to independently compile an SQLite database (file), ideally via sqlalchemy, and load the training data
  into a single, five-column table. The first column shows the x-values of all

```
Functions. Table 1 at the end of this subsection shows you what structure your table will probably
have.
```

- The fifty ideal functions, which are also provided via a CSV file, must be loaded into another table.
  Similarly, the first column shows the x-values, which means that there are 51 columns in total. Table
  2 at the end of this subsection describes schematically which structure is expected.
- After the training data and the ideal functions have been loaded into the database, the test data (B)
  must be loaded line by line from another CSV file and - if it fulfills the criterion in subsection 2 - saved
  with one of the four matched functions.
- The results must then be stored in another four-column table in the SQLite database. According to
  Table 3 at the end of this subsection, this table contains four columns with x and y values as well as
  the correspondingly selected ideal function and the associated deviation.
- Finally, the training data, the test data, the selected ideal functions and the corresponding assigned data sets are visualized under an appropriately selected representation of the deviation.

**1.3 Structure of the Python program**

- The program should be object-oriented as far as possible.
- It should have at least one inheritance hierarchy.
- Use both standard and user-defined exception handling.
- You should use Pandas for the program logic, but also visualization using Bokeh, matlibplot, etc.
- Write unit tests wherever possible.
- Document your program completely and make use of docstrings.

**Use of Git**

- Please use Git for version control of your code.

**Table 1: Training data database table**

| X   | Y1 (Training function) | Y2 (Training function) | Y3 (Training function) | Y4 (Training function) |
| --- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| x1  | y11                    | y21                    | y31                    | y41                    |
| ... | ...                    | ...                    | ...                    | ...                    |
| xn  | y1n                    | y2n                    | y3n                    | y4n                    |

**Table 2: Table of ideal functions**

| X   | Y1 (ideal function) | Y2 (ideal function) | ... | Y50 (ideal function) |
| --- | ------------------- | ------------------- | --- | -------------------- |
| x1  | y11                 | y21                 | ... | y51                  |
| ... | ...                 | ...                 | ... | ...                  |
| xn  | y1n                 | y2n                 | ... | y5n                  |

**Table 3: Test data table**

| X (Test function) | Y1 (test function) | Delta Y (deviation) | Number of the ideal function (e.g. Funk37) |
| ----------------- | ------------------ | ------------------- | ------------------------------------------ |
| x1                | y11                | y21                 | Funk37                                     |
| ...               | ...                | ...                 | ...                                        |
| xn                | y1n                | y2n                 | y3n                                        |

**1.3. Notes**
The data set for this assignment will be made available on request for each individual student. Therefore, a ticket
should be opened for the tutor, whereupon access to the data is granted. A copy will be sent to the responsible
persons - this will prevent later manipulation by the students.
It is expected that your entire source code is included in the appendix of your written assignment so that your
entire program, including output, can be tested. Your input data is not required.
The aim is to fully reconstruct your work, your decisions and your assessment of the task result through your
submission.

## 2. ADDITIONAL INFORMATION ON THE ASSESSMENT OF THE HOMEWORK

The assessment criteria and explanations listed in the examination guide should be taken into account when
designing and writing the term paper.
With regard to **introduction and thematic delimitation,** care should be taken to ensure that these are
demonstrated in the chosen approach to the task.
The evaluation of the **structure** refers to the design of the program, class structure, choice of generalizations in the
program and the composition of the program.
In the **argumentation,** the final functionality and the correctness of the execution of the program are
evaluated.
The **conclusion** should be a scientifically adequate text and a discussion of the advantages and disadvantages of
the chosen solution approach, in particular a discussion of the differentiation from other possible solutions,
the program structure and the modules and frameworks that were used for the solution.

## 3. SUPERVISION PROCESS

In principle, several channels are available for the supervision of term papers. The use of these channels is your
own responsibility. The tutor is available by e-mail for technical consultations on the choice of topic on the one
hand and for formal and general questions about academic work on the other. However, the tutor is not expected
to approve outlines, parts of texts or drafts, as the independent preparation is part of the examination work to be
performed and is included in the overall assessment. However, tips on draft outlines are provided to make it easier
t o start structuring an academic paper.

## PLAN

1. Import necessary libraries (pandas, numpy, matplotlib, sqlalchemy, etc.)
2. Define a class DataHandler to handle all data-related tasks:
   1. Define a method load_csv_to_db to load CSV files into SQLite database using sqlalchemy.
   2. Define a method get_data_from_db to retrieve data from the SQLite database.
3. Define a class DataAnalyzer that inherits from DataHandler to handle data analysis tasks:
   1. Define a method find_best_fit to find the best fit from the dataset of 50 ideal functions.
   2. Define a method validate_selection to validate the selection using the test dataset.
   3. Define a method save_deviation to save the corresponding deviations for each test dataset.
4. Define a class DataVisualizer to handle data visualization tasks:
   1. Define a method visualize_data to visualize all data logically.
5. Define a class UnitTest to handle unit testing:
   1. Define various methods to test each functionality of the program.
6. In the main function:
   1. Create an instance of DataHandler and load all CSV files into the SQLite database.
   2. Create an instance of DataAnalyzer and perform data analysis tasks.
   3. Create an instance of DataVisualizer and visualize all data.
   4. Create an instance of UnitTest and perform unit testing.
