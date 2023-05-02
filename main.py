import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import * 
 
#data=pd.read_csv("test.csv")
data=pd.read_csv("vacsi-v-fra-2022.csv")
#print(data.jour)
x =data.jour
y=data.n_dose1
plt.plot(x,y)
plt.xlim(25, 2)
plt.show()
#plt.mean(data.n_dose1_h)

 


#names = data.jour# nom des barres

#values = data.n_dose1_h
 

#plt.bar(names, values) ; plt.show() # Tracer
#print(sum(data.nombre))

""" print(sum(data.n_dose1_h))
print(sum(data.n_dose1_f))
print(sum(data.n_dose1_e))
 """
Categories = ["Hommes","Femmes","Enfants"] # 3 échantillons

Sous_categories = ['n_dose1', 'n_complet' ,'n_rappel','n_2_rappel'] # comparés selon 4 critères

# Valeurs pour chaque catégories

y1 = [sum(data.n_dose1),sum(data.n_complet_h),sum(data.n_rappel_h),sum(data.n_2_rappel_h) ]; 
y2 = [sum(data.n_dose1_f),sum(data.n_complet_f),sum(data.n_rappel_f),sum(data.n_2_rappel_f) ]; 
y3 =  [sum(data.n_dose1_e),sum(data.n_complet_e),sum(data.n_rappel_e),sum(data.n_2_rappel_e) ]; 


nb_categories = len(Categories)

largeur_barre = floor(1*10/nb_categories)/10

x1 = range(len(y1))

x2 = [i + largeur_barre for i in x1]

x3 = [i + 2*largeur_barre for i in x1]



plt.bar(x1, y1, width = largeur_barre, color = 'red',

           edgecolor = 'black', linewidth = 2)

plt.bar(x2, y2, width = largeur_barre, color = 'blue',

           edgecolor = 'black', linewidth = 2)

plt.bar(x3, y3, width = largeur_barre, color = 'green',

           edgecolor = 'black', linewidth = 2)

plt.xticks([r + largeur_barre / nb_categories for r in range(len(y1))],

              Sous_categories)

plt.legend(Categories,loc=2)

plt.show()

labels = 'Hommes', 'Femmes', 'Enfants'
sizes = [sum(data.n_dose1_h), sum(data.n_dose1_f), sum(data.n_dose1_e)]
colors = ['yellowgreen', 'gold', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.savefig('PieChart01.png')
plt.show()
 

labels = 'Hommes', 'Femmes', 'Enfants'
sizes = [sum(data.n_2_rappel_h), sum(data.n_2_rappel_f), sum(data.n_2_rappel_e)]
colors = ['yellowgreen', 'gold', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.savefig('PieChart01.png')
plt.show()
