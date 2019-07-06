#apt-get -y install netcat


#/usr/share/memcached/scripts/memcached-tool
memcached-tool  mem:11211 display
memcached-tool  mem:11211 stats
memcached-tool  mem:11211 dump


echo "stats settings" | nc mem 11211
echo "stats " | nc mem 11211

memcached-tool mem:11211
memcached-tool mem:11211 display
memcached-tool mem:11211 stats 
memcached-tool mem:11211 dump       
echo
echo memcached-tool mem:11211 dump       
echo
echo delete all
echo "$ echo 'flush_all' | nc mem 11211"

echo
echo watch -n1 "memcached-tool mem:11211 dump | wc -l"
