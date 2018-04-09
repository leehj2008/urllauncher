#coding:utf-8
'''
Created on 2018年3月15日

@author: lihaijiang
'''
import win32api
import win32gui
import win32con
import time
import threading
class FindCom(object):
    '''
    find pid box from win32api in a C++Builder Application
    '''

    hdl=0
    pid=None
    pidgui=None
    def __init__(self):
        '''
        Constructor
        '''
        
    def handleSub(self,hdl,param): 
        if win32gui.GetClassName(hdl)=='TEdit':
            self.hdl=hdl        
        return True

    def findPid(self,windowName):
        #find Main Window
        self.mainWin=win32gui.FindWindow("TPanel",None)  
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
    
    def run(self):
        while True:
            time.sleep(2)
            r = self.findPid(u"检查机房")
            if r>0:
                self.pidgui.xls_text.set(self.pid)
    def start(self):
        t = threading.Thread(target=self.run)
        t.start()       
        
def handleSub(hdl,param): 
    cls = win32gui.GetClassName(hdl)
    print cls
    if cls!='TPanel':
        return True
    try:
        txt = win32gui.GetWindowText(hdl)
        if txt.decode('gbk')==u'检查机房':
            print 'match'
    except Exception,e:
        print e

if __name__ == '__main__':
    h=win32gui.FindWindow(None,u"首都医科大学附属北京友谊医院影像科信息管理系统")
    
    print h  
    #win32gui.EnumChildWindows(h,handleSub,None)
    hwndChildList=[]
    win32gui.EnumChildWindows(h, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    i=0
    for hdl in hwndChildList:
        txt = win32gui.GetWindowText(hdl)
        print i,txt.decode('gbk')
        i+=1
    print 'PatietID=',win32gui.GetWindowText(hwndChildList[17])
        
        
        
    