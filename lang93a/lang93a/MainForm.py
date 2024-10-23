import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
					self._label1 = System.Windows.Forms.Label()
					self._textBox1 = System.Windows.Forms.TextBox()
					self._button1 = System.Windows.Forms.Button()
					self._button2 = System.Windows.Forms.Button()
					self._button3 = System.Windows.Forms.Button()
					self._label6 = System.Windows.Forms.Label()
					self._label7 = System.Windows.Forms.Label()
					self._label8 = System.Windows.Forms.Label()
					self._label9 = System.Windows.Forms.Label()
					self._label11 = System.Windows.Forms.Label()
					self._label12 = System.Windows.Forms.Label()
					self._label13 = System.Windows.Forms.Label()
					self._label15 = System.Windows.Forms.Label()
					self._label17 = System.Windows.Forms.Label()
					self._label14 = System.Windows.Forms.Label()
					self._label16 = System.Windows.Forms.Label()
					self._label18 = System.Windows.Forms.Label()
					self._label19 = System.Windows.Forms.Label()
					self._label20 = System.Windows.Forms.Label()
					self._label21 = System.Windows.Forms.Label()
					self._label10 = System.Windows.Forms.Label()
					self._label5 = System.Windows.Forms.Label()
					self.SuspendLayout()
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.Pink
					self._label1.Font = System.Drawing.Font("Papyrus", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label1.Location = System.Drawing.Point(23, 26)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(172, 46)
					self._label1.TabIndex = 0
					self._label1.Text = "KWH:"
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
					# 
					# textBox1
					# 
					self._textBox1.BackColor = System.Drawing.Color.Pink
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.Location = System.Drawing.Point(85, 36)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(100, 26)
					self._textBox1.TabIndex = 1
					self._textBox1.TextChanged += self.TextBox1TextChanged
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.Pink
					self._button1.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.Location = System.Drawing.Point(23, 95)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(172, 44)
					self._button1.TabIndex = 2
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.Pink
					self._button2.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.Location = System.Drawing.Point(23, 163)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(172, 44)
					self._button2.TabIndex = 3
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.Pink
					self._button3.Font = System.Drawing.Font("Microsoft Yi Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.Location = System.Drawing.Point(23, 232)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(172, 44)
					self._button3.TabIndex = 4
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# label6
					# 
					self._label6.BackColor = System.Drawing.Color.Pink
					self._label6.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label6.Location = System.Drawing.Point(245, 40)
					self._label6.Name = "label6"
					self._label6.Size = System.Drawing.Size(229, 32)
					self._label6.TabIndex = 10
					self._label6.Text = "Kilowats Used:"
					# 
					# label7
					# 
					self._label7.BackColor = System.Drawing.Color.Pink
					self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label7.Location = System.Drawing.Point(384, 44)
					self._label7.Name = "label7"
					self._label7.Size = System.Drawing.Size(64, 32)
					self._label7.TabIndex = 11
					# 
					# label8
					# 
					self._label8.BackColor = System.Drawing.Color.Pink
					self._label8.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label8.Location = System.Drawing.Point(245, 76)
					self._label8.Name = "label8"
					self._label8.Size = System.Drawing.Size(229, 32)
					self._label8.TabIndex = 12
					self._label8.Text = "Base Rate:"
					# 
					# label9
					# 
					self._label9.BackColor = System.Drawing.Color.Pink
					self._label9.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label9.Location = System.Drawing.Point(326, 74)
					self._label9.Name = "label9"
					self._label9.Size = System.Drawing.Size(55, 32)
					self._label9.TabIndex = 13
					self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label11
					# 
					self._label11.BackColor = System.Drawing.Color.Pink
					self._label11.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label11.Location = System.Drawing.Point(245, 106)
					self._label11.Name = "label11"
					self._label11.Size = System.Drawing.Size(229, 32)
					self._label11.TabIndex = 15
					self._label11.Text = "Base Rate Price:"
					# 
					# label12
					# 
					self._label12.BackColor = System.Drawing.Color.Pink
					self._label12.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label12.Location = System.Drawing.Point(384, 104)
					self._label12.Name = "label12"
					self._label12.Size = System.Drawing.Size(84, 32)
					self._label12.TabIndex = 16
					self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleRight
					# 
					# label13
					# 
					self._label13.BackColor = System.Drawing.Color.Pink
					self._label13.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label13.Location = System.Drawing.Point(245, 129)
					self._label13.Name = "label13"
					self._label13.Size = System.Drawing.Size(229, 32)
					self._label13.TabIndex = 17
					self._label13.Text = "Surcharge:"
					# 
					# label15
					# 
					self._label15.BackColor = System.Drawing.Color.Pink
					self._label15.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label15.Location = System.Drawing.Point(384, 127)
					self._label15.Name = "label15"
					self._label15.Size = System.Drawing.Size(84, 32)
					self._label15.TabIndex = 19
					self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleRight
					# 
					# label17
					# 
					self._label17.BackColor = System.Drawing.Color.Pink
					self._label17.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label17.Location = System.Drawing.Point(245, 161)
					self._label17.Name = "label17"
					self._label17.Size = System.Drawing.Size(229, 32)
					self._label17.TabIndex = 21
					self._label17.Text = "______________________________________"
					# 
					# label14
					# 
					self._label14.BackColor = System.Drawing.Color.Pink
					self._label14.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label14.Location = System.Drawing.Point(245, 153)
					self._label14.Name = "label14"
					self._label14.Size = System.Drawing.Size(229, 32)
					self._label14.TabIndex = 22
					self._label14.Text = "Tax:"
					# 
					# label16
					# 
					self._label16.BackColor = System.Drawing.Color.Pink
					self._label16.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label16.Location = System.Drawing.Point(384, 150)
					self._label16.Name = "label16"
					self._label16.Size = System.Drawing.Size(84, 32)
					self._label16.TabIndex = 23
					self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleRight
					# 
					# label18
					# 
					self._label18.BackColor = System.Drawing.Color.Pink
					self._label18.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label18.Location = System.Drawing.Point(245, 218)
					self._label18.Name = "label18"
					self._label18.Size = System.Drawing.Size(104, 32)
					self._label18.TabIndex = 24
					self._label18.Text = "Pay Amount:"
					# 
					# label19
					# 
					self._label19.BackColor = System.Drawing.Color.Pink
					self._label19.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label19.Location = System.Drawing.Point(364, 218)
					self._label19.Name = "label19"
					self._label19.Size = System.Drawing.Size(104, 32)
					self._label19.TabIndex = 25
					self._label19.Text = "After May 20:"
					# 
					# label20
					# 
					self._label20.BackColor = System.Drawing.Color.Pink
					self._label20.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label20.Location = System.Drawing.Point(245, 238)
					self._label20.Name = "label20"
					self._label20.Size = System.Drawing.Size(104, 32)
					self._label20.TabIndex = 26
					self._label20.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label21
					# 
					self._label21.BackColor = System.Drawing.Color.Pink
					self._label21.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label21.Location = System.Drawing.Point(364, 244)
					self._label21.Name = "label21"
					self._label21.Size = System.Drawing.Size(104, 26)
					self._label21.TabIndex = 27
					self._label21.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# label10
					# 
					self._label10.BackColor = System.Drawing.Color.Pink
					self._label10.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label10.Location = System.Drawing.Point(384, 76)
					self._label10.Name = "label10"
					self._label10.Size = System.Drawing.Size(84, 32)
					self._label10.TabIndex = 14
					self._label10.Text = "@ $ 0.0475"
					# 
					# label5
					# 
					self._label5.BackColor = System.Drawing.Color.Pink
					self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label5.Location = System.Drawing.Point(245, 50)
					self._label5.Name = "label5"
					self._label5.Size = System.Drawing.Size(229, 32)
					self._label5.TabIndex = 9
					self._label5.Text = "______________________________________"
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.MediumPurple
					self.ClientSize = System.Drawing.Size(504, 298)
					self.Controls.Add(self._label21)
					self.Controls.Add(self._label20)
					self.Controls.Add(self._label19)
					self.Controls.Add(self._label18)
					self.Controls.Add(self._label16)
					self.Controls.Add(self._label14)
					self.Controls.Add(self._label17)
					self.Controls.Add(self._label15)
					self.Controls.Add(self._label13)
					self.Controls.Add(self._label12)
					self.Controls.Add(self._label11)
					self.Controls.Add(self._label10)
					self.Controls.Add(self._label9)
					self.Controls.Add(self._label8)
					self.Controls.Add(self._label7)
					self.Controls.Add(self._label6)
					self.Controls.Add(self._label5)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._label1)
					self.Name = "MainForm"
					self.Text = "Prog93a"
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        KWH = int(self._textBox1.Text)
        BaseRate = round(KWH * 0.0475,2)
        Surcharge = round(BaseRate * 0.1,2)
        Tax = round(BaseRate * 0.03,2)
        Total = BaseRate + Surcharge + Tax
        LateTotal = round(Total + Total * 0.04,2)
        
        self._label12.Text = "$ " + str(BaseRate)
        self._label15.Text = "$ " + str(Surcharge)
        self._label16.Text = "$ " + str(Tax)
        
        self._label20.Text = "$ " + str(Total)
        self._label21.Text = "$ " 

    def Button2Click(self, sender, e):
        self._label12.Text = ""
        self._label15.Text = ""
        self._label16.Text = ""
        self._label20.Text = ""
        self._label21.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()


   

    

    def TextBox1TextChanged(self, sender, e):
        self._label7.Text = (self._textBox1.Text)
        self._label9.Text = (self._textBox1.Text)