# Britecore Hiring Assignment - Seif Elmughrabi

## Demo
[here.](https://brightcoreassignment.pythonanywhere.com/)

## ER Diagram
[here.](https://docs.google.com/drawings/d/1-Jn1S1-FXbYzKDbg8uk2qdep7qzh9Z4MBR3wGt4HD4Q/edit?usp=sharing)

## Intro
The idea is to help insurance companys' clients to freely choose what to insure.

For example, instead of choosing what to insure from a list, built on a regimented database, like: House, Golf Course, School building ...etc. They can set what to ensure *themselves* whether it's Automobile Policies, Cyber Liability Coverage (protection against hacking), or Prize Insurance (if someone gets a $1 million hole-in-one prize at a golf tournament, the golf course doesn't pay it, they have an insurance policy to cover them).

## Tech stack.

Backend:
SQLAlchemy + Flask

Frontend:
VueJS + Materialize.css

## Tech stack discussion
### Backend
Instead of using ORM, I used SQLAlchemy's Metadata which is a collection object that can hold the *description* of a set of tables as Python
data structure. Tables can then be created and traversed in a similar manner to an XML DOM.

Why?
Metadata makes it possible to create and interact with the tables it holds *programtically*, instead of creating ORM representational classes
upfont.
In a production environment, each user can be assigned a Metadata object that can hold all the tables of the *risks* she has chosen for her
bespoke insurance policy.

### Frontend
For frontend I used VueJS (as required by the assignment) so that the client has the freedom of insuring as many risks as she wants with as many fields as desired. Fields are bits of data like first name, age, zip code, model, serial number...etc.

I also used a bit of Materialize.css for some styling.

## Questions
For questions, email me at: [seif@seif.rocks](mailto:seif@seif.rocks) 
