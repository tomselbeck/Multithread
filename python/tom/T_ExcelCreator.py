
import os 
import xlsxwriter

# Declae Path Varaibles 





serv = "Z:/projects/"
project = "PipelineDev/"
editorial = "editorial/"
plates ="plates/"
nulversie = "nulversie/"
lastpublish ="lastpublish/"
sequences = "sequences/"
fslash = "/"


shotlist =[]
shotdir = {}
shotcount = 0

print ("")
print ("")
print ("")

print ("Dictionary Creator, v001. Written by Tom selbeck")
print ("")

print ("Creating dictionary for following Path:")
lookpath = serv + project + editorial + plates
print lookpath
print ("")
# List the sequence folders  #
seqs = os.listdir(lookpath)

print ("These sequences are present:")
print seqs
print ("")

# list how many sequences there are 
print ("Number of sequences :")
print len(seqs)
print ("")

print ("Creating dictionary")
print ("")




# for every sequence 
for x in xrange(0,len(seqs)):
    lookpath = serv + project + editorial + plates + seqs[x] + fslash
    print lookpath
    # List the shot folders  
    shots = os.listdir(lookpath)
    
    
    # For every shot 
    for i in xrange(0,len(shots)):
        shotlist.extend(shots)
        lookpath = lookpath = serv + project + editorial + plates + seqs [x] + fslash + shots [i]
        print lookpath
        print shots[i]
        # Check the shot lenth 
        length =  len(os.walk(lookpath).next()[2])
        # Add to shot dictionary
        shotdir [shotcount]  = seqs[x],shots[i],length+1000
        shotcount = shotcount + 1


print ("")
print shotdir

print ("")
print ("Dictionary created! Saved it in Shotdir variable")









print shotdir

print ("")
print ("")
print ("")
print ("Writing Excell")




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








