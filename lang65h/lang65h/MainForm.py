import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkTurquoise
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label1.Location = System.Drawing.Point(36, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(298, 42)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Pounds:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkTurquoise
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label2.Location = System.Drawing.Point(36, 81)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(298, 42)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter Shillings:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkTurquoise
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label3.Location = System.Drawing.Point(36, 132)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(298, 42)
		self._label3.TabIndex = 2
		self._label3.Text = "Enter Pence:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkTurquoise
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label4.Location = System.Drawing.Point(36, 185)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(298, 42)
		self._label4.TabIndex = 3
		self._label4.Text = "Decimals Pounds ="
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkTurquoise
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.DarkSlateGray
		self._textBox1.Location = System.Drawing.Point(340, 27)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(146, 44)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkTurquoise
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.DarkSlateGray
		self._textBox2.Location = System.Drawing.Point(340, 77)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(146, 44)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.DarkTurquoise
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.DarkSlateGray
		self._textBox3.Location = System.Drawing.Point(340, 132)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(146, 44)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkTurquoise
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label5.Location = System.Drawing.Point(341, 185)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(145, 42)
		self._label5.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkTurquoise
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DarkSlateGray
		self._button1.Location = System.Drawing.Point(37, 231)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 42)
		self._button1.TabIndex = 8
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkTurquoise
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DarkSlateGray
		self._button2.Location = System.Drawing.Point(201, 231)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(97, 42)
		self._button2.TabIndex = 9
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkTurquoise
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DarkSlateGray
		self._button3.Location = System.Drawing.Point(304, 231)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(80, 42)
		self._button3.TabIndex = 10
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SeaGreen
		self.ClientSize = System.Drawing.Size(504, 315)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pro65h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label5.Text = " "
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._textBox3.Text = " "

	def Button1Click(self, sender, e):
		pounds = int(self._textBox1.Text)
		shilling = int(self._textBox2.Text)
		pence = int(self._textBox3.Text)
		decimals = 7.89
		self._label5.Text = str(decimals)