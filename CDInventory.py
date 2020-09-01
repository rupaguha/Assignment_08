#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# Rupa Guha, 2020-August-31, created file
# Rupa Guha, 2020-August-31, added code to create the CD class
# Rupa Guha, 2020-August-31, added code for some of the methods in FileIO and IO classes as well as main body 
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

    """
    # TODone Add Code to the CD class
    #----Constructor--------
    
    def __init__(self,cd_id,cd_title,cd_artist):
         #-----Attributes-----
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name, lstOfCDs):
        """ Loads inventory data from the text file into a list in object format."""
        objFile = None
        lstOfCDs.clear()  # clearning any existing data
        objFile = open(file_name, 'r')

        try:
            for line in objFile:
                data = line.strip().split(',')
                cdObj = CD(data[0],data[1],data[2])
                lstOfCDs.append(cdObj)
        except:
            ("Something happened here - maybe there is nothing in the file yet?")
        objFile.close()
        
           
    # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Saves data from a list of objects to an inventory file"""
        new_line = ""
        objFile = None
        counter = 0

        while counter < (len(lst_Inventory) -1):
            new_line = new_line + lst_Inventory[counter].cd_id + ","
            new_line = new_line + lst_Inventory[counter].cd_title + ","
            new_line = new_line + lst_Inventory[counter].cd_artist + ","
            new_line = new_line[:-1] + "\n"
            counter += 1

        objFile = open(strFileName, "w")    
        objFile.write(new_line)    
        objFile.close()
        print("Data saved!")
        
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    
    # TODone add code to show menu to user
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

    # TODone add code to captures user's choice
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
    
    # TODO add code to display the current data on screen
    def show_inventory(lstObj):
        
        pass
    
    # TODO add code to get CD data from user
    pass

# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName, lstOfCDObjects)

while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # let user exit program
    if strChoice == 'x':
        break
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # let user add data to the inventory
    if strChoice == 'a':
        pass
    
    # show user current inventory
    if strChoice == 'i':
        pass

    # let user save inventory to file
    if strChoice == 's':
        FileIO.save_inventory(strFileName, lstOfCDObjects)
        
    
    

