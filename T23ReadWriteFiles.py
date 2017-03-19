'''
fw = open('T23Sample.txt','w')
fw.write('write some stuff in the text files\n')
fw.write('Good Tuna\n')
fw.close()
'''

fr = open('T23Sample.txt','r')
text = fr.read()
print(text)
fr.close()


