import tkinter
import time as tm
import os
window_main = tkinter.Tk(className='JailBreak ur Android', )
window_main.geometry("600x400")
window_main.configure(bg='red')




def submitFunction() :
    print('Jailbreaking, please wait')
    tm.sleep(5)
    os.system("C:\\JailbreakAndroid\\Jailbreak_Lan.cmd");
    print("Jailbreaking almost done")
    tm.sleep(50)
    print("Done! now click on install Cydia")

def submitFunction2() :
    print('Installing Cydia, please wait')
    os.system("G:\\JailbreakAndroid\\Install_Cydia.cmd");
    tm.sleep(5)
    print('Done! now ur android is JailBreaked with Cydia')

    
message_1 = tkinter.Message(window_main, text='Welcome to Jailbreak for android, Before you jailbreak make sure you have adb and fastboot installed!')
message_1.pack(expand=True, fill='both')
message_2 = tkinter.Message(window_main, text='After finishing the jailbreak, unlock your device and click install Cydia')
message_2.pack(expand=True, fill='both')
Jailbreak = tkinter.Button(window_main, text ="Jailbreak", command=submitFunction)
Jailbreak.config(width=20, height=2)
Jailbreak.place(x=100, y=200)
Cydia = tkinter.Button(window_main, text ="Install Cydia", command=submitFunction2)
Cydia.config(width=20, height=2)
Cydia.place(x=400, y=200)
window_main.mainloop()
