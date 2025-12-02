import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

bmi = 0
canvas = None

def on_click(event):
    global bmi
    h = float(height_input.GetValue()) / 100
    w = float(weight_input.GetValue())

    bmi = round(w / (h * h), 2)
    result.SetLabel(f"Your BMI: {bmi}")

def plot_bmi_graph(event):
    global bmi, canvas
    
    if canvas:
        canvas.Destroy()
    
    categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
    ranges = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]
    colors = ['lightblue', 'lightgreen', 'khaki', 'lightcoral']
    
    fig = Figure(figsize=(7, 5))
    ax = fig.add_subplot(111)
    
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
    fig.tight_layout()

    canvas = FigureCanvas(panel, -1, fig)
    graph_sizer.Add(canvas, 1, wx.EXPAND | wx.ALL, 10)
    panel.Layout()

def tips(event):
    global bmi
    
    if bmi < 18.5:
        category = "Underweight-Consider gaining some weight with nutritious food"
    elif bmi < 24.9:
        category = "Normal- You are fit!"
    elif bmi < 29.9:
        category = "Slightly Overweight- Consider light exercise and balanced diet"
    else:
        category = "Overweight- Consider a healthier lifestyle with diet and exercise"
    
    gen = gender_input.GetValue()
    result2.SetLabel(f"Gender: {gen}")

    result3.SetLabel(f"""You are {category}

• Maintain balanced eating habits
• Aim for regular physical activity
• Ensure enough sleep and hydration""")

app = wx.App()
frame = wx.Frame(None, title="Weigh2Go", size=(750,900))
panel = wx.Panel(frame)
panel.SetBackgroundColour("#7E4873")

main_sizer = wx.BoxSizer(wx.VERTICAL)

# Title
title = wx.StaticText(panel, label="Welcome to Weigh2Go!")
main_sizer.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 20)

# Form section
form_sizer = wx.BoxSizer(wx.VERTICAL)

row1 = wx.BoxSizer(wx.HORIZONTAL)
row1.Add(wx.StaticText(panel, label="Name:"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
name_input = wx.TextCtrl(panel, size=(200, 25))
row1.Add(name_input, 0, wx.ALL, 5)

row2 = wx.BoxSizer(wx.HORIZONTAL)
row2.Add(wx.StaticText(panel, label="Gender:"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
gender_input = wx.TextCtrl(panel, size=(200, 25))
row2.Add(gender_input, 0, wx.ALL, 5)

row3 = wx.BoxSizer(wx.HORIZONTAL)
row3.Add(wx.StaticText(panel, label="Height (cm):"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
height_input = wx.TextCtrl(panel, size=(200, 25))
row3.Add(height_input, 0, wx.ALL, 5)

row4 = wx.BoxSizer(wx.HORIZONTAL)
row4.Add(wx.StaticText(panel, label="Weight (kg):"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
weight_input = wx.TextCtrl(panel, size=(200, 25))
row4.Add(weight_input, 0, wx.ALL, 5)

form_sizer.Add(row1)
form_sizer.Add(row2)
form_sizer.Add(row3)
form_sizer.Add(row4)

main_sizer.Add(form_sizer, 0, wx.ALL, 20)

# Button row
button_sizer = wx.BoxSizer(wx.HORIZONTAL)

bmi_button = wx.Button(panel, label="Calculate BMI")
bmi_button.Bind(wx.EVT_BUTTON, on_click)
button_sizer.Add(bmi_button, 0, wx.ALL, 10)

result = wx.StaticText(panel, label="Your BMI:")
button_sizer.Add(result, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)

main_sizer.Add(button_sizer)

# Graph + Tips buttons
btn2_sizer = wx.BoxSizer(wx.HORIZONTAL)

button_graph = wx.Button(panel, label="Show graph")
button_graph.Bind(wx.EVT_BUTTON, plot_bmi_graph)
btn2_sizer.Add(button_graph, 0, wx.ALL, 10)

button_tips = wx.Button(panel, label="Show tips")
button_tips.Bind(wx.EVT_BUTTON, tips)
btn2_sizer.Add(button_tips, 0, wx.ALL, 10)

main_sizer.Add(btn2_sizer)

result2 = wx.StaticText(panel, label="Gender:")
result3 = wx.StaticText(panel, label="Tips:")

main_sizer.Add(result2, 0, wx.LEFT | wx.TOP, 20)
main_sizer.Add(result3, 0, wx.LEFT | wx.TOP, 10)
main_sizer.Add((0, 75))   # adds vertical space before graph


# Graph area sizer
graph_sizer = wx.BoxSizer(wx.VERTICAL)
main_sizer.Add(graph_sizer, 1, wx.EXPAND | wx.ALL, 10)

panel.SetSizer(main_sizer)

frame.Show()
app.MainLoop()
