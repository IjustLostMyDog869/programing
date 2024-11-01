import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
					self._listBox1 = System.Windows.Forms.ListBox()
					self._button1 = System.Windows.Forms.Button()
					self._button2 = System.Windows.Forms.Button()
					self._button3 = System.Windows.Forms.Button()
					self.SuspendLayout()
					# 
					# listBox1
					# 
					self._listBox1.Font = System.Drawing.Font("Nirmala UI", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._listBox1.ForeColor = System.Drawing.Color.Navy
					self._listBox1.FormattingEnabled = True
					self._listBox1.Location = System.Drawing.Point(2, 12)
					self._listBox1.Name = "listBox1"
					self._listBox1.Size = System.Drawing.Size(373, 290)
					self._listBox1.TabIndex = 0
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.Aquamarine
					self._button1.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.Location = System.Drawing.Point(381, 24)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(109, 49)
					self._button1.TabIndex = 1
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.Aquamarine
					self._button2.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.Location = System.Drawing.Point(381, 132)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(109, 49)
					self._button2.TabIndex = 2
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.Aquamarine
					self._button3.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.Location = System.Drawing.Point(381, 245)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(109, 49)
					self._button3.TabIndex = 3
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
					self.ClientSize = System.Drawing.Size(497, 328)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Controls.Add(self._listBox1)
					self.Name = "MainForm"
					self.Text = "Prog152a"
					self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        header = "Sum :  "
        self._listBox1.Items.Add(header)
        sum = 0
        for num in range (3,9669+1,3):
            sum = sum + num 
        self._listBox1.Items.Add(sum)
        
        list = "3 + 6 + 9 + 12 + 15 + 18 + 21 + ...+ 24 + 9663 + 9666 + 9669 = " + str(sum)
        self._listBox1.Items.Add(list)

        
    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label1Click(self, sender, e):
        pass