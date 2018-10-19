
file = open('/Users/mia/Desktop/RAAsxi360/10.15/Series/Series_id.txt')
with open('series_vector.txt','w') as f:
    for line in file.readlines():
        line = line.strip('\n')
        line = line.split('|')
        id = line[0]
        series = line[1]
        if series == 'None':
            code = [0]
        else:
            code = [1]
        print(id,code)
        f.write(id + '|'+ str(code) +'\n')
