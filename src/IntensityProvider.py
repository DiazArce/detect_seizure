#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import csv
import matplotlib.pyplot as plt
import ast
from matplotlib.widgets import Button
import Tkinter as tk
import __builtin__

__builtin__.intensities = []
    

#if __name__ == '__main__' :
def computeIntensities(self, allIntensities): 
    

    # déclaration des variables concernant les régions d'intérêt
    
    scale = 1.
    
    vecRect=[]
    file_rects = csv.reader(open("fichierROI.csv", "r")) #ouvrir et enregistre les coordonnées dans la list vectRect
    for row in file_rects:
        vecRect.append(row)
        
       
    

    source = csv.reader(open("fichierMultiVideos.csv", "r"))#ouvrir le fichier qui contient les données de vidéos
    listSource = []
    for row in source:
        listSource.append(row)
   
    recurseInVideo(self, listSource, vecRect, scale, 0, allIntensities)
    


def recurseInVideo(self, source, vecRect, scale, i, allIntensities):
    
    nVideos = float(len(source))
    self.updating((i+1)/nVideos)
    
    if i < nVideos :
        processVideo(source[i][0], float(source[i][1]), vecRect, scale, allIntensities)
        self.after(1, recurseInVideo, self, source, vecRect, scale, i + 1, allIntensities)



def processVideo(videoPath, fps, regions, scale, allIntensities):
    file_rects_out = csv.writer(open("fichier.csv", "w"))
    vidcap=cv2.VideoCapture(videoPath)  
         
    _, frame = vidcap.read() 
    
    previous_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    previous_gray = cv2.resize(previous_gray, None, fx = scale, fy  = scale, interpolation = cv2.INTER_CUBIC)# Size?
    previous_gray = cv2.blur(previous_gray,(5,5))
    
    intensity=[]
    aIndex = 0
    
    old_percentage = 0
    
    while True:
        
        for i in range(24) :
            aIndex = aIndex + 1
            # on extraie une nouvelle image de la vidéo
            ret, frame = vidcap.read()
        
        if not ret:
            break
           
        row = []
        next_gray = []

        next_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #modif
        next_gray = cv2.resize(next_gray, None, fx = scale, fy = scale, interpolation = cv2.INTER_CUBIC)
        next_gray = cv2.blur(next_gray,(5, 5)) 
        
        

        row.append(aIndex / fps)
        
        for k in range(0, len(regions[0])):#python
            
            roi = ast.literal_eval(regions[0][k])

            previous_cage = previous_gray[int(roi[0][1]*scale):int(roi[1][1]*scale),
                                           int(roi[0][0]*scale):int(roi[1][0]*scale)]
            next_cage = next_gray[int(roi[0][1]*scale):int(roi[1][1]*scale),
                                   int(roi[0][0]*scale):int(roi[1][0]*scale)]  
            
            
            flow = cv2.calcOpticalFlowFarneback(previous_cage, next_cage,None, 0.5, levels = 5, winsize = 3, iterations = 3, poly_n = 5, poly_sigma = 1.2, flags = 0)
                
            #_, flow = cv2.threshold(flow, 400000,0,cv2.THRESH_TRUNC)
            #_, flow = cv2.threshold(flow, scale, 5, 3)
            gx = cv2.Sobel(flow, cv2.CV_64F, 1, 0, ksize=5)   
            gy = cv2.Sobel(flow, cv2.CV_64F, 0, 1, ksize=5)
            
            #print "gx = ", gx
                      
            mag = cv2.magnitude(gx, gy)            
            
            #cv2.waitKey(1)
            
            
            #print "mag = ", mag
            
            #row.append(sum(mag)[0][0]+sum(mag)[0][1])
            row.append( sum(sum(sum(mag))))
            new_percentage = aIndex * 100 / int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
            if new_percentage > old_percentage :
                print new_percentage, " %"
                old_percentage = new_percentage
            #row.append( sum(sum(sum(mag))))
        file_rects_out.writerow(row)    
        intensity.append(row)

        previous_gray = next_gray.copy() 
    allIntensities.append(intensity)
    
    __builtin__.intensities = allIntensities
  

