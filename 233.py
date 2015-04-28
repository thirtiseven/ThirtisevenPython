233.py
N1 = set('alice')
N2 = set('bob')
N3 = set('clack')
N4 = set('david')
WOOO = N1 | N2 | N3 | N4
YOOO = N1 & N2 & N3 & N4
KONGJI = set('')
YAOQIUDE = set('')
if YOOO != KONGJI :
	print(YAOQIUDE)
elif : (N1 & N2 & N3!= KONGJI):
		YAOQIUDE.update(random.sample(N1 & N2 & N3 , 1))
		YAOQIUDE.update(random.sample(N4 , 1))
		print(YAOQIUDE)
elif : (N4 & N2 & N3!= KONGJI):
		YAOQIUDE.update(random.sample(N4 & N2 & N3 , 1))
		YAOQIUDE.update(random.sample(N1 , 1))
		print(YAOQIUDE)
elif : (N4 & N2 & N1!= KONGJI):
		YAOQIUDE.update(random.sample(N4 & N2 & N1 , 1))
		YAOQIUDE.update(random.sample(N3 , 1))
		print(YAOQIUDE)
elif : (N4 & N1 & N3!= KONGJI):
		YAOQIUDE.update(random.sample(N4 & N1 & N3 , 1))
		YAOQIUDE.update(random.sample(N2 , 1))
		print(YAOQIUDE)
elif : (N1 & N2 != KONGJI):
		if (N3 & N4 != KONGJI):
			YAOQIUDE.update(random.sample(N2 & N1 , 1))
			YAOQIUDE.update(random.sample(N3 & N4 , 1))
			print(YAOQIUDE)
		else :
			YAOQIUDE.update(random.sample(N2 & N1 , 1))
			YAOQIUDE.update(random.sample(N3 , 1))
			YAOQIUDE.update(random.sample(N4 , 1))
			print(YAOQIUDE)
elif : (N3 & N2 != KONGJI):
		if (N1 & N4 != KONGJI):
			YAOQIUDE.update(random.sample(N2 & N3 , 1))
			YAOQIUDE.update(random.sample(N1 & N4 , 1))
			print(YAOQIUDE)
		else :
			YAOQIUDE.update(random.sample(N2 & N3 , 1))
			YAOQIUDE.update(random.sample(N1 , 1))
			YAOQIUDE.update(random.sample(N4 , 1))
			print(YAOQIUDE)
elif : (N1 & N3 != KONGJI):
		if (N2 & N4 != KONGJI):
			YAOQIUDE.update(random.sample(N3 & N1 , 1))
			YAOQIUDE.update(random.sample(N2 & N4 , 1))
			print(YAOQIUDE)
		else :
			YAOQIUDE.update(random.sample(N3 & N1 , 1))
			YAOQIUDE.update(random.sample(N2 , 1))
			YAOQIUDE.update(random.sample(N4 , 1))
			print(YAOQIUDE)
else : 
	YAOQIUDE.update(random.sample(N1 , 1))
	YAOQIUDE.update(random.sample(N2 , 1))
	YAOQIUDE.update(random.sample(N3 , 1))
	YAOQIUDE.update(random.sample(N4 , 1))
	print(YAOQIUDE)