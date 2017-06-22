#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from Selection import * 

refPt = []                              # inicialisation de varible refPt qui est une liste de deux coordonnées (x, y)
boxes = []                              # en spécifiant la région rectangulaire que nous allons recadrer de notre image
rect_endpoint_tmp = []                               
cropping = False                       #un boolean indiquant si nous sommes en Mode de recadrage ou non.
got_roi = False                        # un boolean pour indiquer si on a la zone

def click(pathImg):
    #///////////////////////////////////////   BEGIN FONCTION CLICK AND CROP  ////////////////////////////////////////////
    def click_and_crop(event, x, y, flags, param):   
        global refPt, cropping, got_roi,rect_endpoint_tmp                                               
              
        if event == cv2.EVENT_LBUTTONDOWN:              #Si le bouton gauche de la souris a été cliqué, enregistrez le démarrage                                                    # (X, y) coordonnées et indiquent que la selection est en cours
            refPt = [(x, y)]  
            cropping = True
                                                        # Vérifiez si le bouton gauche de la souris a été libéré
        elif event == cv2.EVENT_LBUTTONUP:              # Enregistrez les coordonnées de fin (x, y) et indiquez que                                                               #L'opération de selection est terminée                                                    
            refPt.append((x,y))
            p1,p2=refPt
            cv2.rectangle(img, p1, p2, color=(0, 255, 0), thickness=1)# Draw a rectangle vert  with thickness of 1 px
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, "R = Record", (10, 50),font, 1,(0, 255, 0), 1) ;
            cv2.putText(img, "D = Discard", (10, 80), font, 1, (0, 0, 255), 1) ;
            cv2.putText(img, "Q = Quit", (10, 110), font, 1,(255, 255, 255), 1) ;           
            cv2.imshow("image", img)
            cropping = False
            got_roi = True              
                     
        elif event == cv2.EVENT_MOUSEMOVE and cropping:        
            rect_endpoint_tmp = [(x, y)]
    #////////////////////////////////////    END FONCTION CLICK AND CROP  ////////////////////////////////////////////////////    
    
    img = cv2.imread(pathImg)                           # Charger l'image, la cloner et configurer la fonction de rappel de la souris
    clone = img.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop) 
    key = cv2.waitKey(1) & 0xFF
    
    while key != ord("q"):                               # Continuez à boucler jusqu'à ce que la touche 'q' soit enfoncée
        cv2.imshow('image', img)                        # Afficher l'image et attendre une touche                     
        if cropping and rect_endpoint_tmp:
            img = clone.copy()
            
            X=refPt[0]
            Y=rect_endpoint_tmp[0]                        
            
            cv2.rectangle(img, X, Y,(0,0,255),1)                # Draw a rectangle blue  with thickness of 1 px                
            cv2.imshow('image', img)
       
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):                               # Si la touche 'r' est enfoncée,on enregistre les coordonnées 
            boxes.append(refPt)    
            #création de un fichier pour stocker les coordonnées
            source=csv.writer(open("fichierROI.csv","w"))
            source.writerow(boxes)  
            
        elif key == ord("d"):                            # Si la touche 'd' est enfoncée,réinitialiser la zone de recadrage
            img = clone.copy() 
         
        elif key==ord("q")  :  
            cv2.destroyWindow("image")                    
    #cv2.destroyWindow("image")
  
  
  