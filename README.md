# Puppy adoption REST website design using Python Flask

## Project Description:
This project aims at using the powerful REST Python framework "Flask" for building a website used for :-
- Adding a puppy to database
- Deleting a puppy fron database
- Associating a puppy with an owner
- Adding a new owner with Puppy ID
- Listing the number of puppies

![alt text](https://github.com/grv231/Puppy-adoption-PythonFlask/blob/master/Images/HomePage.jpg "Home_Page")

## Project Setup
Copy the required files in a directory. Then use the following steps to setup the project:

1. Create an optional virtual environment for flask project.
2. Install python for running the project. (I have used Anaconda distribution here)
3. Use the **requirements.txt** file for installing the dependencies. Use the following command for dependencies installation:
   *pip install -r requirments.txt*
4. Test the installation by using the command *import flask*
5. Change the directory to the folder where the files have been cloned/downloaded.
6. Use the following commands to initiate the project

```python
flask db init

flask db migrate -m "<Custom Message>"

flask db upgrade
```
7. Initiate the python project using the following command: **python app.py**
8. Finally, test the project using - http://127.0.0.1:5000

