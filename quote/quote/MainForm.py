import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._pictureBox1.BeginInit()
		self.SuspendLayout()
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._pictureBox1.Dock = System.Windows.Forms.DockStyle.Fill
		self._pictureBox1.ErrorImage = None
		self._pictureBox1.InitialImage = None
		self._pictureBox1.Location = System.Drawing.Point(0, 0)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(900, 484)
		self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
		self._pictureBox1.TabIndex = 0
		self._pictureBox1.TabStop = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._label1.Font = System.Drawing.Font("Tempus Sans ITC", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(172, 134)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(528, 154)
		self._label1.TabIndex = 1
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Pristina", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(66, 373)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(137, 53)
		self._button1.TabIndex = 2
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Pristina", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(376, 373)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(137, 53)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Pristina", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(687, 373)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(137, 53)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ButtonFace
		self.ClientSize = System.Drawing.Size(900, 484)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._pictureBox1)
		self.Font = System.Drawing.Font("Pristina", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "quote"
		self._pictureBox1.EndInit()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Let go of who you think you're supposed to be and embrace who you are."

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()