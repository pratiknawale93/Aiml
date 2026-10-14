print("pratik")

no1=int(input("enter the no :-"))
print(no1)
print(f"the inputed no is {no1}")
print(f"The books has the no : {no1}")


def first_non_repeating_index(s: str) -> int:
  counts = {}

  # Step 1: Count frequency of each character
  for char in s:
    counts[char] = counts.get(char, 0) + 1

  # Step 2: Find the index of the first character with a count of 1
  for index, char in enumerate(s):
    if counts[char] == 1:
      return index

  return -1  # Return -1 if no non-repeating character exists


# Example usage:
text = "geeksforgeeks"
result = first_non_repeating_index(text)
print(f"Index: {result}, Character: {text[result] if result != -1 else 'None'}")


