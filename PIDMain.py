#coding:utf-8
'''
Created on 2018年3月15日

@author: lihaijiang
'''
import subprocess,os
import win32api
from Tkinter import * 
from ConfigParser import ConfigParser
class PIDMain(object):
    root = Tk() 
    icon=PhotoImage(file="logo.gif")
    dragLabel=None
    menu=None
    pidtext = StringVar()
    entry = None
    x,y=0,0
    url=''
    command=''
    fgcolor='black'
    bgcolor='white'
    width=100
    height=30
    state='disabled'
    title='PIDPICKER'
    hidetitle=True
    scree_w=win32api.GetSystemMetrics (0)
    scree_h=win32api.GetSystemMetrics (1)
    wintitle=""
    pidindex=-1
    regexpr=""
    
    def callback(self,obj):
        finalUrl = self.url%(self.entry.get())
        print finalUrl
        finalCmd = r'%s %s'%(self.command,finalUrl)
        print finalCmd
        os.system(finalCmd)
        
    def exitApp(self):
        self.root.destroy()
    
    def popup(self,event):
        self.menu.post(event.x_root,event.y_root)
    
    def move(self,event):
        new_x = (event.x-self.x)+self.root.winfo_x()
        new_y = (event.y-self.y)+self.root.winfo_y()
        #s = "300x200+" + str(new_x)+"+" + str(new_y)
        s='%dx%d+%d+%d'%(self.width,self.height,new_x,new_y)
        self.root.geometry(s)
        
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('conf.ini')
        self.pidindex=self.config.getint('pid', 'index')
        self.regexpr=self.config.get('pid', 'regexpr')
        self.url=self.config.get('pid', 'url')
        self.command=self.config.get('pid', 'command')
        self.fgcolor=self.config.get('gui', 'fgcolor')
        self.bgcolor=self.config.get('gui', 'bgcolor')
        self.width=self.config.getint('gui', 'width')
        self.height=self.config.getint('gui', 'height')
        self.state=self.config.get('gui', 'state')
        self.hidetitle=self.config.getboolean('gui', 'hidetitle')
        self.title=self.config.get('gui', 'title')
        self.wintitle=self.config.get('gui', 'wintitle').decode('utf-8')
        
        self.root.title(self.title)
        self.root.overrideredirect(self.hidetitle)
        self.root.wm_attributes('-topmost',1)
        geo='%dx%d+%d+%d'%(self.width,self.height,self.scree_w-self.width,100)
        self.root.geometry(geo)
        self.root.resizable(0, 0)
        self.pidtext.set("")
        print self.bgcolor,self.fgcolor
        self.dragLabel=Label(image=self.icon)
        self.entry=Entry(self.root, 
                       textvariable =self.pidtext,
                       disabledbackground=self.bgcolor,
                       disabledforeground=self.fgcolor,
                       fg=self.fgcolor,
                       bg=self.bgcolor,
                       #cursor='hand2',
                       state = self.state)
        self.dragLabel.bind('<Double-Button-1>', self.callback)
        self.entry.grid(row=0,column=1)
        self.menu = Menu(self.root,tearoff=0)
        self.menu.add_command(label="Exit",command=self.exitApp)
        self.dragLabel.bind("<Button-3>",self.popup)
        self.dragLabel.bind("<B1-Motion>",self.move)
        self.dragLabel.grid(row=0,column=0)
        

if __name__ == '__main__':
    p = PIDMain()
    p.root.mainloop()
