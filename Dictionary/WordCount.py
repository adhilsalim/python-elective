def word_count(sentence):
  # Convert the sentence to lowercase and split it into words. Output is a list of words.
  words = sentence.lower().split()

  # Create an empty dictionary to store the word frequencies.
  word_counts = {}

  # Iterate through each word in the sentence.
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  # Return the dictionary containing the word frequencies.
  return word_counts

# Get the sentence from the user. Remove any periods and commas.
sentence = input("Enter a sentence: ").replace(".", "").replace(",", "")

# Get the word count.
word_frequencies = word_count(sentence)

print(word_frequencies)
