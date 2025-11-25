import wx 
import wx.lib.scrolledpanel as scrolled 
import random 
import matplotlib 
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as fc
from matplotlib.figure import Figure

class w2g(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Weigh2Go",size=(750,650))

        panel=wx.Panel(self)
        nb=wx.Notebook(panel)

        self.input=wx.Panel(nb)
        self.tips=scrolled.ScrolledPanel(nb,style=wx.TAB_TRAVERSAL)
        self.tips.SetupScrolling()

        nb.AddPage(self.input,"Input")
        nb.AddPage(self.tips,"Graph + Tips")

        self.build_input(nb)
        self.build_tips()

        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nb,1,wx.EXPAND)
        panel.SetSizer(sizer)

        self.nb=nb
        self.bmi_value=0

        self.Centre()
        self.Show()

    def build_input(self,nb):
        panel=self.input
        panel.SetBackgroundColour("#7E4873")

        vbox=wx.BoxSizer(wx.VERTICAL)

        title=wx.StaticText(panel,label="Welcome to w2g!")
        title.SetFont(wx.Font(20,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        vbox.Add(title,0,wx.ALIGN_CENTER|wx.TOP,20)

        grid=wx.FlexGridSizer(4,2,10,10)

        lbl_name=wx.StaticText(panel,label="Name:")
        self.txt_name=wx.TextCtrl(panel,size=(300,30))

        lbl_gender=wx.StaticText(panel,label="Gender:")
        self.choice_gender=wx.Choice(panel,choices=["Male","Female"])

        lbl_height=wx.StaticText(panel,label="Height (cm):")
        self.txt_height=wx.TextCtrl(panel,size=(300,30))

        lbl_weight=wx.StaticText(panel,label="Weight(kg):")
        self.txt_weight=wx.TextCtrl(panel,size=(300,30))

        for item in [lbl_name,self.txt_name,lbl_gender,self.choice_gender,
                     lbl_height,self.txt_height,lbl_weight,self.txt_weight]:
            grid.Add(item,0,wx.EXPAND)

        vbox.Add(grid,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,20)

        self.lbl_bmi_result=wx.StaticText(panel,label="Your BMI = ")
        self.lbl_bmi_result.SetFont(wx.Font(14,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        vbox.Add(self.lbl_bmi_result,0,wx.LEFT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL,15)

        hbox=wx.BoxSizer(wx.HORIZONTAL)

        btn_calc=wx.Button(panel,label="Calculate BMI")
        btn_calc.Bind(wx.EVT_BUTTON,self.calculate_bmi)
        hbox.Add(btn_calc,0,wx.RIGHT,10)

        btn_next=wx.Button(panel,label="Show Graph + Tips")
        btn_next.Bind(wx.EVT_BUTTON,self.show_graph_and_tips)
        hbox.Add(btn_next)

        vbox.Add(hbox,0,wx.ALIGN_CENTER|wx.TOP,10)

        panel.SetSizer(vbox)

    def build_tips(self):
        self.tips.SetBackgroundColour("#7E4873")
        vbox=wx.BoxSizer(wx.VERTICAL)

        heading=wx.StaticText(self.tips,label="BMI Graph & Personalized Tips")
        heading.SetFont(wx.Font(18,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        vbox.Add(heading,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,15)

        self.figure=Figure(figsize=(6,4))
        self.ax=self.figure.add_subplot(111)
        self.canvas=fc(self.tips,-1,self.figure)
        vbox.Add(self.canvas,0,wx.EXPAND|wx.ALL, 15)

        self.lbl_message=wx.StaticText(self.tips,label="Your friendly message will appear here.")
        self.lbl_message.SetFont(wx.Font(14,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        vbox.Add(self.lbl_message,0,wx.LEFT|wx.TOP,10)

        tips_heading=wx.StaticText(self.tips,label="Health Tips")
        tips_heading.SetFont(wx.Font(16,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
        vbox.Add(tips_heading,0,wx.ALL,10)

        self.lbl_tips=wx.StaticText(self.tips,label="Health Tips will appear here.")
        self.lbl_tips.SetFont(wx.Font(13,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))
        vbox.Add(self.lbl_tips,0,wx.ALL,15)

        self.tips.SetSizer(vbox)

    def calculate_bmi(self,event):
        try:
            h=float(self.txt_height.GetValue())/100
            w=float(self.txt_weight.GetValue())
            self.bmi_value=round(w/(h*h),2)
            self.lbl_bmi_result.SetLabel(f"Your BMI = {self.bmi_value}")
        except:
            wx.MessageBox("Enter valid height and weight","Error")

    def show_graph_and_tips(self,event):
        if self.bmi_value==0:
            wx.MessageBox("Please calculate BMI first","Error")
            return
        self.draw_graph()
        self.show_messages_and_tips()
        self.nb.ChangeSelection(1)

    def draw_graph(self):
        self.ax.clear()
        bmi=self.bmi_value
        self.ax.axvspan(0,18.5,color="#D0E8FF")
        self.ax.axvspan(18.5,24.9,color="#D6F8C3")
        self.ax.axvspan(24.9,29.9,color="#FFF7A6")
        self.ax.axvspan(29.9,100,color="#FFC4B0")
        self.ax.plot(bmi,1,'ko')
        self.ax.text(bmi,1.1,f"Your BMI = {bmi}",ha='center',fontsize=10)
        self.ax.set_ylim(0,2)
        self.ax.set_yticks([])
        self.ax.set_xlabel("BMI Value")
        self.ax.set_title("Your BMI Position")
        self.canvas.draw()

    def show_messages_and_tips(self):
        bmi=self.bmi_value
        gender=self.choice_gender.GetStringSelection()
        if bmi<18.5:
            category= "Underweight"
        elif bmi<24.9:
            category="Normal"
        elif bmi<29.9:
            category="Slightly Overweight"
        else:
            category="Overweight"

        messages={
            "Underweight": ["A bit under the mark — nourishing meals will help!", "You seem underweight — consider boosting calories."],
            "Normal": ["You're in a healthy range — great job!", "Nice! Your BMI is normal."],
            "Slightly Overweight": ["Slightly above — small lifestyle tweaks can help.", "You're close to the healthy range — keep going!"],
            "Overweight": ["Above the healthy range — consider regular exercise.", "Some adjustments in diet and movement can help."]
        }
        self.lbl_message.SetLabel(random.choice(messages[category]))

        tips_text=f"""Category: {category}
Gender: {gender}

• Maintain balanced eating habits
• Aim for regular physical activity
• Ensure enough sleep and hydration"""
        
        self.lbl_tips.SetLabel(tips_text)

if __name__=="__main__":
    app=wx.App()
    w2g()
    app.MainLoop()
