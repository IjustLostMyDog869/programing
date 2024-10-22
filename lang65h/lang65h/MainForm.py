import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
					self._button1 = System.Windows.Forms.Button()
					self._button2 = System.Windows.Forms.Button()
					self._button3 = System.Windows.Forms.Button()
					self._label1 = System.Windows.Forms.Label()
					self._label2 = System.Windows.Forms.Label()
					self._label3 = System.Windows.Forms.Label()
					self._textBox1 = System.Windows.Forms.TextBox()
					self._textBox2 = System.Windows.Forms.TextBox()
					self._textBox3 = System.Windows.Forms.TextBox()
					self._label4 = System.Windows.Forms.Label()
					self.SuspendLayout()
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.DarkTurquoise
					self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.Location = System.Drawing.Point(12, 218)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(130, 56)
					self._button1.TabIndex = 0
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.DarkTurquoise
					self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.Location = System.Drawing.Point(148, 218)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(130, 56)
					self._button2.TabIndex = 1
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.DarkTurquoise
					self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.Location = System.Drawing.Point(285, 218)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(130, 56)
					self._button3.TabIndex = 2
					self._button3.Text = "Quit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.DarkTurquoise
					self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label1.Location = System.Drawing.Point(26, 18)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(174, 35)
					self._label1.TabIndex = 3
					self._label1.Text = "Enter Pounds:"
					# 
					# label2
					# 
					self._label2.BackColor = System.Drawing.Color.DarkTurquoise
					self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label2.Location = System.Drawing.Point(26, 70)
					self._label2.Name = "label2"
					self._label2.Size = System.Drawing.Size(174, 35)
					self._label2.TabIndex = 4
					self._label2.Text = "Enter Shillings:"
					# 
					# label3
					# 
					self._label3.BackColor = System.Drawing.Color.DarkTurquoise
					self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label3.Location = System.Drawing.Point(26, 120)
					self._label3.Name = "label3"
					self._label3.Size = System.Drawing.Size(174, 35)
					self._label3.TabIndex = 5
					self._label3.Text = "Enter Pence:"
					# 
					# textBox1
					# 
					self._textBox1.BackColor = System.Drawing.Color.DarkTurquoise
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.Location = System.Drawing.Point(206, 18)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(189, 35)
					self._textBox1.TabIndex = 6
					# 
					# textBox2
					# 
					self._textBox2.BackColor = System.Drawing.Color.DarkTurquoise
					self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox2.Location = System.Drawing.Point(206, 70)
					self._textBox2.Name = "textBox2"
					self._textBox2.Size = System.Drawing.Size(189, 35)
					self._textBox2.TabIndex = 7
					# 
					# textBox3
					# 
					self._textBox3.BackColor = System.Drawing.Color.DarkTurquoise
					self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox3.Location = System.Drawing.Point(206, 123)
					self._textBox3.Name = "textBox3"
					self._textBox3.Size = System.Drawing.Size(189, 35)
					self._textBox3.TabIndex = 8
					# 
					# label4
					# 
					self._label4.BackColor = System.Drawing.Color.DarkTurquoise
					self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label4.Location = System.Drawing.Point(12, 187)
					self._label4.Name = "label4"
					self._label4.Size = System.Drawing.Size(388, 28)
					self._label4.TabIndex = 9
					self._label4.Text = "Decimal Pounds: "
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.SeaGreen
					self.ClientSize = System.Drawing.Size(427, 283)
					self.Controls.Add(self._label4)
					self.Controls.Add(self._textBox3)
					self.Controls.Add(self._textBox2)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._label3)
					self.Controls.Add(self._label2)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Name = "MainForm"
					self.Text = "Prog65H"
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        pnd = float(self._textBox1.Text)
        shill = float(self._textBox2.Text) / 20
        pen = float(self._textBox3.Text) / 240
        ttl = str(pnd + shill + pen)
        self._label4.Text = "Decimal Pounds: %.2f" % float(ttl)


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label4.Text = "Decimal Pounds: "

    def Button3Click(self, sender, e):
        Application.Exit()