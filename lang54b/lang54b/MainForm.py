import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._textBox1.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.Black
        self._textBox1.Location = System.Drawing.Point(296, 369)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(118, 33)
        self._textBox1.TabIndex = 1
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._textBox2.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.Black
        self._textBox2.Location = System.Drawing.Point(153, 369)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(118, 33)
        self._textBox2.TabIndex = 3
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._textBox3.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.ForeColor = System.Drawing.Color.Black
        self._textBox3.Location = System.Drawing.Point(440, 369)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(118, 33)
        self._textBox3.TabIndex = 5
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._textBox4.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.ForeColor = System.Drawing.Color.Black
        self._textBox4.Location = System.Drawing.Point(12, 369)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(118, 33)
        self._textBox4.TabIndex = 6
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button1.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Black
        self._button1.Location = System.Drawing.Point(612, 25)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(161, 109)
        self._button1.TabIndex = 7
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button3.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Black
        self._button3.Location = System.Drawing.Point(612, 179)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(166, 109)
        self._button3.TabIndex = 8
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button2.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Black
        self._button2.Location = System.Drawing.Point(612, 331)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(166, 109)
        self._button2.TabIndex = 9
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Black
        self._label1.Location = System.Drawing.Point(28, 45)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(118, 29)
        self._label1.TabIndex = 10
        self._label1.Text = "average:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label2.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Black
        self._label2.Location = System.Drawing.Point(28, 88)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(118, 29)
        self._label2.TabIndex = 11
        self._label2.Text = "sum:"
        # 
        # textBox5
        # 
        self._textBox5.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._textBox5.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.ForeColor = System.Drawing.Color.Black
        self._textBox5.Location = System.Drawing.Point(162, 45)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(100, 33)
        self._textBox5.TabIndex = 12
        # 
        # textBox6
        # 
        self._textBox6.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._textBox6.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.ForeColor = System.Drawing.Color.Black
        self._textBox6.Location = System.Drawing.Point(162, 88)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(100, 33)
        self._textBox6.TabIndex = 13
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label3.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(153, 278)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(261, 61)
        self._label3.TabIndex = 14
        self._label3.Text = "Write 4 integers"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DodgerBlue
        self.ClientSize = System.Drawing.Size(817, 452)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Lang54b Gui"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def Label1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        Application.Exit()

    def Button3Click(self, sender, e):
        self._textBox5.Text = " "
        self._textBox6.Text = " "
        self._textBox1.Text = " "
        self._textBox2.Text = " "
        self._textBox3.Text = " "
        self._textBox4.Text = " "

    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        Sum = num1 + num2 + num3 + num4
        average = Sum / 4.0
        self._textBox6.Text = str(Sum)
        self._textBox5.Text = str(average)