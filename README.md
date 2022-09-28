1 Running instructions 

psql -d gym_manager -f db/gym_manager.sql

python3 console

flask run

Then go to  http://127.0.0.1:5000/
Although look at the terminal after you run “flask run” that “5000” there might be different.


2 Brief

Gym
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP
The app should allow the gym to create and edit Members
The app should allow the gym to create and edit Classes
The app should allow the gym to book members on specific classes
The app should show a list of all upcoming classes
The app should show all members that are booked in for a particular class
Inspired By
Glofox, Pike13

Possible Extensions
Classes could have a maximum capacity, and users can only be added while there is space remaining.
The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.

3 Technologies used

Python, PostgreSQL, Jinja, CSS, Flask, HTML