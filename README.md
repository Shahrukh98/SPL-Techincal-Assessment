# SPL-Techincal-Assessment

## Introduction :

<<<<<<< HEAD
**This repository is designed and created to test the basic, advanced and challenging
technical skills for the new recruits.
Remains the intellectual property of System Plus Pvt. Limited.**
=======
**Assessment branch contains the problems that you need to solve and all
the problems are converted to basic, adavanced and OOP. Each folder has
a separate Readme.md file. Basic and Advanced problems are mostly functional.
Solve them in the order you prefer.**
>>>>>>> b511a06eb114ea8d2311a7dee966332b02ecd3e8

## Basic Assessment:

<<<<<<< HEAD
**In the field of Computer Science, we have different programmaing paradigms, patterns and approaches to problem solving. You will be majorly tested on these listed programming paradigms.**

#### Imperative Programming:

_Imperative Programming is a programming paradigm that uses statements that_
_change a program's state. In much the same way that the imperative mood in_
_natural languages expresses commands, an imperative program consists of_
_commands for the computer to perform. Imperative programming focuses on_
_describing how a program operates._

_e.g. Object Oriented Programming, Procedural Calls, Polymorphic Algorithms etc._

#### Declarative Programming:

_In Computer Science, declarative programming is a programming paradigm,_
_a style of building the structure and elements of computer programs that_
_expresses the logic of a computation without describing its control flow._

_e.g. Functional Programming, Inductive Logic, Concurrent Logic etc.._
=======
### Arrays

1. Array Left Rotation
2. Array Reversal

### Dictionaries And Hashmaps

1. Shared SubStrings between Two Strings
2. Comparison of Two dictionaries/maps for equality

### Sorting
>>>>>>> b511a06eb114ea8d2311a7dee966332b02ecd3e8

1. Distribute a set of Numbers around given pivot.
   _(Make a good choice for sorting algorithm)_
2. Find maximum number from a list of numbers (both negative and non-negative).
   _(Make a good choice for sorting algorithm)_

<<<<<<< HEAD
1. This repository has a branch name Assessment. Clone this repository
   and checkout to Assessment branch.

2. You are not allowed to push code to this repository. Therefore you are
   required to create a copy of this repository on your own account and work on it.
   Hint: Make good use of git clone, git fork, git plugins for vs code etc.

3. In Assessment branch there will be tasks in folders. Each task folder will have
   a descriptive name and will have Readme.md file, please read the instructions carefully
   and implement solutions.

4. A programming language of desired choice can be used to implement solution
   keeping the paradigms in mind i.e. Object Oriented Solutions are not implementable
   in Functional Programming Languages.

5. After you are done implementing a task, please add comments in the code file
   for clear understanding and edit Readme.md file at the end of it with a heading
   "Run Instructions" and write the command required to run your file to test it.

6. This will be an open ended programming exercise. Problem descriptions are
   provided and you are free to choose the programming language, although you will have
   to follow the paradigm instructed to solve that problem. You are allowed to write
   your own test cases where required to elaborate your approach.

7. In case of confusions, please contact us at our email.
=======
### String Manipulation & Trees

1. Compare the strands of two genomes report similarity index in percentages.
2. Remove a character from the entire string.

## Advanced

### Greedy Algorithms

1. Minimum absolute difference in an array.

### Search

1. Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
2. Find the frequency of numbers in a array.

### Dynamic Programming

1. Solve Fibonacci problem using memoization.
2. Find Longest Common SubSequence in two strings.

### Recursion And Backtracking

1. Calculate Mean of An Array using recursion.

## Object Oriented Programming

### Simple Learning Management System:

You are required to use Object Oriented Approach to design a Learning
Management System for students and professors.

A user of LMS has three data members: firstName, lastName, password and userName. (may be other
data members also). A user can sign in/sign out to LMS system.
A user of LMS can be a

1. Student
2. Instructor

A student has two additional data members: roll number and status (status can be freshman,
sophomore, junior and senior). A student can:

1.  View his own marks only
2.  View resources uploaded by instructor
3.  View roster of a course (list of students enrolled in a course + instructor(s) offering that course)
4.  View Assignments of a course

An instructor has two additional data members: designation and qualification. An instructor can:

1. Add/View Marks of all students enrolled in a course being taught by that teacher
2. Add/View Resources to a course tab
3. View roster of a course (list of students enrolled in a course + instructor(s) offering that course)
4. Add/View Assignments of a course

A course has data members: courseName, courseCode and offeringSchool and capacity. (may be other
data members also).
You are free to add data members to any class. Make sure that you can’t declare data members of any
class public.

When a student logs in to LMS, (s)he will see the list of course tabs in which (s)he is enrolled in. On
navigating to particular course tab, a student can view list of resources, assignments, view list of
students enrolled in that course and can view his/her marks list only.
When an instructor logs in to LMS, he will see the list of courses being taught by him. On navigating to a
particular course tab, instructor can view list of resources, add a new resource item to resources list,
view list of assignments, add a new assignment to assignment list, add marks of students enrolled in that
course, view marks of all students enrolled in that course and view list of students enrolled in that
course. [For adding a new assignment/resource, instructor only adds name of assignment/resource or
some text as content. Obviously there will be a due date only for assignments.]
You have to implement concepts of inheritance and polymorphism in this assignment.

#### Requirements:

1. _Create Interfaces/Abstractions for Users and Course Class_.
2. _Create Interface/Abstractions for Student And Professor Class_.
3. _Proper Encapsulations for all the classes based on Functionality_
4. _Override a method getProfile in User class that will print status for Student_
   _and designation for a Professor_
   _i.e. for Student("Sohail Aslam","senior") getProfile_
   _prints Sohail Aslam is a senior student at LUMS_

   _And for a Professor("Habib-ur-Rehman","Assistant Professor") overridden_
   _getProfile will print Habib-ur-Rehman is Assistant Professor at LUMS_

5. _Overload operators if required._
6. _Thought Process and Approach in this problem should be well documented_
>>>>>>> b511a06eb114ea8d2311a7dee966332b02ecd3e8
