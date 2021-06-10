def fun(a):
	if(a>0):
		res=a+fun(a-1)
		print(res)
	else:
		res=0
	return res

fun(6)		
		