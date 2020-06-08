'''
Write a functions which would transform the given phrase (you can assume there is no special characters) such that 
every word's first letter and last letter is capitalized. 
Example:  
input: 'i am palaniappan'
output: 'I AM PalaniappaN'
'''

def first_last_upper(str):
  word_list = str.split(" ") #word_list[i,am,good,in,coding]
  result = []
  for word in word_list:
    length = len(word)
    if length == 1:
      result.append(word.upper())
    else:
      final_word=''
      counter = 0
      for char in word:
        if counter==0:
          final_word += char.upper()
        elif counter == length-1:
          final_word += char.upper()
        else:
          final_word += char
        counter += 1
      result.append(final_word)
    
  return (" ").join(result)
