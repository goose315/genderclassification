from genderize import Genderize
import pandas as pd
import csv
from decimal import *
#f=open("C:/Users/86131/Desktop/Sample1.csv",mode="w",encoding="utf-8",newline="")
#wcsv=csv.writer(f)
NAME=pd.read_excel(r"C:\Users\86131\Desktop\EEE.xlsx")
#author 1
ls1=NAME['author1']
gender_1=(Genderize().get(ls1))
gender1=[]
for a in gender_1:
    gender1.append(a['gender'])
NAME["gender1"]=gender1
prob1=[]
for a in gender_1:
    prob1.append(a['probability'])
NAME["prob1"]=prob1
#author2
ls2=NAME['author2']
gender_2=(Genderize().get(ls2))
gender2=[]
for a in gender_2:
    gender2.append(a['gender'])
NAME["gender2"]=gender2
prob2=[]
for a in gender_2:
    prob2.append(a['probability'])
NAME["prob2"]=prob2
#author3
ls3=NAME['author3']
gender_3=(Genderize().get(ls3))
gender3=[]
for a in gender_3:
    gender3.append(a['gender'])
NAME["gender3"]=gender3
prob3=[]
for a in gender_3:
    prob3.append(a['probability'])
NAME["prob3"]=prob3
#author4
ls4=NAME['author4']
gender_4=(Genderize().get(ls4))
gender4=[]
for a in gender_4:
    gender4.append(a['gender'])
NAME["gender4"]=gender4
prob4=[]
for a in gender_4:
    prob4.append(a['probability'])
NAME["prob4"]=prob4

scores = {'gender1':gender1, 'prob1':prob1, 'gender2':gender2, 'prob2':prob2, 'gender3':gender3, 'prob3':prob3, 'gender4':gender4, 'prob4':prob4}
df = pd.DataFrame(scores)
print(df)
df.to_csv("C:/Users/86131/Desktop/Sample1.csv")
#wcsv.writerow([gender1, prob1, gender2, prob2, gender3, prob3, gender4, prob4])
#f.close()
#print(NAME)