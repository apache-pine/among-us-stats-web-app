# Overview

I love data science and I am passionate about learning more about it. I often have questions about the data that I see all around me in my day to day life. This app was born out of that curiosity and from a passion to learn more about the technology surrounding data science.

The purpose of this app is to provide an interface to more easily interact with a cloud database that I created. The database contains information about individual matches of Among Us played by a streamer named Kyr_Sp33dyy and his friends. While watching them one day, I was mentally questioning the odds of each player winning as each role. I wanted to know how accurate a machine learning algorithm would be at determining the outcome of games given enough data. I decided to create a database to store the data. Eventually, I wanted an easier way to interact with the data and this app was born.

The secondary, and perhaps more profound and important purpose of this app, was to provide myself with a project with requirements beyond my knowledge and abilities at the time of starting the project. This was an excuse and a means for me to learn how to use Django and to interact with cloud databases through a web application. I had previously created a python app to interact with my database, but I didn't have a GUI with that app. Through building a web app, I was able to learn how to use Django and build a web app which provides a GUI for interacting with the database more easily and more intuitively.

The app is easily run from a computer using Django and the command prompt or a terminal in an IDE. Once the app is installed, a user can start the server using the following command: `python manage.py runserver`. Once the server is running, the user can navigate to the first page of the app by opening a web browser and navigating to `http://127.0.0.1:8000/stats/main/`. The user can then navigate through the app by clicking on the links provided on each page in the navigation bar. Below is a link to a video demonstration starting and navigating through the app.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

There are three main pages, each of which have a few subpages. The three main pages are:

- Home found at `http://127.0.0.1:8000/stats/main/`
- Insert found at `http://127.0.0.1:8000/stats/insert/`
- Query found at `http://127.0.0.1:8000/stats/query/`

The home page is dominated by a large table showing the summary of the most recent game recorded in the database. This entire table is created dynamically through querying the database and displaying the results in the table. Below this table are small boxes that display the players and roles with the most kills, most deaths, most wins and most losses. The names and  numbers in each box are created dynamically. If the user clicks on any of the titles of the boxes they will see a subpage of the homepage that displays a table with the totals of the given stat for each player or role. For example, if the user clicks on the heading for the box `Player with the Most Wins` they will be shown a new home page that shows a table with the total number of wins for each player. 

The next page, the `insert` page, starts by displaying a short message and two buttons. In this web app, the user only has access to insert data into two tables, the `match` table and the `match_results` table. There is a button that will take the user to a new `insert` page displaying a form generated through Django. The form is based on whichever table was selected, so it has constraints and validation checks on each field to ensure the data is valid. The user can then fill out the form and submit it. The data is then inserted into the database. The user can then navigate back to the `insert` page and reselect the table they want to insert data into.

The last page is the `query` page. This one is the most simple for now, however there are big plans in the future for this page. Currently, there is only one input field and it is for players. The user can enter a player's name and then click the `Submit` button. The page will then display a table with the player's name, id, and alias (if any). This is all the `query` page currently does, but there is much more planned for this page. Eventually, this page will be where a user can input the information for a player and the app will query the database to determine the player's chances of winning the game. Other queries will also be possible in the future.

# Development Environment

The following tools, languages, libraries, and frameworks were used to develop this software:
- Django
- PyMySQL
- Python
- HTML
- CSS
- Javascript
- Visual Studio Code
- MySQL Workbench
- Amazon Web Services (AWS) Relational Database Service (RDS)

# Useful Websites

- [Django Documentation](https://docs.djangoproject.com/en/4.1/)
- [PyMySQL Documentation](https://pymysql.readthedocs.io/en/latest/index.html)
- [Python Documentation](https://docs.python.org/3/)
- [TutorialsPoint Django Tutorial](https://www.tutorialspoint.com/django/index.htm)
- [Python Django Tutorial for Beginners](https://www.youtube.com/watch?v=rHux0gMZ3Eg&ab_channel=ProgrammingwithMosh)
- [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4)

# Future Work

- More queries for the `query` page.
- More data to be inserted into the database. The database is still pretty empty.
- More pages to be added to the app.
    - A page to update data in the database.
    - A page to delete data from the database.
- A more robust and secure database.
- A more robust and secure web app.
- The ability to insert data into more tables.
- Improve visuals of the web app.
- Add graphs and charts to the web app.
