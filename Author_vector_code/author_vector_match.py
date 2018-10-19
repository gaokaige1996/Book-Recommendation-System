
import pandas as pd
#build a dictionary each author is a key, value is the famouse group his or her in
df = pd.read_csv('/Users/mia/Desktop/RAAsxi360/10.15/author_match_all.csv',encoding='latin-1',index_col='Unnamed: 0')
df = df.reset_index()
df['Name'] = df['Unnamed: 1'].apply(lambda x: x.replace(" ", "").replace(',',''))
df = df.set_index('Name')
del df['Unnamed: 1']
dic  = df.to_dict()['index']

#match the key in dictionary and actual author of each book
#transfer the book author to their famouse group
#transfer it to vector
#for those books whose author doesn't exist in famous group(has no checkout information in past three years. )
# we identify those author as group 1, which is least famous group
file = open('/Users/mia/Desktop/RAAsxi360/10.15/author_id.txt')
with open('allbook_author_vector.txt','w') as f:
    for line in file.readlines():
        line = line.strip('\n')
        line = line.split('|')
        id = line[0]
        author = line[1].split(';')
        authorl = [0]*10
        if len(author) > 0:
            for i in author:
                i = i.replace(' ','').replace(',','')
                if i in dic:
                    value = dic[i]
                    authorl[value-1] = 1
                else:
                    value =1
                    authorl[value - 1] = 1
        else:
            print('no author',id,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        print(id,authorl)
        f.write(id + '|' +str(authorl)+'\n')