### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

# COMMENT KEY: 
# ditto mark (") - indicates 'same as above'
# ; - seperates comments
# () - used to provide examples for clarification 

class CardGame:


  def check_for_ace(self, card): 
    if card.value = 1:                    # equality not assignment (= should be ==)
      return True
    else                                  # needs a colon (else:)
      return False
   

  dif highest_card(self, card1 card2):    # dif should be def; needs a comma between 2nd and 3rd parameter
  if card1.value > card2.value:           # body of the function should be indented
    return card                           # "; card is not defined, presumably should be card1
  else:                                   # "
    return card2                          # "
  


def cards_total(self, cards):             # function should be indented from class
  total                                   # total is not defined, could be assigned 0 to start
  for card in cards:
    total += card.value
    return "You have a total of" + total  # cannot concatenate str and int, use f-string (f"You have a total of {total}"); return should not be part of for loop, return after for loop has finished
  
```
