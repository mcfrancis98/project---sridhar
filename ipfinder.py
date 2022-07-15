import tkinter as tk
from socket import gethostbyname
 
def ipFinder(outputMsg, inputValue):
    try:
        ipAddress = gethostbyname(inputValue.get())
        outputMsg.config(text="The IP of domain " + inputValue.get() + " is \"" + ipAddress + "\"")
    except Exception:
        outputMsg.config(text="Please Enter Correct Domain")
 
Tk = tk.Tk()
 
Tk.geometry("400x400+{}+{}".format(400, 400))
 
authorLable = tk.Label(Tk, text="Sridhar J (Consultant - EY)", background='#28334A', foreground="#FFFFFF")
authorLable.grid(row=0, columnspan=4)
 
inputString = tk.StringVar()
 
websiteName = tk.Label(Tk, text="Enter domain", background='#28334A', foreground="#F65058")
input_entry = tk.Entry(Tk, textvariable=inputString)
websiteName.grid(row=1)
input_entry.grid(row=1, column=1)
 
outputMsg = tk.Label(Tk, background='#28334A', foreground="#F65058")
outputMsg.grid(row=3, columnspan=4)
 
button = tk.Button(Tk, text="Check IP", command=lambda : ipFinder(outputMsg, inputString))
button.grid(row=2, columnspan=4)
 
Tk.title('Domain-IP Checker')
Tk.configure(background='#28334A')
Tk.rowconfigure(0, weight=1)
Tk.columnconfigure(0, weight=1)
Tk.rowconfigure(2, weight=1)
Tk.columnconfigure(2, weight=1)
contents = tk.Frame(Tk)
contents.grid(row=1, column=1)
Tk.mainloop()
