import tkinter
import time as tm
import os
window_main = tkinter.Tk(className='JailBreak ur Android', )
window_main.geometry("700x500")
window_main['bg']='green'


def submitFunction() :
    print('Jailbreaking, please wait... (If the device after 60 seconds doesnt restart press and hold the power button)')
    tm.sleep(5)
    os.system("C:\\JailbreakAndroid\\Jailbreak_Lan.cmd");
    print("Jailbreaking almost done")
    tm.sleep(50)
    print("Done! now click on install Cydia")

def submitFunction2() :
    print('Installing Cydia, please wait... (This may take a while)')
    os.system("C:\\JailbreakAndroid\\RunCydiaInstall.bat");
    tm.sleep(6)
    print('Done! now ur android is JailBreaked with Cydia')


def submitFunction3() :
    print('Uninstalling Jailbreak, please wait... At the end the device will reboot')
    os.system("C:\\JailbreakAndroid\\UninstallStarter.bat");
    tm.sleep(2)
    print('Rebooting...')
    tm.sleep(5)
    print("Finished")

def Help():
    
    window_main = tkinter.Tk(className='Help guide', )
    window_main.geometry("350x400")
    message_1 = tkinter.Message(window_main, text='Heres The Help to install Jailbreak in your Android')
    message_1.pack(expand=True, fill='both')
    message_2 = tkinter.Message(window_main, text='First Enable USB Debugging: Open Settings > Abot this phone and then tap System version 7 times')
    message_2.pack(expand=True, fill='both')
    message_3 = tkinter.Message(window_main, text='Then Click Jailbreak and wait the device to reboot 2 times (If it doesnt reboot another time after the first time then force reboot it)')
    message_3.pack(expand=True, fill='both')
    message_3 = tkinter.Message(window_main, text='Then once it reboots, unlock the device and Click install Cydia and you finished Jailbreaking your android')
    message_3.pack(expand=True, fill='both')
    
message_1 = tkinter.Message(window_main, text='Welcome to Jailbreak for android, Before you jailbreak make sure you have adb and fastboot installed!')
message_1.pack(expand=True, fill='both')
message_2 = tkinter.Message(window_main, text='After finishing the jailbreak, unlock your device and click install Cydia')
message_2.pack(expand=True, fill='both')
Jailbreak = tkinter.Button(window_main, text ="Jailbreak", command=submitFunction)
Jailbreak.config(width=20, height=2)
Jailbreak.place(x=100, y=200)
Jailbreak = tkinter.Button(window_main, text ="Uninstall Jailbreak", command=submitFunction3)
Jailbreak.config(width=20, height=2)
Jailbreak.place(x=250, y=200)
Cydia = tkinter.Button(window_main, text ="Install Cydia", command=submitFunction2)
Cydia.config(width=20, height=2)
Cydia.place(x=400, y=200)
Cydia = tkinter.Button(window_main, text ="Help", command=Help)
Cydia.config(width=20, height=2)
Cydia.place(x=100, y=350)
window_main.mainloop()
