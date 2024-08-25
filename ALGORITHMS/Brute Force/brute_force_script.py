import itertools
import string
import pdb  

# define the charset to be used
# this is a combination of lowercase letters and digits
# charset = string.ascii_lowercase + string.digits

#define our password to be cracked
#On real scenarios, this would be unknown and the main goal of the script
# password = "abc"


def get_charset(options):
  charset = ''
  if '1' in options:
        charset += string.ascii_lowercase
  if '2' in options:
      charset += string.digits
  if not charset:
      raise ValueError("Invalid input")
  return charset
  
def brute_force(password, charset, keywords):
  # pdb.set_trace()
  if keywords:    
    for keyword in keywords:
      print(f"Trying {keyword}")
      if keyword == password:
        print(f"Password has been cracked! It was {keyword}")
        return keyword
      
    for keyword_combination in itertools.permutations(keywords):
      attempt = "".join(keyword_combination)
      print(f"Trying {attempt}")
      if attempt == password:
        print(f"Password has been cracked! It was {attempt}")
        return attempt
      
  for length in range(1, len(password)+1):
    for attempt in itertools.product(charset, repeat=length):
      attempt = "".join(attempt)
      print(f"Trying {attempt}")
      if attempt == password:
        print(f"Password has been cracked! It was {attempt}")
        return attempt
      
  print("Password not found")
  print("- - - - - ")
  print("- - - -  ")
  print("- - -  ")
  print("- -  ")
  print("- ")
  
  return ("Password not found")

if __name__ == "__main__":
  
  while True:
    password = input("Enter the password to crack: ")
    print("Choose charset options (you can combine them):")
    print("1: Lowercase letters")
    print("2: Digits")
    charset_options = input("Enter your choices (e.g., '1', '2', or '12'): ")

    try:
      charset = get_charset(charset_options)
    except ValueError as e:
      print(e)
      continue
    
    keywords_input = input("Enter possible keywords separated by commas (e.g., first name, last name, year of birth) or leave empty: ")
    keywords = [keyword.strip() for keyword in keywords_input.split(',')] if keywords_input else []
    
    brute_force(password, charset, keywords)

    again = input("Type 'exit' to quit or press Enter to run again: ")
    if again.lower() == 'exit':
      break






