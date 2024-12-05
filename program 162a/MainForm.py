import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
					resources = System.Resources.ResourceManager("program_162a.MainForm", System.Reflection.Assembly.GetEntryAssembly())
					self._textBox1 = System.Windows.Forms.TextBox()
					self._button1 = System.Windows.Forms.Button()
					self._label1 = System.Windows.Forms.Label()
					self._button2 = System.Windows.Forms.Button()
					self._button3 = System.Windows.Forms.Button()
					self._pictureBox1 = System.Windows.Forms.PictureBox()
					self._pictureBox1.BeginInit()
					self.SuspendLayout()
					# 
					# textBox1
					# 
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.Location = System.Drawing.Point(12, 12)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(122, 33)
					self._textBox1.TabIndex = 0
					# 
					# button1
					# 
					self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.Location = System.Drawing.Point(140, 12)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(101, 33)
					self._button1.TabIndex = 1
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = True
					self._button1.Click += self.Button1Click
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.LightCoral
					self._label1.Font = System.Drawing.Font("Haettenschweiler", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._label1.ForeColor = System.Drawing.Color.Maroon
					self._label1.Location = System.Drawing.Point(12, 48)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(382, 402)
					self._label1.TabIndex = 2
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# button2
					# 
					self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.Location = System.Drawing.Point(247, 12)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(71, 33)
					self._button2.TabIndex = 3
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = True
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.PowderBlue
					self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.Location = System.Drawing.Point(323, 12)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(71, 33)
					self._button3.TabIndex = 4
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# pictureBox1
					# 
					self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
					self._pictureBox1.Location = System.Drawing.Point(397, 12)
					self._pictureBox1.Name = "pictureBox1"
					self._pictureBox1.Size = System.Drawing.Size(415, 456)
					self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
					self._pictureBox1.TabIndex = 5
					self._pictureBox1.TabStop = False
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.IndianRed
					self.ClientSize = System.Drawing.Size(824, 480)
					self.Controls.Add(self._pictureBox1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._button1)
					self.Controls.Add(self._textBox1)
					self.Name = "MainForm"
					self.Text = "Lang162a"
					self._pictureBox1.EndInit()
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        n = int(self._textBox1.Text)
        f = 1
        tot = 1
        while f <= n:
            tot = tot * f
            f = f + 1
        self._label1.Text = "The value of " + str(n) + "! is " + str(tot)

    def Button2Click(self, sender, e):
        self._label1.Text = " "

    def Button3Click(self, sender, e):
        Application.Exit()
