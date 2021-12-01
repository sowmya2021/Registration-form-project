from tkinter import *
root = Tk()
root.geometry("400x300")

def getvals():
    print("Accepted")

# heading
Label(root, text="Python Registration form" , font="ar 15 bold").grid(row=0,column=3)

# fied name
name= Label(root, text="Name")
phone= Label(root, text="Phone")
gender= Label(root, text="Gender")
date= Label(root, text="Date")
paymentmode= Label(root, text="Payment Mode")

# packing fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
date.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

# variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
datevalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

# creating entry fields
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
dateentry = Entry(root, textvariable=datevalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# packing entry fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
dateentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# creating check box
checkbtn = Checkbutton(text="Remember me?", variable = checkvalue)

# packing check box
checkbtn.grid(row=6 , column=3)

# submit button
Button(text="Submit" , command=getvals).grid(row=7 , column=3)

root.mainloop()


