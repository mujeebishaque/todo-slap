from tkinter import messagebox
from tkinter import Tk

class Alerts:

    @staticmethod
    def show_alert(type=None, text=None):
        window = Tk()
        window.withdraw()
        if type.lower() == 'warning':
            return messagebox.showwarning('Warning', text)
        if type.lower() == 'error':
            return messagebox.showerror('Error', text)    
        return messagebox.showinfo('Info', text)
    
    @staticmethod
    def ask_question(text: str = ''):
        window = Tk()
        window.withdraw()
        return messagebox.askyesno('Info Required', text)
