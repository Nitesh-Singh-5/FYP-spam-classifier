from django.shortcuts import render
import numpy
import pickle
import string
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from utils import text_process
from manage import importPipelines
from .models import Form_Message, Feedback_Model

# Create your views here.
def home(request):
    if request.method == "POST" and 'htmlsubmitbutton1' in request.POST:
        print("initialize")
        message = request.POST.get('message')
        print("get")
        message_cp = message
        message = [message]
        message = text_process(message)
        message = [' '.join(message)]
        result, accuracy = predict(message)
        Form_Message.objects.create(
            message = message_cp,
            result = result,
            accuracy = accuracy
        )
        print('result is ', result, 'with accuracy ', accuracy)
        return render(request, 'home.html', {'result': result, 'message': message_cp, 'accuracy': accuracy})

    if request.method=='POST' and 'htmlsubmitbutton2' in request.POST:
        message = request.POST.get('message')
        your_prediction = request.POST.get('your_prediction')
        result = request.POST.get('result')
        Feedback_Model.objects.create(
            message = message,
            your_prediction = your_prediction,
            our_prediction = result
        )
        return render(request, 'home.html')

    return render(request, "home.html")


def predict(message):
    result = " "

    pipeline, pipeline_second = importPipelines()

    test = pipeline.predict(message)
    test_prob = pipeline.predict_proba(message)
    print(test[0])
    test_second = pipeline_second.predict(message)
    test_second_prob = pipeline_second.predict_proba(message)

    value_spam = test_prob[0][1]
    value_spam_second = test_second_prob[0][1]

    value_ham = test_prob[0][0]
    value_ham_second = test_second_prob[0][0]

    print('\ntest second is ', test_second[0])
    print('Portability of test1 is', test_prob, 'Portability of second test is ', test_second_prob)

    print('value...', test_prob[0][1])

    if value_spam > 0.5 and value_spam_second > 0.5:
        result = 'spam'
        accuracy = max(value_spam, value_spam_second)

    elif value_spam <= 0.5 and value_spam_second <= 0.5:
        result = 'ham'
        accuracy = max(value_ham, value_ham_second)
    elif value_spam > 0.5 or value_spam_second > 0.5:
        value = math.fabs(test_second_prob[0][1] - test_prob[0][1])

        if max(value_spam, value_spam_second) + 0.1 > max(value_ham, value_ham_second):
            accuracy = max(value_spam, value_spam_second)
            result = 'spam'
        else:
            result = 'ham'
            accuracy = max(value_ham, value_ham_second)
    else:
        result = 'ham'
        accuracy = max(value_ham, value_ham_second)

    accuracy = round(accuracy, 3) * 100

    print('final result', result, accuracy)

    if result == 'spam':
        if accuracy > 80:
            result = 'very likely a spam'
        else:
            result = 'less likely a spam'

    elif accuracy > 80:
        result = 'very likely a ham'
    else:
        result = 'less likely a ham'

    return result, accuracy

def RecentMessages(request):
    recent = Form_Message.objects.all()
    return render(request, 'recent_messages_list.html',{'recent_list':recent})
