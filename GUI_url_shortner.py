from tkinter import *
from tkinter import ttk
import pyshorteners # pip install pyshortneres
import webbrowser

# main window
root=Tk()
root.title("URL Shortner")
root.geometry("500x250")
root.resizable(0, 0)
# label
label=ttk.Label(root, text="URL Shortener", font=('Popping', 25))
label.grid(row=0)
# label for input URL
url_input=ttk.Label(root, text="Enter URL: ")
url_input.grid(row=1, column=0, pady=10)
# input fied for URL
url=StringVar()
url_entry=ttk.Entry(root, textvariable=url, width=40)
url_entry.grid(row=1, column=1, pady=10)

# Button for Short URL
shorten_button=ttk.Button(root, text="Shorten", command= lambda: shorten_url(url.get()))
shorten_button.grid(row=2, column=0, pady=10)

# label for shortebed Url
shortened_url_label=ttk.Label(root, text="Shortened Url: ")
shortened_url_label.grid(row=4, column=0, pady=10)
# input field for output Url
output_url=StringVar()
output_url_entry=ttk.Entry(root, textvariable=output_url, width=40)
output_url_entry.grid(row=4, column=1, pady=10)

# button for Copy Url
copy_button=ttk.Button(root, text="Copy", command=lambda: copy_url(output_url.get()))
copy_button.grid(row=5, column=0, pady=10)
# open Button
open_button=ttk.Button(root, text="Open", command=lambda: open_url(url.get()))
open_button.grid(row=5, column=1, pady=10)

# Function to short URL
def shorten_url(url):
    try:
        short_url=pyshorteners.Shortener().tinyurl.short(url)
        output_url.set(short_url)
    except:
        print("Invalid Url")

# function to copy url
def copy_url(url):
    try:
        url_entry.clipboard_clear()
        url_entry.clipboard_append(url)
        print("Url Copied to clipboard")
    except:
        print("invalid URL")

# function to open URL
def open_url(url):
    try:
        webbrowser.open(url)
    except:
        print("invalid Url")
root.mainloop()