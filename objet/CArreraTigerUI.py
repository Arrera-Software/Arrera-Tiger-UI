from tkinter import*
from objet.CArreraTiger import*
from tkinter import filedialog 
from tkinter.messagebox import*
import threading as th

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
        # Ouverture du fichier de config
        self.__fileConfig = jsonWork()
        self.__fileConfig.loadFile("tigerConfig.json")
        # Varriable
        self.__varSoft = StringVar(self.__screen)
        # Menu top 
        self.__topMenu = Menu(self.__screen)
        self.__topMenu.add_command(label="Definir emplacement",command=self.__addEmplacement)
        self.__topMenu.add_command(label="a propos")
        # Main Frame 
        self.__frameMain = Frame(self.__screen,width=700,height=500,bg="white")
        # Frame install
        self.__frameInstall = Frame(self.__screen,width=700,height=500,bg="white")
        # Label Frame Install
        labelInstall = Label(self.__frameInstall,text="Installation en cours",bg="white",fg="black",font=("arial","30"))
        # Widget fenetre principal
        labelTitle =  Label(self.__frameMain,text="Arrera Tiger",bg="white",fg="black",font=("arial","30"))
        btnValider = Button(self.__frameMain,text="Installer",bg="white",fg="black",font=("arial","15"),command=self.__install)
        # Affichage
        self.__screen.configure(menu=self.__topMenu)
        self.__frameMain.pack()
        labelInstall.place(relx=0.5,rely=0.5,anchor="center")
        btnValider.place(relx=0.5, rely=1.0, anchor="s")  
        labelTitle.place(relx=0.5, rely=0.0, anchor="n") 
    
    def show(self):
        listeSoft = self.__objTiger.listSoft()
        menuSoft = OptionMenu(self.__frameMain,self.__varSoft,*listeSoft)
        menuSoft.place(relx=0.5,rely=0.5,anchor="center")
        self.__varSoft.set(listeSoft[0])
        self.__screen.mainloop()
    
    def __addEmplacement(self):
        showinfo("Arrera : Tiger","Selectionner le dossier ou installer vos application Arrera")
        folder = filedialog.askdirectory(title="Sélectionner un dossier")
        self.__fileConfig.EcritureJSON("file",folder)
        showinfo("Arrera : Tiger","Dossier enregistrer")
    
    def __install(self):
        soft = self.__varSoft.get()
        folder = self.__fileConfig.lectureJSON("file")
        if (folder==""):
            showerror("Arrera : Tiger","Aucun dossier n'a etais defini")
        else :
            self.__frameMain.pack_forget()
            self.__frameInstall.pack()
            self.__screen.update()
            theardInstall = th.Thread(target=self.__objTiger.install,args=(soft,"cache/"+soft+".zip",folder,))
            theardInstall.start()
            theardInstall.join()
            self.__frameInstall.pack_forget()
            self.__frameMain.pack()
            showinfo("Arrera : Tiger","Logiciel installer")