import pylibmc
db = pylibmc.Client([mem], binary=True,
                     behaviors={"tcp_nodelay": True,
                                "ketama": True})


db.set('name', '太郎')
db.get('name')

for i in range(100):
  db.set('key'+str(i), "data"+str(i))

for i in range(100):
  print("key="+str(i)+"=")
  res = db.get('key'+str(i))
  print("      "+res)
#####################################
##### with tmeout
if 1:
  for i in range(1000):
    db.set('us-wether-'+str(i), "timeout-"+str(i), time=i)

for i in range(1000):
  print("key="+str(i)+"=")
  res = db.get('us-wether-'+str(i))
  print("      "+res)

