# Instagram Analytics

>Created by:- Pratiksha Shirsath, Yash Saini, Jasleen Kaur\
>Date:- 30 April 23

<br>

# Data Source

The create.sql script can be used to create all the tables in our database. We have a total of seven tables, and the data for these tables was generated using the instagram_data_generation.py and create_followee_follower_id.ipynb files. These scripts utilize the faker library in Python to generate synthetic data. \
To execute the script, you will need to provide the username and password, which are currently masked for security reasons. The data that was loaded into our database is stored as CSV files in the data subdirectory. These csv files can be used to import data directly into the database in pgadmin.

<br>

# Setting up instructions

To run the webpage on your local machine and display the data, the initial step is to ensure that all the necessary requirements are installed. To do this, follow these steps:
1. Open a command prompt or terminal.
2. Navigate to the directory where the requirements.txt file is located. You can use the cd command to change directories.
3. Once you are in the correct directory, execute the following command to install all the required dependencies:

> pip install -r requirements.txt

This command will read the requirements.txt file and install all the specified packages and their respective versions.

\
To run our webpage created using the Flask web framework for Python, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where the app.py file is located. You can use the cd command to change directories.
3. Once you are in the correct directory, execute the following command to run the Flask application:

> flask --app app run

4. After running the command, you should see output similar to the following:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

This means that the Flask application is now running on your localhost at http://127.0.0.1:5000/. You can open your web browser and visit this address to view your webpage. 

<br>

# Folder and Files descriptions

>In the main directory, you will find a PDF report named "Milestone2.pdf." This report serves as our team's final report and contains relevant information about our project. Additionally, there is a demo video available where we provide a detailed explanation of the data we have loaded into our database and how our frontend interacts with the database. The video offers insights into the functionality and connectivity of our application.

<br>

>In the "data" subdirectory, you will find the "create.sql" file, which can be utilized in pgAdmin to create the schema for all the tables. The synthetic data was generated using the "instagram_data_generation.py" and "create_followee_follower_id.ipynb" files. Additionally, there are seven CSV files present in the directory. These CSV files contain the data that has been loaded into our database. 

<br>

>In the "frontend" subdirectory, you will find all the necessary subdirectories and files that are required to run our webpage on localhost. The specific instructions on how to run the webpage were provided in a previous section. Please refer to the earlier instructions to set up and run the webpage successfully.

\
**THANK YOU**







