import math
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
		self._listBox1.BackColor = System.Drawing.Color.White
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.Black
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 33
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(514, 202)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.White
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Black
		self._button1.Location = System.Drawing.Point(12, 220)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(167, 123)
		self._button1.TabIndex = 1
		self._button1.Text = "calcaulate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.White
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Black
		self._button2.Location = System.Drawing.Point(185, 221)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(167, 122)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.White
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Black
		self._button3.Location = System.Drawing.Point(358, 220)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(168, 122)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.AliceBlue
		self.ClientSize = System.Drawing.Size(538, 408)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.ForeColor = System.Drawing.Color.Sienna
		self.Name = "MainForm"
		self.Text = "pro122.i"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		heading = "number\tcube root\t	cubed"
		self._listBox1.Items.Add(heading)
		for num in range(-25, 26):
			root = round(abs(num) ** 0.3333333333333, 5) 
			
			cubed = num ** 3
			line = str(num) + "\t" + str(root) + "\t" + "\t" + str(cubed)
			self._listBox1.Items.Add(line)