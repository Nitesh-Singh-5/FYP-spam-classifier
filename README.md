## Overview
How often have we received messages informing us that we have won a trip to Hawaii, a million dollars, or a cash prize? Smishing is a type of text-message scam. A lot of the time, they ask us to fill out forms and give them our personal information or SSN number, which is suspicious and almost always a scam. The goal of this project is to use Machine Learning to accurately classify whether a message is spam or not.

## Spam Classifier: Project Description
Spam Classifier is a text-classification app which detects whether the message/email is a spam or not. we have used Naive-Bayes along with NLP (TF-IDF, Bag of Words and more). <br>
To acquire additional data for an experiment, We have merged two datasets (Enron email spam/ham and SMS spam classification) into one.
The system will be developed in Python using popular machine learning libraries such as Scikit-Learn and Tensorflow.

The spam detection system will have two main components: the training component and the prediction component. The training component will use a dataset of labeled emails to train the machine learning model. The labeled emails will be used to identify the characteristics of spam emails, which will then be used to develop the machine learning algorithm.

Once the model has been trained, the prediction component of the system will be used to classify new incoming emails as either spam or not spam. The system will analyze the email's content and characteristics and compare them with the learned characteristics of spam emails. Based on this comparison, the system will generate a probability score for the email being spam. If the score is above a certain threshold, the email will be classified as spam.
<br>

### Built With

1. Python 3.6
2. Django 2.1+
3. Scikit-Learn
4. Numpy
5. Pandas
6. Matplotlib
7. Seaborn
8. HTML5
9. CSS
10. Bootstrap-v4
11. Javascript


### Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Nitesh-Singh-5/FYP-spam-classifier.git
$ cd FYP-spam-classifier
```

Create a virtual environment using conda or makevirtualenv to install dependencies in and activate it:

```sh
$ virtualenv env
$ env\Scripts\activate      # for windows
$ source env/bin/activate   # Mac OS/Linux
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

For working with databases or getting the data from databases:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

For entering admin panel:
```sh
$ python manage.py createsuperuser
```