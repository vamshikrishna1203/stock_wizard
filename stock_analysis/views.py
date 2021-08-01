from django.shortcuts import render

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas_datareader as web

import pandas as pd
import matplotlib.pyplot as plt

def home(request):
    return render(request,"index.html")

def pred(request):

    comp_code =request.GET['cname']
    high = float(request.GET['high'])
    low = float(request.GET['low'])
    open = float(request.GET['open'])
    vol = float(request.GET['vol'])

    dataset=web.DataReader(comp_code,data_source="yahoo",start='2000-04-21',end='2021-04-22')
    x=dataset[['High','Low','Open','Volume']].values
    y=dataset['Close'].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=0)
    model=LinearRegression()
    model.fit(x_train,y_train)
    prediction=model.predict(x_test)
    #sample prediction value
    pre=model.predict([[high,low,open,vol]])

    return render(request,"result.html",{'pred':pre})

