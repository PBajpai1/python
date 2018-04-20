#parisha
#16csu238

from tkinter import *
import tkinter
top=tkinter.Tk()
count=0

DOR=StringVar()
moviename=StringVar()
budget=StringVar()
actress=StringVar()
actor=StringVar()

def Add_movie():
    f=open('C:/Users/Admin/Desktop/movies.txt','a')
    DOR=E1.get()
    moviename=E2.get()
    budget=E3.get()
    actress=E4.get()
    actor=E5.get()
    if(DOR=='' or moviename=='' or budget=='' or actress=='' or actor==''):
        print("Details can't be empty!")
        exit()
    f.writelines(DOR.ljust(20)+moviename.ljust(20)+budget.ljust(20)+actress.ljust(20)+actor.ljust(3)+"\n")
    print("Record added to file!")
    f.close()

def Delete_movie():
    k=DOR.get()
    f=open('C:/Users/Admin/Desktop/movies.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    f.close()
    f=open('C:/Users/Admin/Desktop/movies.txt','w')
    for book in lines: 
        j=book.split()
        print(j)
        if(j[0]!=k): 
             f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")
    f.close()
    
def Search_movie():
    k=DOR.get()
    f=open('C:/Users/Admin/Desktop/movies.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    for book in lines: 
        j=book.split() 
        if(j[0]==k):   
            print(j) 
            DOR.set(j[0]) 
            moviename.set(j[1]) 
            budget.set(j[2]) 
            actress.set(j[3]) 
            actor.set(j[4])
            flag=1
            break
    if(flag==0):
        print("Record not found!")
    else:
        print("Record found!")
    f.close()

def Update_movie():
    new_dor=DOR.get() 
    new_name=moviename.get() 
    new_bugdet=budget.get() 
    new_actress=actress.get() 
    new_actor=actor.get() 
    f=open('C:/Users/Admin/Desktop/movies.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines() 
    f.close() 
    f=open('C:/Users/Admin/Desktop/movies.txt','w') 
    for book in lines: 
        j=book.split() 
        if(j[0]!=new_dor): 
            f.writelines(j[0].ljust(3)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n") 
     
        else: 
            f.writelines(j[0].ljust(3)+new_name.ljust(20)+new_bugdet.ljust(20)+new_actress.ljust(20)+new_actor.ljust(5)+"\n")
    print("Record updated!!")        
    f.close()        

def Get_First_Record():
    f=open('C:/Users/Admin/Desktop/movies.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print("\n")
    print(l)
    j=l[0].split()
    DOR.set(j[0])
    moviename.set(j[1]) 
    budget.set(j[2]) 
    actress.set(j[3]) 
    actor.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()
    
 
def Get_Last_Record():
    f=open('C:/Users/Admin/Desktop/movies.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")    
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print(l)
    j=l[ctr-1].split()
    DOR.set(j[0])
    moviename.set(j[1]) 
    budget.set(j[2]) 
    actress.set(j[3]) 
    actor.set(j[4])
    print("\n Last Record of file is as:")
    print(l[ctr-1])
    f.close()

def Get_Next_Record():
    f=open('C:/Users/Admin/Desktop/movies.txt','r')
    ctr=0
    count=0
    i=0
    for line in f:
        count=count+1
    try:
        while(i<=ctr):
            ln=f.readline()
            i=i+1
        m=ln.split()
        DOR.set(m[0])
        moviename.set(m[1])
        budget.set(m[2])
        actress.set(m[3])
        actor.set(m[4])

    except:  
        print("No More Record Found")
    ctr=ctr+1
    f.close()

top.configure(background="misty rose")

   
tkinter.Label(top, text="DATE OF RELEASE:",font=('Verdana',22,' italic')).grid(row=0)
tkinter.Label(top, text="MOVIE NAME:",font=('Verdana',22,'italic')).grid(row=1)
tkinter.Label(top, text="BUDGET:",font=('Verdana',22,'italic')).grid(row=2)
tkinter.Label(top, text="ACTRESS:",font=('Verdana',22,'italic')).grid(row=3)
tkinter.Label(top, text="ACTOR:",font=('Verdana',22,'italic')).grid(row=4)


E1 = tkinter.Entry(top,textvariable=DOR)
E2 = tkinter.Entry(top,textvariable=moviename)
E3 = tkinter.Entry(top,textvariable=budget)
E4 = tkinter.Entry(top,textvariable=actress)
E5 = tkinter.Entry(top,textvariable=actor)
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)
E4.grid(row=3, column=1)
E5.grid(row=4, column=1)


fr=tkinter.Button(top,text="|<",width=15,bg="plum",font=('Ariel',10,'bold'),command=Get_First_Record).grid(row=6, column=0)
pr=tkinter.Button(top,text="<",width=15,bg="plum",font=('Ariel',10,'bold'),command=top.event_add).grid(row=5, column=1)
nr=tkinter.Button(top,text=">",width=15,bg="plum",font=('Ariel',10,'bold'),command=Get_Next_Record).grid(row=5, column=2)
lr=tkinter.Button(top,text=">|",width=15,bg="plum",font=('Ariel',10,'bold'),command=Get_Last_Record).grid(row=6, column=3)

rb=tkinter.Button(top,text="ADD MOVIE",width=15,bg="firebrick2",font=('Ariel',20,'bold'),command=Add_movie).grid(row=9, column=0)
db=tkinter.Button(top,text="DELETE MOVIE",width=15,bg="firebrick2",font=('Ariel',20,'bold'),command=Delete_movie).grid(row=9, column=3)
sb=tkinter.Button(top,text="SEARCH MOVIE",width=15,bg="firebrick2",font=('Ariel',20,'bold'),command=Search_movie).grid(row=8, column=1)
ub=tkinter.Button(top,text="UPDATE MOVIE ",width=15,bg="firebrick2",font=('Ariel',20,'bold'),command=Update_movie).grid(row=8, column=2)

top.mainloop()
