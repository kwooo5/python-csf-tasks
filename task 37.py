month = input('enter month:')
if month in ['februray','march','april','may']:
   print('spring')
elif month in ['june','july','august']:
   print('summer')
elif month in ['september','october', 'november']:
   print('Fall')
elif month in ['december']:
   print('winter')
else:
   print('invalid month')