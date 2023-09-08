import sys

#Initializtion
dest={'':'000','M':'001','D':'010','MD':'011',
      'A':'100','AM':'101','AD':'110','AMD':'111'}
jump={'':'000','JGT':'001','JEQ':'010','JGE':'011',
      'JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
comp={'0':'0101010','1':'0111111','-1':'0111010','D':'0001100',
      'A':'0110000','M':'1110000','!D':'0001101','!A':'0110001',
      '!M':'1110001','-D':'0001111','-A':'0110011','-M':'1110011',
      'D+1':'0011111','A+1':'0110111','M+1':'1110111','D-1':'0001110',
      'A-1':'0110010','M-1':'1110010','D+A':'0000010','D+M':'1000010',
      'D-A':'0010011','D-M':'1010011','A-D':'0000111','M-D':'1000111',
      'D&A':'00000000','D&M':'1000000','D|A':'0010101','D|M':'1010101'}
symbols={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576,
         'R0':0,'R1':1,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
         'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15}

filename=sys.argv[1]
finalname=filename.split('.')[0]

#Clean the file to standard form
fr = open (filename, 'r')
fw = open ('inter.asm', 'w')
for line in fr.readlines():
      i = 0
      for i in range(len(line)):
            if line[i] == '\n':
                  break
            elif line[i:i+2] == '//':
                  break
            elif line[i] == ' ':
                  continue
            else:
                  print(line[i], end='', file=fw)
      if i != 0:
            print('', file=fw)
fr.close()
fw.close()

#collect all symbols
symbolcount=15
addr=-1
fr = open ('inter.asm', 'r')
fr1 = open ('inter.asm', 'r')
for line in fr.readlines():
      addr=addr+1
      if (line[0] == '('):
            if line[1:len(line)-2] not in symbols:
                  symbols[line[1:len(line)-2]]=addr
                  addr=addr-1
for line1 in fr1.readlines():
      if (line1[0] == '@') and (line1[1:len(line1)-1].islower()):
            if line1[1:len(line1)-1] not in symbols:
                  symbolcount=symbolcount+1
                  symbols[line1[1:len(line1)-1]]=symbolcount
fr.close()
fr1.close()

#translate all commands
fr = open ('inter.asm', 'r')
fw = open (finalname+'.hack', 'w')
for line in fr.readlines():
      if line[0] == '@':
            if line[1:len(line)-1].isnumeric():
                  print('0'+bin(int(line[1:len(line)-1]))[2:].zfill(15), file=fw)
            elif line[1:len(line)-1] in symbols:
                  print('0'+(bin(symbols[line[1:len(line)-1]])[2:].zfill(15)), file=fw)
      elif line[0] != '(':
            if '=' in line[:len(line)-1]:
                  dest1=dest[line[:len(line)-1].split('=')[0]]
                  if ';' in line[:len(line)-1]:
                        jump1=jump[line[:len(line)-1].split(';')[1]]
                        comp1=comp[line[:len(line)-1].split('=')[1].split(';')[0]]
                  else:
                        jump1=jump['']
                        comp1=comp[line[:len(line)-1].split('=')[1]]
            else:
                  dest1=dest['']
                  comp1=comp[line[:len(line)-1].split(';')[0]]
                  jump1=jump[line[:len(line)-1].split(';')[1]]
            print('111'+comp1+dest1+jump1, file=fw)

fr.close()
fw.close()