def value(x):
	try:
		return float(x)
	except ValueError:
		print('エラー')
result=value('55.0')
print(result)
