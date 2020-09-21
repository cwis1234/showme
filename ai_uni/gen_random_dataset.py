import numpy as np
import pickle

def generate(R,dimension=10,N=1000):
	alpha = 0.1
	disp = alpha*R
	disp = disp**2
	tw = np.random.uniform(-R,R,size=[dimension])
	tb = np.random.uniform(-R,R)

	x = np.zeros([N,dimension])
	y = np.zeros([N])

	for i in range(N):
		x[i] = np.random.uniform(-R,R,size=[dimension])
		tmpy = np.dot(tw.T,x[i]) + tb
		y[i] = np.random.normal(tmpy,disp)

	a = int(0.85*N)
	b = int(0.05*N)
	c = int(0.1*N)
	train_input = x[0:a]
	train_target = y[0:a]
	dev_input = x[a:a+b]
	dev_target = y[a:a+b]
	test_input = x[a+b:a+b+c]
	test_target = y[a+b:a+b+c]

	with open('myrandomdatainput.pkl','wb') as f:
		pickle.dump(x,f,pickle.HIGHEST_PROTOCOL)
	with open('myrandomdatatarget.pkl','wb') as f:
		pickle.dump(y,f,pickle.HIGHEST_PROTOCOL)

	return tw,tb,train_input,train_target,dev_input,dev_target,test_input,test_target
