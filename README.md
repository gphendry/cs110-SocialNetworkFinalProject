# Introduction to Computer Science I - Social Network Final Project

A repository containing all of the files for my final Python project for the Introduction to Computer Science I class that I took Spring Semester 2017 at USF. 

The project is a primitive command-line simulation of a basic social network with a text-based menu and user I/O system using a local CSV file to store the network's data in between sessions. 

**Network user data is initialized and stored from network.csv**

Program created by Graham Hendry between 5/4/2017 and 5/6/2017

Figuring out the overall design of the program was tough and I ended up redesigning the whole thing a few times until I found something viable.

The CSV-based data storage/access system I ended up going with became more complicated than I thought it was going to be due to special cases and defensive programming.

I would have liked to rely less on file input/output but it was the only way I found to ensure changes were always saved when exiting or switching users.


Resources Used:

- Python for Everyone

- Python 3 Documentation for CSV read/write usage
