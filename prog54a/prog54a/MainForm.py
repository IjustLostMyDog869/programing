import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(187, 42)
		self._label1.TabIndex = 0
		self._label1.Text = "Pick a Car:"
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 FireBird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(237, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(302, 41)
		self._comboBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 66)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(187, 42)
		self._label2.TabIndex = 2
		self._label2.Text = "Miles:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 174)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(187, 42)
		self._label3.TabIndex = 3
		self._label3.Text = "MPG:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 120)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(187, 42)
		self._label4.TabIndex = 4
		self._label4.Text = "Gallons:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(237, 66)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(187, 42)
		self._label5.TabIndex = 5
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(237, 120)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(187, 42)
		self._label6.TabIndex = 6
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(237, 174)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(187, 42)
		self._label7.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(23, 289)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(165, 45)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(220, 289)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(165, 45)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(403, 289)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(165, 45)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(592, 488)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog. 54"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._label5.Text = " "
		self._label6.Text = " "
		self._label7.Text = " "
		self.car = " "

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		miles = 0
		gallons = 0 
		mpg = 0 
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286
			gallons = 9
			
			mpg = miles / float(gallons)
			mpg = round(mpg, 1)
			
			self._label7.Text = str(mpg)
			self._label6.Text = str(gallons)
			self._label5.Text = str(miles)
			
		if car == "1979 FireBird":
			miles = 412
			gallons = 40
			
			mpg = miles / float(gallons)
			mpg = round(mpg, 1)
			
			self._label7.Text = str(mpg)
			self._label6.Text = str(gallons)
			self._label5.Text = str(miles)
			
		if car == "1980 Subaru":
			miles = 361
			gallons = 18
			
			mpg = miles / float(gallons)
			mpg = round(mpg, 1)
			
			self._label7.Text = str(mpg)
			self._label6.Text = str(gallons)
			self._label5.Text = str(miles)
			
		if car == "1975 Cutlass":
			miles = 161
			gallons = 11
			
			mpg = miles / float(gallons)
			mpg = round(mpg, 1)
			
			self._label7.Text = str(mpg)
			self._label6.Text = str(gallons)
			self._label5.Text = str(miles)