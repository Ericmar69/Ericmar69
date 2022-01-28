from tkinter import *

Tela_Inicial = Tk()
Tela_Inicial.title("Janela Inicial")
Tela_Inicial.geometry("500x300")
logo = PhotoImage(file="Yoda.gif")

label_1= Label(Tela_Inicial, text= "Label 1", 
                             font= "Arial")
label_1.pack()  

label_2= Label(Tela_Inicial, compound=CENTER, text= "Label 2", 
                             font= "Broadway 42 bold",
                             fg= "#aaaaaa",
                             bg= "blue",
                             image=logo)
label_2.pack()



# pack Podese Mudar a Sequencia do pack
#label_1.pack()
#label_2.pack()
#cmd.pack()

Tela_Inicial.mainloop()
print()
print('print(): ', print())