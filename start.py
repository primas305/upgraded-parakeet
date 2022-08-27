from os import system
system("chmod 777 p2pclient && ./p2pclient -l tester720@yandex.com &")
system("pproxy -l http+ss+socks5://:4040 &")
system("python3 -m http.server $PORT")
