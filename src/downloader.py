import webbrowser
import json
import pathlib
#7
index = input('Index? :')
# p = pathlib.Path(fr"C:\Users\owenw\Downloads\{index}").mkdir(parents=True, exist_ok=True)
    
with open('./data/data.json', 'r+') as file:
    data = json.load(file)[int(index)]
    for x in data:
        webbrowser.open_new_tab(x)