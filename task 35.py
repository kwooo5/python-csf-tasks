day = input('Enter a day of a week:')
if day in ['monday','tuesday','wednesday','thursday']:
   print('weekday')
elif day == 'friday':
   print ('TGIF')
elif day in ['saturday', 'sunday']:
   print('weekend')
else:
   print('invalid input')
   