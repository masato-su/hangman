# x,zは引数値が確定しているが、扱いは従来通り。
def value(a,b,c,x=100,z=1000):
	return a+b+c+x+z

#関数への値(a,b,c)を設定。じゃないとa,b,cが処理されない。
#返り値を変数でまとめる
result=value(1,2,3)
print(result)
