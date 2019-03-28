dict={}

dict={
	'S':'special',
        'A':'better',
        'B':'usually'
}

Choice=input('sentaku!:')

if Choice in dict:
	print(dict[Choice])
	#answer=dict[Choice]
	#print(answer)
else:
	print('miss')
