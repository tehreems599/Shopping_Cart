from abc import ABC,abstractmethod

class FileREcords(ABC):
# Abstract method, all child classes provide their own implementation for it
    @abstractmethod
    def SaveToFile(self,fil):
        pass
    
class Administrator(FileREcords) :
    '''Take name of items and quantities as input and stores them in list, then save that list into  a file'''

#As this is a group project, as an extended feature we made this administrator class which controls the items displayed in main menu, it can add/remove items and adjusts their quantity
    lst=[]
    def setList(self):
        print("Add items to the menu!!\n")
        for j in range(10):
            a=input("\nPlease Enter Item Name:").lower()
            try:              ##Exception
                b=int(input("\nEnter the Quantity of Item:"))
            except:
                print("Quantity Must be a number\nTry again")
                b=int(input("Please Enter Quantity Again and Make Sure its a Number:"))
            Administrator.lst.append([[">>", a, b]])
    def getList(self):
        return Administrator.lst
    def RemoveItems(self):
        int1=input("Enter the Name of the Item that You Want to Remove:").lower()
        for i in Administrator.lst:
            for j in i:
                if j[1]==int1:
                    Administrator.lst.remove(i)
        print(int1, "has been Removed Successfully!")
        
    def AddItems(self):
        int2=input("Enter the Name of the Item that You Want to Add:").lower()
        if [int2] not in self.lst:
            try:
                c=int(input("Please Enter the Quantity of Item:"))
            except:
                print("Quantity Must be a number\nTry again")
                c=int(input("Please Enter Quantity Again and Make Sure its a Number:"))
            Administrator.lst.append([[">>",int2,c]])
        print(int2,"has been Added Successfully!")
    def SaveToFile(self,fil):          ##Storing list of items into a file
        f = open ( fil , 'a' )
        for item in self.lst:
            f.write ( str( item) + "\n" )
        f.close ( )
            
            

class PrintMenu (Administrator) :       ##Inheritance
    '''Prints main menu on shell'''
    def settingInputs(self):
        Administrator.setList(self)
    def Display(self):
        a=Administrator.getList(self)
        print("******************************************************************")
        for [i] in a :
            print ( f'{i[ 0 ]:6} {i[ 1 ]:13} {i[ 2 ]}' )
        print("------------------------------------------------------------------")

class ChangeList(PrintMenu):        ##Inheritance
    '''Take input from user and Calls the methods of Parent classes accordingly to add or remove items from menu'''
    
    def __init__(self):
        PrintMenu.settingInputs(self)
        PrintMenu.Display(self)
    def addList(self):
        d=input('Do You Want to Add Something? If Yes then Enter "Y" and If No then Enter "N"\nEnter:').lower()
        if d =="y":
            Administrator.AddItems(self)
            PrintMenu.Display(self)
        else:
            print("Your Operation has been Declined")
    def removeList(self):
        e=input('Do You Want to Remove Something? If Yes then Enter "Y" and If No then Enter "N"\nEnter:').lower()
        if e=='y':
            Administrator.RemoveItems(self)
            PrintMenu.Display(self)
        else:
            print("Your Operation has been Declined")
    def Records(self):
        Administrator.SaveToFile(self,"Menu.txt")

class Info (FileREcords):          ##Inheritance
    '''Take username, full name, password etc. as input and create and account for user'''
    def __init__ (self , s=[]) :
        self.Infolist = list ( s )
    def userInput (self) :
        self.usr=input("Enter User name:").lower()
        self.name=input("Enter full name:").lower()
        self.add=input("Enter Address:").lower()
        try:                          ##Exception
            self.pw=int(input("Enter Pin code:"))
        except:
            print ("Your Password is Invalid!!!")
            self.pw=int(input("Please Enter Password Again:"))
        finally:
            self.Infolist.append(self.usr)
            self.Infolist.append(str(self.pw))
            self.Infolist.append(self.name)
            self.Infolist.append(self.add)
            print("Congratulations!!\nYour account has been created successfully!!\n")
        self.SaveToFile("User Records.txt")

    def SaveToFile(self,fil):
        f=open(fil,"a")
        f.write(str(self.Infolist)+"\n")
        f.close()
    def readFromFile (self , file) :
        i=1
        f=open(file,"r")
        for items in f:
            self.rec=eval(items)
            print(f'{str(i):15}{self.rec[0]:15}{self.rec[1]:15}{self.rec[2]:20}{self.rec[3]}')
            i+=1
        f.close()

            
class ShoppingItems(Administrator):             ##Inheritance
    '''Takes shopping itmes as input and place them into the current cart of customer'''
    lst2=[]
    def UserInput(self):
        self.ch2=input("Please Enter the Name of Item:").lower()
        try:                         ##Exception
            self.ch3=int(input("Enter the Quantity of Item:"))
        except ValueError:
            print("Quantity Must be a Niumber!!")
            self.ch3=int(input("Enter Again and Make Sure it Must be in Digits:"))
    def AddToCart(self):
        Administrator.getList(self)
        for i in self.lst:
            for j in i:
                if j[1]==self.ch2:
                    if self.ch3 in range (j[2]):
                        j[2]-=self.ch3
                        ShoppingItems.lst2+=[[self.ch2,self.ch3]]
                        print("Congratulations!!Items have been Added to Your Cart Successfully!\n")
                    elif self.ch3== j[2]:
                        print("********\nSorry!!The Quantity You have Entered is Equal to the Range, We Can't let this Item Run Out of Stock....\n********")
                        break
                    else:
                       print("********\nSorry!!The Quantity You have entered is Greater than to the rangeof our Stock...\n********")
                       break
                    
        a=PrintMenu()
        a.Display()
    def getUserCart(self):
        return ShoppingItems.lst2

