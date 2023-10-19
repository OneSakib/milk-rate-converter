from tkinter import *
from PIL import Image, ImageTk
import datetime
from tkinter.filedialog import *
from tkinter import messagebox as mb
from logic import gen_data
import xlrd
 # GUI Decleration
root = Tk()
root.title("Milk Rate Converter")
root.geometry('738x415')
photo = Image.open(r'background.jpeg')
bg = ImageTk.PhotoImage(photo)
logophoto = Image.open(r'logo.jpeg')
logo = ImageTk.PhotoImage(logophoto)
root.iconphoto(False, logo)
label1 = Label(root, image=bg)
label1.place(x=0, y=0)
root.resizable(0, 0)
# Static Value
filename=''
# # Dropdown menu options
# sheet_list = [
#     "Cow",
#     "Buffalo",
#     "Mix"
# ]
# select_sheet=None
# datatype of menu text
# select_sheet = StringVar()
# save generated file
def savefile(data):
    try:
        file_extension = [('Text Document', '*.txt'),('All Files', '*.*')]
        name = asksaveasfile(mode='w', filetypes=file_extension,defaultextension=file_extension)
        if name:
            name.write(data)
            name.close()
            mb.showinfo("Save File", "File Save Successfully")
    except Exception as e:
        mb.showerror("Error on Save", f"Error is : {e}")

def select_file(file_path_text):
    filetypes = (
        ('Excel files', '*.xls'),
        ('All files', '*.*')
    )
    global filename
    filename = askopenfilename(
        title='Open a file',
        initialdir='/Users/malik/Desktop',
        filetypes=filetypes)
    filename=filename    
    file_path_text.delete("1.0",END)
    file_path_text.insert("1.0",filename)
    file_extension=filename.split('.')[-1]
    if(file_extension not in ['xls']):
        mb.showerror('File','File formart is wrong, please chose corrent file format like xls.')
    else: 
        # global select_sheet
        # book=xlrd.open_workbook(filename)
        # book_sheets_names=book.sheet_names()
        # sheet_list=book_sheets_names
        # select_sheet_option_menu=OptionMenu(root,select_sheet,*sheet_list)
        # select_sheet.set(sheet_list[0])
        # select_sheet_option_menu.configure(width=8,height=1,font='TimesNewRoman 15 bold italic',fg='blue')
        # select_sheet_option_menu.place(relx=0.05, rely=0.4)
        mb.showinfo("File", "File is in processing!")
def convert_file():
    if(len(filename)==0):
        mb.showerror('File','Please select file first!')
    else:
        file_extension=filename.split('.')[-1]
        if(file_extension not in ['xls']):
            mb.showerror('File','File formart is wrong, please chose corrent file format like xls.')
        else:
            mb.showinfo("File", "File is in processing!")
            global sheet_list
            status,data=gen_data(file_path=filename)
            if status:
                savefile(data)
            else:
                mb.showerror("File","Error occur while convert file")                
def gui_main():
    label = Label(root, text="Milk Rate Converter", font='TimesNewRoman 25 bold italic underline', fg='red', bd=5, bg=None)
    label.place(relx=0.3, rely=0.01)
    dateis = datetime.datetime.now()
    label = Label(root, text=f"Today: {dateis.day}/{dateis.month}/{dateis.year}",
                font='TimesNewRoman 15 bold italic underline', fg='red', bd=5, bg=None)
    label.place(relx=0.4, rely=0.12)

    pricestring = ""
    # Lables for Input VaLue
    file_path_text = Text(root, font='TimesNewRoman 15 bold italic', width=40,height=5,
                      bd=3)
    select_file_btn = Button(root, text='Select File: ', font='TimesNewRoman 15 bold italic', fg='blue',command=lambda:select_file(file_path_text))
    # btn for action performed
    convert_file_btn = Button(root, text='Convert File', font='TimesNewRoman 15 bold italic', fg='white', bg='green', bd=3,
                     command=convert_file)
    exitbtn = Button(root, text='Exit', font='TimesNewRoman 15 bold italic', fg='white', bg='red', bd=3,
                     command=root.destroy)
    select_file_btn.place(relx=0.05, rely=0.3)
    file_path_text.place(relx=0.3, rely=0.3)
    convert_file_btn.place(relx=0.6, rely=0.8)
    exitbtn.place(relx=0.8, rely=0.8)
    root.mainloop()
