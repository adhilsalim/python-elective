def display_file_content():
  try:
    filename = input("Enter the filename: ")
    with open(filename, "r") as file:
      content = file.read()

      # Count sentences (assuming sentences end with periods)
      num_sentences = content.count(".")

      # Split the content into words
      words = content.split()
      # Count words
      num_words = len(words)

      # Count characters (excluding whitespaces)
      num_chars = len(content.replace(" ", ""))

      # Print the content and counts
      print("\nContent:")
      print(content)
      print("\nNumber of sentences:", num_sentences)
      print("Number of words:", num_words)
      print("Number of characters:", num_chars)
  except FileNotFoundError:
    print("Error: File not found!")

if __name__ == "__main__":
  display_file_content()
