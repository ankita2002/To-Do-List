from tkinter import *
from tkinter import messagebox
tasks = [] 
count = 1

def inputError():
    if enterTaskField.get() == " ":
        return 0
    return 1 

def clear_taskNumberfield():
    taskNumberfield.delete(0.0, END)

def clear_taskfeild():
    enterTaskField.delete(0,END)

def insertTask():
    global count
    value = inputError()
    if(value==0):
        return
    content = enterTaskField.get() + "\n"
    tasks.append(content)
    textArea.insert('end -1 chars'," [ " + str(count)+ " ] " + content )
    count += 1
    clear_taskfeild()

def delete():
    global count
    if len(tasks) == 0 :
        messagebox.showerror("No Task")
        return
    
    number = taskNumberfield.get(1.0,END)
    
    if number == "\n" :
        messagebox.showerror("Input Error")
        return
    else:
        taskno = int(number)

    clear_taskNumberfield()
    tasks.pop(taskno - 1)
    count -= 1
    textArea.delete(1.0,END)
    for i in range(len(tasks)):
        textArea.insert('end -1 chars', " [ "+ str(i+1) + " ] " + tasks[i])

#driver code
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="hot pink1") #background color
    gui.title("To Do List") #title of GUI window
    gui.geometry("250x300") #window size
    entertask = Label(gui, text="Enter your task", bg="hot pink1") #label
    enterTaskField = Entry(gui,bg="lemon chiffon",) #text
    #Save the task using submit button
    submit = Button(gui,text="Submit",fg="Black",bg="cyan", command= insertTask)
    textArea = Text(gui,height=5,width=25, font="lucida 13",bg="lemon chiffon")
    taskNumber = Label(gui, text="Delete Task Number", bg="Yellow")
    taskNumberfield = Text(gui,height=1,width=2,font="lucida 13",bg="Lemon chiffon")
    delete = Button(gui,text="Delete",fg="Black",bg="green",command = delete)
    Exit = Button(gui,text="Exit",fg="Black",bg="green",command = exit)
    entertask.grid(row=0, column =3)
    enterTaskField.grid(row=1, column =3,ipadx=50)
    submit.grid(row=3, column =3) 
    textArea.grid(row=4, column =3,padx=10 , sticky= W)    
    taskNumber.grid(row=5, column =3,pady=5)    
    taskNumberfield.grid(row=6, column =3)    
    delete.grid(row=7, column =3,pady=5)
    Exit.grid(row=8, column =3)
    gui.mainloop() #start gui