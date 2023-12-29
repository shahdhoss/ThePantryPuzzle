# ThePantryPuzzle
    Our Project Idea: Our project idea mainly focuses on recommending and finding different recipes for the user as they enter the ingredients
    they have. Users can be divided into 2 categories: chef (recipes provider), and customer (the one searching for the recipes). Chefs can add
    whatever recipes they want and gain insights about how well a recipe is from the customer trials. In addition to adding ingredients and recipe
    searching, customers can provide reviews and ratings for each recipe. Moreover, customers can share the results of each recipe with the
    community.

# Installation
1) Download and install Python v3.10 from the official website: https://www.python.org/downloads/.

2) Clone the repository or download the source code.

3) Install the required libraries using the following commands:

```bash
pip install flask
pip install flask_login
pip install werkzeug
pip install Flask-SQLAlchemy
pip install requests
```
Note: The sqlite3 library is not required to be installed separately as it is included in the Python standard library.

# How to create the database
1) you can create the MainDB by running the files in the "add_all_to_main_db" folder, all you have to do is change the path of the sqlite3 connection and then, it will create the tables needed and save the database in the chosen path 
2) you can insert, delete and fetch the data from the database by running the functions in the "database.py" file in the controllers folder, just call the functions 

# How to run the project
    make sure that no files are missing and the paths changed to your correct paths and run the "main.py" from the integrated terminal or from the external terminal by running the following "<your file path> 
   ```bash
    python main.py
```

# Competitve Analysis
![Competitive Analysis](<system_designs/Competitive Analysis.png>)
# Technical Approach
    Project Setup (MPA):
    Multi-Page Application: it is SEO friendly, compatible with a wider range of web browsers, a more straightforward development process.
    Front-end: HTML, CSS
    Back-end: Python
    Framework: Flask
    API: EdammamAPI
    Database: to store the scraped recipe data (SQL databases)

# Risk Mitigation 
    How users respond is a great risk to our business, as our service is built upon users interacting and rating each other’s recipes. 
    The main concern is that other users review bombing chefs' recipes they don't like, which could be avoided 
    by verifying reviews before posting them through a captcha verification system.

# Feasibility Matrix
![Feasibility Matrix](<system_designs/Feasibility Matrix.png>)

# Context Diagram
![Context Diagram](<system_designs/Context Diagram.png>)

# Class Diagram
![Class Diagram](<system_designs/Class Diagram.png>)

# Use Case Diagrams
![Use Case](<system_designs/Use Case.png>)
