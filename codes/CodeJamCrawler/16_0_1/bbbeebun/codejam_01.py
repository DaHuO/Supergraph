def has_completed(mapping):
	count = 0
	for key in mapping:
		count += mapping[key]
	if count == 10:
		return True
	else:
		return False


def update_mapping(current_n, mapping):
	current_n_str = str(current_n)
	for each in current_n_str:
		if mapping[each] == 0:
		 	mapping[each] = 1
	

def counting_sheep(n):
	if n == 0:
		return 'INSOMNIA'
	mapping = {
		'0':0, '1':0, '2':0, 
		'3':0, '4':0, '5':0, 
		'6':0, '7':0, '8':0,
		'9':0
	}
	current_n = n
	update_mapping(current_n, mapping)
	while not has_completed(mapping):
		current_n += n
		update_mapping(current_n, mapping)
	return current_n

i = 1
dataset = [0,1,2,11,1692,213858,999995,292164,265199,1000000,10,663708,25,674735,762196,519439,205639,686594,851051,506636,72961,571071,380018,721364,271918,124,362718,40,779467,125000,9,4,104652,20,999998,34,133688,911210,71670,403183,3,999999,777164,999991,999996,954404,999997,200,771909,535557,621518,246569,816478,12500,854110,434198,610249,562071,679849,999992,5,427795,889527,739756,866179,8,513404,125,211763,408914,1250,225473,541210,687079,839403,6,557598,816751,584871,857249,999993,999994,467549,364901,988598,659695,402255,657006,637531,224284,441246,192103,166,565718,300682,596698,584551,410726,7,90188]
for each in dataset:
	print 'Case #'+str(i) +': ' + str(counting_sheep(each))
	i += 1