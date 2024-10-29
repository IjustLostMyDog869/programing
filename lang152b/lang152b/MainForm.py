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
					self._label1 = System.Windows.Forms.Label()
					self._textBox1 = System.Windows.Forms.TextBox()
					self.SuspendLayout()
					# 
					# listBox1
					# 
					self._listBox1.Font = System.Drawing.Font("Mongolian Baiti", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._listBox1.FormattingEnabled = True
					self._listBox1.ItemHeight = 16
					self._listBox1.Location = System.Drawing.Point(31, 94)
					self._listBox1.Name = "listBox1"
					self._listBox1.Size = System.Drawing.Size(537, 212)
					self._listBox1.TabIndex = 0
					# 
					# button1
					# 
					self._button1.BackColor = System.Drawing.Color.Tan
					self._button1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._button1.ForeColor = System.Drawing.SystemColors.ControlText
					self._button1.Location = System.Drawing.Point(12, 323)
					self._button1.Name = "button1"
					self._button1.Size = System.Drawing.Size(187, 84)
					self._button1.TabIndex = 1
					self._button1.Text = "Calculate"
					self._button1.UseVisualStyleBackColor = False
					self._button1.Click += self.Button1Click
					# 
					# button2
					# 
					self._button2.BackColor = System.Drawing.Color.Tan
					self._button2.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._button2.ForeColor = System.Drawing.SystemColors.ControlText
					self._button2.Location = System.Drawing.Point(205, 324)
					self._button2.Name = "button2"
					self._button2.Size = System.Drawing.Size(187, 85)
					self._button2.TabIndex = 2
					self._button2.Text = "Clear"
					self._button2.UseVisualStyleBackColor = False
					self._button2.Click += self.Button2Click
					# 
					# button3
					# 
					self._button3.BackColor = System.Drawing.Color.Tan
					self._button3.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._button3.ForeColor = System.Drawing.SystemColors.ControlText
					self._button3.Location = System.Drawing.Point(398, 324)
					self._button3.Name = "button3"
					self._button3.Size = System.Drawing.Size(187, 87)
					self._button3.TabIndex = 3
					self._button3.Text = "Exit"
					self._button3.UseVisualStyleBackColor = False
					self._button3.Click += self.Button3Click
					# 
					# label1
					# 
					self._label1.BackColor = System.Drawing.Color.Tan
					self._label1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
					self._label1.Location = System.Drawing.Point(12, 14)
					self._label1.Name = "label1"
					self._label1.Size = System.Drawing.Size(187, 32)
					self._label1.TabIndex = 4
					self._label1.Text = "Enter test value:"
					self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
					# 
					# textBox1
					# 
					self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
					self._textBox1.Location = System.Drawing.Point(12, 50)
					self._textBox1.Name = "textBox1"
					self._textBox1.Size = System.Drawing.Size(187, 26)
					self._textBox1.TabIndex = 5
					# 
					# MainForm
					# 
					self.BackColor = System.Drawing.Color.NavajoWhite
					self.ClientSize = System.Drawing.Size(594, 422)
					self.Controls.Add(self._textBox1)
					self.Controls.Add(self._label1)
					self.Controls.Add(self._button3)
					self.Controls.Add(self._button2)
					self.Controls.Add(self._button1)
					self.Controls.Add(self._listBox1)
					self.Name = "MainForm"
					self.Text = "Prog152b"
					self.ResumeLayout(False)
					self.PerformLayout()


    def Button1Click(self, sender, e):
        Limit = int(self._textBox1.Text)
        Num = 1
        EvenNum = 0
        Sum = 0
        self._listBox1.Items.Add("Even Integer\tSum")
        while Sum <= Limit:
            EvenNum = Num * 2
            Sum = Sum + EvenNum
            Num = Num + 1
            Line = str(EvenNum) + "\t\t" + str(Sum)
            self._listBox1.Items.Add(Line)            
        
        
        
            

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()