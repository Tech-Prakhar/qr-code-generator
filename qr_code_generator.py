import tkinter
import clipboard
global base_url

sc = tkinter.Tk()
base_url = "https://api.qrserver.com/v1/create-qr-code/?size=150x150"






title = tkinter.Label(text="Welcome To QR CODE GENERATOR!")
title.pack()

info = tkinter.Label(text="Enter a link or text you want a qr code of")
info.pack()

input_user = tkinter.Entry()
input_user.pack()

def generate():
    global url
    get_info = input_user.get()
    transform_string = str(get_info)
    url = base_url +  "&data=" + transform_string
    
    
def copy_to_clipboard():
    text = "hi! "
    clipboard.copy(url)

    
    






generate_button = tkinter.Button(text="Generate",command=generate)
generate_button.pack()

copy_to_clipboard_button = tkinter.Button(text="Copy to clipboard",command=copy_to_clipboard)
copy_to_clipboard_button.pack()

directi = tkinter.Label(text="paste in the search bar of your browser")
directi.pack()




tkinter.mainloop()










