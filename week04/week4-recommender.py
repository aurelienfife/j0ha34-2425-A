
late = input('Are you late?')
rain = input('Is it raining?')
faraway = input('Are you going far?')


if late=='yes' and rain == 'yes' and faraway == 'yes':
    print('Take a flight')
elif late=='yes' and rain == 'yes' and faraway == 'no':
    print('Take a bus')
elif late=='no' and rain == 'yes':
    print('Take a canoe or swim')
elif late=='no' and rain == 'no' and faraway == 'yes':
    print('Ride a bicycle')
else:
    print('Just walk')

