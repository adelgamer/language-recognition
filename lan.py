import re #re is library that allowed me to split the text passed to the function as an argument

#initiating the list which is going to store all french words contained in francais.text
french = []
#opening the text file in read mode as file
with open("francais.txt", "r") as file:
  #storing the entrire text in lower case characters in french_text variable
  french_text = file.read().lower()
  #splitting the text into a list of words 'french'
  french = french_text.split()

#initiating the list which is going to store all english words contained in words.text
english = []
#opening the text file in read mode as file
with open("words.txt", "r") as file:
  #storing the entrire text in lower case characters in english_text variable
  english_text = file.read().lower()
  #splitting the text into a list of words 'english'
  english = english_text.split()

class language:
  def recognise_french(text):
    """This function return the percentage of french in the provided text"""
    #converting the text to lower case letters
    text = text.lower()
    #splitting the text into words (all special characters are delimiters) and storing the words inside the   variable words
    words = re.split(r"[\'{}[\]|.,;:!§µ?$<>\"\n\s]", text)

    # Remove empty strings using list comprehension
    words = [word for word in words if word != ""]
    #counting how many word is there and storing the value in word_count
    word_count = len(words)
    #init the score, for every word inside the list of language words adds 1 to the score
    score = 0

    #checking words that are inside the list and adding 1 to the score
    for word in words:
      if word in french:
        score += 1

    #calculating the final score in percentage and avoiding zerodivision error
    try:
      percentage = (score*100)/word_count
      return percentage
    except ZeroDivisionError:
      raise Exception("There is no word to analyse")


  def recognise_english(text):
    """This function return the percentage of french in the provided text"""
    #converting the text to lower case letters
    text = text.lower()
    #splitting the text into words (all special characters are delimiters) and storing the words inside the   variable words
    words = re.split(r"[\'{}[\]|.,;:!§µ?$<>\"\n\s]", text)

    # Remove empty strings using list comprehension
    words = [word for word in words if word != ""]
    #counting how many word is there and storing the value in word_count
    word_count = len(words)
    #init the score, for every word inside the list of language words adds 1 to the scor
    score = 0

    #checking words that are inside the list and adding 1 to the score
    for word in words:
      if word in english:
        score += 1

    #calculating the final score in percentage and avoiding zerodivision error
    try:
      percentage = (score*100)/word_count
      return percentage
    except ZeroDivisionError:
      raise Exception("There is no word to analyse")
    

# while (True):
#   input_text = input("\n\nEnter a text:\n")
#   print("\n" + str(language.recognise_english(input_text)))