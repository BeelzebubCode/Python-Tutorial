from pyfiglet import Figlet

def render(text, number_of_styles):
    f = Figlet(font=list_of_styles[number_of_styles-1])
    print(f.renderText(text))

list_of_styles = ["univers", "slant", "linux", "epic", "dotmatrix", "broadway", "3x5"]
text = input("Enter message: ")

for i in range(len(list_of_styles)):
    print(f"{i+1}: {list_of_styles[i]}")

styles = int(input("Enter a number of styles: "))
render(text, styles)
#univers slant linux epic dotmatrix broadway