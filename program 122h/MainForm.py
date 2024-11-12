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
		self._listBox1.BackColor = System.Drawing.Color.Tan
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.AntiqueWhite
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 37
		self._listBox1.Location = System.Drawing.Point(13, 3)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(307, 263)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Teal
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.AntiqueWhite
		self._button1.Location = System.Drawing.Point(344, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(145, 67)
		self._button1.TabIndex = 1
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Olive
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.AntiqueWhite
		self._button2.Location = System.Drawing.Point(344, 97)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(144, 66)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Peru
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 32.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.AntiqueWhite
		self._button3.Location = System.Drawing.Point(345, 184)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(144, 67)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOrange
		self.ClientSize = System.Drawing.Size(524, 278)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "pro.122h"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		heading = "number\t"+"square\t"+"square root\t""cubed\t"+"4th root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 21):
			y = num ** 2
			x = round(math.sqrt(num), 4)
			t = num ** 3 
			d = round(math.sqrt(num), 4)
			line = str(num) + "\t" + str(y) + "\t" + str(x) + "\t" + "\t" + str(t) + "\t" + str(d)
			self._listBox1.Items.Add(line)