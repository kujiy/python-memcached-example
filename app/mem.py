import memcache

db = memcache.Client(['mem:11211'])

db.set('name', '太郎')
db.get('name')

#for i in range(100):
#  db.set('key'+str(i), "data"+str(i))
#
#for i in range(100):
#  print("key="+str(i)+"=")
#  res = db.get('key'+str(i))
#  print("      "+res)
#####################################
##### with tmeout
if 1:
  for i in range(20):
    db.set('us-wether-'+str(i), "timeout-"+str(i), time=i)

for i in range(20):
  print("us-wether="+str(i)+"=")
  res = db.get('us-wether-'+str(i))
  print("      "+res)

