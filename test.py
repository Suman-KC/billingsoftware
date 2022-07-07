from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.title('my box Gui')
name='#4D0039'

#set variables
cnamee=StringVar()
cphonee=StringVar()
billnoo=StringVar()
Ittem=StringVar()
Raate=IntVar()
Quanntity=IntVar()
x=random.randint(1000,9999)
billnoo.set(str(x))
global t
t=[]
#function name
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t welcome kAMAL retails")
    textarea.insert(END,f'\n\nbill number:\t\t{billnoo.get()}')
    textarea.insert(END,f'\ncustomer name:\t\t{cnamee.get()}')
    textarea.insert(END,f"\nphnone number:\t\t{cphonee.get()}")
    textarea.insert(END,f"\n\n======================================")
    textarea.insert(END,f'\nProduct\t\tQty\t\tPrice')
    textarea.insert(END,f"\n======================================\n")
    textarea.configure(font='areal 15 bold')
         
    ###add item
def additem():
    N=Raate.get()
    M=Quanntity.get()*N
    t.append(M)
    if Ittem.get()=='':
     messagebox.showerror('error ','please enter the item')
    else:
     textarea.insert(10.0+float(len(t)-1),f'{Ittem.get()}\t\t{Quanntity.get()}\t\t{M}\n')

#generate bill;

def gbill():
    if cnamee.get()=='' or cphonee.get()=='':
     messagebox.showerror('error','customer details are most')
    else:
     tex=textarea.get(10.0,(10.0+float(len(t))))
    welcome()
    textarea.insert(END,tex)
    textarea.insert(END,f'\n===================================')
    textarea.insert(END,f"\ntotal paybill amount :\t\t\t{sum(t)}")
    textarea.insert(END,f'\n===================================')
    savebill()
    
    
    # for save bill

def savebill():
    op=messagebox.askyesno('savebill','do you want to save the bill')
    if op>0:
      bill_details=textarea.get(1.0,END)
      f1=open("text/"+str(billnoo.get())+".txt",'w')
      f1.write(bill_details)
      f1.close()
      messagebox.showinfo('saved ',f'Bill no: {billnoo.get()} saved successfully')
    else:
      return

# for clear
def clear():
    cnamee.set('')
    cphonee.set('')
    Ittem.set('')
    Raate.set(0)
    Quanntity.set(0)
    welcome()


 

def exit():
    op=messagebox.askyesno('exit','Do you want to really exit')
    if op>0:
     root.destroy()


                   

#main title start#
# 
title=Label(root,text='SANGAM SWEET HOUSE',bg=name,fg='white',font=('times new roman',30,'bold'),relief=GROOVE,bd=15)
title.pack(fill=X)
F1=LabelFrame(root,text='customer details',font=('times new roman',18,'bold'),relief=GROOVE,bg=name,fg='gold',bd=10)
F1.place(x=0,y=80,relwidth=1)
cname_lbl=Label(F1,text='customer name',font=('times new roman',18,'bold'),bg=name,fg='white')
cname_lbl.grid(row=0,column=0,padx=10,pady=5)
cname_txt=Entry(F1,width=15,font='areal 15 bold',relief=SUNKEN,textvariable=cnamee)
cname_txt.grid(row=0,column=1,padx=10,pady=5)
#mobile_number
mname_lbl=Label(F1,text='mobile number',font=('times new roman',18,'bold'),bg=name,fg='white')
mname_lbl.grid(row=0,column=2,padx=10,pady=5)
mname_txt=Entry(F1,width=15,font='areal 15 bold',relief=SUNKEN,textvariable=cphonee)
mname_txt.grid(row=0,column=3,padx=5,pady=5)
#product details
F2=LabelFrame(root,text='product details',font=('times new roman',18,'bold'),relief=GROOVE,bg=name,fg='gold',bd=10)
F2.place(x=20,y=180,width=630,height=550)
item=Label(F2,text='product name',font=('times new roman',18,'bold'),bg=name,fg='light green')
item.grid(row=0,column=0,padx=20,pady=30)
item_txt=Entry(F2,width=15,font='areal 15 bold',relief=SUNKEN,textvariable=Ittem)
item_txt.grid(row=0,column=1,padx=20,pady=30)
#rate
rate=Label(F2,text='product rate',font=('times new roman',18,'bold'),bg=name,fg='light green')
rate.grid(row=1,column=0,padx=20,pady=30)
rate_txt=Entry(F2,width=15,font='areal 15 bold',relief=SUNKEN,textvariable=Raate)
rate_txt.grid(row=1,column=1,padx=20,pady=30)
#for quantity
quantity=Label(F2,text='product amount',font=('times new roman',18,'bold'),bg=name,fg='light green')
quantity.grid(row=2,column=0,padx=20,pady=30)
quantity_txt=Entry(F2,width=15,font='areal 15 bold',relief=SUNKEN,textvariable=Quanntity)
quantity_txt.grid(row=2,column=1,padx=20,pady=30)
#button
btn1=Button(F2,text='Add item',font='areal 15 bold',padx=5,pady=5,bg='lime',width=10,command=additem)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Generate',font='areal 15 bold',padx=5,pady=5,bg='lime',width=10,command=gbill)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='areal 15 bold',padx=5,pady=5,bg='lime',width=10,command=clear)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='areal 15 bold',padx=5,pady=5,bg='lime',width=10,command=exit)
btn4.grid(row=4,column=1,padx=0,pady=0)
#bill area
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)
billtitle=Label(F3,text='Bill Area',font='areal 15 bold',relief=GROOVE,bg=name,bd=10).pack(fill=X)
scroll_txt=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_txt)
scroll_txt.pack(side=LEFT,fill=Y)
scroll_txt.config(command=textarea.yview())
textarea.pack()
welcome()








root.mainloop()