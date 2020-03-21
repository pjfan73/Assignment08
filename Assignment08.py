#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# jstevens, 2020-Mar-17, added code and docstrings
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        print_cdrow: prints values formatted for IO
        print_filerow: prints values formatted for file
    """

    def __init__(self, cd_id, cd_title, cd_artist):
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = cd_title
            self.__cd_artist = cd_artist
        except Exception as e:
            raise Exception('Error setting intial values:\n' + str(e))

    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value

    @property
    def cd_title(self):
            return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be a String!')

    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Title needs to be a String!')

    #prints row for IO  
    def print_cdrow(self):
        """Print the values for IO output

            properties:

            returns: string formatted as 'cd_id, cd_title, cd_artist with formatting for IO display'

        """

        return '{}\t{} (by:{})'.format(self.cd_id, self.cd_title, self.cd_artist)

    #prints row for FileIO
    def print_filerow(self):
        """Print the values for file output

            properties:

            returns: string formatted as 'cd_id, cd_title, cd_artist with formatting for file storage'

        """

        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    #default print
    def __str__(self):
        return '{}, {}, {}'.format(self.cd_id, self.cd_title, self.cd_artist)


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        load_inventory(file_name): -> (a list of CD objects)
        save_inventory(file_name, lst_Inventory): -> Saved to file defined in strFileName
        
    """

    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of CDObjects

        Reads the data from the test file identified by file_name into a 2D table

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            newfile(Boolean) = returns 1 if no file is loaded
            table (list) = list of CDObjects loaded from file_name
        """

        table=[]
        while True:
            try:
                open(file_name, 'r') 
            except OSError as e:
                print('The file CDInventory.txt was not found, Please make sure the file is in the correct path.', e)
                userexit = (input ("If you want to load the file, please put it in the correct path and press enter, type 'continue' to start without loading a file or to start a new file, type 'exit' to not load anything\n"))
                if userexit.lower() == 'exit':
                    print('Goodbye!')
                    quit()
                elif userexit.lower() == 'continue':
                    print("Not loading a file, Plese save to make a new one!")
                    print()
                    newfile = 1
                    return newfile
                else: 
                    print("Attepting to load the file!")
                    print()
                    continue
            else:
                with open(file_name, 'r') as f:
                    for line in f:
                        data = line.strip().split(',')
                        row = CD(data[0], data[1], data[2])
                        table.append(row)
                return table

    @staticmethod
    def save_inventory(file_name, table):
        """Function to manage data degestion from a list of CDObjects to a file

        Writes the data from a 2D table to the text file identified by file_name.

        Args:
            file_name (string): name of file used to write the data to
            table (list of CDObjects): 2D data structure (list of CDObjects) that holds the data during runtime

        Returns:
            None.
        """

        objFile = open(file_name, 'w')
        for row in table:
            objFile.write(row.print_filerow())
        objFile.close()


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output

    properties:

    methods:
        print_menu(): Displays a menu of choices to the user
        menu_choice(): Gets user input for menu selection
        get_CDId_info(): Gets the user input for the CD ID.
        get_CD_info(cdIdi): Get the CD info and returns a tuple
        show_inventory(table): Displays current inventory table
        load_inventory(): Gets user input whether or not to reload the inventory from a file
        save_inventory(table): Gets user input to save the inventory to a file
        get_input(value_type, input_message, error_message): Prompts the user for a value of specified type and returns
        
    """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def get_CDId_info():
        """fuction that gets user input for the CD ID.

        Args:
            None.

        Returns:
            cdId (string)   

        """

        cdId = IO.get_input(int, 'Enter ID: ', 'Please enter an integer value')
        return cdId

    @staticmethod
    def get_CD_info(cdIdi):
        """fuction that gets user input for the CD.
        
        Args:
            cdIdi (int): ID of the CD to be used

        Returns:
            cdId (string)   
            cdTitle (string)
            cdArtinst (string)

        """

        cdId = cdIdi
        cdTitle = IO.get_input(str, 'What is the CD\'s title? ', 'Please enter letters and numbers only')
        cdArtist = IO.get_input(str, 'What is the Artist\'s name? ', 'Please enter letters and numbers only')
        return cdId, cdTitle, cdArtist

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of CDObjects): 2D data structure (list of CDObjects) that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row.print_cdrow())
        print('======================================')
    
    @staticmethod
    def load_inventory():
        """Function that will get user input to reload the inventory from a file

        Will ask for user confirmation then if received the returns loadchoice as True
        If the user chooses not to load then the user is informed

        Args:
            None.

        Returns:
            loadchoice (Boolean): Returns the loadchoice as True if file is to be reloaded
        """

        print('WARNING: If you continue, all unsaved data will be lost and the Inventory will attempt to re-loaded from file or you can start a new file')
        strYesNo = input('type \'yes\' to continue and reload from file or start a new file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            loadchoice = True
            print('reloading...')
            return loadchoice
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')

    @staticmethod
    def save_inventory(table):
        """Function to get user input to save the inventory to a file

        Call the show inventory fuction then ask for user input to save the file, 
        if received then call the function to save the file and set and return the saveFlag,
        if not received then return to the main menu.

        Args:
            table (list of CDObjects): 2D data structure (list ofCDObjects) that holds the data during runtime

        Returns:
            saveCon (int): Returns the saveCon as 1 if the file is to be saved
        """
        IO.show_inventory(table)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        saveCon = 0
        if strYesNo == 'y':
           saveCon = 1
           print('File Saved!')
           return saveCon
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

    @staticmethod
    def get_input(value_type, input_message, error_message):
        """ Prompts the user for a value of specified type and returns

        Args:
            value_type (type): Requested data type (int, str, float...)
            input_message (str): Message displayed to the user via input() prompting for data
            error_message (str): Message displayed to the user if an incorrect data type is entered.

        Returns:
            new_value (value_type): Data of the requested type provided by the user
        
        """
        while True:
            try:
                new_value = value_type(input(input_message).strip())
                return new_value
            except ValueError:
                print(error_message)
   

class DataProcessor:
    """Processing the data during runtime

    methods:
        write_cd (cdInfo, table): -> (new row added to a list of CD objects)
        find_next_ID (table): Finds the next available ID number
        check_ID (idnf, table): Checks if the user entered ID has been used 
    """

    @staticmethod
    def write_cd (cdInfo, table):
        """Function to write data as CDObject row in a list of CDObjects

        Takes user input or data from a file and forms a dictionary row
        Then appends the row to the list of dictionaries 

        Args:
            idn (string): ID number of the CD, entered by user or read from file, saved as int()
            title (string): Title of the CD, entered by user or read from file, saved as string()
            artist (string): Artist of the CD, entered by user or read from file, saved as string()
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """

        cdId, cdTitle, cdArtist = cdInfo
        try:
            cdId = int(cdId)
        except ValueError as e:
            print('ID is not an Integer!')
            print(e)
        cdRow = CD(cdId, cdTitle, cdArtist)
        table.append(cdRow)

    @staticmethod
    def find_next_ID (table):
        """Function to find the next available ID number

        Takes the table and looks for the next ID number that has not been used by matching the ID value of each CDObject starting at 1 and ascending until no match is found

        Args:
            table (list of CDObjects): 2D data structure (list of CDObjects) that holds the data during runtime

        Returns:
            next_ID (int): Returns the number of the next available ID
        """

        # Default ID value
        next_ID = 1

        # Generate a list of all ID's currently in use
        used_id = [cd.cd_id for cd in table]

        # Loop and increment next_ID until a free value is found.
        while next_ID in used_id:
            next_ID += 1
        print('The next available ID is: ' + str(next_ID))
        return next_ID

    @staticmethod
    def check_ID (idnf, table):
        """Function to check if the user entered ID has been used 

        Takes the user entered ID number and the table and looks in the ID value to see if it has been used before in any of the dict in the table

        Args:
            idnf (int): ID number of the CD to be checked, entered by user
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            usedid (boolean): Returns True if the ID of the CD was matched or False if it was not matched
        """

        if any(row.cd_id == int(idnf) for row in table):
            usedid = True       
        else:
            usedid = False     
        return usedid
 

# -- Main Body of Script -- #

# 1. When program starts, read in the currently saved Inventory
lstOfCDObjects = FileIO.load_inventory(strFileName)
if lstOfCDObjects == 1:
    print('Did not load a file, please save to start a new one! ')
    lstOfCDObjects = []
else:
    print('The following CDs have been loaded from ' + strFileName)
    IO.show_inventory(lstOfCDObjects) #show loaded inventory at start of script
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection

    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        loadchoice = IO.load_inventory()
        if loadchoice == True:
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            if lstOfCDObjects == 1:
                print('Did not load a file, please save to start a new one! ')
                lstOfCDObjects = []
            else:
                print('The following CDs have been loaded from ' + strFileName)
                IO.show_inventory(lstOfCDObjects) #show loaded inventory at start of script
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        DataProcessor.find_next_ID(lstOfCDObjects)
        cdId = IO.get_CDId_info()
        usedid = DataProcessor.check_ID(cdId, lstOfCDObjects)
        if usedid == True:
            print('That ID is already being used, Please try again!')
            continue
        cdInfo = IO.get_CD_info(cdId)
        DataProcessor.write_cd(cdInfo, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects) 
        #continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        saveCon = IO.save_inventory(lstOfCDObjects)
        if saveCon == 1:
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')




