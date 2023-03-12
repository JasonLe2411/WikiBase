import threading
import tkinter as tk
import time
from azureSpeechModule import AzureSpeechModule


stop_flag = False

def python_main( ): 
    input("Enter number of users") #and so on.
    def python_sub( ): #and complete program of multiple functions
        pass

tkwindow = tk.Tk()

def flip_stop():
    global stop_flag
    if stop_flag:
        stop_flag = False
    else:
        stop_flag = True
    print(stop_flag)

def fuck():
    while not stop_flag:
        print("hihihdasifhadsfhiasdhif")
        time.sleep(1)
        azureSpeechModule = AzureSpeechModule()
        azureSpeechModule.speech_recognize_continuous_async_from_microphone()
            

def tkinter_func():
    button = tk.Button(tkwindow, text="press me", border=0, command=threading.Thread(target=fuck).start) 
    button.place(x=4,y=4)

def tkinter_stop_button():
    button2 = tk.Button(tkwindow, text="FLIP FLIP", border=0, command=flip_stop) 
    button2.place(x=100, y=4)


tkinter_func()
tkinter_stop_button()
tkwindow.mainloop()