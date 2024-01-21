# from tkinter import *
# from tkinter import font

# root = Tk()
# root.title('Font Families')
# fonts=list(font.families())
# fonts.sort()

# def populate(frame):
#     '''Put in the fonts'''
#     listnumber = 1
#     for item in fonts:
#         label = "listlabel" + str(listnumber)
#         label = Label(frame,text=f"{item} X O",font=(item, 40)).pack()
#         listnumber += 1

# def onFrameConfigure(canvas):
#     '''Reset the scroll region to encompass the inner frame'''
#     canvas.configure(scrollregion=canvas.bbox("all"))

# canvas = Canvas(root, borderwidth=0, background="#ffffff")
# frame = Frame(canvas, background="#ffffff")
# vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)

# vsb.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((4,4), window=frame, anchor="nw")

# frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# populate(frame)

# root.mainloop()

# count = 0

# for i in range(5):
#     count = (count + 1) % 2
#     print(count)

[0,0,0.114,0.161,0.031,0.026000000000000002,0.007,0.003,0.111,0.036000000000000004,0.184,0.034,0.005,0.007,0.025,0.076,0.107,0.11900000000000001,0.10200000000000001,0.08700000000000001,0.08600000000000001,0.089,0.088,0.081,0.083,0.081,0.094,0.089,0.12,0.111,0.10300000000000001,0.10400000000000001,0.10400000000000001,0.096,0.099,0.097,0.085,0.096,0.084,0.094,0.095,0.08700000000000001,0.091,0.081,0.08600000000000001,0.081,0.074,0.077,0.077,0.068,0.079,0.063,0.07200000000000001,0.065,0.045,0.06,0.042,0.051000000000000004,0.047,0.033,0.043000000000000003,0.038,0.037,0.033,0.026000000000000002,0.029,0.025,0.019,0.02,0.018000000000000002,0.015,0.015,0.012,0.012,0.011,0.007,0.011,0.005,0.01,0.009000000000000001,0.005,0.008,0.005,0.007,0.005,0.003,0.004,0.004,0.003,0.004,0.005,0.003,0.005,0.003,0.004,0.004,0.003,0.004,0.003,0.003,0.002,0.003,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.001,0.002,0.002,0.002,0.002,0.001,0.002,0.001,0.002,0.002,0.002,0.002,0.001,0.002,0.002,0.001,0.001,0.001,0.001,0.001,0.001,0,0.001,0,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
