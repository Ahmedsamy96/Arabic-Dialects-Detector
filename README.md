# **AIM Technologies ML & NLP Task**
# **Arabic Dialect detector**

# Use case: 
I was given a dataset of (IDs and dialect ) can be considered as Target values about 18 classes, and also
was given a link to be used in Text fetching, each ID match a specific Text record.

# My Solution: 
As I was requested in the task proposal, The task may be portioned into small processes
1- Data Fetching Task
2- Data Preprocessing Task
3- Training Model using Traditional ML
4- Deep Learning Model
5- Model Deployment (Flask)


So lets move forward by discussing each process mentioned above.

# A. Data Fetching Task
In this step their was an obvious challenges which is Using a large amount of data using POST request .
I've solved this problem by creating a block of code iterate over the whole data, each iteration return 1000 text
rows . Each Iteration was returning a dictionary of (ID and Text)
After that I converted the final complete dictionary into a dataframe and merged it with the given dataset to
finish this step with a Dataset of 458000 row (id, dialect or target, Text).

**Trick**: To set the number of iteration I divided the number of rows of the given dataset by 1000 .


# B. Data Preprocessing Task
To perform preprocessing in this task was a challenge to clean Arabic languages for the first time not like the
traditional ways of dealing with English text.
After looking at the dataframe many times I noticed the main issues, the data have to be clean of them:
    a- Emoji's (will not be useful for the model).
    b- An English word repeated many times in the text which is starting with (http).
    c- Converting the labels (dialect) to be numerical to be ready for the model training.
    
**Note**: I also showed up the classes balance to deal with this in the Model training task.


# C. Training Model using Traditional ML
I used many algorithms such SVM, logistic regression, Random Forest but the best in Time consuming and
Accuracy was Naïve Bayes ( But anyway it's hard to train a traditional ML model on 18 classes and take fulfilling
results )
So the Accuracy all over the classes was only 53%, the more data about a specific class was the more Accuracy
(precision and recall ) was.


# D. Deep Learning Model
In this step I used LSTM as it deal very well with Text data which have long sequences better than RNN.
The Training model took hours just to finish one epoch but I see if the model was trained on more epochs
the model will significantly improve without overfitting I just trained the model as much as I could to use it
for the Deployment task (so the model can be better).

**Note**: All the task processes was performed on my own local machine without GPU or even strong processor.


# E. Model Deployment (Flask)
I used Flask to get the user input, then tested it on the model weights ( .pkl for Naïve Bayes - .pt for the
LSTM). And the predicted class is sent to another HTML page.
