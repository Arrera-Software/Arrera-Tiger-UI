from tkinter import*
from objet.CArreraTiger import*

class CArreraTigerUI :
    def __init__(self):
        # Objet Tiger
        self.__objTiger = CArreraTiger("https://raw.githubusercontent.com/Arrera-Software/Software-debot/main/arrerasoft.json")
        # Fenetre
        self.__screen = Tk()
        self.__screen.title("Arrera : Tiger")
        self.__screen.iconphoto(False,PhotoImage(file="image/ArreraTiger.png"))
        self.__screen.maxsize(700,500)
        self.__screen.minsize(700,500)
        self.__screen.configure(bg="white")
        # Varriable
        self.__varSoft = StringVar(self.__screen)
        # Menu top 
        self.__topMenu = Menu(self.__screen)
        self.__topMenu.add_command(label="Definir emplacement")
        self.__topMenu.add_command(label="a propos")
        # Frame install
        self.__frameInstall = Frame(self.__screen,width=700,height=500,bg="white")
        # Label Frame Install
        labelInstall = Label(self.__frameInstall,text="Installation en cours",bg="white",fg="black",font=("arial","30"))
        # Affichage
        self.__screen.configure(menu=self.__topMenu)
        labelInstall.place(relx=0.5,rely=0.5,anchor="center")
    
    def show(self):
        listeSoft = self.__objTiger.listSoft()
        menuSoft = OptionMenu(self.__screen,self.__varSoft,*listeSoft)
        menuSoft.place(relx=0.5,rely=0.5,anchor="center")
        self.__varSoft.set(listeSoft[0])
        self.__screen.mainloop()