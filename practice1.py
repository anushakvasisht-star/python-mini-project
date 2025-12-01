import wx
import matplotlib.pyplot as plt

bmi=0

def on_click(event):
    global bmi
    h=float(height_input.GetValue())/100
    w=float(weight_input.GetValue())
    bmi=round(w/(h*h),2)
    result.SetLabel(f"Your BMI: {bmi}",)

def plot_bmi_graph(event):
    global bmi
    import matplotlib.pyplot as plt
    categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
    ranges = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]
    colors = ['lightblue', 'lightgreen', 'khaki', 'lightcoral']
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, (start, end) in enumerate(ranges):
        ax.axvspan(start, end, color=colors[i], alpha=0.7)
    ax.plot(bmi, 0.5, 'ko', markersize=12)
    ax.text(bmi, 0.65, f'Your BMI = {bmi:.2f}', 
            ha='center', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1)
    ax.set_xlabel('BMI Value', fontsize=12)
    ax.set_title('Your BMI Position', fontsize=16, fontweight='bold')
    ax.set_yticks([])
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['left'].set_visible(True)
    plt.tight_layout()
    plt.show()

def tips(event):
    global bmi
    if bmi<18.5:
        category="Underweight"
    elif bmi<24.9:
        category="Normal"
    elif bmi<29.9:
        category="Slightly Overweight"
    else:
        category="Overweight"
    
    gen=gender_input.GetValue()
    result2.SetLabel(f"Gender: {gen}")

    result3.SetLabel(f"""You are {category}

• Maintain balanced eating habits
• Aim for regular physical activity
• Ensure enough sleep and hydration """)
                                        

app=wx.App()

frame=wx.Frame(None,title="Weigh2Go",size=(750,750))
panel=wx.Panel(frame)
panel.SetBackgroundColour("#7E4873")

wx.StaticText(panel,label="Welcome to Weigh2Go!",pos=(300,50))

wx.StaticText(panel,label="Name:",pos=(125,100))
name_input=wx.TextCtrl(panel,pos=(250,100),size=(200, 25))

wx.StaticText(panel,label="Gender:",pos=(125,150))
gender_input=wx.TextCtrl(panel,pos=(250,150),size=(200, 25))

wx.StaticText(panel,label="Height (cm):",pos=(125,200))
height_input=wx.TextCtrl(panel,pos=(250,200),size=(200, 25))

wx.StaticText(panel,label="Weight (kg):",pos=(125,250))
weight_input=wx.TextCtrl(panel,pos=(250,250),size=(200, 25))

bmi_button=wx.Button(panel,label="Calculate BMI",pos=(125,300))
bmi_button.Bind(wx.EVT_BUTTON,on_click)
result=wx.StaticText(panel,label="Your BMI:",pos=(250,300))

button_graph=wx.Button(panel,label="Show graph",pos=(125,350))
button_graph.Bind(wx.EVT_BUTTON,plot_bmi_graph)

button_tips=wx.Button(panel,label="Show tips",pos=(250,350))
button_tips.Bind(wx.EVT_BUTTON,tips)
result2=wx.StaticText(panel,label="Gender:",pos=(125,400))
result3=wx.StaticText(panel,label="Tips:",pos=(125,450))

frame.Show()
app.MainLoop()