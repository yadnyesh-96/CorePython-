import wikipedia 
import random

def get_wiki_summary(name):
  """
  Fetches a summary of the given name from Wikipedia.

  Args:
      name: The name of the person to search for.

  Returns: 
      A string containing the Wikipedia summary of the person, 
      or an informative message if not found.
  """
  try:
    summary = wikipedia.summary(name, sentences=2)
    return summary
  except wikipedia.DisambiguationError as e:
    options = ", ".join(e.options)
    return f"Sorry, there are multiple Wikipedia pages for '{name}'. Did you mean: {options}?"
  except wikipedia.PageError:
    return f"Sorry, I couldn't find any information about '{name}' on Wikipedia."

def main():
  greetings = ["Hi there!", "Hello! How can I help you today?", "What would you like to know?"]

  print(random.choice(greetings))

  while True:
    user_input = input("Who would you like to learn about? (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
      print("See you later!")
      break
    summary = get_wiki_summary(user_input)
    print(summary)

if __name__ == "__main__":
  main()