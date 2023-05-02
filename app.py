from tkinter import *
import statistics
import pandas as pd


data=pd.read_csv("vaccintotalfrance.csv")
#créer une fenetre
fenetre = Tk()

#personalisation de la fenetre
label=Label(fenetre, text="PROJET POCINE DATA ET ANALYTICS",bg="green")
label.pack()
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
#afficher


""" 
photo = PhotoImage(file="tellat.png")

canvas = Canvas(fenetre,width=550, height=500)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

photom = PhotoImage(file="image.png")

canvas = Canvas(fenetre,width=550, height=600)
canvas.create_image(0, 0, anchor=NW, image=photom)
canvas.pack()

 """

fenetre.mainloop()


bouton.pack()

#la moyenne du  nombre de dose1 pour les hommes
print("la moyenne du  nombre de dose1 pour les hommes")
list = data.n_dose1_h
mean = statistics.mean(list)
print(mean)

#la moyenne du  nombre de dose1 pour les femmes
print("la moyenne du  nombre de dose1 pour les femmes")
list = data.n_dose1_f
mean = statistics.mean(list)
print(mean)


#la moyenne du  nombre de dose1 pour les enfants

print("la moyenne du  nombre de dose1 pour les enfants")
list = data.n_dose1_e
mean = statistics.mean(list)
print(mean)


#la médiane

print("La médiane du  nombre de dose1 pour les hommes")
list = data.n_dose1_h
mean = statistics.median(list)
print(mean)


print("La médiane du  nombre de dose1 pour les femmes")
list = data.n_dose1_f
mean = statistics.median(list)
print(mean)

print("La médiane du  nombre de dose1 pour les enfants")
list = data.n_dose1_e
mean = statistics.median(list)
print(mean)


print("Le mode du  nombre de dose1 pour les enfants")
list = data.n_dose1_e
mean = statistics.mode(list)
print(mean)



