from tkinter import*
from PIL import Image,ImageTk
import Speech_To_Text
import Action

#ASk funcation 
def ask():
    user_val = Speech_To_Text.speech_to_text().strip().lower()
    if user_val:  # Only process if there's actual input
        bot_val = Action.Action(user_val)
        text.insert(END, "User --> " + user_val + "\n")
        if bot_val:
            text.insert(END, "BOT <-- " + str(bot_val) + "\n")
        if bot_val == "Take care! I hope I was able to assist you with everything you needed.":
            root.destroy()
    else:
        text.insert(END, "BOT <-- I didn't catch that. Please try again.\n")





def Send():
    user = entry.get().strip().lower()  # Convert to lowercase and strip extra spaces
    if user:  # Proceed only if there's actual input
        bot = Action.Action(user)
        text.insert(END, "User --> " + user + "\n")
        if bot:
            text.insert(END, "Bot <-- " + str(bot) + "\n")
        if bot == "Take care! I hope I was able to assist you with everything you needed.":
            root.destroy()  # Close the GUI
    else:
        text.insert(END, "Bot <-- I didn't catch that. Please try again.\n")

   
def Delete():
   text.delete("1.0","end")

root=Tk()
root.title("EmpathAI Assistant")
root.geometry('650x775')
root.resizable(False,False)
root.configure(bg= "Light Blue")




#frame

frame = LabelFrame(root , padx=100 ,pady=7 , borderwidth=3 , relief="raised")
frame.grid(row=0 , column=1 , padx=55 , pady=10)
frame.configure(bg="Light Blue")

#textlable
Text_lable = Label(frame, text="EmpathAI Assistant", font= ("comic sans ms", 14 ,"bold") ,  bg="lightBlue" )
Text_lable.grid(row=0 , column=0 , padx =20 , pady =10)

#image
image = ImageTk.PhotoImage(Image.open("image/Aii.png"))
image_lable= Label(frame , image=image)
image_lable.grid(row=1,column=0,pady=20)

#text Adding widget 

text = Text(root , font= ("courior 10 bold") ,bg="lightblue" )
text.grid(row=2 , column= 0)
text.place(x= 100 , y= 443 , width= 385 , height= 140)
#Entry widget 

entry= Entry(root, justify=CENTER)
entry.place(x= 120, y=600 , width= 350 , height= 30)

#button for Ask

ButtonAsk = Button(root , text= "Ask" , font= ("comic sans ms", 12 ,"bold") ,bg="green", pady= 10 , padx= 35, borderwidth= 3, relief=SOLID ,command=ask)
ButtonAsk.place(x=80 , y= 660 )

# button for delet

ButtonDel= Button(root , text= "Delete" , font= ("comic sans ms", 12 ,"bold") , bg="red", pady= 10 , padx= 35, borderwidth= 3, relief=SOLID ,command=Delete)
ButtonDel.place(x=400 , y= 660 )

#button for send

ButtonSend= Button(root , text= "Send" , font= ("comic sans ms", 12 ,"bold") ,bg="yellow", pady= 10 , padx= 35 , borderwidth= 3, relief=SOLID ,command=Send)
ButtonSend.place(x=230 , y= 660 )

root.mainloop()

