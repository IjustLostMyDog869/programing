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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(24, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(231, 38)
		self._label1.TabIndex = 0
		self._label1.Text = "purchase prices"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(24, 68)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(231, 38)
		self._label2.TabIndex = 1
		self._label2.Text = "amount prices"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(286, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(133, 40)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(286, 64)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(133, 40)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(23, 115)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(231, 38)
		self._label3.TabIndex = 4
		self._label3.Text = "change due"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(23, 377)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(231, 38)
		self._label4.TabIndex = 5
		self._label4.Text = "Pennies"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(23, 320)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(231, 38)
		self._label5.TabIndex = 6
		self._label5.Text = "Nickel"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(23, 269)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(231, 38)
		self._label6.TabIndex = 7
		self._label6.Text = "Dimes"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(23, 218)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(231, 38)
		self._label7.TabIndex = 8
		self._label7.Text = "Quarters"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(23, 166)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(231, 38)
		self._label8.TabIndex = 9
		self._label8.Text = "Dollars"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.White
		self._label9.Location = System.Drawing.Point(278, 115)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(141, 38)
		self._label9.TabIndex = 10
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.White
		self._label10.Location = System.Drawing.Point(278, 166)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(141, 38)
		self._label10.TabIndex = 11
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.White
		self._label11.Location = System.Drawing.Point(278, 218)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(141, 38)
		self._label11.TabIndex = 12
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.White
		self._label12.Location = System.Drawing.Point(278, 269)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(141, 38)
		self._label12.TabIndex = 13
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.White
		self._label13.Location = System.Drawing.Point(278, 320)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(141, 38)
		self._label13.TabIndex = 14
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.White
		self._label14.Location = System.Drawing.Point(278, 377)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(141, 38)
		self._label14.TabIndex = 15
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._button1.Font = System.Drawing.Font("MS Reference Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(443, 16)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(156, 114)
		self._button1.TabIndex = 16
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._button2.Font = System.Drawing.Font("MS Reference Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(443, 157)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(156, 114)
		self._button2.TabIndex = 17
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._button3.Font = System.Drawing.Font("MS Reference Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(443, 298)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(156, 114)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(652, 464)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "lang58t.2"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._label9.Text = " "
		self._label10.Text = " "
		self._label11.Text = " "
		self._label12.Text = " "
		self._label13.Text = " "
		self._label14.Text = " "

	def Button1Click(self, sender, e):
		purchase = float(self._textBox1.Text)
		amount = float(self._textBox2.Text)
		change = amount - purchase
		self._label9.Text = str(change)
		dollar = change // 1
		change -= 1 * dollar
		self._label10.Text = str(dollar)
		quarter = change // .25
		change -= .25 * quarter
		self._label11.Text = str(quarter)
		dime = change // .10
		change -= .10 * dime
		self._label12.Text = str(dime)
		nickel = change // .05
		change -= 0.05 * nickel
		self._label13.Text = str(dime)
		pennie = change // 0.01
		change -= 0.01 * pennie
		self._label14.Text = str(pennie)

	def MainFormLoad(self, sender, e):
		pass