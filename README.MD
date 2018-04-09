set up envirent
1.安装python
2.安装win32api
3.安装pyinstaller pip install pyinstaller
4.打包过程：
    准备：
    先确认C:\Python27\Scripts，在环境变量PATH中。
    只有这样，才可以在命令行使用pyinstaller这个命令。
    打开cmd输入pyinstaller输出帮助信息就说明安装成功了
  a. cd 到PIDPicker.py所在目录
  b. 带控制台打包: pyinstaller.exe -F PIDPicker.py -n win7C.exe
  c. 不带控制台打包:pyinstaller.exe -F -w PIDPicker.py -n win7W.exe
  d. -F 是打成单文件 -W是隐藏控制台 -n是指写输出名字，可以省略则与.py文件同名。
5.打包不是必须的，目的是为了部署方便。
  如果安装了python及win32api，只要双击PIDPicker.py也可以运行
  如果不想看到控制台，只要把PIDPicker.py后加一个"w"，即改文件名为:PIDPicker.pyw
  就看不到控制台了。这样也是可以直接用的。  
  
    