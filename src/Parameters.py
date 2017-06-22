#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import csv
import Tkinter as tk
from Tkinter import *
from tkFileDialog import askopenfilename, askdirectory,askopenfilenames  # chercher le path d'un fichier
import subprocess 
from os import listdir # pour afficher le contenu d'un repertoire
from tkMessageBox import * # dialogo message de confirmation
from Selection import *
from PIL import Image, ImageTk
import os.path as path
import __builtin__
import re
class Parameters(tk.Frame):  # Definition de notre class Parameters 

    def __init__(self, parent, controller): # constructeur de notre class
        tk.Frame.__init__(self, parent)
        self.ratioHeight = parent.winfo_screenheight() / 1024
        self.ratioWidth  = parent.winfo_screenwidth() / 1280
        
        
        frame=tk.Frame(self,borderwidth=2,
                       width=900*self.ratioWidth,
                       height=120*self.ratioHeight,
                       relief=GROOVE,bg="#FFFFCC")   #Frame on haut dans la tête qui contient les frames 1 ,2 et 3
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
          
        # les boutons qui permettent le passage entre pages
        
        button = tk.Button(frameBtn, text="Main",
                           command=lambda: controller.show_frame("PageMain"))
        button1 = tk.Button(frameBtn, text="Select Files",state="disabled",background="yellow", disabledforeground="#F50743",
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
       
        # variables de controle 
        
        self.filename = StringVar(value='Results')
        self.fps = StringVar()
        self.hh = StringVar()
        self.mm=StringVar()
        self.ss=StringVar()
        self.movie_files=StringVar()
        self.Contenu()
       
               
    def Contenu(self):  # fontion qui contient tous les wiget et fonctions 
        
        contenu=tk.Frame(self,borderwidth=3,
                         width=900*self.ratioWidth,
                         height=500*self.ratioHeight,
                         relief=GROOVE, bg="#FFFFCC" )  #Frame Conteneur du contenu qui contient 4 grandes frames
        contenu.pack(side="top", expand=True,padx=(50,50),pady=(5,10))
        contenu.pack_propagate(False)
     
        
    #////////////////////////////// CONTENU FRAME PATH et INFO VIDEO /////////////////////////////////////////////////////          
    
        contVideo=tk.Frame(contenu,
                           width=800*self.ratioWidth,
                           height=300*self.ratioHeight,
                           borderwidth=2, relief=GROOVE,bg='ivory') #conteneur generale
        
        #***************************************frame pour les boutons a gauches correspondant à select videos***************************
        labelTitle=tk.Label(contVideo,text="Seizure Report Videos : ",bg= "#f3af38" ).pack(side="top",padx=10,pady=10)
        framebtn1=tk.Frame(contVideo,borderwidth=2, relief=GROOVE,bg="#FFFFCC") 
        button=tk.Button(framebtn1,text="Select Directory",activebackground="yellow",command=self.selectMultiVideo)
        button.pack(side="top",padx=10,pady=10)
        
        btnInfo=tk.Button(framebtn1,text="Select a Video",activebackground="yellow",command=self.selectOneVideo)
        btnInfo.pack(side="top",padx=10,pady=5)  
                       
        framebtn1.pack(side="left",padx=10,pady=10)
        
        
        #************************** la listBox où s'affichera les info demandé **************************
        self.info=tk.Listbox(contVideo,width=50, height=15,)
        self.info.pack(side="left",padx=15,pady=10)
        #fpsInfo=StringVar()
        
        #************************************frame pour les boutons à droit correspondant à effacer la listBox******************************
        framebtn2=tk.Frame(contVideo,borderwidth=2, relief=GROOVE,bg="#FFFFCC")       
        btnClear=tk.Button(framebtn2,text="Clear",activebackground="yellow",command=self.clear)
        btnClear.pack(side="top",padx=10,pady=5) 
               
        framebtn2.pack(side="right",padx=(10,50),pady=10)
        
        contVideo.pack(padx=50,pady=(30,10),side="top")
        contVideo.pack_propagate(False)
              
        
        
    #////////////////////////////// CONTENEUR FRAME POUR FPS et POUR RADIOBUTTON  /////////////////////////////////////////////////////    
        
        
        
        
        
    # ////////////////////////////// CONTENEUR FRAME POUR LA  DUREE /////////////////////////////////////////////////////              
      
          
        FileReport=tk.Frame (contenu,
                             width=800*self.ratioWidth,
                             height=40*self.ratioHeight,
                             borderwidth=2, relief=GROOVE,bg='ivory')
        labelR=tk.Label(FileReport,text="Seizure Report Files : ",bg= "#f3af38" ).pack(side="top",padx=10,pady=10)
        FileReport.pack(padx=5,pady=5,side="top")
        FileReport.pack_propagate(False)
    #////////////////////////////// CONTENEUR FRAME POUR FILE NAME txt /////////////////////////////////////////////////////                     
        contFile=tk.Frame (contenu,
                           width=800*self.ratioWidth,
                           height=100*self.ratioHeight,
                            borderwidth=2, relief=GROOVE,bg='ivory')
        
        
        label=tk.Label(contFile,text="New File Name : ").pack(side="left",padx=(60,40),pady=(5,5))
       
        self.entry = tk.Entry(contFile,textvariable=self.filename,width=40)   # boite pour ecrire le nom du fichier
        self.entry.pack(side="left",padx=(50,5),pady=(5,5))
        
        frameOpen=tk.Frame(contFile,borderwidth=1, relief=GROOVE,bg="#FFFFCC")    #frame qui contient les boutons
        label=tk.Label(frameOpen,text="Previous File Name : ").pack(side="top",padx=10,pady=(5,5))
        btnfile= tk.Button(frameOpen, text="Open",command=self.choose_file_name)
        btnfile.pack(side="top",padx=10,pady=(5,5))
        #btnOk= tk.Button(btnframe, text="OK") 
        #btnOk.pack(side="bottom",padx=(20,20),pady=(5,5))
        
        frameOpen.pack(side="right",padx=(30,30),pady=(5,5))
        
        contFile.pack(padx=5,pady=5,side="top")
        contFile.pack_propagate(False)
        
               
        
    #////////////////////////////// CONTENEUR FRAME POUR PIE de PAGE  /////////////////////////////////////////////////////       
        
        contPie=tk.Frame (self,width=900*self.ratioWidth,
                           height=70*self.ratioHeight,
                           borderwidth=3, relief=GROOVE,bg="#FFFFCC")
        framePie=tk.Frame(contPie,borderwidth=2, relief=GROOVE,bg='ivory')
        btnSave=tk.Button(framePie,text="SAVE",activebackground="yellow",command=self.save)
        btnSave.pack(padx=5,pady=5)
        btnSave.pack_propagate(False)
        framePie.pack(side="bottom",padx=5,pady=5)
        
        contPie.pack(padx=5,pady=(10,50),side="bottom")
        contPie.pack_propagate(False)
        
        
        
    #**************************************** FONCTIONS ************************************************
      
    
    
       
    def save(self):          #On récupère la valeur de fps, duration, nom de fichier text, et  On l'enregistre dans les variables
            list=[]
            #nomFile=self.filename.get()
            choose_file = self.filename.get()
                   
            if not path.exists(choose_file):
                choose_file = choose_file + '.csv'
                
            nameFile=choose_file    
            fic = csv.reader(open("ListFichierCSV.csv", "r")) 
            for row in fic:
                list=row
            if not nameFile in list:    
            #if not path.exists(nomFile):
                
                list.append(nameFile)
                fic = csv.writer(open("ListFichierCSV.csv", "w")) 
                fic.writerow(list)
            
             
            if   self.pathDir != "" :      #si tous les info ont été saisi , message de confirmation et on peut envoyer les parametres             
                showinfo('result','Your selection has been registered successfully!!! .\nNext step Select Cages!')
                __builtin__.namefile=nameFile
                print  __builtin__.namefile
                
                             
            else:
                showwarning('Résult','Attention empty spaces.\nwould you like to complete please  !')                            
                
            
       
    def selectMultiVideo(self):   # On selectionne un repertoire et on affiche le contenu
            
            source = csv.writer(open("fichierMultiVideos.csv", "w"))
            self.pathDir=askdirectory(title="Choose a directory to save to",initialdir = '/home/fabrice/IPMC/VIDEOS').encode('utf-8')
            
            if self.pathDir != "" :    
                self.info.insert(END,"-------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
                self.info.insert(END,"                                            PATH DIRECTORY SELECTED                                                  ")
                self.info.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
                self.info.insert(END,"       From:  "+self.pathDir)
                self.info.insert(END,"\n","----------------------------------------------------------------------------------------------------------------------------------------------------------- ")
                self.info.insert(END,"****************************** CONTENT : ***********************************")
                
                dirs = os.listdir(self.pathDir)

                for file in dirs:
                                    
                    command = ['ffmpeg', '-i', self.pathDir+'/'+file]
                            
                    p = subprocess.Popen(command, stderr=subprocess.PIPE)
                
                    text = p.stderr.read() 
                    
                    duration = re.search(r'Duration:(\s)*((\d+[:])*(\d+)[.](\d+))', text)               
                    if duration is not None:

                        duration = duration.group(2)      
                    else:
                        pass
                
                    fps = re.search(r'(\d+([\,\.]{1}\d+)?)(\s)fps', text)
                    if fps is not None:

                        fps = fps.group(1)
                    else:
                        pass 
                        
                    self.info.insert(END,"       Name :   "+file )
                    self.info.insert(END,"       fps :   "+fps )
                    self.info.insert(END,"       Duration :   "+duration )
                    self.info.insert(END,"--------------------------------------------------------------------------------------------- ")
                   
                    #fichier qui va contenir le file, fps et duration de tous les vidéos selectionnés
                    source = csv.writer(open("fichierMultiVideos.csv", "a")) # à revoir
                    source.writerow([self.pathDir+'/'+file,fps,duration])
                
                          
            else: 
                self.info.insert(END,"************************ You have not selected No folder!!! ... ********************")
            
    def selectOneVideo(self):      # On selectionne un filevideo et on affiche les info de fps et duration
            
             
            path_movie_file = askopenfilename(filetypes = [("Video files", "*.avi *.flv *.mp4 *.mpeg *.asf *.dav")], title=("Choose a video file"),initialdir = '/home/fabrice/IPMC/VIDEOS')
            self.file=path_movie_file
            
            if self.file != "":
                
                command = ['ffmpeg', '-i', self.file]
                  
                p = subprocess.Popen(command, stderr=subprocess.PIPE)
                
                text = p.stderr.read()                
                  
                duration = re.search(r'Duration:(\s)*((\d+[:])*(\d+)[.](\d+))', text)
                if duration is not None:

                    duration = duration.group(2)              
                
                fps = re.search(r'(\d+([\,\.]{1}\d+)?)(\s)fps', text)
                if fps is not None:

                    fps = fps.group(1)
                



                self.info.insert(END," ***************************************************************")
                self.info.insert(END,"                         INFO (FPS and DURATION)                            ")
                self.info.insert(END," ------------------------------------------------------------------------------------------- -")
                self.info.insert(END,"  from :   "+ self.file)
                self.info.insert(END,"  fps :   "+fps)           
                self.info.insert(END,"  duration : "+duration)
                self.info.insert(END," **************************** END *****************************")
                
                source = csv.writer(open("fichierMultiVideos.csv", "w"))
                source.writerow([self.file,fps,duration])
            
            else:               
                self.info.insert(END,"************************ You have not selected No file!!! ... ********************")

                    
                    
   
    def choose_file_name(self):  # On on récupère le nom du fichier où sera stocké les infos de "seizure infos"
            
            choose_file_name= askopenfilename(filetypes = [("files", "*.csv ")], title=("Choose a  file"),initialdir = '/home/fabrice/workspace/Stage_interface/src')
            file=choose_file_name
            
            file=os.path.split(file)[1]
            
            self.entry.delete(0,"end")
            self.entry.insert(END, file)
                
            
            
                         
    def clear(self):  # On effacer tout le contenu affiché dans le listBox
          
        self.info.delete(0,"end") 
        
            
    
                        
    
            
                 
         
            