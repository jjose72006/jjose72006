## Programmer : Jose, Jason
## Course :     B104

import os
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


path = r"C:\Users\JJose\OneDrive\Desktop\Desktop\B104\B104_YRBS_Project.xlsx"

data= pd.read_excel(path)


def male_female():
    df = pd.DataFrame(data, columns=['q2'])
    
    gender_counts = df['q2'].value_counts()
    
    value = ['Males', 'Female']
    sizes = [gender_counts.get(1, 0), gender_counts.get(2, 0)]
    
    plt.figure(figsize=(7, 7 ))
    plt.pie(sizes, autopct='%1.1f%%', startangle=90, colors=['blue', 'pink'])
    plt.title('Gender Distribution (Males=1, Females=2)')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

print(male_female())

def age(): 
   df = pd.DataFrame(data, columns=['q1'])
    
   age = df['q1'].value_count()
   value = ['12 years old or younger', '13 years old','14 years old','15 years old','16 years old','17 years old','18 years old']
   size = [age.get(1,0), age.get(2,0)]
    
   plt.figure(figsize=(7,7))
   plt.pie(size, autopct='%1.1f%%', startangle = 90, color=['Blue', 'Green','Red','Pink','Purple','Yellow','Orange'])    
   plt.title('Age of The People')
   plt.axis('Equal')
   plt.show()
   
   

data = pd.read_excel(path)

# Preprocess the data
# Count the occurrences of each demographic combination
heatmap_data = data.groupby(['Age', 'Sex', 'Grade', 'Hispanic_Latino', 'Race']).size().unstack(fill_value=0)

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt='d')
plt.title('Demographics Heatmap')
plt.xlabel('Demographics Categories')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()





















