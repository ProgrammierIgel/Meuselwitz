import os
import time



def run(wait: int) -> None:
  while True:
    os.system("cd ./themes/Meuselwitz/ && pdflatex demo.tex")
    os.system("cd ./themes/Meuselwitz/ && bibtex demo")
    os.system("cd ./themes/Meuselwitz/ && pdflatex demo.tex")
    os.system("cd ./themes/Meuselwitz/ && pdflatex demo.tex")


    os.system("cd ./themes/Meuselwitz/ && pdflatex demo2.tex")
    os.system("cd ./themes/Meuselwitz/ && bibtex demo2")
    os.system("cd ./themes/Meuselwitz/ && pdflatex demo2.tex")
    os.system("cd ./themes/Meuselwitz/ && pdflatex demo2.tex")


    time.sleep(wait)


if __name__ == "__main__":
  wait = 30
  try:
    wait = int(os.args[0])
  except:
    wait = 30

  run(wait)
