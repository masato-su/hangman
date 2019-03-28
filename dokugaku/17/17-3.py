import re

moji='The ghost that says boo haunts the loo'
m=re.findall('.oo',moji,re.IGNORECASE)

print(m)
