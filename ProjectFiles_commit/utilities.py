# Import external packages

from multiprocessing.connection import wait
import pandas as pd
from datetime import datetime
import numpy as np
import re

# Classes 

class Subject():
    def __init__(self, file_name):

        ### Aufgabe 1: Interpolation ###

        __f = open(file_name)
        self.subject_data = pd.read_csv(__f)
        self.subject_data = self.subject_data.interpolate(method='quadratic', axis=0)      
        self.subject_id = file_name.split('.csv')[0][-1]
        self.names = self.subject_data.columns.values.tolist()
        self.time = self.subject_data["Time (s)"]        
        self.spO2 = self.subject_data["SpO2 (%)"]
        self.temp = self.subject_data["Temp (C)"]
        self.blood_flow = self.subject_data["Blood Flow (ml/s)"]
        print('Subject ' + self.subject_id + ' initialized')





        

### Aufgabe 2: Datenverarbeitung ###


def calculate_CMA(df,n):

    return df.expanding(n).mean()

    pass



def calculate_SMA(df,n):

    return df.rolling(n).mean()

    pass

### Aufgabe 4: Moving Average Kommentar ###

# 1. Allgemein ist der SMA immer der gleitende Durchschnitt über einen bestimmten Zeitraum. Hier könnte man sagen, 
# um damit Ausreißer zu erkennen, welche dann eine Warnung ausgeben.
# Der SMA ist ungeeignet für Signale, die Definitionslücken enthalten und geeignet für Signale die keine Definitionslücken enthalten 
# 2. Die Linie im Graphen wird immer flacher.