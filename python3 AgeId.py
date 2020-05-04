from tkinter import*

def bclick():
    value1=(text_input1.get())
    value2=(text_input2.get())
    value3=(text_input3.get())

    value4=(text_input4.get())
    value5=(text_input5.get())
    value6=(text_input6.get())

    if (value1>value4):
        value1=(int(value1)-int(1))
    if(value2<value5):
        value2=(int(value2)+int(12)-int(1))
    if(value3<value6):
        value3=(int(value3)+int(31)-int(1))

    operator1=(int(value1)-int(value4))
    operator2=(int(value2)-int(value5))
    operator3=(int(value3)-int(value6))

    if(operator1==operator1):
        text=("Your Age Is")
        text_input10.set(text)
        Result=Label(AGE,textvariable=text_input10,font=("Britannic Bold",14),bd=8,bg="medium purple",padx=5,pady=5).grid(row=7,columnspan=10)

        text1=("Years")
        text_input11.set(text1)
        l1=Label(AGE,textvariable=text_input11,font=("Britannic Bold",10),bd=8,bg="DeepSkyBlue",padx=5,pady=5).grid(row=8,column=0)
        Label(AGE,text=" ").grid(row=8,column=1)

        text2=("Months")
        text_input12.set(text2)
        l2=Label(AGE,textvariable=text_input12,font=("Britannic Bold",10),bd=8,bg="DeepSkyBlue",padx=5,pady=5).grid(row=8,column=2)
        Label(AGE,text=" ").grid(row=8,column=3)

        text3=("Days")
        text_input13.set(text3)
        l3=Label(AGE,textvariable=text_input13,font=("Britannic Bold",10),bd=8,bg="DeepSkyBlue",padx=5,pady=5).grid(row=8,column=4)

        result=Label(AGE,textvariable=text_input7,font=("Britannic Bold",10),bd=8,bg="DeepSkyBlue",padx=3,pady=2).grid(row=9,column=0)
        result2=Label(AGE,textvariable=text_input8,font=("Britannic Bold",10),bd=8,bg="DeepSkyBlue",padx=3,pady=2).grid(row=9,column=2)
        result3=Label(AGE,textvariable=text_input9,font=("Britannic Bold",10),bd=8,bg="DeepSkyBlue",padx=3,pady=2).grid(row=9,column=4)
   

    text_input7.set(abs(operator1))
    text_input8.set(abs(operator2))
    text_input9.set(abs(operator3))

def rclick():
    
    text_input1.set("")
    text_input2.set("")
    text_input3.set("")
    text_input4.set("")
    text_input5.set("")
    text_input6.set("")
    text_input7.set("")
    text_input8.set("")
    text_input9.set("")
    text_input10.set("")
    text_input11.set("")
    text_input12.set("")
    text_input13.set("")
    

AGE=Tk()
AGE.title("AGE IDENTIFIER")
AGE.resizable(0,0)

text_input1=StringVar()
text_input2=StringVar()
text_input3=StringVar()
text_input4=StringVar()
text_input5=StringVar()
text_input6=StringVar()
text_input7=StringVar()
text_input8=StringVar()
text_input9=StringVar()
text_input10=StringVar()
text_input11=StringVar()
text_input12=StringVar()
text_input13=StringVar()




#=====================================================================================
Present=Label(AGE,text="Enter The Present Year",font=("Britannic Bold",14),bd=8,bg="mediumpurple",padx=5,pady=5).grid(row=0,columnspan=10)

year2=Label(AGE,text="Year",font=("Britannic Bold",10),bd=8,bg="deepSky Blue",padx=3,pady=3).grid(row=1,column=0)

space6=Label(AGE,text=" ").grid(row=1,column=1)
month2=Label(AGE,text="Month",font=("Britannic Bold",10),bd=8,bg="deepSky Blue",padx=3,pady=3).grid(row=1,column=2)

space7=Label(AGE,text=" ").grid(row=1,column=3)
Date2=Label(AGE,text="Date",font=("Britannic Bold",10),bd=8,bg="deepSky Blue",padx=3,pady=3).grid(row=1,column=4)

YearEntryBox1=Entry(AGE,textvariable=text_input1,font=("Britannic Bold",7),bd=8,bg="Ghost white",insertwidth=4,justify="right").grid(row=2,column=0)
space8=Label(AGE,text=" ").grid(row=2,column=1)

MonthEntryBOx1=Entry(AGE,textvariable=text_input2,font=("Britannic Bold",7),bd=8,bg="ghost white",insertwidth=4,justify="right").grid(row=2,column=2)
space9=Label(AGE,text=" ").grid(row=2,column=3)

DateEntryBox1=Entry(AGE,textvariable=text_input3,font=("Britannic Bold",7),bd=8,bg="ghost white",insertwidth=4,justify="right").grid(row=2,column=4)


#=====================================================================================
OldAge=Label(AGE,text="Enter Your Date Of Birth",font=("Britannic Bold",14),bd=8,bg="mediumpurple",padx=5,pady=5).grid(row=3,columnspan=10)

year=Label(AGE,text="Year",font=("Britannic Bold",10),bd=8,bg="deepSky Blue",padx=3,pady=3).grid(row=4,column=0)

space2=Label(AGE,text=" ").grid(row=4,column=1)
month=Label(AGE,text="Month",font=("Britannic Bold",10),bd=8,bg="deepSky Blue",padx=3,pady=3).grid(row=4,column=2)

space3=Label(AGE,text=" ").grid(row=4,column=3)
Date=Label(AGE,text="Date",font=("Britannic Bold",10),bd=8,bg="deepSky Blue",padx=3,pady=3).grid(row=4,column=4)

YearEntryBox=Entry(AGE,textvariable=text_input4,font=("Britannic Bold",7),bd=8,bg="Ghost white",insertwidth=4,justify="right").grid(row=5,column=0)
space4=Label(AGE,text=" ").grid(row=5,column=1)

MonthEntryBOx=Entry(AGE,textvariable=text_input5,font=("Britannic Bold",7),bd=8,bg="ghost white",insertwidth=4,justify="right").grid(row=5,column=2)
space5=Label(AGE,text=" ").grid(row=5,column=3)

DateEntryBox=Entry(AGE,textvariable=text_input6,font=("Britannic Bold",7),bd=8,bg="ghost white",insertwidth=4,justify="right").grid(row=5,column=4)


#====================================================================================
Reset=Button(AGE,text="RESET",font=("Britannic Bold",10),bd=8,bg="SeaGreen",relief="raised",padx=4,pady=4,command=rclick).grid(row=6,column=0)
Submit=Button(AGE,text="SUBMIT",font=("Britannic Bold",10),bd=8,bg="Sea Green",relief="raised",padx=4,pady=4,command=bclick).grid(row=6,column=4)


AGE.mainloop()
