# Rasa_bot_backend
Django backend for the Rasa_bot

# How to Set up
* Git clone the repository
* Enter into the folder Rasa_bot_backend
* Create a python environment and name it virtual
* Run the command:
    * pip install -r requirements
* Ask the administrator for the env contents
* Run the app!!!

# How to use the api to perform CRUD functions
#Pre-requisites:
    * Run python manage.py runserver
    * Connect to the Mongo DB, USIUdb_chatbot
    * Run Postman and feed the port number in the url
    * Item can be Student/Course/Faculty/Assignment
    * Items can be Students/Courses/Assignments
    * id can be stdId, crsId, ftyId, asgmtId

# To GET One Record:
    * In Postman, add /getOneItem/id in the url then select body then none then click send

# To GET All Records:
    * In Postman, add /getAllItems in the url then select body then none then click send

# To POST a Record:
    * In Postman, add /createItem in the url the select body and then form then enter the table's fields in the key section and the data you wanna add in the value section then click send

# To PUT a Record:
    * In Postman, add /updateItem in the url and select the body then raw to add input in JSON format with the same id as the item you wanna update but different content in the rest of the other fields then click send

# To DELETE a Record:
    * In Postman, add /deleteItem/id in the url and select body then none then click send

# How to contribute
* Make sure to work on a different branch other than main
* Make sure the features you work are not the same as those of team members
* Always update main and then rebase with you branch before pushing the code to git hub
* Raise a pull request and tag the admin to review
