music={}

music = {
	'MR':'sign',
	'SE':'tekito---',
	'none':'mohayananimonashi'
}

answer=input('Do you BestSinger?:')

if answer in music:
	print(music[answer])
else:
	print('対象なし')
