import sys

def next_char(c,shift):
  c = c.upper()
  start = ord('A')
  if c.isalpha():
    if ord(c) - 26 >= start:
      return chr((ord(c) - 26) + shift)
    return chr(ord(c) + shift)

output = ""
char_counter = 0
spaces = 0
amount_shifted = int(sys.argv[1])

print("Type 'q' and press enter to exit/finalize")

for line in sys.stdin:
  if line.rstrip() == "q":
    break
  for i in line:
    if next_char(i,amount_shifted) != None:
      char_counter+=1
      output+=next_char(i,amount_shifted)
      if char_counter % 5 == 0:
        output += " "
        spaces +=1
        if spaces != 0 and spaces % 10 == 0:
          output+="\n"
      
print(output)
