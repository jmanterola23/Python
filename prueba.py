def my_sort(line):
    line_fields = line.strip().split(';')
    amount = float(line_fields[2])
    return amount



def concatenar_archivos(file1, file2):
    f1 = open(file1)
    f1_contents = f1.read()
    f1.close()

    f2 = open(file2)
    f2_contents = f2.read()
    f2.close()

    f3 = open("concatenated.txt", "w") # open in `w` mode to write
    f3.write(f1_contents + "\n" + f2_contents) # concatenate the contents
    f3.close()




arch1 ='ar1.txt'
arch2 ='ar2.txt'


concatenar_archivos(arch1,arch2)

fp = open('concatenated.txt')
contents = fp.readlines()
  
contents.sort(key=my_sort)
textfile = open('concatenated.txt','w') 
for line in contents:
    textfile.write(line + "\n" )
textfile.close()
fp.close()
  

