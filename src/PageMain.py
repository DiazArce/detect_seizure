#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk

TITLE_FONT = ("Helvetica", 18, "bold")
class PageMain(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.ratioHeight = parent.winfo_screenheight() / 1024
        self.ratioWidth  = parent.winfo_screenwidth() / 1280
        
        
     # FRAME qui contient les buttons de passage   
        frame=tk.Frame(self,borderwidth=2,
                       width=900 * self.ratioWidth,
                       height=120 * self.ratioHeight,
                       relief=GROOVE,bg="#FFFFCC")   #Frame on haut dans la tête qui contient les frames 1 ,2 et 3
        frame.pack(side="top", expand=True,padx=20,pady=(50,5)  ) 
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
        
        button = tk.Button(frameBtn, text="Main",state="disabled", disabledforeground="#F50743",background="yellow",
                           command=lambda: controller.show_frame("PageMain"))
        button1 = tk.Button(frameBtn, text="Select Files",
                           command=lambda: controller.show_frame("Parameters"))   
        button2 = tk.Button(frameBtn, text="Select ROI",
                            command=lambda: controller.show_frame("Selection"))
        button3 = tk.Button(frameBtn, text="Detect",
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
        
        contPie=tk.Frame (self,width=900* self.ratioWidth,
                           height=70* self.ratioHeight,
                           borderwidth=2, relief=GROOVE,bg="#FFFFCC")

           
        Frame=tk.Frame(contPie, borderwidth=2, relief=GROOVE,bg='ivory')
        exitButton = tk.Button(Frame, text="EXIT",activebackground="yellow",width=10, height=9, command=exit)
        exitButton.pack(padx=5,pady=5)
        exitButton.pack_propagate(False)
        Frame.pack(padx=5,pady=5)
        
        contPie.pack(padx=5,pady=(5,50),side="bottom")   
        contPie.pack_propagate(False)
        
        self.Container() #initialiser la fonction Container
        
           
    def Container(self):   
                 
        
        contenu=tk.Frame(self,borderwidth=2,width=900* self.ratioWidth,
                         height=500* self.ratioHeight,
                         relief=GROOVE,bg="#FFFFCC")
        
        frameTitle=tk.Frame(contenu,borderwidth=2,width=900* self.ratioWidth,
                            height=100* self.ratioHeight,
                            relief=GROOVE, bg='ivory')
        labeltitle=tk.Label(frameTitle,borderwidth=2,relief=GROOVE,text=" SASDI - Semi Automatic Seizure Detection from Images ",font=TITLE_FONT,bg="#FFFFCC")
        labeltitle.pack(side="top",padx=20,pady=20)
        frameTitle.pack(side="top", expand=True,padx=10,pady=5)
        frameTitle.pack_propagate(False)
        
        frameImage=tk.Frame(contenu,borderwidth=2,
                            width=450*self.ratioWidth,
                            height=300*self.ratioHeight,
                             relief=GROOVE, bg='ivory')
        frameImage.pack(side="left",padx=10,pady=5)
        frameImage.pack_propagate(False)
        img = Image.open("ipmc.jpg")                                                        #avec la librery PIL on utilise le module Image
        photoimg = ImageTk.PhotoImage(img)                                                  # et ImageTk.PhotoImage qui sert à ouvir et charge une image
            
        lblLeft =tk. Label(frameImage,image=photoimg,borderwidth=3,relief=GROOVE)                                             # Label qui contient l'image de logo ipmc
        lblLeft.image = photoimg 
        lblLeft.pack()
        
        
        frameGuide=tk.Frame(contenu,borderwidth=2,
                            width=450*self.ratioHeight,
                            height=300*self.ratioHeight,
                            relief=GROOVE, bg='ivory')
        frameGuide.pack(side="right",padx=10,pady=5)
        frameGuide.pack_propagate(False)
        img1 = Image.open("souri.gif")                                                        #avec la librery PIL on utilise le module Image
        photoimg1 = ImageTk.PhotoImage(img1)                                                  # et ImageTk.PhotoImage qui sert à ouvir et charge une image
            
        lblRight =tk. Label(frameGuide,image=photoimg1,borderwidth=3,relief=GROOVE)                                             # Label qui contient l'image de logo ipmc
        lblRight.image = photoimg1 
        lblRight.pack(padx=10, pady=5) 
        
        btnR=tk.Button(frameGuide,text="User Guide")
        btnR.pack(side="bottom",padx=10,pady=5)
        
        contenu.pack(side="bottom", expand=True,padx=(50,50),pady=(5,10))
        contenu.pack_propagate(False)
        
