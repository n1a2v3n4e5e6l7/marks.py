  
import plotly.express as px
import csv
import numpy as np

def getDataSource(DataPath):
    RollNo = []
    MarksInPercentage = []

    with open (DataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            RollNo.append(float(row["RollNo"]))
            MarksInPercentage.append(float(row["Ice-cream Sales"]))
   
        return{"x":RollNo,"y":SoftDrinkSales}

def findCo_Relation(DataSource):
    corelation = np.corrcoef(DataSource["x"],DataSource["y"])
    print("co-relation between roll no and marks in percentage: \n --->",corelation[0,1])

def Main():
    createDataPth = "marks.csv"
    DataSource = getDataSource(createDataPth)
    findCo_Relation(DataSource)

Main()