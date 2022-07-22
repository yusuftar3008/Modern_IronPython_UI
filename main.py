# coding=utf-8
import os
import sys
import clr
import json
import threading
import datetime
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('Microsoft.VisualBasic')
clr.AddReference('System')
from Microsoft.VisualBasic import *
from System.Drawing import *
from System.Windows.Forms import *



class DashBoard(Form,threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.StartPosition=FormStartPosition.CenterScreen
        self.FormBorderStyle=FormBorderStyle.None
        self.BackColor=Color.FromArgb(46, 51, 73)
        self.Size=Size(951,577)

        self.Panel1=Panel()
        self.Panel1.BackColor=Color.FromArgb(24,30,54)
        self.Panel1.Dock=DockStyle.Left
        self.Panel1.Size=Size(186,577)

        self.Panel1_1=Panel()
        self.Panel1_1.BackColor = Color.FromArgb(24, 30, 54)
        self.Panel1_1.Dock=DockStyle.Top
        self.Panel1_1.Size=Size(186,144)

        self.PictureBox1_1_1=PictureBox()
        self.PictureBox1_1_1.Image = Image.FromFile("user_icon.png")
        self.PictureBox1_1_1.SizeMode=PictureBoxSizeMode.Zoom
        self.PictureBox1_1_1.Size=Size(63,63)
        self.PictureBox1_1_1.Location=Point(60,22)

        self.Label1_1_2=Label()
        self.Label1_1_2.Text="User Name"
        self.Label1_1_2.ForeColor=Color.FromArgb(0,156,149)
        self.Label1_1_2.Font=Font("Microsoft Sans Serif",10, FontStyle.Bold)
        self.Label1_1_2.Location=Point(48,97)

        self.Label1_1_3 = Label()
        self.Label1_1_3.Text = "Some User Text Here"
        self.Label1_1_3.ForeColor = Color.FromArgb(158, 161, 178)
        self.Label1_1_3.Font = Font("Microsoft Sans Serif", 7, FontStyle.Bold)
        self.Label1_1_3.Location = Point(32, 120)
        self.Label1_1_3.AutoSize=True

        self.Button1_1=Button()
        self.Button1_1.Text="DashBoard"
        self.Button1_1.ForeColor=Color.FromArgb(0,126,249)
        self.Button1_1.Font = Font("Nirmala UI", 10, FontStyle.Bold)
        self.Button1_1.FlatStyle=FlatStyle.Flat
        self.Button1_1.FlatAppearance.BorderSize=0
        self.Button1_1.Dock=DockStyle.Top
        self.Button1_1.Name="Dashboard"
        img=Image.FromFile("home.png")
        img_new=Bitmap(img,Size(23,23))
        self.Button1_1.Image=img_new
        self.Button1_1.Size=Size(186,42)
        self.Button1_1.TextImageRelation=TextImageRelation.TextBeforeImage
        self.Button1_1.Click+=self.Clicked_Button
        self.Button1_1.Leave += self.Release_Button


        self.Button1_2 = Button()
        self.Button1_2.Text = "Analytics"
        self.Button1_2.ForeColor = Color.FromArgb(0, 126, 249)
        self.Button1_2.Font = Font("Nirmala UI", 10, FontStyle.Bold)
        self.Button1_2.FlatStyle = FlatStyle.Flat
        self.Button1_2.FlatAppearance.BorderSize = 0
        self.Button1_2.Dock = DockStyle.Top
        self.Button1_2.Name = "Analytics"
        img = Image.FromFile("analytics.png")
        img_new = Bitmap(img, Size(23, 23))
        self.Button1_2.Image = img_new
        self.Button1_2.Size = Size(186, 42)
        self.Button1_2.TextImageRelation = TextImageRelation.TextBeforeImage
        self.Button1_2.Click += self.Clicked_Button
        self.Button1_2.Leave += self.Release_Button


        self.Button1_3 = Button()
        self.Button1_3.Text = "Calender"
        self.Button1_3.ForeColor = Color.FromArgb(0, 126, 249)
        self.Button1_3.Font = Font("Nirmala UI", 10, FontStyle.Bold)
        self.Button1_3.FlatStyle = FlatStyle.Flat
        self.Button1_3.FlatAppearance.BorderSize = 0
        self.Button1_3.Dock = DockStyle.Top
        self.Button1_3.Name = "Calender"
        img = Image.FromFile("calender.png")
        img_new = Bitmap(img, Size(23, 23))
        self.Button1_3.Image = img_new
        self.Button1_3.Size = Size(186, 42)
        self.Button1_3.TextImageRelation = TextImageRelation.TextBeforeImage
        self.Button1_3.Click += self.Clicked_Button
        self.Button1_3.Leave += self.Release_Button


        self.Button1_4 = Button()
        self.Button1_4.Text = "Contact Us"
        self.Button1_4.ForeColor = Color.FromArgb(0, 126, 249)
        self.Button1_4.Font = Font("Nirmala UI", 10, FontStyle.Bold)
        self.Button1_4.FlatStyle = FlatStyle.Flat
        self.Button1_4.FlatAppearance.BorderSize = 0
        self.Button1_4.Dock = DockStyle.Top
        self.Button1_4.Name = "Contact_Us"
        img = Image.FromFile("contact_us.png")
        img_new = Bitmap(img, Size(23, 23))
        self.Button1_4.Image = img_new
        self.Button1_4.Size = Size(186, 42)
        self.Button1_4.TextImageRelation = TextImageRelation.TextBeforeImage
        self.Button1_4.Click += self.Clicked_Button
        self.Button1_4.Leave += self.Release_Button

        self.Button1_5 = Button()
        self.Button1_5.Text = "Settings"
        self.Button1_5.ForeColor = Color.FromArgb(0, 126, 249)
        self.Button1_5.Font = Font("Nirmala UI", 10, FontStyle.Bold)
        self.Button1_5.FlatStyle = FlatStyle.Flat
        self.Button1_5.FlatAppearance.BorderSize = 0
        self.Button1_5.Dock = DockStyle.Bottom
        self.Button1_5.Name = "Settings"
        img = Image.FromFile("settings.png")
        img_new = Bitmap(img, Size(23, 23))
        self.Button1_5.Image = img_new
        self.Button1_5.Size = Size(186, 42)
        self.Button1_5.TextImageRelation = TextImageRelation.TextBeforeImage
        self.Button1_5.Click += self.Clicked_Button
        self.Button1_5.Leave += self.Release_Button

        self.Panel1_2=Panel()
        self.Panel1_2.BackColor=Color.FromArgb(0,126,249)
        self.Panel1_2.Size=Size(3,100)
        self.Panel1_2.Location=Point(0,193)


        ###########################################
        diameter=25
        bounds=Rectangle(0,0,951,577)
        arc=Rectangle(bounds.Location,Size(diameter,diameter))
        path=Drawing2D.GraphicsPath()

        path.AddArc(arc,180,90)
        arc.X=bounds.Right-diameter
        path.AddArc(arc,270,90)
        arc.Y=bounds.Bottom-diameter
        path.AddArc(arc, 0, 90)
        arc.X = bounds.Left
        path.AddArc(arc, 90, 90)
        path.CloseFigure()
        self.Region=Region(path)

        ##########################################

        self.Button1=Button()
        self.Button1.Text='x'
        self.Button1.Size=Size(25,25)
        self.Button1.ForeColor=Color.White
        self.Button1.Location=Point(920,7)
        self.Button1.FlatStyle=FlatStyle.Flat
        self.Button1.FlatAppearance.BorderSize=0
        self.Button1.Font = Font("Microsoft Sans Serif", 10, FontStyle.Bold)
        self.Button1.Name="Exit"
        self.Button1.Click+=self.Clicked_Button




        self.Panel1_1.Controls.Add(self.PictureBox1_1_1)
        self.Panel1_1.Controls.Add(self.Label1_1_2)
        self.Panel1_1.Controls.Add(self.Label1_1_3)

        self.Panel1.Controls.Add(self.Panel1_2)
        self.Panel1.Controls.Add(self.Button1_5)
        self.Panel1.Controls.Add(self.Button1_4)
        self.Panel1.Controls.Add(self.Button1_3)
        self.Panel1.Controls.Add(self.Button1_2)
        self.Panel1.Controls.Add(self.Button1_1)
        self.Panel1.Controls.Add(self.Panel1_1)

        self.Controls.Add(self.Panel1)
        self.Controls.Add(self.Button1)

    def Clicked_Button(self,sender,e):
        self.action=sender.Name
        if(self.action=="Dashboard"):
            self.Panel1_2.Height = self.Button1_1.Height
            self.Panel1_2.Top = self.Button1_1.Top
            self.Panel1_2.Left = self.Button1_1.Left
            self.Button1_1.BackColor = Color.FromArgb(46, 51, 73)

        elif (self.action == "Analytics"):
            self.Panel1_2.Height = self.Button1_2.Height
            self.Panel1_2.Top = self.Button1_2.Top
            self.Panel1_2.Left = self.Button1_2.Left
            self.Button1_2.BackColor = Color.FromArgb(46, 51, 73)

        elif (self.action == "Calender"):
            self.Panel1_2.Height = self.Button1_3.Height
            self.Panel1_2.Top = self.Button1_3.Top
            self.Panel1_2.Left = self.Button1_3.Left
            self.Button1_3.BackColor = Color.FromArgb(46, 51, 73)

        elif (self.action == "Contact_Us"):
            self.Panel1_2.Height = self.Button1_4.Height
            self.Panel1_2.Top = self.Button1_4.Top
            self.Panel1_2.Left = self.Button1_4.Left
            self.Button1_4.BackColor = Color.FromArgb(46, 51, 73)

        elif (self.action == "Settings"):
            self.Panel1_2.Height = self.Button1_5.Height
            self.Panel1_2.Top = self.Button1_5.Top
            self.Panel1_2.Left = self.Button1_5.Left
            self.Button1_5.BackColor = Color.FromArgb(46, 51, 73)

        elif (self.action=="Exit"):
            Application.Exit()
            sys.exit()

    def Release_Button(self,sender,e):
        self.action = sender.Name
        if (self.action == "Dashboard"):
            self.Button1_1.BackColor=Color.FromArgb(24,30,54)

        elif (self.action == "Analytics"):
            self.Button1_2.BackColor=Color.FromArgb(24,30,54)

        elif (self.action == "Calender"):
            self.Button1_3.BackColor=Color.FromArgb(24,30,54)

        elif (self.action == "Contact_Us"):
            self.Button1_4.BackColor=Color.FromArgb(24,30,54)

        elif (self.action == "Settings"):
            self.Button1_5.BackColor=Color.FromArgb(24,30,54)



Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = DashBoard()
Application.Run(form)
form.start()



