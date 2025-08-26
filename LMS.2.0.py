from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:
   def __init__(self, root):
      self.root = root
      self.root.title("Library Management Systems")
      self.root.geometry("1350x750+0+0")
      self.root.configure(background = "powder blue")

      MType = StringVar()
      Ref = StringVar()
      Title = StringVar()
      Firstname = StringVar()
      Surname = StringVar()
      Address1 = StringVar()
      Address2 = StringVar()
      PostCode = StringVar()
      MobileNo = StringVar()
      BookID = StringVar()
      BookTitle = StringVar()
      BookType = StringVar()
      Author = StringVar()
      DateBorrowed = StringVar()
      DateDue = StringVar()
      SellingPrice = StringVar()
      LateReturnFine = StringVar()
      DateOverDue = StringVar()
      DaysOnLoan = StringVar()
      Prescription = StringVar()

      def iReset():
         MType.set("")
         Ref.set("")
         Title.set("")
         Firstname.set("")
         Surname.set("")
         Address1.set("")
         Address2.set("")
         PostCode.set("")
         MobileNo.set("")
         BookID.set("")
         BookTitle.set("")
         BookType.set("")
         Author.set("")
         DateBorrowed.set("")
         DateDue.set("")
         SellingPrice.set("")
         LateReturnFine.set("")
         DateOverDue.set("")
         DaysOnLoan.set("")
         # The FrameDetail text widget was named txtDisplayR in the previous version
         self.txtFrameDetail.delete("1.0", END)
         self.txtDisplayR.delete("1.0", END)
      
      def iDelete():
         iReset()
         self.txtDisplayR.delete("1.0", END)

      def iExit():
         iExit = tkinter.messagebox.askyesno("Library Management Systems", "Confirm if you want to exit")
         if iExit > 0:
            root.destroy()
            return
      
      def iDisplayData():
         self.txtFrameDetail.insert(END, "\t" + MType.get() + "\t\t" + Ref.get() + "\t" + Title.get() + "\t" +
                                    Firstname.get() + "\t" + Surname.get() + "\t\t" + Address1.get() + "\t\t" + Address2.get() + "\t" +
                                    PostCode.get() + "\t" + BookTitle.get() + "\t\t" + DateBorrowed.get() + "\t\t" + DaysOnLoan.get() + "\n")
      
      def iReceipt():
         self.txtDisplayR.insert(END, "Member Type: \t\t" + MType.get() + "\n")
         self.txtDisplayR.insert(END, "Ref No: \t\t" + Ref.get() + "\n")
         self.txtDisplayR.insert(END, "Title: \t\t" + Title.get() + "\n")
         self.txtDisplayR.insert(END, "Firstname: \t\t" + Firstname.get() + "\n")
         self.txtDisplayR.insert(END, "Surname: \t\t" + Surname.get() + "\n")
         self.txtDisplayR.insert(END, "Address 1: \t\t" + Address1.get() + "\n")
         self.txtDisplayR.insert(END, "Address 2: \t\t" + Address2.get() + "\n")
         self.txtDisplayR.insert(END, "Post Code: \t\t" + PostCode.get() + "\n")
         self.txtDisplayR.insert(END, "Mobile No: \t\t" + MobileNo.get() + "\n")
         self.txtDisplayR.insert(END, "Book ID: \t\t" + BookID.get() + "\n")
         self.txtDisplayR.insert(END, "Book Title: \t\t" + BookTitle.get() + "\n")
         self.txtDisplayR.insert(END, "Author: \t\t" + Author.get() + "\n")
         self.txtDisplayR.insert(END, "Date Borrowed: \t\t" + DateBorrowed.get() + "\n")

      #==================================================Frame==================================================
      MainFrame = Frame(self.root)
      MainFrame.grid()

      TitleFrame = Frame(MainFrame, width= 1350, padx= 20, bd= 20, relief= RIDGE)
      TitleFrame.pack(side= TOP)
      
      self.lblTitle = Label(TitleFrame, width= 39, font= ("arial", 40, "bold"), text= "\tLibrary Management Systems\t", padx= 12)
      self.lblTitle.grid()

      ButtonFrame = Frame(MainFrame, bd= 20, width= 1350, height= 50, padx= 20, relief= RIDGE)
      ButtonFrame.pack(side= BOTTOM)

      FrameDetail = Frame(MainFrame, bd= 20, width= 1350, height= 100, padx= 20, relief= RIDGE)
      FrameDetail.pack(side= BOTTOM)

      DataFrame = Frame(MainFrame, bd= 20, width= 1300, height= 400, padx= 20, relief= RIDGE)
      DataFrame.pack(side= BOTTOM)

      DataFrameLEFT = LabelFrame(DataFrame, bd= 10, width= 800, height= 300, padx= 20, relief= RIDGE, 
                                font= ("arial", 12, "bold"), text= "Library Membership Info:",)
      DataFrameLEFT.pack(side= LEFT)

      DataFrameRIGHT =  LabelFrame(DataFrame, bd= 10, width= 450, height= 300, padx= 20, relief= RIDGE, 
                                  font= ("arial", 12, "bold"), text= "Book Details:",)
      DataFrameRIGHT.pack(side= RIGHT)

      #==================================================Widget==================================================
      # --- Member Type Widgets ---
      self.lblMemberType = Label(DataFrameLEFT, font= ("arial", 12, "bold"), text= "Member Type:", padx= 2, pady= 2)
      self.lblMemberType.grid(row= 0, column= 0, sticky= W)
      self.cboMemberType = ttk.Combobox(DataFrameLEFT, font= ("arial", 12, "bold"), state= "readonly", textvariable=  MType, width= 23)
      self.cboMemberType["value"]= ("", "Student", "Lecturer", "Admin Staff")
      self.cboMemberType.current(0)
      self.cboMemberType.grid(row= 0, column= 1)

      # --- Book ID Widgets ---
      self.lblBookID = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Book ID:", padx= 2, pady= 2)
      self.lblBookID.grid(row= 0, column= 2, sticky= W)
      self.txtBookID = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= BookID, width= 25)
      self.txtBookID.grid(row= 0, column= 3)

      # --- Reference No. Widgets ---
      self.lblRef = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Reference No:", padx= 2, pady= 2)
      self.lblRef.grid(row=1, column= 0, sticky= W)
      self.txtRef = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= Ref, width= 25)
      self.txtRef.grid(row= 1, column= 1)

      # --- Book Title Widgets ---
      self.lblBookTitle = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Book Title:", padx= 2, pady= 2)
      self.lblBookTitle.grid(row= 1, column= 2, sticky= W)
      self.txtBookTitle = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= BookTitle, width= 25)
      self.txtBookTitle.grid(row= 1, column= 3)

      # --- Title Combobox ---
      self.lblTitle = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Title:", padx= 2, pady= 2)
      self.lblTitle.grid(row=2, column= 0, sticky= W)
      self.cboTitle = ttk.Combobox(DataFrameLEFT, state= "readonly", textvariable= Title, 
                                   font= ("arial", 12, "bold"), width= 23)
      self.cboTitle["value"]= ("", "Mr.", "Miss.", "Mrs.", "Dr.", "Capt.", "Ms.", "Prof.", "Other.")
      self.cboTitle.current(0)
      self.cboTitle.grid(row= 2, column= 1)

      # --- Author Widgets ---
      self.lblAuthor = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Author:", padx= 2, pady= 2)
      self.lblAuthor.grid(row= 2, column= 2, sticky= W)
      self.txtAuthor = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= Author, width= 25)
      self.txtAuthor.grid(row= 2, column= 3)
      
      # --- Firstname Widgets ---
      self.lblFirstname = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Firstname:", padx= 2, pady= 2)
      self.lblFirstname.grid(row= 3, column= 0, sticky= W)
      self.txtFirstname = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= Firstname, width= 25)
      self.txtFirstname.grid(row= 3, column= 1)

      # --- Date Borrowed Widgets ---
      self.lblDateBorrowed = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Date Borrowed:", padx= 2, pady= 2)
      self.lblDateBorrowed.grid(row= 3, column= 2, sticky= W)
      self.txtDateBorrowed = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= DateBorrowed, width= 25)
      self.txtDateBorrowed.grid(row= 3, column= 3)

      # --- Surname Widgets ---
      self.lblSurname = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Surname:", padx= 2, pady= 6)
      self.lblSurname.grid(row= 4, column= 0, sticky= W)
      self.txtSurname = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= Surname, width= 25)
      self.txtSurname.grid(row= 4, column= 1)

      # --- Date Due Widgets ---
      self.lblDateDue = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Date Due:", padx= 2, pady= 2)
      self.lblDateDue.grid(row= 4, column= 2, sticky= W)
      self.txtDateDue = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= DateDue, width= 25)
      self.txtDateDue.grid(row= 4, column= 3)

      # --- Address 1 Widgets ---
      self.lblAddress1 = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Address 1:", padx= 2, pady= 2)
      self.lblAddress1.grid(row= 5, column= 0, sticky= W)
      self.txtAddress1 = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= Address1, width= 25)
      self.txtAddress1.grid(row= 5, column= 1)

      # --- Days On Loan Widgets ---
      self.lblDaysOnLoan = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Days On Loan:", padx= 2, pady= 2)
      self.lblDaysOnLoan.grid(row= 5, column= 2, sticky= W)
      self.txtDaysOnLoan = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= DaysOnLoan, width= 25)
      self.txtDaysOnLoan.grid(row= 5, column= 3)

      # --- Address 2 Widgets ---
      self.lblAddress2 = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Address 2:", padx= 2, pady= 2)
      self.lblAddress2.grid(row= 6, column= 0, sticky= W)
      self.txtAddress2 = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= Address2, width= 25)
      self.txtAddress2.grid(row= 6, column= 1)

      # --- Late Return Fine Widgets ---
      self.lblLateReturnFine = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Late Return Fine:", padx= 2, pady= 2)
      self.lblLateReturnFine.grid(row= 6, column= 2, sticky= W)
      self.txtLateReturnFine = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= LateReturnFine, width= 25)
      self.txtLateReturnFine.grid(row= 6, column= 3)

      # --- Post Code Widgets ---
      self.lblPostCode = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Post Code:", padx= 2, pady= 2)
      self.lblPostCode.grid(row= 7, column= 0, sticky= W)
      self.txtPostCode = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= PostCode, width= 25)
      self.txtPostCode.grid(row= 7, column= 1)

      # --- Date Over Due Widgets ---
      self.lblDateOverDue = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Date Over Due:", padx= 2, pady= 2)
      self.lblDateOverDue.grid(row= 7, column= 2, sticky= W)
      self.txtDateOverDue = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= DateOverDue, width= 25)
      self.txtDateOverDue.grid(row= 7, column= 3)

      # --- Mobile No. Widgets ---
      self.lblMobileNo = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Mobile No:", padx= 2, pady= 2)
      self.lblMobileNo.grid(row= 8, column= 0, sticky= W)
      self.txtMobileNo = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= MobileNo, width= 25)
      self.txtMobileNo.grid(row= 8, column= 1)

      # --- Selling Price Widgets ---
      self.lblSellingPrice = Label(DataFrameLEFT, font=("arial", 12, "bold"), text= "Selling Price:", padx= 2, pady= 2)
      self.lblSellingPrice.grid(row= 8, column= 2, sticky= W)
      self.txtSellingPrice = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable= SellingPrice, width= 25)
      self.txtSellingPrice.grid(row= 8, column= 3)

      #==================================================Listbox, Scrollbar and Text Widget==================================================
      myScrollbar = Scrollbar (DataFrameRIGHT)
      myScrollbar.grid(row= 0, column= 1, sticky= "ns")

      ListOfBooks = ["The Monk Who Sold His Ferrari", "Richest Man in Babylon", "The Magic of Thinking Big", "Think Like a Man and Act Like a Woman", "Rich Dad Poor Dad",
                     "The 7 Habits of Highly Succcessful Man", "The Mountain is You", "The Diary of a CEO","The Power of Your Potential", "The Power of Your Subconscious Mind",
                     "Boundaries", "Atomic Habits", "The 5AM Club", "Don't Believe Everything You Think", "Forgiving What You Can't Forget", "Think and Grow Rich", 
                     "How to Win Friends & Influence People", "The Four Agreements", "Man's Search for Meaning", "The Power of Now", 
                     "The Subtle Art of Not Giving a fuck: A Counterintuitive Approach to Living a Good Life", "12 Rules for Life", "The Power of Habit", "Thinking Fast and Slow",
                     "Outliers", "The Gift of Imperfection", "As a Man Thinketh", "The Courage to Be Disliked", "Daring Greatly"]
      
      def SelectedBook(evt):
         value = str(booklist.get(booklist.curselection()))
         w = value
         iReset()
         
         # The date calculation.
         import datetime
         d1 = datetime.date.today()
         d2 = datetime.timedelta(days=14)
         d3 = d1 + d2
         
         # Now setting all the StringVar variables
         DateBorrowed.set(d1)
         DateDue.set(d3)
         DateOverDue.set("No")
         
         if (w == "The Monk Who Sold His Ferrari"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780002008778")
            BookTitle.set("The Monk Who Sold His Ferrari")
            Author.set("Robin Sharma")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R450.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Richest Man in Babylon"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781503259880")
            BookTitle.set("Richest Man in Babylon")
            Author.set("George S. Clason")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R350.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Magic of Thinking Big"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780671649367")
            BookTitle.set("The Magic of Thinking Big")
            Author.set("David J. Schwartz")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R400.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Think Like a Man and Act Like a Woman"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780061986422")
            BookTitle.set("Think Like a Man and Act Like a Woman")
            Author.set("Steve Harvey")
            LateReturnFine.set("R30.00")
            SellingPrice.set("R380.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Rich Dad Poor Dad"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781612680194")
            BookTitle.set("Rich Dad Poor Dad")
            Author.set("Robert Kiyosaki")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R420.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The 7 Habits of Highly Succcessful Man"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781455246757")
            BookTitle.set("The 7 Habits of Highly Succcessful Man")
            Author.set("Stephen R. Covey")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R470.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Mountain is You"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781982181283")
            BookTitle.set("The Mountain is You")
            Author.set("Brianna Wiest")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R360.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Diary of a CEO"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781399708608")
            BookTitle.set("The Diary of a CEO")
            Author.set("Steven Bartlett")
            LateReturnFine.set("R30.00")
            SellingPrice.set("R490.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Power of Your Potential"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781400213501")
            BookTitle.set("The Power of Your Potential")
            Author.set("John C. Maxwell")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R410.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Power of Your Subconscious Mind"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780735201193")
            BookTitle.set("The Power of Your Subconscious Mind")
            Author.set("Joseph Murphy")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R340.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Boundaries"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780310247454")
            BookTitle.set("Boundaries")
            Author.set("Henry Cloud")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R375.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Atomic Habits"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780735211299")
            BookTitle.set("Atomic Habits")
            Author.set("James Clear")
            LateReturnFine.set("R30.00")
            SellingPrice.set("R500.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The 5AM Club"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780008312831")
            BookTitle.set("The 5AM Club")
            Author.set("Robin Sharma")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R460.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Don't Believe Everything You Think"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781637740921")
            BookTitle.set("Don't Believe Everything You Think")
            Author.set("Joseph Nguyen")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R330.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Forgiving What You Can't Forget"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780718098730")
            BookTitle.set("Forgiving What You Can't Forget")
            Author.set("Lysa TerKeurst")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R390.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Think and Grow Rich"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781585424337")
            BookTitle.set("Think and Grow Rich")
            Author.set("Napoleon Hill")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R425.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "How to Win Friends & Influence People"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780671027032")
            BookTitle.set("How to Win Friends & Influence People")
            Author.set("Dale Carnegie")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R415.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Four Agreements"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781878424310")
            BookTitle.set("The Four Agreements")
            Author.set("Don Miguel Ruiz")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R355.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Man's Search for Meaning"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780807014295")
            BookTitle.set("Man's Search for Meaning")
            Author.set("Viktor E. Frankl")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R430.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Power of Now"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781577314806")
            BookTitle.set("The Power of Now")
            Author.set("Eckhart Tolle")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R440.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Subtle Art of Not Giving a fuck: A Counterintuitive Approach to Living a Good Life"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780062457714")
            BookTitle.set("The Subtle Art of Not Giving a fuck: A Counterintuitive Approach to Living a Good Life")
            Author.set("Mark Manson")
            LateReturnFine.set("R30.00")
            SellingPrice.set("R480.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "12 Rules for Life"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780345816023")
            BookTitle.set("12 Rules for Life")
            Author.set("Jordan B. Peterson")
            LateReturnFine.set("R30.00")
            SellingPrice.set("R495.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Power of Habit"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780812981605")
            BookTitle.set("The Power of Habit")
            Author.set("Charles Duhigg")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R405.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Thinking Fast and Slow"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780374533557")
            BookTitle.set("Thinking Fast and Slow")
            Author.set("Daniel Kahneman")
            LateReturnFine.set("R30.00")
            SellingPrice.set("R475.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Outliers"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780316017923")
            BookTitle.set("Outliers")
            Author.set("Malcolm Gladwell")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R420.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Gift of Imperfection"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781592858498")
            BookTitle.set("The Gift of Imperfection")
            Author.set("Brené Brown")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R365.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "As a Man Thinketh"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9780486241315")
            BookTitle.set("As a Man Thinketh")
            Author.set("James Allen")
            LateReturnFine.set("R15.00")
            SellingPrice.set("R250.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "The Courage to Be Disliked"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781501197775")
            BookTitle.set("The Courage to Be Disliked")
            Author.set("Ichiro Kishimi, Fumitake Koga")
            LateReturnFine.set("R25.00")
            SellingPrice.set("R435.00")
            DaysOnLoan.set(14)
            iReceipt()

         elif (w == "Daring Greatly"):
            Ref.set(random.randint(1000, 9999))
            BookID.set("ISBN 9781592858498")
            BookTitle.set("Daring Greatly")
            Author.set("Brené Brown")
            LateReturnFine.set("R20.00")
            SellingPrice.set("R395.00")
            DaysOnLoan.set(14)
            iReceipt()


      booklist = Listbox(DataFrameRIGHT, width= 20, height= 12, font= ("arial", 12, "bold"), yscrollcommand= myScrollbar.set)
      booklist.bind("<<ListboxSelect>>", SelectedBook)
      booklist.grid(row= 0, column= 0, padx= 8)
      myScrollbar.config(command= booklist.yview)

      for items in ListOfBooks:
         booklist.insert(END, items)

      # The text widget is now properly gridded in the second column to align with the Listbox.
      self.txtDisplayR = Text(DataFrameRIGHT, font=("arial", 12, "bold"), width= 32, height= 13, padx= 8, pady= 20)
      self.txtDisplayR.grid(row= 0, column= 2, sticky= "nsew")

      #==================================================[____]==================================================
      self.lblLabel = Label(FrameDetail, font=("arial", 10, "bold"), pady= 8, text= "Member Type\tReference No.\t Title\t Firstname\t" \
                           "Surname\t Address 1\t Address 2\t Post Code\t Book Title\t Date Borrowed\t Days on Loan\t Late Return Fine\n")
      self.lblLabel.grid(row= 0, column= 0)

      self.txtFrameDetail = Text(FrameDetail, font=("arial", 12, "bold"), width= 121, height= 4, padx= 2, pady= 4)
      self.txtFrameDetail.grid(row= 1, column= 0, sticky= "nsew")

      #==================================================Button==================================================
      self.btnDisplayData = Button(ButtonFrame, text= "Display data", font= ("arial", 12, "bold"), width= 30, bd= 4, command= iDisplayData)
      self.btnDisplayData.grid(row= 0, column= 0)

      self.btnDelete = Button(ButtonFrame, text= "Delete", font= ("arial", 12, "bold"), width= 30, bd= 4, command= iDelete)
      self.btnDelete.grid(row= 0, column= 1)

      self.btnReset = Button(ButtonFrame, text= "Reset", font= ("arial", 12, "bold"), width= 30, bd= 4, command= iReset)
      self.btnReset.grid(row= 0, column= 2)

      self.btnExit = Button(ButtonFrame, text= "Exit", font= ("arial", 12, "bold"), width= 30, bd= 4, command= iExit)
      self.btnExit.grid(row= 0, column= 3)

if __name__ == "__main__":
   root = Tk()
   application = Library(root)
   root.mainloop()