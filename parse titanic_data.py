import csv
import pandas as pd

taitanic = pd.read_csv('titanic_data.tsv')
taitanic['num']=1
taitanic['survival']=taitanic['Survived'].map(lambda x:'Survived' if x==1 else 'Not Survived')

taitanic.to_csv('titanic.tsv')


    
