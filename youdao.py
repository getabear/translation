import requests
import json
import time
import random
import hashlib
class youdao:
    def fun(self,i):     #返回值为英文的对应中文   i为要翻译的英文
        data={'i': 'nice to meet you',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'15750273475230',
        'sign':'cf4fc6adf742fb9e61b0522bec6370c2',
        'ts': '1575027347523',
        'bv': '710f3e24cb0088b9d9ea448919deb3bb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
        }
        url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        head = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Content-Length':'200',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Host':'fanyi.youdao.com',
            'Origin':'http://fanyi.youdao.com',
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=862583056@10.108.160.18; JSESSIONID=aaafWlKTZTlC65cdT626w; OUTFOX_SEARCH_USER_ID_NCOO=532446634.82282144; ___rl__test__cookies=1575027347521'
        }
        #此处是在js代码中查找salt找到的
        # r = "" + (new Date).getTime(),
        # i = r + parseInt(10 * Math.random(), 10);
        # return {
        # ts: r,
        # bv: t,
        # salt: i,
        # sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
        ts=int(time.time()*1000)
        salt=str(ts+random.randint(1,10))
        flowerStr="n%A-rKaT5fb[Gy?;N5@Tj"
        client = "fanyideskweb"
        sign=hashlib.md5((client+i+salt+flowerStr).encode('utf-8')).hexdigest()
        s=requests.session()
        data['i']=i
        data['client']=client
        data['salt']=salt
        data['ts']=ts
        data['sign']=sign
        # print(data)
        r=s.post(url=url,data=data,headers=head)
        # print(r.text)
        result=json.loads(r.text)
        return result['translateResult'][0][0]['tgt']

