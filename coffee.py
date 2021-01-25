import numpy as np 

import csv

import pandas as pd 

import plotly.express as px

with open("coffeehours.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()

def getDataSource(data_path):
    coffeeml = []
    sleepHours = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            coffeeml.append(float(row["Coffee in ml"]))
            sleepHours.append(float(row["sleep in hours"]))
    return {"x":coffeeml, "y":sleepHours}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("The correlation between ammount of coffee drank and ammount of sleep is: ", correlation[0,1])

def main():
    data_path = "coffeehours.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
main()

