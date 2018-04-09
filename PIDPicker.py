#coding:utf-8
'''
Created on 2018年3月15日

@author: lihaijiang
'''

import win32gui
import win32con
import time,re
import threading
from PIDMain import PIDMain
class PIDPicker(object):
    '''
    find pid box from win32api in a C++Builder Application
    '''

    hdl=0
    pid=None
    pidgui=None
    def __init__(self,pidgui):
        self.pidgui = pidgui
        
        
    def handleSub(self,hdl,param): 
        if win32gui.GetClassName(hdl)=='TEdit':
            self.hdl=hdl        
        return True

    def findPid(self,windowName):
        #find Main Window
        self.mainWin=win32gui.FindWindow(None,windowName)  
        if self.mainWin==0:
            print 'no window..'
            return 0
        #find pid component
        win32gui.EnumChildWindows(self.mainWin,self.handleSub,None)
        if self.hdl==0:
            print 'no box..'
            return -1
        buffer = '0' *50
        len = win32gui.SendMessage(self.hdl, win32con.WM_GETTEXTLENGTH)+1 #获取edit控件文本长度
        win32gui.SendMessage(self.hdl, win32con.WM_GETTEXT, len, buffer) #读取文本
        self.pid=buffer[:len-1]
        return 1
    
    def findPidNew(self,windowName):
        h=win32gui.FindWindow(None,windowName)
        if h==0:
            print 'no window..'
            return 0
        hwndChildList=[]
        try:
            win32gui.EnumChildWindows(h, lambda hwnd, param: param.append(hwnd),  hwndChildList)
        except Exception,e:
            print 'no sub'
            return -1
        if len(hwndChildList)<1:
            print 'no box..'
            return -1
        i=0
        matched=False
        for hdl in hwndChildList:
            txt = win32gui.GetWindowText(hdl)
            try:
                clsname=win32gui.GetClassName(hdl)
            except Exception,e:
                print e
                i+=1
                continue
            if win32gui.GetClassName(hdl)=='TEdit':
                buffer = '0' *50
                lenth = win32gui.SendMessage(hdl, win32con.WM_GETTEXTLENGTH)+1 #获取edit控件文本长度
                win32gui.SendMessage(hdl, win32con.WM_GETTEXT, lenth, buffer) #读取文本
                txt=buffer[:lenth-1]
            if re.match(self.pidgui.regexpr, txt):
                self.pidgui.pidindex=i
                print self.pidgui.regexpr
                print 'matched expr index=',i
                matched=True
            try:
                print i,txt,txt.decode('gbk')
            except Exception,e:
                print e
                print i,txt
                i+=1
                continue
            i+=1
        if not matched:
            print 'Not matched, returned!'
            return 0
        try:
            temp = win32gui.GetWindowText(hwndChildList[self.pidgui.pidindex])
            clsname=win32gui.GetClassName(hwndChildList[self.pidgui.pidindex])
        except Exception,e:
            print e
            return 0
        if win32gui.GetClassName(hwndChildList[self.pidgui.pidindex])=='TEdit':
            buffer = '0' *50
            lenth = win32gui.SendMessage(hwndChildList[self.pidgui.pidindex], win32con.WM_GETTEXTLENGTH)+1 #获取edit控件文本长度
            win32gui.SendMessage(hwndChildList[self.pidgui.pidindex], win32con.WM_GETTEXT, lenth, buffer) #读取文本
            temp=buffer[:lenth-1]
        self.pid=temp.decode('gbk')
        print 'PatietID=',self.pid
        return 1
    
    def run(self):
        while True:
            time.sleep(2)
            try:
                print '---------------',self.pidgui.root.winfo_exists()
            except Exception,e:
                break
            print self.pidgui.wintitle,type(self.pidgui.wintitle)
            r = pidPicker.findPidNew(self.pidgui.wintitle)#u"首都医科大学附属北京友谊医院影像科信息管理系统"
            if r>0:
                self.pidgui.pidtext.set(self.pid)
            else:
                self.pid=''
                self.pidgui.pidtext.set(self.pid)
                
                
    def start(self):
        t = threading.Thread(target=self.run)
        t.start()    
        p.root.mainloop()       
if __name__ == '__main__':
    p = PIDMain()
    pidPicker = PIDPicker(p)
    pidPicker.start()

        
    
