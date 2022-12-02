from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk , Image
root = Tk()
root.geometry('1200x730')
root.title('Hotel Management System')
root.configure(background="#23ada6")
root.resizable(False, False)
root.iconbitmap("golden_duck.ico")


title = Label(root, text='Golden Duck Hotel', bg="#008780", font=('arial', 25,'bold'), fg='White')
title.place(x=449,y=0)

my_img=ImageTk.PhotoImage(Image.open("gold.png"))
my_lable=Label(image=my_img ,bg="#23ada6")
my_lable.place(x=750,y=0)

my_img2=ImageTk.PhotoImage(Image.open("gold.png"))
my_lable2=Label(image=my_img ,bg="#23ada6")
my_lable2.place(x=393,y=0)


my_img3=ImageTk.PhotoImage(Image.open("gg.png"))
my_lable3=Label(image=my_img3 ,bg="#23ada6")
my_lable3.place(x=860,y=550)



#----------left frame GUI
left_frame = Frame(root, bg='white')
left_frame.place(x=7, y=50, width=740, height=670)

lbl_CheckIn = Label(left_frame, text='Check in',bg='#008780', font=('Helvetica', 26, 'bold'), fg='White')
lbl_CheckIn.place(x=0, y=0, height=50,width =740)

lbl_CheckIn_1 = Label(left_frame, text='Enter Name ',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_CheckIn_1.place(x=7, y=60, height=35,width =180)
entstringvarname=StringVar()
Entry_CheckIn_1 = Entry(left_frame,textvariable=entstringvarname, bd='5', justify="left" ,fg='#006778')
Entry_CheckIn_1.place(x=200, y=64,width =375)
entstringvaradd=StringVar()
lbl_CheckIn_2 = Label(left_frame, text='Enter Address ',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_CheckIn_2.place(x=7, y=100, height=35,width =180)


Entry_CheckIn_2 = Entry(left_frame,textvariable=entstringvaradd, bd='5', justify="left",fg='#006778')
Entry_CheckIn_2.place(x=200, y=104,width =375)


entstringvarNUM=IntVar()
lbl_CheckIn_3 = Label(left_frame, text='Enter Number ',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_CheckIn_3.place(x=7, y=140, height=35,width =180)
Entry_CheckIn_3 = Entry(left_frame,textvariable=entstringvarNUM, bd='5',font=('Helvetica', 16, 'bold'),justify="left",fg='#006778')
Entry_CheckIn_3.place(x=200, y=144,width =375)

entstringvarDays=IntVar()

lbl_CheckIn_4 = Label(left_frame, text='Number Of Days ',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_CheckIn_4.place(x=7, y=180, height=35,width =190)
Entry_CheckIn_4 = Entry(left_frame,textvariable=entstringvarDays, bd='5',font=('Helvetica', 16, 'bold'), justify="left",fg='#006778')
Entry_CheckIn_4.place(x=210, y=184,width =367)
#----------check button1
lbl_Choose = Label(left_frame, text='Choose room number',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_Choose.place( x=7,y=220, height=40,width =250)

entSingleRoomString = IntVar()
entSingleRoom = Entry(left_frame , text = "Single",textvariable=entSingleRoomString,width = 6,bg='white', font=('Helvetica', 16, 'bold'), fg='#006778')
entSingleRoom.place(x=90,y=270)

#---------------check button2----------------
lbl_Choose2 = Label(left_frame, text='Choose Payment ',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_Choose2.place( x=350,y=220, height=40,width =250)

Button3 = Checkbutton(left_frame , text = "by cash",onvalue = 1,offvalue = 0,width = 6,bg='#008780', font=('Helvetica', 16, 'bold'), fg='White')
Button3.place(x=350,y=270)

Button4 = Checkbutton(left_frame , text = "by credit card",onvalue = 1,offvalue = 0,width = 10,bg='#008780', font=('Helvetica', 16, 'bold'), fg='White')
Button4.place(x=510,y=270)

#----------fram tree view
lbl_Choose = Label(left_frame, text='Guests Data',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_Choose.place( x=7,y=420, height=200,width =200)

frame_view= Frame(left_frame, bg='#008780')
frame_view.place(x=210, y=420, width=530, height=240)

#Tree View
Gust_Data = ttk.Treeview(frame_view, columns=['Name', 'Room','Address','Number','Days'], show='headings')
Gust_Data.place(x=7,y=7)

#Heading of tree view
Gust_Data['show'] = 'headings'
Gust_Data.heading('Name', text='Name')
Gust_Data.heading('Room', text='Room')
Gust_Data.heading('Address', text='Address')
Gust_Data.heading('Number', text='Number')
Gust_Data.heading('Days', text='Days')

#Names of columns
Gust_Data.column('Name', width=150)
Gust_Data.column('Room', width=50)
Gust_Data.column('Address', width=150)
Gust_Data.column('Number', width=100)
Gust_Data.column('Days', width=50)
#Scrollbar
scrollY = ttk.Scrollbar(frame_view, orient=VERTICAL)
scrollY.pack(side ='right', fill='y')
#button submit------------------------------
left_frame_submit= Frame(left_frame, bg='#008780')
left_frame_submit.place(x=560, y=330, width=150, height=70)
#-------right frame GUI
#search frame
right_frame_search= Frame(root, bg='white')
right_frame_search.place(x=755, y=50, width=440, height=290)

lbl_Search = Label(right_frame_search, text='Search',bg='#008780', font=('Helvetica', 24, 'bold'), fg='White')
lbl_Search.place(x=0, y=0, height=50,width =440)

entSearchVarString = StringVar()
Entry_Search = Entry(right_frame_search, textvariable=entSearchVarString, bd='5', justify="left")
Entry_Search.place(x=7, y=52,width =250)

Combo_Search = ttk.Combobox(right_frame_search)
Combo_Search['values'] = ('Name','Room Number')
Combo_Search.place(x=270, y=52)

Search_btn = Button(right_frame_search, text='Search', bg=('#006778'), font=('arial', 14))
Search_btn.place(x=310, y=80, width=100, height=30)

lbl_Search = Label(right_frame_search, text='Search Result',bg='#008780', font=('Helvetica', 18, 'bold'), fg='White')
lbl_Search.place(x=7, y=120, height=30,width =420)
#Frame for Tree View

frameSearch_TreeView = Frame(right_frame_search)
frameSearch_TreeView.place(x=15, y=170, width=405, height=100)


#Tree View
TableSearch = ttk.Treeview(frameSearch_TreeView, columns=['Name', 'Room'], show='headings')
TableSearch.pack(side ='left')

#Heading of tree view
TableSearch['show'] = 'headings'
TableSearch.heading('Name', text='Name')
TableSearch.heading('Room', text='Room')

#---------------------------------------------------------------------------------------------------------------

#check out frame

right_frame_out= Frame(root, bg='white')
right_frame_out.place(x=755, y=350, width=440, height=90)

lbl_out = Label(right_frame_out, text='check out',bg='#008780', font=('Helvetica', 24, 'bold'), fg='White')
lbl_out.place(x=0, y=0, height=40,width =440)

entDeleteSingleRoomVar = StringVar()
Entry_out = Entry(right_frame_out,textvariable=entDeleteSingleRoomVar, bd='5', justify="left")
Entry_out.place(x=200, y=52,width =130)

lbl_out2 = Label(right_frame_out, text='Enter room number',bg='#008780', font=('Helvetica', 14, 'bold'), fg='White')
lbl_out2.place(x=7, y=52, height=30,width =190)

#-------------------------------------
############################################################################################################################
#Connection Database
import mysql.connector
conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='golden')
cursor = conn.cursor()
selectQuery = 'select * from goldentable'
cursor.execute(selectQuery)
records = cursor.fetchall()
print(records)
for row in records:
    Gust_Data.insert(parent='', index=0, iid=row[0], text='', values=(row[0],row[1],row[2],row[3],row[4]))
conn.commit()
conn.close()
############################################################################################################################
#All Functions
def funBtnSearch():
    conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='golden')
    cursor = conn.cursor()
    selectQuery = 'select * from goldenTable where Name like %s'
    val = [entSearchVarString.get()]
    cursor.execute(selectQuery, val)
    records = cursor.fetchall()
    print(records)  
    for row in records:
        TableSearch.insert(parent='', index=0, iid=row[0], text='', values=(row[0],row[1]))
    conn.commit()
    conn.close()

def funBtnAddData():
    conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='golden')
    cursor = conn.cursor()
    insertQuery = 'insert into goldentable values(%s,%s,%s,%s,%s)'
    cursor.execute(insertQuery, (
    entstringvarname.get(), entSingleRoomString.get(), entstringvaradd.get(), entstringvarNUM.get(),
    entstringvarDays.get()))
    messagebox.showinfo("Message", "Data is inserted!")
    entstringvarname.set("")
    entSingleRoomString.set("")
    entstringvaradd.set("")
    entstringvarNUM.set("")
    entstringvarDays.set("")

    conn.commit()
    conn.close()


def funBtnDelete():
    conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='golden')
    cursor = conn.cursor()

    val = [entDeleteSingleRoomVar.get()]
    cursor.execute('DELETE FROM  goldentable WHERE Room=(%s)', val)
    messagebox.showerror("Message", "Data is deleted!")
    entDeleteSingleRoomVar.set("")
    conn.commit()
    conn.close()



def funExist():
    pass
############################################################################################################################
#All Buttons
#btn search
add_btn = Button(left_frame_submit, text='Submit', command=funBtnAddData, bg=('gold'),fg=('white'), font=('arial',20,'bold'))
add_btn.place(x=7, y=7, width=135, height=55)
#btn add
Search_btn = Button(right_frame_search, text='Search',command=funBtnSearch, bg=('#006778'), font=('arial', 14),fg=('white'))
Search_btn.place(x=310, y=80, width=100, height=30)
#btn delete
delete_btn = Button(right_frame_out, text='Check out', command=funBtnDelete,bg=('#006778'), font=('arial', 14),fg=('white'))
delete_btn.place(x=335, y=52, width=100, height=25)
############################################################################################################################
#exit----------------
right_frame_exit= Frame(root, bg='white')
right_frame_exit.place(x=755, y=460, width=440, height=90)
exist_btn = Button(right_frame_exit, text='Exit',command=root.quit, bg=('#006778'), font=('arial', 26,'bold'),fg=('white'))
exist_btn.place(x=7, y=7, width=425, height=75)




root.mainloop()