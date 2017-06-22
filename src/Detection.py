#!/usr/bin/env python
# -*- coding: utf-8 -*
import Tkinter as tk
import ttk
from matplotlib import pyplot as plt
import cv2
from Tkinter import *
from PIL import Image, ImageTk
import csv
#import maindetec
import imgSeizure
#import testProgressbar
import IntensityProvider


class Detection(tk.Frame):
    intensities = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        
        self.ratioHeight = parent.winfo_screenheight() / 1024
        self.ratioWidth  = parent.winfo_screenwidth() / 1280
        
        
        frame=tk.Frame(self,borderwidth=2,
                       width=900*self.ratioWidth,
                       height=120*self.ratioHeight,
                       relief=GROOVE,bg="#FFFFCC")    #Frame on haut dans la tête qui contient les frames 1 ,2 et 3
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
        
        button = tk.Button(frameBtn, text="Main",
                           command=lambda: controller.show_frame("PageMain"))
        button1 = tk.Button(frameBtn, text="Select Files",
                           command=lambda: controller.show_frame("Parameters"))
    
        button2 = tk.Button(frameBtn, text="Select ROI",
                            command=lambda: controller.show_frame("Selection"))
        button3 = tk.Button(frameBtn, text="Detect",state="disabled", disabledforeground="#F50743",background="yellow",
                            command=lambda: controller.show_frame("Detection"))
        button4 = tk.Button(frameBtn, text="Results",
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
                
        #obj.choose_files.movie_files
        contenu=tk.Frame(self,borderwidth=2,
                         width=900*self.ratioWidth,
                         height=500*self.ratioHeight,
                         relief=GROOVE,bg="#FFFFCC")
    
        contenu.pack(side="top", expand=True,padx=(50,50),pady=5)
        contenu.pack_propagate(False)
        
        
        #/////////////////////////////////  FRAME à GAUCHE pour FICHIERS SEIZURE ANALYSé ///////////////////////////
         
        self.frameSeizure=tk.Frame(contenu,borderwidth=2,
                                   width=400*self.ratioWidth,
                                   height=400*self.ratioHeight,
                                    relief=GROOVE, bg='ivory')
        label=tk.Label(self.frameSeizure,borderwidth=2,text=" Seizure Report File ",bg= "#f3af38" )
        label.pack(side="top",padx=10,pady=10)
        
        self.frameCarre=tk.Frame(self.frameSeizure,
                                 width=350*self.ratioWidth,
                                 height=200*self.ratioHeight,
                                 borderwidth=2, relief=GROOVE,bg="#FFFFCC")  
        self.frameCarre.pack(side="top",expand=True,padx=5,pady=(10,10))
        self.frameCarre.pack_propagate(False)
        
        self.info=tk.Listbox(self.frameCarre,
                             width=90*self.ratioWidth,
                             height=10*self.ratioHeight,)
        self.info.pack(side="top",padx=10,pady=(5,5))
        btnlist=tk.Button(self.frameCarre,text="List Videos",command=self.ListFichiers)
        btnlist.pack(side="top")
        
    
        self.frameS=tk.Frame(self.frameSeizure,borderwidth=2,
                             width=350*self.ratioWidth,
                             height=200*self.ratioHeight,
                             relief=GROOVE, bg='ivory')
        
        self.label=tk.Label(self.frameS,text="Select Video number ")   
        self.label.pack(side="left",padx=5)
        self.choix = IntVar()
        self.entry= tk.Entry(self.frameS,textvariable=self.choix,width=5)
        self.entry.pack(side="left",padx=10,pady=10)
        self.btnClear=tk.Button(self.frameSeizure,text="Clear",command=self.clear)
        self.btnClear.pack(side="bottom",padx=10,pady=5) 
        
        self.framebtn=tk.Frame(self.frameS,
                               width=100*self.ratioWidth,
                               height=90*self.ratioHeight,
                               borderwidth=2, relief=GROOVE,bg="#FFFFCC")  
        self.framebtn.pack(side="right",expand=True,padx=(50,5),pady=5)
        self.framebtn.pack_propagate(False)
        
        self.btnMontrer=tk.Button(self.framebtn,text="Show",state="disabled", disabledforeground="#F50743",command=self.Montrer)
        self.btnMontrer.pack(side="top",padx=5,pady=(5,1))
        self.btnSupp=tk.Button(self.framebtn,text="Remove",state="disabled", disabledforeground="#F50743",command=self.Supprimer)
        self.btnSupp.pack(side="bottom",padx=5, pady=(1,5))
        
        self.frameS.pack(side="bottom",expand=True,padx=10,pady=5)
        self.frameS.pack_propagate(False)
        
        self.frameSeizure.pack(side="left",expand=True,padx=5,pady=(10,10))
        self.frameSeizure.pack_propagate(False)
        
     #////////////////////////////////////// FRAME à DROITE POUR BAR PROGRESS /////////////////////////////   
        frameProg=tk.Frame(contenu,borderwidth=2,
                           width=400*self.ratioWidth,
                           height=400*self.ratioHeight,
                           relief=GROOVE, bg='ivory')
        
        label=tk.Label(frameProg,borderwidth=2,text="Seizure Analysis",bg="#f3af38")
        label.pack(side="top",padx=10, pady=10)
        
        frame=tk.Frame(frameProg,borderwidth=2,
                       width=400*self.ratioWidth,
                       height=150*self.ratioHeight,
                       relief=GROOVE, bg='ivory')
        frame.pack(side="top",expand=True,padx=10,pady=5)
        frame.pack_propagate(False)
        ############################## BUTTONS POUR MANIPULATION DE LA BAR PROGRESS ##################################
        frameD=tk.Frame(frame,borderwidth=2,
                        width=70*self.ratioWidth,
                        height=70*self.ratioHeight,
                        relief=GROOVE, bg='ivory')
        btnStop=tk.Button(frameD,text="Stop",activebackground="yellow")
        btnStop.pack(side="top",padx=10,pady=5)
        
        btnRestart=tk.Button(frameD,text="Restart",activebackground="yellow",command=self.Restart)
        btnRestart.pack(side="top",padx=10,pady=5)
        frameD.pack(side="right")
    
        self.btnStart = tk.Button(frame,text="start",state="disabled", disabledforeground="#F50743" ,command=self.start)
        self.btnStart.pack(side="left",pady=5,padx=5)
        self.progress = ttk.Progressbar(frame, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack(side="left",pady=5,padx=5)

        self.bytes = 0
        self.maxbytes = 0
        
        ################################# FRAME POUR MESSAGE DE ALERTE ########################################
        self.frameBas=tk.Frame(frameProg,borderwidth=2,
                               width=400*self.ratioWidth,
                               height=250*self.ratioHeight,
                               relief=GROOVE, bg='ivory')
        labl=tk.Label(self.frameBas,borderwidth=2,text="!!! Alert Message !!!",bg="#f3af38")
        labl.pack(side="top",padx=10, pady=(10,5))
        self.AfficheMessage=tk.Listbox(self.frameBas,
                                       width=40*self.ratioWidth,
                                       height=5*self.ratioHeight,)
        self.AfficheMessage.pack(side="bottom",padx=10,pady=(5,20))
        
        
        self.frameBas.pack(side="top",expand=True,padx=10,pady=10)
        self.frameBas.pack_propagate(False)
        
        
        frameProg.pack(side="top",expand=True,padx=(5,30),pady=10)
        frameProg.pack_propagate(False)
        
        
        
     # ///////////////////////////////////// FRAME PIE DE PAGE ///////////////////////////////////////////   
        contPie=tk.Frame (self,
                          width=900*self.ratioWidth,
                          height=70*self.ratioHeight,
                          borderwidth=2,relief=GROOVE,bg="#FFFFCC")
        framePie=tk.Frame(contPie,borderwidth=2, relief=GROOVE,bg='ivory')
        btnSave=tk.Button(framePie,text="SAVE",activebackground="yellow").pack(padx=10,pady=10)
        framePie.pack(side="bottom",padx=10,pady=10)
        
        contPie.pack(padx=5,pady=(10,50),side="bottom")
        contPie.pack_propagate(False)
    
    
    #////////////////////////////////////////////////////  LES FONCTIONS ///////////////////////////////////////
    def updating(self, val):
        
        source = csv.reader(open("fichierMultiVideos.csv", "r"))#ouvrir le fichier qui contient les données de vidéos
        listSource = []
        for row in source:
            listSource.append(row[0])
        nVideos= float(len(listSource))
        self.progress["value"] = val
        percent=val*100
        #print(val)
    
        '''if self.bytes == self.maxbytes:
            self.destroy()'''
        
        
        print nVideos
        print "  -  "
        k=(nVideos+1)/nVideos*100
        print k
        if percent == k:
            self.AfficheMessage.delete(0,"end")
            
            self.AfficheMessage.insert(END,"-!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "  )
            self.AfficheMessage.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
            self.AfficheMessage.insert(END,"                load completed          ")
            self.AfficheMessage.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
            self.AfficheMessage.insert(END,"-!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "  )
        else:    
        #for i in range(3):
            self.AfficheMessage.delete(0,"end")    
            self.AfficheMessage.insert(END,"---!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!--- "  )        
            self.AfficheMessage.insert(END,"============================================================================================================= "  )
            self.AfficheMessage.insert(END,"                load "+str(percent)+" %        ")
            self.AfficheMessage.insert(END,"============================================================================================================= "  )
            self.AfficheMessage.insert(END,"---!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!--- "  )
        
    # ////////////////////////// ICI POUR DEVELOPPER LA BAR PROGRESS ///////////////    
    def start(self):
        '''
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000'''
        self.progress["maximum"] = 1
        #self.suma = [0.0]
        #IntensityProvider.test(self, 0.0, self.suma);

        self.intensities = []
        IntensityProvider.computeIntensities(self, self.intensities)    
        
    def startIMG(self):
        #print self.suma
        imgSeizure.mainImg(self.intensities)   
        
    #////////////////////////////////// ICI POUR GESTION FICHIER SEIZURE //////////////////////////////////   
    def Restart(self):
        
        self.progress["value"] = 0 
        self.AfficheMessage.delete(0,"end")   
    
    def csv_to_var(self,dico):  #fonction que permet le passage  csv à variable
       global nameVideo, fps, duration   # ces variables(nameVideo, fps, duration ,etc ) est juste pour un test , mais normalmente on va mettre les info corrspondant après analyses de vidéos c'est à dire 
                                                                # par exemple la cantité de decoupage des videos ,le numero des images que on pourra visualizer dans l'onglet results etc
       nameVideo = dico[0]
       fps = dico[1]
       duration = dico[2]
       
       
      
    def var_to_csv(self,dico):  # fonction de passage de var à csv
       dico[0] = nameVideo
       dico[1] = fps
       dico[2] = duration
       
       
        
    def ListFichiers(self):   # fontion que permet afficher les analyses effectué ça depend du cas (global ou sequentiel) on ouvrira les fichier
        
        self.info.delete(0,"end")
        self.liste=[]
        cpt=1
        
        '''fichier = csv.reader(open("fichierVar.csv", "r"), delimiter=',') # on ouvre le fichierVar pour obtenir la variable chooix et savoir si utilisateur est en mode sequentiel ou global
        for row in fichier:
            choix=row[0]            #on garde dans la variable choix
            
        
        if choix=='1':  # le numero 1 correspond au mode sequentiel , et normalement le numero 2 est global
            
            source = csv.reader(open("fichierOneVideo.csv", "r"), delimiter=',')  #on va ouvrir le fichierOneVideo pour sorter les info
        else :
            '''
        source = csv.reader(open("fichierMultiVideos.csv", "r"), delimiter=',')  # si on est en mode global on va ouvrir le fichierMultiVideos  
        
        self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )      
        self.info.insert(END,"                   Videos that will be analyzed               "  )     # ça depend du choix on va afficher la lsite de fihcier ou videos analysé
        self.info.insert(END,"----------------------------------------------------------------------------------------------------------- "  )
        for line in source:
            l=[]                #liste qui contiendra les informations d'un contact sans les balises VCard
            for x in line:                 
                l.append(x)
            self.liste.append(l)
            self.csv_to_var(l)
                
            self.info.insert(END," video "+str(cpt)+". >>> " + nameVideo )
            cpt=cpt+1
              
        self.entry.configure(textvariable=self.choix)
        self.btnMontrer.configure(state="active") 
        self.btnSupp.configure(state="active")
        self.btnStart.configure(state="active")
    def Montrer(self):                        # permet de afficher les informations concernant le fichier choisi
            
            self.info.delete(0,"end") 
            choix=self.choix.get()
            if  choix!="":
                choix=int(choix)
                choix=choix-1
                liste=self.liste[choix]
                self.csv_to_var(liste)
             
             
                self.info.insert(END,"Name :   "+nameVideo )
                self.info.insert(END,"fps :   "+fps )
                self.info.insert(END,"duration :   "+duration )
                
              
     
    def rewrite(self,dico):                #Réecrit le fichier  après modification d'une liste "dico"
        
        global nameVideo, fps, duration 
        
        '''fichier = csv.reader(open("fichierVar.csv", "r"), delimiter=',') # on ouvre le fichierVar pour obtenir la variable chooix et savoir si utilisateur est en mode sequentiel ou global
        for row in fichier:
            choix=row[0]            #on garde dans la variable choix
            
        
        if choix=='1':  # le numero 1 correspond au mode sequentiel , et normalement le numero 2 est global
            
            source = csv.writer(open("fichierOneVideo.csv", "w"))  #on va ouvrir le fichierOneVideo pour enregistrer les changement
        else :'''
            
        source = csv.writer(open("fichierMultiVideos.csv", "w"))#on va ouvrir le fichierMultiVideos pour enregistrer les changement
        
        
        for i in dico:
            nameVideo = i[0]
            fps = i[1]
            duration = i[2]
            
            source.writerow([nameVideo,fps,duration]) # enregistrement des changement effectué      
    
        
    def Supprimer(self):    
        
        
        choix=self.choix.get()
         
        choix=int(choix)
        choix=choix-1
         
        self.liste.pop(choix)        
        self.rewrite(self.liste)   #on envoie la nouvelle liste dans la fonction rewrite pour enregistre les changement
        
        return self.ListFichiers()
    
    
    def clear(self):  # On effacer tout le contenu affiché dans le listBox
          
        self.info.delete(0,"end")
           
        
           
         
        