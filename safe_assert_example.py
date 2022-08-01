def simpleInterest(p,t,r):
	print('The principal is', p)
	assert isinstance(p, int) and p>0, "Error Principle must be an positive value integer"
	print('The time period is', t)
	assert isinstance(t, int) and t>0, "Error Time must be a positive value integer"
	print('The rate of interest is',r)
	assert isinstance(r, int) and r>0, "Error Rate of interest must be a positive value integer"
	simpleInterest = (p * t * r)/100
	print('The Simple Interest is', simpleInterest)
	return simpleInterest

simpleInterest(3, 5 , 8)
