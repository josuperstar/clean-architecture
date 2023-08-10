## Description
This is a test project to show how we can use the 'Clean Architecture'
from Uncle Bob. To show how flexible and decouple it is, we are using
two different databases: one in SqlLite and the other in MySQL, both
of them using a different schema. For the user interface, we are using
both QT and Flask (HTML). The specificities on the databases and the user interfaces API have no
impact of the core implementation of the tools, proving that we can
keep the volatile details outside in an easy fashion.

## Requirements
- Python 3.8.1
- PySide 2
- Flask

## Run Flask in Powershell
cd clean-architecture\clean_architecture\frameworks\user_interface\flask
$env:FLASK_APP='app.py'

flask run

## Run QT app
Add the project folder to the python path, then run:

python clean-architecture\clean_architecture\frameworks\user_interface\qt\app.py

## UML
![uml.png](uml.png)
