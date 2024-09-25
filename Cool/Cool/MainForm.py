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
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(32, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "lenght"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label2.Location = System.Drawing.Point(32, 97)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "width"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label3.Location = System.Drawing.Point(32, 186)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(164, 41)
		self._label3.TabIndex = 2
		self._label3.Text = "area"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label4.Location = System.Drawing.Point(32, 239)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(164, 34)
		self._label4.TabIndex = 3
		self._label4.Text = "perimiter"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label5.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label5.Location = System.Drawing.Point(354, 186)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(342, 41)
		self._label5.TabIndex = 4
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label6.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label6.Location = System.Drawing.Point(354, 239)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(342, 34)
		self._label6.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._button1.Location = System.Drawing.Point(32, 343)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(181, 64)
		self._button1.TabIndex = 6
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._button2.Location = System.Drawing.Point(264, 343)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(190, 64)
		self._button2.TabIndex = 7
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._button3.Location = System.Drawing.Point(506, 343)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(190, 64)
		self._button3.TabIndex = 8
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._textBox1.Location = System.Drawing.Point(354, 12)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(323, 39)
		self._textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("SketchFlow Print", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._textBox2.Location = System.Drawing.Point(354, 83)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(323, 37)
		self._textBox2.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self.ClientSize = System.Drawing.Size(735, 437)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Cool"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		lenght = int (self._TextBox1.Text)
		width = int (self._TextBox1.Text)
		area = leangth * width 
		perim = 2 * lenght + 2 * width
		self._label5.Text = str(area)
		self._label6.Text = str(perim)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		sel._label5.Text = ""
		sel._textBox6.Text = ""