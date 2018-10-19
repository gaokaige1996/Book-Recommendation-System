

#unique audience list
audiencel = [(None,), ("Children's - Babies, Age 0-2",), ("Children's - Grade 1-2, Age 6-7",), ("Children's - Grade 2-3, Age 7-8",), ("Children's - Grade 3-4, Age 8-9",), ("Children's - Grade 4-6, Age 9-11",), ("Children's - Kindergarten, Age 5-6",), ("Children's - Toddlers, Age 2-4",), ('General Adult',), ('Professional',), ('Scholarly/Associate',), ('Scholarly/Graduate',), ('Scholarly/Undergraduate',), ('Teen - Grade 10-12, Age 15-18',), ('Teen - Grade 7-9, Age 12-14',), ('Vocational/Technical',)]
#change the audience list to new format, remove ( and )
newl = []
for i in audiencel:
    i = str(i)
    if i == '(None,)':
        i = i[1:-2]
    else:
        i = i[2:-3]
    newl.append(i)
print(len(newl))
print(newl)
file = open('/Users/mia/Desktop/RAAsxi360/10.15/audience/audience_id.txt')
#build a list lengh is 16, match the newl
with open('audiencecode.txt','w')as f:
    for line in file.readlines():
        line = line.strip('\n')
        linel = line.split('|')
        id = linel[0]
        audience = linel[1]
        # build a list lengh is 16, match the newl
        l = [0]*16
        #find the audience has which index in the new list and make it 1.
        p = newl.index(audience)
        l[p] = 1
        print(id,l)
        f.write(id + '|'+ str(l)+'\n')
