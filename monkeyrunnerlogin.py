#!/usr/bin/python
#coding:utf-8
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
device = MonkeyRunner.waitForConnection()
device = removePackage('com.qttecx.utop.activity')
MonkeyRunner.sleep(5)
print('Uninstall Success')
device.installPackage('F:/android/UTOP_gradle/app/app-baidu-release.apk')
MonkeyRunner.sleep(5)
print ('Install Success')

device.startActivity('com.qttecx.utop.activity/.MainLoadingActivity') 
MonkeyRunner.sleep(5)
device.touch(600,1200,'DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.touch(300,100,'DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.touch(100,250,'DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.type('15982363762')
MonkeyRunner.sleep(2)
device.touch(550,400,'DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.type('123456')
MonkeyRunner.sleep(2)
device.touch(400,500,'DOWN_AND_UP')
