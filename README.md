# Britecore Hiring Assignment - Seif Elmughrabi

## Demo
[here.](https://brightcoreassignment.pythonanywhere.com/)

## ER Diagram
[here.](https://docs.google.com/drawings/d/1-Jn1S1-FXbYzKDbg8uk2qdep7qzh9Z4MBR3wGt4HD4Q/edit?usp=sharing)

## Tech stack.

Backend:
SQLAlchemy + Flask

Frontend:
VueJS + Materialize.css

## Techstach discussion
Instead of using ORM, I used SQLAlchmy's Metadata which is a collection object that can hold the *description* of a set of tables as Python
data structure. Tables can then be created and traversed in a similar manner to an XML DOM.

Why?
Metadata makes it possible to create and interact with the tables it holds *programtically*, instead of creating ORM representational classes
upfont.
In a production environment, each user can be assigned a Metadata object that can hold all the tables of the *risks* she has chosen for her
bespoke insurance policy.

## Shortcomings/Limitations
1. Validation is implemented in a user-friendly manner. However, if table names are not unique the error shows in the browser console.
1. In order to reset the tables for each submission, there needs to be WSGI touch command which is not yet implemented. If you'd like to reset
tables, please email me.
2. The app is resposnive. However, it is best viewed on a computer.

## Questions
For questions, email me at: [seif@seif.rocks](mailto:seif@seif.rocks) 
