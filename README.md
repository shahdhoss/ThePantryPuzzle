# ThePantryPuzzle
    Our Project Idea: Our project idea mainly focuses on recommending and finding different recipes for the user as they enter the ingredients
    they have. Users can be divided into 2 categories: chef (recipes provider), and customer (the one searching for the recipes). Chefs can add
    whatever recipes they want and gain insights about how well a recipe is from the customer trials. In addition to adding ingredients and recipe
    searching, customers can provide reviews and ratings for each recipe. Moreover, customers can share the results of each recipe with the
    community.

# Installation
    Download the required libraries
    - flask
    ```bash
        pip install flask
    ```
    - sqlite3 --> https://www.sqlite.org/download.html 
    - flask_login
    ```bash
        pip install flask_login
    ```
    - werkzeug.security
    ```bash
        pip install werkzeug
    ```
    - flask_sqlalchemy
    ```bash
        pip install Flask-SQLAlchemy
    ```
    - requests
    ```bash
        pip install requests
    ```
# How to create the database
    - you can create the MainDB by running the files in the "add_all_to_main_db" folder, all you have to do is change the path of the sqlite3 connection and then, it will create the tables needed and save the database in the chosen path 
    - you can insert, delete and fetch the data from the database by running the functions in the "database.py" file in the controllers folder, just call the functions 

# How to run the project
    - make sure that no files are missing and the paths changed to your correct paths and run the "main.py" from the integrated terminal or from the external terminal by running the following "<your file path> 
    ```bash
    python main.py
    ```

# Competitve Analysis
![Competitve Analysis](<https://github.com/malak-elbanna/ThePantryPuzzle/blob/main/System%20Designs/Competitive%20Analysis.png>)

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
![Alt text](<https://github.com/malak-elbanna/ThePantryPuzzle/blob/main/System%20Designs/Feasibility%20Matrix.png>)

# Context Diagram
![Context Diagram](<https://github.com/malak-elbanna/ThePantryPuzzle/blob/main/System%20Designs/Context%20Diagram.png>)

# Class Diagram
![Class Diagram](<https://github.com/malak-elbanna/ThePantryPuzzle/blob/main/System%20Designs/Class%20Diagram.png>)

# Use Case Diagrams
![Use Case](<https://github.com/malak-elbanna/ThePantryPuzzle/blob/main/System%20Designs/Use%20Case.png>)
