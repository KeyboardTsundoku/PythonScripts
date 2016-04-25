import os
import subprocess
import sys

# make sure to check if the file exists on directory and is .tex
tex = str(sys.argv[1]) 

assert tex.endswith(".tex")

print("the latex file is: ", tex)

subprocess.call(["latexmk", "-pdf", tex])

source = tex[:-4] + ".pdf"
print("the source is: ", source)
destination = os.path.expanduser('~') + "/Dropbox/Research/My Papers/" + source 
print("the destination is: ", destination)

#lists = os.listdir(destination)
#print(lists)
try:
  os.remove(destination)
except OSError:
  pass
os.rename(source, destination)
subprocess.call(["latexmk", "-c"])
