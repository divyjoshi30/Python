import webbrowser
print("Opening Web-Browser...")
# webbrowser.open("https://www.python.org/", new=1)
# webbrowser.open_new("hhtps://www.google.com/")      #opens new window, if possible
# webbrowser.open_new_tab("https://www.google.com")   #opens new tab, if possible
firefox = webbrowser.get(using='mozilla')
firefox.open_new("https://www.google.com/")
