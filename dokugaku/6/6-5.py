moji=["The", "fox", "jumped", "over", "the", "fence", "."]
result=" ".join(moji)
## [0: -2] + "." で"."の位置を決めている
result=result[0: -2] + "."
print(result)
