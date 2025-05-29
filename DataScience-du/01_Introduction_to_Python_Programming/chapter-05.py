# 1. Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
# The find method returns the index of the character you have been searching for.
# String slicing starts at zero and ends at n-1 if n refers to the number of characters.
# String slicing is applied from including up to excluding.

text = "X-DSPAM-Confidence:    0.8475"

pos_n = text.find('0')
x = text[pos_n:]
x_i = float(x)
print(x_i, type(x_i))
