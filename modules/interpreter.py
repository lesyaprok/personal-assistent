import webbrowser
import wolframalpha
import sys
import re
from urllib import error
from constants import WOLFRAM_ID, messages, errors

def interpreter(command):
  try:
    if "bye" in command or "finish" in command or "exit" in command:
      sys.exit("Goodbye! :)")
    elif "translate" in command:
      text_to_translate = re.search(r"translate (.+)", command).group(1).lower().strip()
      print(messages["OPEN_TRANSLATOR"])
      webbrowser.open_new_tab(f"https://translate.google.com/?text={text_to_translate}&tl=en")
      print(messages["DONE"])
    elif "search" in command:
      query = re.search(r"search (.+)", command).group(1).lower().strip()
      print(messages["OPEN_GOOGLE"])
      webbrowser.open_new_tab(f"https://google.com/search?q={query}")  
      print(messages["DONE"])
    elif "youtube" in command:
      query = re.search(r"youtube (.+)", command).group(1).lower().strip()
      print(messages["OPEN_YOUTUBE"])
      webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
      print(messages["DONE"])
    elif "list" in command:
      filename = "commands_list.txt"
      with open(filename) as f:
        content = "".join(f.readlines())
      print(content)  
    else:
      print(wolfram_alpha(command))
  except ValueError:
    print(messages["UNKNOWN_COMMAND"])

def wolfram_alpha(command):
  try:
    print(messages["THINK"])
    app_id = WOLFRAM_ID
    client = wolframalpha.Client(app_id)
    result = client.query(command)
    answer = next(result.results).text
    return answer
  except error.URLError:
    return errors["CONNECTION_ERROR"]
  except:
    return errors["UNKNOWN_QUESTION"](command)

while True:
  try:
    user_input = input(messages["INPUT"]).strip().lower()
    if not user_input:
      continue
    interpreter(user_input)    
  except KeyboardInterrupt:
    sys.exit(messages["GOODBYE"])  
