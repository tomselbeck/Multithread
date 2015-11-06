
import os 

 

#import xlsxwriter

# Create a workbook and add a worksheet.
#workbook = xlsxwriter.Workbook('Shotgunlist_v01.xlsx')
#worksheet = workbook.add_worksheet()





# Declae Path Varaibles 

print ("")
print ("")

serv = "Z:/projects/"
project = "PipelineDev/"
platefolder = "editorial/plates/"
fslash = "/"
shotlist =[]
testlist =[100]
shotdir = {}
shotcount = 0




lookpath = serv + project + platefolder
print ("Creating excell based on this path")
print lookpath
print ("")
# List the sequence folders  #
seqs = os.listdir(lookpath)

print ("These sequences are present:")
print seqs
print ("")

# list how many sequences there are 
print ("Thera Are these amounts of sequences :")
print len(seqs)
print ("")

print ("Creating dictionary")
print ("")

# for every sequence 
for x in xrange(0,len(seqs)):
    lookpath = serv + project + platefolder + seqs [x]
    print lookpath
    # List the shot folders  
    shots = os.listdir(lookpath)
    
    
    # For every shot 
    for i in xrange(0,len(shots)):
        shotlist.extend(shots)
        lookpath = lookpath = serv + project + platefolder + seqs [x] + fslash + shots [i]
        print lookpath
        print shots[i]
        # Check the shot lenth 
        length =  len(os.walk(lookpath).next()[2])
        # Add to shot dictionary
        shotdir [shotcount]  = seqs[x],shots[i],length+1000
        shotcount = shotcount + 1





print ("")
print ("")
print ("")
print ("Completed Dictionary :")

# Print finished dictianary 
for t in xrange(0,shotcount):
    print shotdir[t]


print ("")
print ("")
print ("")
print ("Writing Excell")


import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('ShotgunShots.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.

# Start from the first cell. Rows and columns are zero indexed.


# Iterate over the data and write it out row by row.

#worksheet.write(1,0,"Shotno")
worksheet.write(0,0,"Sequence")
worksheet.write(0,1,"Shot Code")
worksheet.write(0,2,"Cut In")
worksheet.write(0,3,"Cut Out")


for h in xrange(0,shotcount):
    #write shotnumbers
   # worksheet.write(h+1,0,h+1)
    #write sequencename
    worksheet.write(h+1,0,shotdir[h][0])
    #write shotname
    worksheet.write(h+1,1,shotdir[h][1])
    #write frame in
    worksheet.write(h+1,2,1001)    
    #write frameout
    worksheet.write(h+1,3,shotdir[h][2])

workbook.close()








