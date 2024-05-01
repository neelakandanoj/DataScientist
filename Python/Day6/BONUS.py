contents=['loreasihiuaccncdasuisdhc','wdwSDAECWECWEWAE','SEDCWEFCFWEFWEFWAEQWEFVAERFER']
FILE=['1.txt','b.txt','c.txt']

for i,j in zip(contents,FILE):
    file=open(j,'w')
    file.writelines(i)
file.close()