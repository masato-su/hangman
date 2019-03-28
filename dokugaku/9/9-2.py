answer = input('Do you like color?')

with open('fav_color.txt','w',encoding='utf-8') as f:
	f.write(answer)
