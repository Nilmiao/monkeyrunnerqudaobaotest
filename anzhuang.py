#!/usr/bin/python
#coding:utf-8
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
device = MonkeyRunner.waitForConnection()

device.removePackage('com.qttecx.utop.activity')
MonkeyRunner.sleep(5)
print('Uninstall Success')
device.installPackage('F:/android/UTOP_gradle/app/app-baidu-release.apk')
MonkeyRunner.sleep(5)
print ('Install Success')

device.startActivity('com.qttecx.utop.activity/.MainLoadingActivity') 
MonkeyRunner.sleep(50)
result=device.takeSnapshot()
result.writeToFile('F:\\test\\Test1_001.png','png')
