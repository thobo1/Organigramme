from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter.ttk import *
import csv


from bdd import *
from hotel import *
from DataBaseOnportal.keyCode import *
from DataBaseOnportal.lockProfile import *
from DataBaseOnportal.lockProfilKeyCode import *
from DataBaseOnportal.room import *



class MainWindow:

    def __init__(self):
        self.__minLeight = 1000
        self.__minHeight = 800
        self.__title = "Onity Database Management"
        self.__pathToIco = "image/sql-logo.ico"
        self.__mainWindow = Tk()
        self.__menuBar = Menu(self.__mainWindow)
        self.__mainMenu = Menu(self.__menuBar, tearoff=0)
        self.__mainFrame = Frame(self.__mainWindow)
        self.__tabs = ttk.Notebook(self.__mainWindow)
        self.__tabTimeTable = ttk.Frame(self.__tabs, width=500, height=500)
        self.__tabUser = ttk.Frame(self.__tabs, width=500, height=500)
        self.__tabLocks = ttk.Frame(self.__tabs, width=500, height=500)
        self.__table_time_table = Treeview(self.__tabTimeTable, columns=('timeTableId', 'hour'))
        self.__tableUser = Treeview(self.__tabUser, columns=('nameUserGroup', 'groupLocksOpen'))
        self.__tableLocks = Treeview(self.__tabLocks, columns=('locksGroup', 'openBy'))
        self.__labelDatabaseConnection = Label(self.__mainWindow, text="Not connected")
        self.__bdd = Database()
        self.__hotel = Hotel()
        self.__keyCode = []
        self.__keyCodeMaster = []
        self.__lockProfile = []
        self.__lockProfileKeyCode = []
        self.__room = []


    def getTabs(self):
        return self.__tabs

    def show(self):
        self.__mainWindow.title(self.__title)
        self.__mainWindow.minsize(self.__minLeight, self.__minHeight)
        #self.__mainWindow.iconbitmap(self.__pathToIco)
        # Création de la bar de menu
        self.__mainWindow.config(menu=self.__menuBar)
        self.__menuBar.add_cascade(label="Connection base de donnée", menu=self.__mainMenu)
        self.__mainMenu.add_command(label="Ouvrir nouvelle base ", command=self.windowDbConnection)
        self.__mainMenu.add_command(label="Importer groupe usager", command=self.importFromCSVUser) #, state="disabled")
        self.__mainMenu.add_command(label="Importer serrures", command=self.importFromCSVLocks)
        #Ajout de la frame principale
        self.__mainFrame.pack()

        # Ajout du label
        self.__labelDatabaseConnection.pack()

        #Configuration des onglets
        self.__table_time_table.heading('timeTableId', text='Id Table')
        self.__table_time_table.heading('hour', text='restriction')
        self.__table_time_table['show'] = 'headings'  # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert

        self.__tableUser.heading('nameUserGroup', text='Nom famille de passe')
        self.__tableUser.heading('groupLocksOpen', text='Groupe de serrure ouverte')
        self.__tableUser['show'] = 'headings'

        self.__tableLocks.heading('locksGroup', text='Goupe de serrure')
        self.__tableLocks.heading('openBy', text='Ouverte par')
        self.__tableLocks['show'] = 'headings'


        # Affiche la fenetre
        self.__mainWindow.mainloop()


        #
        # timeTable = TimeTable()

    def windowDbConnection(self):
        filename = askopenfilename(filetypes=(("sdf file", "*.sdf"),))
        second_window = Tk()
        second_window.title("Paramètre connexion à la BDD")
        second_window.minsize(300,100)
        #second_window.iconbitmap(self.__pathToIco)
        second_window.grab_set()

        # Ajout des labels
        label_path_to_db = Label(second_window, text="Chemin de la base de donnée")
        label_path_to_db.pack()
        labelFilename = Label(second_window, text=filename)
        labelFilename.pack()
        # Input Password
        inputPassword = Text(second_window, height=1, width=25)
        inputPassword.pack()
        #Bouton Validate
        buttonConnectToDb = Button(second_window,  text="Valider", command = lambda: self.tryToConnectDb(second_window, filename, inputPassword))
        buttonConnectToDb.pack()

    def tryToConnectDb(self, second_window, path_to_db, pwd):

        self.__bdd.setPath(path_to_db)
        self.__bdd.setPassword(pwd.get("1.0", END))
        if self.__bdd.connect():
            second_window.destroy()
            self.__labelDatabaseConnection['text'] = "Connected"
            self.showDatabaseInformation()
        else:
            fInfos = Toplevel()  # Popup -> Toplevel()
            fInfos.title('Infos')
            Button(fInfos, text='Quitter', command = lambda: self.destroyPopUp(fInfos)).pack(padx=10, pady=10)
            fInfos.transient(second_window)
            fInfos.grab_set()

    def destroyPopUp(self, fInfos):
        fInfos.grab_release()
        fInfos.destroy()

    def showDatabaseInformation(self):
        self.__tabs.pack()
        self.__tabs.bind("<<NotebookTabChanged>>", self.onTabChange)
        self.__tabs.add(self.__tabTimeTable, text='Time Table')
        self.__tabs.add(self.__tabUser, text='Groupe d usager')
        self.__tabs.add(self.__tabLocks, text='Groupe de serrure')

        self.__table_time_table.pack()
        self.__tableUser.pack()
        self.__tableLocks.pack()
        results = self.__bdd.select("Property")
        for r in results:
           self.__hotel.setName(r[1])
           self.__hotel.setAdress(r[2])
        labelHotelName = Label(self.__mainFrame, text="Nom de l´établissement")
        hotelName = Text(self.__mainFrame, height=1)
        hotelName.insert(END, self.__hotel.getName())
        labelHotelAdress = Label(self.__mainFrame, text="Adresse de l´établissement")
        hotelAdress = Text(self.__mainFrame, height=1)
        if self.__hotel.getAdress() != None:
            hotelAdress.insert(END, self.__hotel.getAdress())

    def onTabChange(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == 'Time Table':
            self.update_time_table()

        elif tab_text == 'Groupe d usager':
            self.update_user_table()

        elif tab_text == 'Groupe de serrure':
            self.update_locks_table()


    def update_time_table(self):
        results = self.__bdd.select("TimeTable")
        for r in results:
            print(r)
            #self.__table_time_table.insert('', 'end','PG, FDC')

    def update_user_table(self):
        results = self.__bdd.select_condition("KeyCode","CodeType=6")
        for r in results:
            self.__table_time_table.insert('', 'end', r["KeyCodeId"], r["Name"],'')

    def update_locks_table(self):
        print("lockTable")
        # results = self.__bdd.select("LockProfile")
        # for r in results:
        #     self.__table_time_table.insert('', 'end', 'PG, FDC')

    def importFromCSVUser(self):
        #Récupération des usagers présent dans la BDD
        results = self.__bdd.select("KeyCode")
        for r in results:
            self.__keyCode.append(KeyCode(r["KeyCodeId"], r["Name"], r["CodeType"], r["Description"], r["SequenceNumber"]))
        #Récupération des nouveau du CSV
        filename = askopenfilename(filetypes=(("csv file", "*.CSV"),))
        with open(filename) as csv_file:
            maxSequenceNumber = 0
            for element in self.__keyCode:
                if element.getSequenceNumber()>maxSequenceNumber:
                    maxSequenceNumber=element.getSequenceNumber()
            csv_reader = csv.reader(csv_file, delimiter=';')
            self.__bdd.insert("INSERT INTO TimeTable (TimeTableNumber,Name) VALUES (1,'Workday')")
            for row in csv_reader:
                maxSequenceNumber = maxSequenceNumber+2000
                query = "INSERT INTO KeyCode (Name, CodeType, Description, SequenceNumber, ModifiedDate) VALUES ('%s', %s, '%s', %s, GETDATE())" %(row[0], 6, row[0], maxSequenceNumber)
                self.__bdd.insert(query)

    def importFromCSVLocks(self):
        # Récupération des usagers présent dans la BDD
        del self.__keyCode[:]
        del self.__keyCodeMaster[:]
        del self.__lockProfile[:]
        room_audit_code = 5010
        room_primary_key_code_key_code_id = 8
        results = self.__bdd.select("KeyCode")
        # for r in results:
        #     self.__keyCode.append(
        #         KeyCode(r["KeyCodeId"], r["Name"], r["CodeType"], r["Description"], r["SequenceNumber"]))
        #     lastKeyCodeId = r["KeyCodeId"]
        results = self.__bdd.select_condition("KeyCode","CodeType=6")
        for r in results:
            self.__keyCodeMaster.append(
                KeyCode(r["KeyCodeId"], r["Name"], r["CodeType"], r["Description"], r["SequenceNumber"]))
        # Récupération des présent dans la BDD
        results = self.__bdd.select("LockProfile")
        lastLockProfilID = 0
        for r in results:
            lastLockProfilID = r["LockProfileID"]
            #self.__lockProfile.append(
            #    LockProfile(r["KeyCodeId"], r["Name"], r["CodeType"], r["Description"], r["SequenceNumber"]))
        # Récupération des nouveau du CSV
        filename = askopenfilename(filetypes=(("csv file", "*.CSV"),))
        listRoom = []
        listRoomGroup = [2]
        listPersonalDoor = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if (row[0].isdigit()):
                    listRoom.append(row)
                else:
                    listPersonalDoor.append(row)

            # Traitement des serrures de chambres
            for room in listRoom:
                print(str(room[0])[0:-2])
                find=False
                name = "Chambres " + str(room[0])[0:-2]
                for lockProfil in self.__lockProfile:
                    if lockProfil.getName() == name:
                        find = True
                        self.__keyCode.append(KeyCode(lastLockProfilID, name, room[0], name, 9000))
                        room1 = Room(room[0])
                        room1.set_audit_code(room_audit_code)
                        room1.set_primary_key_code_key_code_id(room_primary_key_code_key_code_id)
                        self.__room.append(room1)
                        room_audit_code = room_audit_code+10
                        room_primary_key_code_key_code_id = room_primary_key_code_key_code_id+1

                if not find:
                    lastLockProfilID = lastLockProfilID + 1
                    self.__lockProfile.append(LockProfile(lastLockProfilID, name))
                    self.__keyCode.append(KeyCode(lastLockProfilID, name, room[0], name, 9000))
                    room1 = Room(room[0])
                    room1.set_audit_code(room_audit_code)
                    room1.set_primary_key_code_key_code_id(room_primary_key_code_key_code_id)
                    self.__room.append(room1)
                    room_audit_code = room_audit_code + 10
                    room_primary_key_code_key_code_id = room_primary_key_code_key_code_id + 1
                    i = 1
                    while i < len(room):
                        if room[i] == "x":
                            self.__lockProfileKeyCode.append(
                                LockProfile_KeyCode(lastLockProfilID, self.__keyCodeMaster[i - 1].getKeyCodeId()))
                        i = i + 1



            #Traitement des serrures du personnel
            for personalDoor in listPersonalDoor:
                lastLockProfilID  = lastLockProfilID+1
                self.__lockProfile.append(LockProfile(lastLockProfilID, personalDoor[0]))
                i = 1
                while i < len(personalDoor) :
                    if personalDoor[i]=="x":
                        self.__lockProfileKeyCode.append(LockProfile_KeyCode(lastLockProfilID,self.__keyCodeMaster[i-1].getKeyCodeId()))
                    i = i+1



        for personalDoor in self.__lockProfile:
            self.__bdd.insert(personalDoor.getInsertString())
        for lockProfileKeyCode in self.__lockProfileKeyCode:
            self.__bdd.insert(lockProfileKeyCode.getInsertString())
        for keyCode in self.__keyCode:
            self.__bdd.insert(keyCode.getInsertString())
        for room in self.__room:
            self.__bdd.insert(room.get_inset_string())









