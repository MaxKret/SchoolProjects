
import math

def create_spiral(strng, op):
  strng=str(strng)
  spiral = []
  strLen = len(strng)

  if op == "en":
    #PAD MESSAGE
    if not math.sqrt(strLen).is_integer():
      M = (math.floor(math.sqrt(strLen)) + 1) ** 2
      for n in range(M-strLen):
        strng += "*"
    else:
      M = strLen
    #FILL ARRAY
    count=0
    for i in range(int(math.sqrt(M))):
        row = []
        for j in range(int(math.sqrt(M))):
            row.append(strng[count])
            count += 1
        spiral.append(row)

  elif op == "de":
    new_strng = list(strng)
    asterickStr = ""

    # create array
    M = (math.ceil(math.sqrt(len(strng))))**2
    dimension = int(math.sqrt(M))
    num_astericks = M - len(strng)
    asterickStr = "*" * num_astericks
    asterickStr = list(asterickStr)

    asterick_array = []
    for i in range (dimension):
        column = []
        for j in range (dimension):
            column.append(0)
        asterick_array.append(column)

    # places "*" going from bottom to top, left to right
    for j in range(dimension):
        for i in range (dimension -1, -1, -1):
            try: 
                asterick_array[i][j] = asterickStr.pop()
            except:
                continue
    
    spiral = []
    for row in asterick_array:
        column = []
        for entry in row:
            if entry != "*":
                column.append(new_strng.pop(0))
            else:
                column.append(entry)
        spiral.append(column)

  else:
    return None

  return spiral

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
  inLst = create_spiral(strng, "en")
  outLst = create_spiral(strng, "en")
  outStr = ""

  outLst = list(zip(*inLst[::-1]))

  for k in range(len(outLst)):
    for m in range(len(outLst[0])):
      if str(outLst[k][m]) != "*":
        outStr += str(outLst[k][m])

  return outStr



# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
  inLst = create_spiral(strng, "de")
  outLst = create_spiral(strng, "de")
  outStr = ""

  rotated_array = list(zip(*inLst[::-1]))
  rotated_array = list(zip(*rotated_array[::-1]))
  outLst = list(zip(*rotated_array[::-1]))

  for k in range(len(outLst)):
    for m in range(len(outLst[0])):
      if str(outLst[k][m]) != "*":
        outStr += str(outLst[k][m])

  return outStr




def main():
  import sys
  # read the strings P and Q from standard input
  inLines_unformatted = sys.stdin.readlines()
  inLines = [entry.strip("\n").strip() for entry in inLines_unformatted]
  encrypt_str = str(inLines[0])
  decrypt_str = str(inLines[1])

  # encrypt the string P
  encrypted_str = encrypt(encrypt_str)
  # decrypt the string Q
  decrypted_str = decrypt(decrypt_str)
  # print the encrypted string of Ps
  sys.stdout.write(encrypted_str+"\n")
  # and the decrypted string of Q
  sys.stdout.write(decrypted_str)

if __name__ == "__main__":
  main()


