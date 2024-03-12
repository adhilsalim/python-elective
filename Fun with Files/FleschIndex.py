def count_sentences(text):
  return text.count(".")

def count_words(text):
  return len(text.split())

def count_characters(text):
  return len(text.replace(" ", ""))

def count_syllables(text):
  vowels = "aeiouAEIOU"
  syllables = 0
  
  for word in text.split():
    for vowel in vowels:
      syllables += word.count(vowel)
    for ending in ["es", "ed", "e"]:
      if word.endswith(ending):
        syllables -= 1
    if word.endswith("le"):
      syllables += 1

  return syllables

def display_file_content():
    try:
        filename = input("Enter the filename: ")
        with open(filename, "r") as file:
            content = file.read()
            num_sentences = count_sentences(content)
            num_words = count_words(content)
            num_chars = count_characters(content)
            total_syllables = count_syllables(content)

            flesch_index = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (total_syllables / num_words)
            level = "Very Confusing" if flesch_index < 30 else "Confusing" if flesch_index < 50 else "Difficult" if flesch_index < 60 else "Fairly Difficult" if flesch_index < 70 else "Standard" if flesch_index < 80 else "Fairly Easy" if flesch_index < 90 else "Easy"

            # Print the content and analysis results
            print("\nContent:")
            print(content)
            print("\nNumber of sentences:", num_sentences)
            print("Number of words:", num_words)
            print("Number of characters:", num_chars)
            print("Total syllables (estimated):", total_syllables)
            print("Flesch Index:", flesch_index)
            print("Reading level:", level)
    except FileNotFoundError:
        print("Error: File not found!")

if __name__ == "__main__":
  display_file_content()
