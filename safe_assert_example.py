def simpleInterest(p, t, r):
	print('The principal is', p)
	assert isinstance(p, int) and p > 0, "Principal must be a positive integer"
	print('The time period is', t)
	assert isinstance(t, int) and t > 0, "Time must be a positive integer"
	print('The rate of interest is', r)
	assert isinstance(r, int) and r > 0, "Rate of interest must be a positive integer"
	simpleInterest = (p * t * r) / 100
	print('The Simple Interest', simpleInterest)
	return simpleInterest

simpleInterest(3, 5, 8)
