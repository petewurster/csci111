#pw_lab04_CtoFtable.py;
#depencancies: none;
#last edit: 2020-05-27, by pWurster;
#Prints table of Celcius to Fahrenheit from Celcius 0 to 40;

#no vars to declare -- only using temp vars in scope of 'for' loop

#loop over degrees 0 to 40
for celciusDegrees in range (0, 41):
	#print ititial table headers and reprint every dozen lines for readability
	if celciusDegrees % 12 == 0:
		print('Celcius  Fahrenheit')
	#calculate Fahrenheit from Celcius using the usual formula
	fahrenheitDegrees: float = 9/5 * celciusDegrees + 32
	#print each line of table, showing converted value to nearest tenth
	print(f'  {celciusDegrees}\t    {fahrenheitDegrees:.1f}')
