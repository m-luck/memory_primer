import webbrowser as wb
import ast
file = open("to_learn_from_recent_session.txt", "r")
for line in file:
     urls = ast.literal_eval(line)
     for url in urls:
         wb.open(url,new=2,autoraise=False)
