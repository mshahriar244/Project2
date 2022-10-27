from googletrans import Translator
ts=Translator()
text = input("Enter Your Text:")
output =ts.translate(text,dest="de")
print(output.text)