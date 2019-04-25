# import tkinter
# import time
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# #tkinter._test()        #to test whether the tkinter is working properly, it shows a pop-up windows.
# sttime= time.perf_counter()
# mainWindow=tkinter.Tk()
# mainWindow.title("Hello World!")     #rename the window.
# mainWindow.geometry('640x480-350+100')
# '''sets the resolution geometry(width * height + pixels_from_left + pixels_from_top)
#     geometry(width * height - pixels_from_right - pixels_from_bottom)'''
# mainWindow.mainloop()                #passes the main control to Tk, so that it can execute.
# edtime=time.perf_counter()
# print("Main loop kept opened for {} seconds".format(edtime - sttime))

'''PACK GEOMETRY MANAGER'''

# import tkinter
# mainWindow= tkinter.Tk()
# mainWindow.title("TKINTER Test")
# mainWindow.geometry('640x480')
# label=tkinter.Label(mainWindow, text="Hello World")   #to label inside main window
# label.pack(side="top")
#
# LeftFrame = tkinter.Frame(mainWindow)
# LeftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
#
# rightFrame=tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', fill=tkinter.X, expand=True)
#
# canvas=tkinter.Canvas(LeftFrame, relief='raise',  borderwidth=2)
# canvas.pack(side='left', anchor='n')
# '''Relief will make the windows raised, borderwidth to specify width of border,
#     canvas will be alligned to the left side (line no. 27),
#     fill in pack to fill the specified side (fill=tkinter.Y)
#     for x axis we use fill=tkinter.X, expand=True
#     anchor is used for positioning of the button in pack, its arrangement depends on the allignment of
#     the canvas as it doesn't affect it'''
# button1 = tkinter.Button(rightFrame, text="Button 1")
# button1.pack(side='top')
# button2 = tkinter.Button(rightFrame, text="Button 2")
# button2.pack(side='top')
# button3 = tkinter.Button(rightFrame, text="Button 3")
# button3.pack(side='top')
# mainWindow.mainloop()    #without this the main screen won't appear

'''-----------------------------------GRID GEOMETRY MANAGER-----------------------------------'''
# print("GRID GEOMETRY MANAGER with tkinter")
#
# import tkinter
# mainWindow= tkinter.Tk()
# mainWindow.title("TKINTER Test")
# mainWindow.geometry('640x480-8-200')
#
# label= tkinter.Label(mainWindow, text="Hello World")   #to label inside main window
# label.grid(row=0, column=0)
#
# LeftFrame = tkinter.Frame(mainWindow)
# LeftFrame.grid(row=1, column=1)
#
# rightFrame=tkinter.Frame(mainWindow)
# rightFrame.grid(row=1, column=2, sticky='n')
# '''sticky hels to make the ui more clean by making them stick to their place by pin-pointing
#     their location'''
# canvas= tkinter.Canvas(LeftFrame, relief='raise', borderwidth=2)
# canvas.grid(row=1, column=2)
#
# button1 = tkinter.Button(rightFrame, text="Button 1")
# button1.grid(row=0, column=0)
# button2 = tkinter.Button(rightFrame, text="Button 2")
# button2.grid(row=1, column=0)
# button3 = tkinter.Button(rightFrame, text="Button 3")
# button3.grid(row=2, column=0)
#
# #configure the columns
# mainWindow.columnconfigure(0, weight=1)
# mainWindow.columnconfigure(1, weight=1)
# mainWindow.grid_columnconfigure(2, weight=1)
# '''grid_columnconfigure and columnconigure works the same, we can write any of them,
#     both have same functionality.'''
#
# LeftFrame.config(relief='sunken', borderwidth=1)
# LeftFrame.grid(sticky='ns')
# rightFrame.config(relief='sunken', borderwidth=1)
# rightFrame.grid(sticky='new')
#
# rightFrame.columnconfigure(0, weight=1)
# button2.grid(sticky='ew')
# '''to customize a specific button'''
# mainWindow.mainloop()

'''ADVANCE GUI EXAMPLE'''