class ManageCart(ShoppingItems,FileREcords):             ##Multiple Inheritence
    '''Manage current cart details such as viewing cart, adding more items to the cart or removing it'''
    def viewCart(self):
            
            print("You Want to View the Details of Your Cart so here are the Details:\n")
            print(f'{"Items":10}{"Quantity"}\n')
            for j in ShoppingItems.getUserCart(self):
                    print(f'{j[0]:10}{j[1]}')
                    print()            
                   
    def AddCart(self):
            ShoppingItems.UserInput(self)
            ShoppingItems.AddToCart(self)

    def RemoveCart(self):
            self.user=input("Enter the Name of the Item You Want to Remove:").lower()
            for items in ShoppingItems.getUserCart(self):
                if items[0]!=self.user:
                    print("Sorry!!This Item is not in Your Cart..")
                else:
                    for i in ShoppingItems.lst2:
                            if i[0]==self.user:
                                ShoppingItems.lst2.remove(i)
                                print("Items have been Removed from Your Cart Successfully!\n")
    def SaveToFile(self,fil):
            f=open(fil,"a")
            f.write(str(ShoppingItems.lst2)+"\n")
            f.close()
        
    def readFromFile (self , file) :
            f=open(file,"r")
            i=0
            for item in f:
                rec=eval(item)
                print("for customer",i+1,", [item,quantity]:",rec)
                i+=1
            f.close()
            
class ViewHistory(Info,ManageCart):           ##Multiple Inheritence
    '''Prints the shopping history and user account details which were saved in files'''
    
    def printHistory(self):
        print("Here is the Record of all Accounts:")
        print(f'{"Customer No.":15}{"UserName":15}{"password":15}{"name":20}{"Address"}')
        Info.readFromFile(self,"User Records.txt")
        print("Here is the List of all the items bought till now;")
        ManageCart.readFromFile(self,"CartDetails.txt")
        
class Options(PrintMenu):
    '''Provides an interactive display menu, user can choose from different available options. Several objects are instantiated as per he choice of user'''
    def inputs(self):
        while True:
            print("1)Want to see the menu?\n2)Place Order\n3)View your cart details\n4)Checkout")
            usr=input("Enter Your Choice No.:")
            if usr=="1":
                PrintMenu.Display(self)
            elif usr=="2":
                print("_________________________________________________\n\nPlease note that all items has a fixed price, that is, Rs 1000/-\n_________________________________________________") 
                PrintMenu.Display(self)
                b=ShoppingItems()             ##Composition
                try:
                    ch1=int(input("How Many Items Yo you Want to Buy:"))
                except ValueError:
                    print("It Must be a Number!")
                    ch1=int(input("Enter the Number of Items Again and Make Sure it Must be a Digit:"))
                finally:
                    for i in range(ch1):
                        b.UserInput()
                        b.AddToCart()
            elif usr=="3":
                c=ManageCart()     ##Composition
                c.viewCart()
                while True:
                    usrr=input("\nDo You Want to Make Changes??\n1)Add Something\n2)Remove Something\n3)Return to Main Menu\nPlease Enter Your Choice No.:")
                    if usrr=="1":
                        c.AddCart()
                        c.viewCart()
                    elif usrr=="2":
                        c.RemoveCart()
                        c.viewCart()
                    elif usrr=="3":
                        break
                c.SaveToFile("CartDetails.txt")
            elif usr=="4":
                d=ShoppingItems()
                g=[]
                for i in ShoppingItems.lst2:
                    a=i[1]*1000
                    g.append(a)
                d=sum(g)
                print("Thanks for shopping\n_______________________________________________________\nFinal Bill=",d)
                break

class MainMenu:
    '''Acts as an interface and instantiate object of other classes within itself'''
    
    def DisplayMenu(self):
        print("HELLO MA'AM!!\nWELCOME TO OUR STORE!\nYOU ARE SIGNING IN AS AN ADMINISTRATOR\nFOR STARTING TODAY'S SALE, FIRST YOU HAVE TO PROVIDE LIST OF AVAILABLE ITEMS\n*********************************************\n")
        self.b=ChangeList()                ##Composition
        ch=input('Do You Want to Add or Remove Something?If YES then Enter \"Y" and if NO then Enter "N"\nEnter:').lower()
        if ch=='y':
            self.b.addList()
            self.b.removeList()
            self.b.Records()
        elif ch=="n":
            print("Happy Shopping!!")
            self.b.Records()
    def DisplayToUser(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nNOW LOGGING IN AS A CUSTOMER\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nPLEASE CREATE AN ACCOUNT BEFORE PROCEEDING\n")
        self.c=Info()                    ##Composition
        self.c.userInput()
    def ChoicesForUser(self):
        f=Options()                      ##Composition
        f.inputs()
    def Customer_Records(self):
        p=input("Do You Want to See the Account Details of all Customers?").lower()
        if p =='y':
            self.d=ViewHistory()                ##Composition
            self.d.printHistory()

    
a=MainMenu()
a.DisplayMenu()
a.DisplayToUser()
a.ChoicesForUser()
a.Customer_Records()
