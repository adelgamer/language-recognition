import re

french = []
with open("francais.txt", "r") as file:
  french_text = file.read().lower()
  french = french_text.split()

english = []
with open("words.txt", "r") as file:
  english_text = file.read().lower()
  english = english_text.split()


def recognise_french(text):
  text = text.lower()
  words = re.split(r"[\'{}[\]|.,;:!§µ?$<>\"\n\s]", text)
  
  # Remove empty strings using list comprehension
  words = [word for word in words if word != ""]
  word_count = len(words)
  score = 0
  
  for word in words:
    if word in french:
      score += 1
  
  try:
    percentage = (score*100)/word_count
    return percentage
  except ZeroDivisionError:
    return "blank"


def recognise_english(text):
  text = text.lower()
  words = re.split(r"[\'{}[\]|.,;:!§µ?$<>\"\n\s]", text)
  # Remove empty strings using list comprehension
  words = [word for word in words if word != ""]
  word_count = len(words)
  score = 0
  
  for word in words:
    if word in english:
      score += 1
  
  try:
    percentage = (score*100)/word_count
    return percentage
  except ZeroDivisionError:
    return "blank"
    

# while (True):
#   input_text = input("\n\nEnter a text:\n")
#   print("\n" + str(recognise_english(input_text)))