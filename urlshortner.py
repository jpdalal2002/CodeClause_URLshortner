import pyshorteners
import pyperclip
from tkinter import *

window = Tk()
window.title("URL Shortner")
window.geometry('500x300')
window.configure(bg='#96b3a7')

url = StringVar()
url_address = StringVar()

def urlshortner():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(window, text="My URL Shortner", font="ivy 20", bg='#96b3a7', fg='#000000').pack(pady=10)
Entry(window, textvariable=url).pack(pady=5)
Button(window, text="Generate short url", command=urlshortner).pack(pady=7)
Entry(window,textvariable=url_address).pack(pady=5)
Button(window, text="Copy URL", command=copyurl).pack(pady=5)

window.mainloop()