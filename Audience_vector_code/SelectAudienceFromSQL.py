import pymssql

conn = pymssql.connect(server='btdigitalsandbox.database.windows.net',
    port = '1433',
    user='Dbadmin@btdigitalsandbox.database.windows.net',
    password='BT!pw0915',
    database='digitalsandbox')
cur = conn.cursor()
cur.execute('SELECT BTkey, AudienceDesc from OMNI')
rows = cur.fetchall()
print('data has extracted from sql')
with open('audience_id.txt','w') as f:
    n = 0
    for i in rows:
        id = i[0]
        audience = i[1]
        f.write(id + '|'+str(audience)+'\n')
        if n%10000 == 0:
            print(n,' is finished')
        n = n + 1

