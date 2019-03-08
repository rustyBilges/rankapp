from interface import implements, Interface
import pandas as pd
import pyodbc
from flask import current_app

class I_PatientData(Interface):

    def returnPatientDf(self):
        pass

class DummyPatientData(implements(I_PatientData)):

    def __init__(self):

        self.df = pd.DataFrame()
        self.df['Name'] = ['Paul Stephenson', 'Princess Campbell', 'Guy Bailey', 
		      'Roy Hackett', 'Carmen Beckford', 'Prince Brown', 
		      'Owen Henry', 'Pero Jones', 'James Peters', 'Alfred Fagon']
        self.df['Bed'] = [1,2,3,5,7,8,11,12,14,15]
        self.df['T_number'] = ['T38746', 'T18346', 'T32985', 'T23190', 'T19583',
                'T49568', 'T30297', 'T43078', 'T89765', 'T34287']
        self.df['Age'] = ['61', '52', '81', '77', '65', '82', '80', '59', '38', '76']
        self.df['Admission'] = ['2019/01/25', '2019/03/01', '2019/02/18', '2019/02/22', 
                                '2019/02/15', '2019/02/24', '2019/03/02', '2019/02/21', '2019/02/28', '2019/02/29' ]


    def returnPatientDf(self):
        return self.df

class IccaPatientData(implements(I_PatientData)):
## This class will get the current patients from ICCA using pyodbc:
    def __init__(self):

        self.df = pd.DataFrame()
        self.df['Name'] = ['Paul Stephenson', 'Princess Campbell', 'Guy Bailey', 
		      'Roy Hackett', 'Carmen Beckford', 'Prince Brown', 
		      'Owen Henry', 'Pero Jones', 'James Peters', 'Alfred Fagon']
        self.df['Bed'] = [1,2,3,5,7,8,11,12,14,15]
        self.df['T_number'] = ['T38746', 'T18346', 'T32985', 'T23190', 'T19583',
                'T49568', 'T30297', 'T43078', 'T89765', 'T34287']
        self.df['Age'] = ['61', '52', '81', '77', '65', '82', '80', '59', '38', '76']
        self.df['Admission'] = ['2019/01/25', '2019/03/01', '2019/02/18', '2019/02/22', 
                                '2019/02/15', '2019/02/24', '2019/03/02', '2019/02/21', '2019/02/28', '2019/02/29' ]


    def returnPatientDf(self):
        return self.df

