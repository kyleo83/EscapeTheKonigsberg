class Cipher:

  textToEncode = "TopSecrectOperationBlowUpTheEarthBeginsthisThursdayatnoonPacificDaylightSavingsTime"
  shiftKey = "earth"

  def shiftCipher(textinput, shift):
    while len(shift) < len(textinput):
          shift += shift
    try:
      textinput = textinput.lower()
    except:
      return("Your word must be alphabet characters.")
    result = ""
    i = 0
    for letter in textinput:
      numrep = ord(letter) + (ord(shift[i]) - ord('a'))
      if numrep > ord('z'):
        numrep -= 26
      finalLetter = chr(numrep)
      result += finalLetter
      i += 1
    return result

  def unShiftCipher(textinput, shift):
    while len(shift) < len(textinput):
          shift += shift
    try:
      textinput = textinput.lower()
    except:
      return("Your word must be alphabet characters.")
    result = ""
    i = 0
    for letter in textinput:
      numrep = ord(letter) - (ord(shift[i]) - ord('a'))
      if numrep < ord('a'):
        numrep += 26
      finalLetter = chr(numrep)
      result += finalLetter
      i += 1
    return result