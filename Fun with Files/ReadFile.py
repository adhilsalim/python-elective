def display_file_content():
  try:
    filename = input("Enter the filename (.txt files): ")
    if not filename.endswith(".txt"):
      filename += ".txt"
    with open(filename, "r") as file:
      content = file.read()
      print(content)
  except FileNotFoundError:
    print(f"Error: {filename} not found!")

if __name__ == "__main__":
  display_file_content()
