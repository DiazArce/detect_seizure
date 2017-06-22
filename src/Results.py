#!/usr/bin/env python
# -*- coding: utf-8 -*
import Tkinter as tk
import ttk
from matplotlib import pyplot as plt #sudo apt-get install python-matplotlib
import random
import os
import cv2
from Tkinter import *
from PIL import Image, ImageTk
import csv
import fichierCSV
from matplotlib.widgets import Button
import imgSeizure
from tkMessageBox import *
from IntensityProvider import *
import __builtin__
from tkFileDialog import askopenfilename 
#from cv2 import videostab

class Results(tk.Frame):
    intensities = []
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        
        self.ratioHeight = parent.winfo_screenheight() / 1024
        self.ratioWidth  = parent.winfo_screenwidth() / 1280
        
        
        frame=tk.Frame(self,borderwidth=2,
                       width=900*self.ratioWidth,
                       height=120*self.ratioHeight,
                       relief=GROOVE,bg="#FFFFCC")     #   #Frame on haut dans la tête qui contient les frames 1 ,2 et 3
        frame.pack(side="top", expand=True,padx=20,pady=(50,5))   
        frame.pack_propagate(False)     
        
        frameBtn=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')                      #frame qui contient tous les 5 boutons de passage en haut                                                                                       
        frmleft=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')  #Frame 2 et 3 sert comme un conteneur pour
        frmRight=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')                      # le label qui continet l'image de logo ipmc
        
        img = Image.open("ipmc.png")                                                        #avec la librery PIL on utilise le module Image
        photoimg = ImageTk.PhotoImage(img)                                                  # et ImageTk.PhotoImage qui sert à ouvir et charge une image
            
        lblLeft =tk. Label(frmleft,image=photoimg)                                             # Label qui contient l'image de logo ipmc
        lblLeft.image = photoimg 
        lblLeft.pack()
           
        lblRight =tk. Label(frmRight,image=photoimg)
        lblRight.image = photoimg 
        lblRight.pack() 
        
        button = tk.Button(frameBtn, text=" Main",
                           command=lambda: controller.show_frame("PageMain"))
        button1 = tk.Button(frameBtn, text="Select Files",
                           command=lambda: controller.show_frame("Parameters"))
    
        button2 = tk.Button(frameBtn, text="Select ROI",
                            command=lambda: controller.show_frame("Selection"))
        button3 = tk.Button(frameBtn, text="Detect",
                            command=lambda: controller.show_frame("Detection"))
        button4 = tk.Button(frameBtn, text="Results",state="disabled", disabledforeground="#F50743",background="yellow",
                            command=lambda: controller.show_frame("Results"))
           
        button.pack(side="left",padx= 5, pady=10)
        button1.pack(side="left",padx= 5, pady=10)
        button2.pack(side="left",padx= 5, pady=10)
        button3.pack(side="left",padx= 5, pady=10)        
        button4.pack(side="left",padx= 5, pady=10)
        
        frmleft.pack(side="left", expand=True,padx=10,pady=10)  
        frameBtn.pack(side="left", expand=True,padx=10,pady=10) #on charge et on fixe le frame qui contient les 5 boutons
        frmRight.pack(side="left",expand=True,padx=10,pady=10)
        
        self.Container()
        
        
    def Container(self):   
                
       
        contenu=tk.Frame(self,borderwidth=2,
                         width=900*self.ratioWidth,
                         height=500*self.ratioHeight,
                         relief=GROOVE,bg="#FFFFCC")
        
    
        contenu.pack(side="top", expand=True,padx=(50,50),pady=(5,10))
        contenu.pack_propagate(False)
        
        #/////////////////////FRAME POUR CONTENEUR DE VISIONEUR DES IMAGES ///////////////////
    
        self.frameImage=tk.Frame(contenu,borderwidth=2,
                                 width=300*self.ratioWidth,
                                 height=450*self.ratioHeight,
                                 relief=GROOVE, bg='ivory')
        label=tk.Label(self.frameImage,borderwidth=2,text="Seizure Detection Graphs",bg= "#f3af38" )
        label.pack(side="top",padx=10,pady=5)
        btnVideo=tk.Label(self.frameImage,text="Open Video")                       
        btnVideo.pack(side="bottom",pady=10)
        
        btnImg=tk.Label(self.frameImage,text="Open Graphs")
        btnImg.pack(side="top",pady=10)    
        self.frameImage.pack(side="left",expand=True,padx=(10,5),pady=5)
        self.frameImage.pack_propagate(False)
        
        framelogo=tk.Frame(self.frameImage,borderwidth=1,
                           width=280*self.ratioWidth,
                           height=400*self.ratioHeight,
                           relief=GROOVE, bg="#FFFFCC")
        framelogo.pack(side="bottom",padx=10,pady=10)
        framelogo.pack_propagate(False)
        
        img = Image.open("index.jpeg")                                                        #avec la librery PIL on utilise le module Image
        
        image = img.resize((120,100), Image.ANTIALIAS)
        photoimg = ImageTk.PhotoImage(image)  
        OpenVideo =tk. Button(framelogo,image=photoimg,borderwidth=1,relief=GROOVE,command=self.InitOpenVideo)                                             # Label qui contient l'image de logo ipmc
        OpenVideo.image = photoimg 
        OpenVideo.pack(side="bottom",pady=10)
        
        img = Image.open("img0.png")                                                        #avec la librery PIL on utilise le module Image
    
        image = img.resize((120,80), Image.ANTIALIAS)
        photoimg = ImageTk.PhotoImage(image)  
        OpenImg =tk. Button(framelogo,image=photoimg,borderwidth=1,relief=GROOVE,command=self.InitOpenImg)                                             # Label qui contient l'image de logo ipmc
        OpenImg.image = photoimg 
        OpenImg.pack(side="top",pady=10)
        
        
        #//////////////////////////  FICHIER SEIZURE RESULTATS////////////////////////
        framefic=tk.Frame(contenu,borderwidth=2,
                          width=480*self.ratioWidth,
                          height=450*self.ratioHeight,
                          relief=GROOVE, bg='ivory')
        
        self.frame=tk.Frame(framefic,borderwidth=2,
                            width=490*self.ratioWidth,
                            height=440*self.ratioHeight,
                            relief=GROOVE, bg='ivory')
        label=tk.Label(self.frame,borderwidth=2,text=" Seizure Report",bg= "#f3af38" )
        label.pack(side="top",padx=10,pady=10)
        
        self.info=tk.Listbox(self.frame,
                             width=50*self.ratioWidth,
                             height=10*self.ratioHeight,)
        self.info.pack(side="top",padx=(20,20),pady=(5,5)) 
        
        btnlist=tk.Button(self.frame,text="Menu main",command=self.ListFichier)
        btnlist.pack(side="top")
        
        
        
        self.btnReturn=tk.Button(self.frame,text="Return", command= self.returner)
        self.btnReturn.pack(side="bottom",padx=5, pady=5)
        #//////////////////////////////FRAME  LEFT////////////////////////////////////////////////////////////
        self.frameLeft=tk.Frame(self.frame,
                                width=100*self.ratioWidth,
                                height=180*self.ratioHeight,
                                borderwidth=2, relief=GROOVE,bg="#FFFFCC")  
        self.frameLeft.pack(side="left",expand=True,padx=5,pady=5)
        self.frameLeft.pack_propagate(False)
        
        self.labelL=tk.Label(self.frameLeft,text="Report File ")   
        self.labelL.pack(side="top",padx=5,pady=10)
        
        self.btnchoixfic=tk.Button(self.frameLeft,text="Content ",state="disabled", disabledforeground="#F50743",command=self.choixFile)
        self.btnchoixfic.pack(side="top",padx=5,pady=(30,5))
        
        self.btnsuppFil=tk.Button(self.frameLeft,text="Remove ",state="disabled", disabledforeground="#F50743",command=self.suppFile)
        self.btnsuppFil.pack(side="bottom",padx=5,pady=5)
        #//////////////////////FRAME CENTER ////////////////////////////
        self.frameCenter=tk.Frame(self.frame,
                                  width=130*self.ratioWidth,
                                  height=80*self.ratioHeight,
                                  borderwidth=2, relief=GROOVE,bg="#FFFFCC")  
        self.frameCenter.pack(side="left",expand=True,padx=5,pady=5)
        self.frameCenter.pack_propagate(False)
        
        self.label=tk.Label(self.frameCenter,text="Select a number ")   
        self.label.pack(side="top",padx=5,pady=5)
        self.choix = IntVar()
        self.entry= tk.Entry(self.frameCenter,textvariable=self.choix,width=5)
        self.entry.pack(side="bottom",padx=5,pady=5) 
        
        #/////////////////////////FRAME RIGHT////////////////////////////////////////
        self.frameRight=tk.Frame(self.frame,
                                 width=100*self.ratioWidth,
                                 height=180*self.ratioHeight,
                                 borderwidth=2, relief=GROOVE,bg="#FFFFCC")  
        self.frameRight.pack(side="right",expand=True,padx=5,pady=5)
        self.frameRight.pack_propagate(False)
        
        self.labelR=tk.Label(self.frameRight,text="Seizure Infos ")   
        self.labelR.pack(side="top",padx=5,pady=10)
        
        self.btnMontrer=tk.Button(self.frameRight,text="Show ",state="disabled", disabledforeground="#F50743", command=self.Montrer)
        self.btnMontrer.pack(side="top",padx=5,pady=(30,5))
        
        self.btnSupp=tk.Button(self.frameRight,text="Remove",state="disabled", disabledforeground="#F50743", command= self.SuppSeizure)
        self.btnSupp.pack(side="bottom",padx=5, pady=5)
    
        
        self.frame.pack(side="left",expand=True,padx=(10,10),pady=5)
        self.frame.pack_propagate(False)
        
        framefic.pack(side="left",expand=True,padx=(5,10),pady=5)
        framefic.pack_propagate(False)
        
       #//////////////////////////////////////////// FRAME PIE DE PAGE /////////////////////////
        
        contPie=tk.Frame (self,
                          width=900*self.ratioWidth,
                          height=60*self.ratioHeight,
                          borderwidth=2, relief=GROOVE,bg="#FFFFCC")
        framePie=tk.Frame(contPie,borderwidth=2, relief=GROOVE,bg='ivory')
        btnSave=tk.Button(framePie,text="Save",activebackground="yellow").pack(padx=10,pady=5)
        framePie.pack(side="bottom",padx=10,pady=10)
        
        contPie.pack(padx=5,pady=(10,50),side="bottom")
        contPie.pack_propagate(False)
             
        
        
        
    #GESTION IMAGES ///////////////////  
    def InitOpenImg(self): 
        
        if len(__builtin__.intensities) == 0:
            showwarning('Résult','Attention empty Videos.\nwould you like to analys  !') 
             
        else:
            imgSeizure.mainImg(__builtin__.intensities) 
     
     
    def InitOpenVideo(self): 
        
        path_movie = askopenfilename(filetypes = [("Video files", "*.avi *.flv *.mp4 *.mpeg *.asf *.dav")], title=("Choose a video file"),initialdir = '/home/fabrice/IPMC/VIDEOS')
        file=path_movie 
        print file
        os.system("vlc " +file)
     
     
    
    #////////////////////////////////////////////////
        
    def csv_to_var(self,dico):  #fonction que permet le passage  csv à variable
       global date,rep1,rep2,rep3,justy,video,cage   # ces variables(nameVideo, fps, duration ,etc ) est juste pour un test , mais normalmente on va mettre les info corrspondant après analyses de vidéos c'est à dire 
                                                                # par exemple la cantité de decoupage des videos ,le numero des images que on pourra visualizer dans l'onglet results etc
       date = dico[0]
       rep1 = dico[1]
       rep2 = dico[2]
       rep3 = dico[3]
       justy = dico[4]
       video = dico[5]
       cage = dico[6]
      
    def var_to_csv(self,dico):  # fonction de passage de var à csv
       dico[0] = date
       dico[1] = rep1
       dico[2] = rep2
       dico[3] = rep3
       dico[4] = justy
       dico[5] = video
       dico[6] = cage
        
    def List(self):   # fontion que permet afficher les analyses effectué ça depend du cas (global ou sequentiel) on ouvrira les fichier
        
        self.info.delete(0,"end")
        self.liste=[]
        cpt=1
        
         # on ouvre le fichierVar pour obtenir la variable chooix et savoir si utilisateur est en mode sequentiel ou global       
        
        self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
        self.info.insert(END,"                      LIST OF SEIZURE IN FILE : " + filename                  )
        self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )     # ça depend du choix on va afficher la lsite de fihcier ou videos analysé
        if not os.path.exists(filename) :
            self.info.insert(END,"                      File vide  : "                  )
            
        else:    
            source = csv.reader(open(filename, "r"))
            
            for line in source:
                l=[]                #liste qui contiendra les informations d'un contact sans les balises VCard
                for x in line:                 
                    l.append(x)
                self.liste.append(l)
                self.csv_to_var(l)
                    
                self.info.insert(END, "   ["+str(cpt)+"]  ------->>  " + " Date of the crisis: " + date )
                cpt=cpt+1
                  
            self.entry.configure(textvariable=self.choix)
            self.btnMontrer.configure(state="active") 
            self.btnSupp.configure(state="active")
            
            self.btnchoixfic.configure(state="disabled") 
            self.btnsuppFil.configure(state="disabled") 
        
    def Montrer(self):                        # permet de afficher les informations concernant le fichier choisi
            
            self.info.delete(0,"end") 
            choix=self.choix.get()
            if  choix!="":
                choix=int(choix)
                choix=choix-1
                liste=self.liste[choix]
                self.csv_to_var(liste)
                
                self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
                self.info.insert(END,"                           INFORMATION SEIZURE                   " )
                self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
                self.info.insert(END,"   Video :   "+video )
                self.info.insert(END,"   ROI :   "+cage )
                self.info.insert(END,"   Date :   "+date )
                self.info.insert(END,"   Start seizure :   "+rep1 )
                self.info.insert(END,"   End seizure :   "+rep2 )
                self.info.insert(END,"   Duration of the crisis :   "+rep3 )
                self.info.insert(END,"   comment :   "+justy )
                
                self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
            else:
                 
                self.listRoi.insert(END,"select a number of seizure")  
    
        
            #return self.List()  
            
            
    def returner(self):
        
        self.List() 
                   
    def rewrite(self,dico):                #Réecrit le fichier  après modification d'une liste "dico"
        
        global date,rep1,rep2,rep3,justy 
        
        source = csv.writer(open(filename, "w")) # on ouvre le fichierVar pour obtenir la variable chooix et savoir si utilisateur est en mode sequentiel ou global     
        
        for i in dico:
            nameVideo = i[0]
            fps = i[1]
            duration = i[2]
            
            source.writerow([date,rep1,rep2,rep3,justy]) # enregistrement des changement effectué      
        
        
    def SuppSeizure(self):    
        
        
        choix=self.choix.get()
         
        choix=int(choix)
        choix=choix-1
         
        self.liste.pop(choix)        
        self.rewrite(self.liste)   #on envoie la nouvelle liste dans la fonction rewrite pour enregistre les changement
        self.List()
        #return self.Listfichier()   
        
    def ListFichier(self):
        
        
        self.info.delete(0,"end")
        self.listefic=[]
        
        cpt=1
        self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
        self.info.insert(END,"                             MENU MAIN  -  LIST OF FILES CSV                "  )
        self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
        
        fic = csv.reader(open("ListFichierCSV.csv", "r"))
        for row in fic:
            self.listefic=row
         # on ouvre le fichierVar pour obtenir la variable chooix et savoir si utilisateur est en mode sequentiel ou global       
        for i in range(len(self.listefic)):
                      
            self.info.insert(END,"  ["+str(cpt)+']  ------->>       '     +self.listefic[i])
            
            cpt=cpt+1
            
        self.btnchoixfic.configure(state="active") 
        self.btnsuppFil.configure(state="active") 
        
        self.btnMontrer.configure(state="disabled") 
        self.btnSupp.configure(state="disabled")
        
    def choixFile(self): 
        
        global filename
        choix=self.choix.get()
        if  choix!="":
            choix=int(choix)
            choix=choix-1
            filename=self.listefic[choix]
            
            self.List()     
        else:
                 
           self.listRoi.insert(END,"select number of file")  
             
             
             
             # ça depend du choix on va afficher la lsite de fihcier ou videos analysé
        
        
        
    def suppFile(self): 
        listefic=[]
        source = csv.reader(open("ListFichierCSV.csv", "r"))
        for row in source:
            listefic=row
        choix=self.choix.get()
        if  choix!="":
            choix=int(choix)
            choix=choix-1
            #liste=listefic[choix]
            listefic.pop(choix)         
        
        fic = csv.writer(open("ListFichierCSV.csv", "w")) 
        fic.writerow(listefic) 
        
        self.ListFichier() 
        
                 
    