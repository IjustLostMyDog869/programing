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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Vivaldi", 36, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.HotTrack
		self._button1.Location = System.Drawing.Point(24, 341)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(159, 56)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Vivaldi", 36, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.HotTrack
		self._button2.Location = System.Drawing.Point(248, 341)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(168, 56)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.White
		self._button3.Font = System.Drawing.Font("Vivaldi", 36, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.HotTrack
		self._button3.Location = System.Drawing.Point(500, 341)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(168, 56)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.HighlightText
		self._label1.Font = System.Drawing.Font("Snap ITC", 48, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label1.Location = System.Drawing.Point(108, 55)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(463, 211)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Green
		self.ClientSize = System.Drawing.Size(722, 424)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)

	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = "Hello World"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()