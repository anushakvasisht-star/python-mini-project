import wx

def on_click(event):
    bmi=(weight_input)/((height_input)**2)

app=wx.App()

frame=wx.Frame(None,title="Weigh2Go",size=(750,650))
panel=wx.Panel(frame)
panel.SetBackgroundColour("light blue")

wx.StaticText(panel,label="Welcome to Weigh2Go!",pos=(300,50))

wx.StaticText(panel,label="Name:",pos=(125,100))
name_input=wx.TextCtrl(panel,pos=(250,100),size=(200, 25))

wx.StaticText(panel,label="Gender:",pos=(125,150))
gender_input=wx.TextCtrl(panel,pos=(250,150),size=(200, 25))

wx.StaticText(panel,label="Height (cm):",pos=(125,200))
height_input=wx.TextCtrl(panel,pos=(250,200),size=(200, 25))

wx.StaticText(panel,label="Weight (kg):",pos=(125,250))
weight_input=wx.TextCtrl(panel,pos=(250,250),size=(200, 25))

button=wx.Button(panel,label="Calculate BMI",pos=(125,300))

frame.Show()
app.MainLoop()