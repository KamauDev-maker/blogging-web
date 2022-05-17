# Pitch Perfect
## Author

[Oscar Kamau](https://github.com/KamauDev-maker)

# Description
This is a for personal blogging website where you can create and share your opinions and other users can read and comment on them.



## Live Link
[Blog Post](https://blogsk2022.herokuapp.com/)


## User Story
-  Can add a category and post a pitch about that category
* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on  pitch they have viwed by giving it a upvote or a downvote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all quote, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches and a  commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository
2. Move to the folder and install requirements
  ```bash
  cd pitch perfect
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.9 manage.py server
  ```
5. Testing the application
  ```bash
  python3.9 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used
[Python3.9](https://docs.python.org/3/ "Python3.9")
[Flask](https://flask.palletsprojects.com/en/2.1.x/ "Flask")
[Heroku](https://devcenter.heroku.com/categories/reference "Heroku")


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [oscarnjenga@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Oscar Kamau*
