#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt
import os.path as path
import os
from Results import *
from Detection import *
from matplotlib.widgets import Button
import __builtin__
import fichierCSV

def mainImg(allIntensities):
  
    nVideos = len(allIntensities)
    numberOfRois = len(allIntensities[0][0]) - 1
#**********************TITLE ******************************************************
    
   
    
#/***************************************************************************************
    
    source = csv.reader(open("fichierMultiVideos.csv", "r"))#ouvrir le fichier qui contient les données de vidéos
    listSource = []
    for row in source:
        listSource.append(row[0])
    
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)

    t = [c[0]/60.0 for c in allIntensities[0]] 
    s = [c[1] for c in allIntensities[0]]
     
    filename=listSource[0]
            
    filename1=path.split(filename)[1]
    fig.canvas.set_window_title(' From :  ' + filename1 + '   ROI:  '+ str(1))
    #l = plt.vlines(t, [0], s
    
    l, = plt.plot(t, s,'g^')
    plt.vlines(t, [0], s)
    ax.relim()
    ax.autoscale_view()
    
    class Index(object):
        ind = 1
        video = 1
        cage = 1
        startTime = 0
        
        
        def onclick(self, event):
            size = fig.get_size_inches()*fig.dpi
            if event.y < (.19 * size[1]):
                return
            #print [event.y, size[1]]
            
            #print size
            axisStart = .1255
            maxTime = t[len(t)-1]*60
            startTime = (event.x - axisStart * size[0])/((.9005 - axisStart)*size[0]) * maxTime
            startTime = min(startTime, maxTime)
            startTime = max(startTime, 0)
            
            
            os.system("vlc --start-time=" + str(startTime) + " " + listSource[self.video - 1])
    
        def next(self, event):
            if self.ind + 1 <= numberOfRois * nVideos:
                self.ind += 1
            
            indexObject = (self.ind - 1) / numberOfRois
            indexColumn = (self.ind - 1) % numberOfRois
            
#             if indexColumn == 0:
            t = [c[0]/60.0 for c in allIntensities[indexObject]] 
            s = [c[indexColumn + 1] for c in allIntensities[indexObject]]  
            ax.clear()
            ax.plot(t, s,'g^')
            ax.vlines(t, [0], s)
            
            filename=listSource[indexObject]
            
            filename1=path.split(filename)[1]
            
            fig.canvas.set_window_title(
                ' From:  ' + filename1 +
                ', ROI: '+ str(indexColumn + 1))
            
            '''fig.canvas.set_window_title(
                'Video ' + str(indexObject + 1) +
                ', Cage: '+ str(indexColumn + 1))'''
           
            ax.relim()
            ax.autoscale_view()
                
            plt.draw()
            self.get(indexObject,indexColumn)
        def prev(self, event):
            if self.ind - 1 >= 1:
                self.ind -= 1
    
            indexObject = (self.ind - 1) / numberOfRois
            indexColumn = (self.ind - 1) % numberOfRois
            
#             if indexColumn == numberOfRois - 1:
            t = [c[0]/60.0 for c in allIntensities[indexObject]] 
            s = [c[indexColumn + 1] for c in allIntensities[indexObject]]  
            ax.clear()
            ax.plot(t, s,'g^')
            ax.vlines(t, [0], s)

            filename=listSource[indexObject]
            
            filename1=path.split(filename)[1]
            fig.canvas.set_window_title(
                ' From:  ' + filename1 + 
                ',  ROI: '+ str(indexColumn + 1))
                  
            ax.relim()
            ax.autoscale_view()
            plt.draw()
            self.get(indexObject,indexColumn)
            
        def get(self,indexObject,indexColumn):
        
            self.video= indexObject + 1
            self.cage= indexColumn + 1
        
        def select(self,event):
            videoPath = listSource[self.video-1]
            video=path.split(videoPath)[1]
            cage = self.cage
            fichierCSV.main(video,cage)
            
            
    callback = Index()
    axprev = plt.axes([0.4, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.5, 0.05, 0.1, 0.075])
    axselect = plt.axes([0.8, 0.05, 0.15, 0.075])
    
    bnext = Button(axnext, ' > ')
    bnext.on_clicked(callback.next)
    
    bprev = Button(axprev, ' < ')
    bprev.on_clicked(callback.prev)
    
    bselect = Button(axselect, 'Add to Report')
    bselect.on_clicked(callback.select)
    
    fig.canvas.mpl_connect('button_press_event', callback.onclick)
    plt.suptitle(' Seizure Detection  ', fontsize=16)
    
    #ax=plt.xlabel('time')
    #plt.title('subplot 2')
    #plt.ylabel('Intensity')
    plt.show()
