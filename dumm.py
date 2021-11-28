string='13'
dct={'3':'buzz'}
newstr=''
for ch in string:
    if ch.isdigit()==True:
        dw=dct[ch]
        newstr=newstr+dw
    else:
        newstr=newstr+ch
print (newstr)