#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from Tkinter import *
from Results import * 
import os.path as path
import __builtin__
import imgSeizure   
        
   
def main (video,Roi):
    global nb_question,message_numero_question 
    namefile =__builtin__.namefile
    video1=video
    cage=Roi
    
    if not path.exists(namefile):
        source = csv.writer(open(namefile, "w"))
    
    
    # création de la fenetre principale pour l'enregistrement des Seizure
    Fen1 = Tk()
    # titre donné à la fenêtre
    Fen1.title(u"Type seizure Analisis")
  
    nb_question = 1 
    
     
     
     
    message_numero_question= StringVar()
    
    
            
    
    Label(Fen1,text = "report will be saved in:  "+namefile,
     
                              bg="#FFFFCC",
                              fg="blue",
                              font="serif 12 bold italic").pack(expand=1, fill=X) 
    
    top=Frame(Fen1,borderwidth=2,width=100,height=20, relief=GROOVE, bg='ivory')
    top.pack(side="top",padx=10,pady=10,expand=True)
    
    label=Label(top,text=u"Information ")
    label.pack()#affichage immédiat
    
      
    Ent_enonce = Listbox(top,height=4,width=35)
    Ent_enonce.insert(END,"===============================  " )  
    Ent_enonce.insert(END,"  video name:  "+ video1  ) 
    Ent_enonce.insert(END,"  ROI:  "+  str(cage)  ) 
    Ent_enonce.insert(END,"===============================  " )  
    Ent_enonce.pack(padx=10,pady=10)
    
    contenu=Frame(Fen1,borderwidth=2,width=100,height=100, relief=GROOVE, bg='ivory')
    contenu.pack(side="top",expand=True)
    
    frame=Frame(contenu,borderwidth=2,width=80,height=100, relief=GROOVE, bg='ivory')
    frame.pack(side="left",padx=10,pady=10)
    
    frame1=Frame(contenu,borderwidth=2,width=80,height=100, relief=GROOVE, bg='ivory')
    frame1.pack(side="right",pady=10,padx=10)
    
    # ///////FRAME POUR ENTRER DONNEES//////////
    datelabel=Label(frame,text=u"Date  :")
    datelabel.pack(side="top",padx=10,pady=10)
    datelabel.configure
    
    Ent_date = Entry(frame1,width=10) 
    Ent_date.pack(side="top",padx=5,pady=10)
    
    r1=Label(frame,text=u"Seizure Start :")
    r1.pack(side="top",padx=10,pady=10)
    r1.configure
    
    Ent_rep1 = Entry(frame1,width=10) 
    Ent_rep1.pack(side="top",padx=5,pady=10)
     
    r2=Label(frame,text=u"Seizure End :")
    r2.pack(side="top",padx=10,pady=10)
    r2.configure
    
    Ent_rep2 = Entry(frame1,width=10) 
    Ent_rep2.pack(side="top",padx=10,pady=10) 
    
    r3=Label(frame,text=u"duration of crisis :")
    r3.pack(side="top",padx=10,pady=10)
    r3.configure
    
    Ent_rep3 = Listbox(frame1,width=10,height=1)
    Ent_rep3.pack(side="top",padx=10,pady=10)   
     
     
    #création d'une zone "invisible"
    Af6=Label(Fen1,text=u"")
    Af6.pack_forget()
 
    # récupération des données des zones de saisie 
    def verifier():
        global calcul,rep1,rep2,calcul,justy,rep3,date
        date=StringVar()
        date = Ent_date.get()
        rep1 = float(Ent_rep1.get())
        rep2 = float(Ent_rep2.get())
        calcul= rep2 - rep1
        Ent_rep3.insert(END,calcul)
        rep3 = calcul
        justy = Ent_justy.get()
        # formulaire incomplet 
        
        if rep1=="" or rep2=="" or justy=="" or date=="" : 
            # masquer le bouton d'enregistrement  
            bouton_enregistrer.pack_forget()
            Af6.configure(text= u"You have not completed all the boxes" )
            Af6.pack()
        # tout est rempli:
        else:
            # montrer le bouton d'enregistrement 
            bouton_enregistrer.pack()
            Af6.configure(text=u"")
            Af6.pack_forget()
     
    # Enregistrement des données
    def enregistrer(): 
        global liste_questions,rep1,rep2,rep3,justy,nb_question, date
        # enregistrement des questions dans la liste.
     
        # effacement des zones de saisie
        Ent_date.delete(0, END)
        Ent_rep1.delete(0, END)
        Ent_rep2.delete(0, END)
        Ent_rep3.delete(0, END)
        Ent_justy.delete(0, END)
        
     
        # je passe à la question suivante
        nb_question += 1
        #mise à jour de l'étiquette 
        message_numero_question.set(u"Question numéro {}".format(nb_question))
     
     
        # masquer le bouton d'enregistrement
        bouton_enregistrer.pack_forget()
     
        #Quitter automatiquement au bout de 20 enregistrements
        if nb_question == 2:
            Fen1.quit()
            Fen1.destroy()
     
            #création d'un fichier pour enregister la liste sur l'ordinateur
            source = csv.writer(open(namefile, "a")) # à revoir
            source.writerow([date,rep1,rep2,rep3,justy,video1,cage])



    FrameBas=Frame(Fen1,borderwidth=2,width=100,height=80, relief=GROOVE, bg='ivory')
    FrameBas.pack(side="bottom",expand=True,padx=(10,10),pady=(30,10))
    
    Af7=Label(FrameBas,text=u"Please give a comment :")
    Af7.pack()
    Af7.configure
    Ent_justy = Entry(FrameBas,width=30) 
    Ent_justy.pack(padx=10,pady=10) 
    # bouton 'Enregistrer'
    bouton_enregistrer = Button(FrameBas,text=u"Enregistrer",command=enregistrer)
    # bouton 'Vérifier'
    bouton_verifier = Button(FrameBas,text=u"Vérifier",command=verifier) 
    bouton_verifier.pack()
     
    Fen1.mainloop()
     
    
    
