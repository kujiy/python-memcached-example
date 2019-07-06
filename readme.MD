     python /app/mem.py
     bash /app/memcached-tool.sh
     ll /usr/share/memcached/scripts
     ls /usr/share/memcached/scripts
     apt-get install -y memcache
     apt-get install -y memcached
     bash /app/memcached-tool.sh
     memcached-tool mem:11211 display
     bash /app/memcached-tool.sh
     memcached-tool mem:11211 dump
     memcached-tool mem:11211 dump | sort
     bash /app/memcached-tool.sh
     echo 'flush_all' | nc mem 11211
     bash /app/memcached-tool.sh
     python /app/mem.py
     memcached-tool mem:11211 dump | sort
     memcached-tool mem:11211 dump | wc -l
     date
     watch -n1 "memcached-tool mem:11211 dump | wc -l"
     echo 'flush_all' | nc mem 11211
     python /app/mem.py
     watch -n1 "memcached-tool mem:11211 dump | wc -l"
     python /app/mem.py
     watch -n1 "memcached-tool mem:11211 dump | wc -l"
     watch -n1 "memcached-tool mem:11211 dump "
     python /app/mem.py
     watch -n1 "memcached-tool mem:11211 dump "
     history

# put
```
http://192.168.56.103/a/1
http://192.168.56.103/b/2
```

# get
```
http://192.168.56.103/a       # key=a, value=1
http://192.168.56.103/b       # key=b, value=2
```
