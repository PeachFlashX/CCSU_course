import requests
import os
import time
import json
from bs4 import BeautifulSoup
import base64
import binascii
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.backends import default_backend
# import rsa
import re
import six
import jsFunction

os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

with open('setting.json','r',encoding='utf-8') as file:
    reji = json.load(file)

# print(reji)

username = reji['username']
password = reji['password']



session = requests.Session()

session.headers.update({'Accept': 'application/json'})
session.headers.update({'accept-language': 'zh-CN,zh;q=0.9'})
session.headers.update({'cache-control': 'max-age=0'})
session.headers.update({'content-type': 'application/x-www-form-urlencoded'})
session.headers.update({'upgrade-insecure-requests': '1'})
session.headers.update({'referer': 'http://jwxt.jwc.ccsu.cn/jwglxt/xtgl/login_slogin.html'})
session.headers.update({'charset': 'UTF-8'})
session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'})
session.headers.update({'"Host': 'jwxt.jwc.ccsu.cn'})
session.headers.update({'Connection': 'keep-alive'})


res_1 = session.get('http://jwxt.jwc.ccsu.cn/jwglxt/xtgl/login_slogin.html')

soup=BeautifulSoup(res_1.text,'html.parser')

# print(soup.title.string)

data_csrftoken = soup.find('input', attrs={'id': 'csrftoken'})
csrftoken = data_csrftoken['value']

# print(csrftoken)

# print(res_1.status_code)
# print(res_1.headers)
# print(res_1.text)

tm=str(int(time.time()*1000))

reji = 'http://jwxt.jwc.ccsu.cn/jwglxt/xtgl/login_getPublicKey.html?time='+tm+'&_='+tm
# print(reji)

res_2 = session.get('http://jwxt.jwc.ccsu.cn/jwglxt/xtgl/login_getPublicKey.html?time='+tm+'&_='+tm)
# print(res_2.text)

reji=json.loads(res_2.text)

# print(reji['modulus'])



# m_str = base64.b64decode('AJpwG4X0+yMEo77lKy2fMxz3UaNjIiUEKu9Jjw8fLWW4KNqqqgOGtzpcLQ8jd0y1/LGuYSKs2/OlIXaYDzzWvnt5z8WLxeYCPwIYEJQDMDMGTF2IewRme1U/UnPGXAafpwBoJ/fFADSaKKfhU9FYZIBIC/1L/oN3fHAcFw/Br1aj')
# e_str = base64.b64decode('AQAB')
# # e_str=base64.b64decode(reji['exponent']) #返回解码后的二进制数据（文本字符串转换成二进制数据）
# # m_str=base64.b64decode(reji['modulus'])
# print(m_str)
# print(e_str)
# m_hex = binascii.b2a_hex(m_str) #返回二进制数据的十六进制表示（二进制转换成十六进制）
# e_hex = binascii.b2a_hex(e_str)
# print(m_hex)
# print(e_hex)
# e=int(e_hex,16) # 将16进制大端格式字符串转换为大整数(十六进制转换成十进制)
# n=int(m_hex,16)
# print(e)
# print(n)

# modulus = int(base64.b64decode(reji['modulus']).hex(),16)
# exponent = int(base64.b64decode(reji['exponent']).hex(),16)

# pubkey=rsa.RSAPublicNumbers(exponent,modulus).public_key(default_backend())
# key = pubkey.encrypt(password.encode('utf-8'),padding.PKCS1v15()) #使用公钥对明文“abc12345”加密，返回加密后的二进制数据
# print(key)
# print(binascii.b2a_base64(key)) #加密后的二进制转换成 字符串




modulus = reji['modulus']
exponent = reji['exponent']
_modulus = base64.b64decode(modulus).hex()
_exponent = base64.b64decode(exponent).hex()
rsa = jsFunction.RSAKey()
rsa.setPublic(_modulus, _exponent)
pwd_rsa = rsa.encrypt(password)
pwd_byte = bytes.fromhex(pwd_rsa)
pwd_cry = base64.b64encode(pwd_byte).decode('utf-8')
# print(pwd_cry)

data = {
        'csrftoken': csrftoken,
        'language':  'zh_CN',
        'yhm': username,
        'mm': pwd_cry,
        'mm': pwd_cry,
    }

res_3 = session.post('http://jwxt.jwc.ccsu.cn/jwglxt/xtgl/login_slogin.html?time='+str(int(time.time()*1000)),data)
# print(res_3.status_code)
# print(res_3.headers)
# print(res_3.text)


#选/查课信息获取part
res_4 = session.get('http://jwxt.jwc.ccsu.cn/jwglxt//xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default')

# print(res_4.status_code)
# print(res_4.headers)
# print(res_4.text)

soup = BeautifulSoup(res_4.text,'html.parser')
xqh_id = soup.find('input', attrs={'id': 'xqh_id'})['value']
jg_id = soup.find('input', attrs={'id': 'jg_id_1'})['value']
njdm_id = soup.find('input',attrs={'id':'njdm_id'})['value']
njdm_id_1 = soup.find('input',attrs={'id':'njdm_id_1'})['value']
zyh_id = soup.find('input',attrs={'id':'zyh_id'})['value']
zyh_id_1 = soup.find('input',attrs={'id':'zyh_id_1'})['value']
zyfx_id = soup.find('input',attrs={'id':'zyfx_id'})['value']
bh_id = soup.find('input',attrs={'id':'bh_id'})['value']
xbm = soup.find('input',attrs={'id':'xbm'})['value']
xslbdm = soup.find('input',attrs={'id':'xslbdm'})['value']
mzm = soup.find('input',attrs={'id':'mzm'})['value']
xz = soup.find('input',attrs={'id':'xz'})['value']
ccdm = soup.find('input',attrs={'id':'ccdm'})['value']
xsbj = soup.find('input',attrs={'id':'xsbj'})['value']
xkxnm = soup.find('input',attrs={'id':'xkxnm'})['value']
xkxqm = soup.find('input',attrs={'id':'xkxqm'})['value']
kklxdm = soup.find('input',attrs={'id':'kklxdm'})['value']



# print(session.headers)
session.headers.pop('content-type')
session.headers.update({'referer': 'http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default'})
session.headers.update({'x-requested-with': 'XMLHttpRequest'})
# print(session.headers)


# 查所有课part
kspage = 1
jspage = 10
data = {
    'yl_list[0]': '1',
    'rwlx': '2',
    'xkly': '0',
    'bklx_id': '0',
    'sfkkjyxdxnxq': '0',
    'xqh_id': xqh_id,#
    'jg_id': jg_id,#
    'njdm_id_1': njdm_id_1,#
    'zyh_id_1': zyh_id_1,
    'zyh_id': zyh_id,
    'zyfx_id': zyfx_id,
    'njdm_id': njdm_id,
    'bh_id': bh_id,
    'bjgkczxbbjwcx': '0',
    'xbm': xbm,
    'xslbdm': xslbdm,
    'mzm': mzm,
    'xz': xz,
    'ccdm': ccdm,
    'xsbj': xsbj,
    'sfkknj': '0',
    'gnjkxdnj': '0',
    'sfkkzy': '0',
    'kzybkxy': '0',
    'sfznkx': '0',
    'zdkxms': '0',
    'sfkxq': '0',
    'sfkcfx': '0',
    'kkbk': '0',
    'kkbkdj': '0',
    'sfkgbcx': '0',
    'sfrxtgkcxd': '0',
    'tykczgxdcs': '0',
    'xkxnm': xkxnm,
    'xkxqm': xkxqm,
    'kklxdm': '10',
    'bbhzxjxb': '0',
    'rlkz': '0',
    'xkzgbj': '0',
    'kspage': kspage,
    'jspage': jspage,
    'jxbzb': '',
}
# print(data)
res_5=session.post('http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512',data)

# print(res_5.status_code)
# print(res_5.headers)
# print(res_5.text)

all_in_one =[]

reji = json.loads(res_5.text)

courst_count = 0

while len(reji['tmpList'])>0:
    courst_count+=len(reji['tmpList'])
    a = 0
    for a in range(len(reji['tmpList'])):
        all_in_one.append(reji['tmpList'][a])
    kspage += 10
    jspage += 10
    data['kspage']=kspage
    data['jspage']=jspage
    res_5=session.post('http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512',data)
    reji = json.loads(res_5.text)

# print(reji['tmpList'])
# print(len(reji['tmpList']))

# a=0
# for a in range(courst_count):
#     print(all_in_one[a])

#get xkkz_id
res_6 = session.get('http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default')

# print(res_6.status_code)
# print(res_6.headers)
# print(res_6.text)



# with open('k.html','w',encoding='utf-8') as file:
#     file.write(str(res_x.text))

soup = BeautifulSoup(res_6.text,'html.parser')
xkkz_id = soup.find('input', attrs={'id': 'firstXkkzId'})['value']

data_fin = []
data = {
    'rwlx' : '2',
    'xkly' : '0',
    'bklx_id' : '0',
    'sfkkjyxdxnxq' : '0',
    'xqh_id' : xqh_id,
    'jg_id' : jg_id,
    'zyh_id' : zyh_id,
    'zyfx_id' : zyfx_id,
    'njdm_id' : njdm_id,
    'bh_id' : bh_id,
    'xbm' : xbm,
    'xslbdm' : xslbdm,
    'mzm' : mzm,
    'xz' : xz,
    'ccdm' : ccdm,
    'xsbj' : xsbj,
    'sfkknj' : '0',
    'gnjkxdnj' : '0',
    'sfkkzy' : '0',
    'kzybkxy' : '0',
    'sfznkx' : '0',
    'zdkxms' : '0',
    'sfkxq' : '0',
    'sfkcfx' : '0',
    'bbhzxjxb' : '0',
    'kkbk' : '0',
    'kkbkdj' : '0',
    'xkxnm' : xkxnm,
    'xkxqm' : xkxqm,
    'xkxskcgskg' : '0',
    'rlkz' : '0',
    'kklxdm' : '10',#存疑
    'kch_id' : '0AA4AAB7194305E2E0638C28C4DA40C4',#
    'jxbzcxskg' : '0',
    'xkkz_id' : xkkz_id,#
    'cxbj' : '0',
    'fxbj' : '0',
}

a = 0
for a in range(len(all_in_one)):
    data['kch_id'] = all_in_one[a]['kch_id']
    res_7 = session.post('http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html?gnmkdm=N253512',data)
    b = 0
    reji_1 = json.loads(res_7.text)
    for b in range(len(reji_1)):
        reji = {
            'name' : all_in_one[a]['kcmc'],
            'kch_id' : all_in_one[a]['kch_id'],
            'jxb_ids' : reji_1[b]['do_jxb_id'],
            'location' : reji_1[b]['jxdd'],
            'time' : reji_1[b]['sksj'],
        }
        if reji['location'] == '--':
            reji['location'] = '网课'
            reji['time'] = '网课'
        data_fin.append(reji)

# 查单课part
a = 0
for a in range(len(data_fin)):
    print(str(a)+'   '+data_fin[a]['name']+'   '+data_fin[a]['location']+'   '+data_fin[a]['time'])


while 1:
    print('---------------请输入想要选择的课程的前缀编号---------------')
    a = int(input())
    data = {
        'jxb_ids': data_fin[a]['jxb_ids'],
        'kch_id': data_fin[a]['kch_id'],
        # 'kcmc': '(RY000D2406)走进西方音乐 - 1.0 学分',
        # 'rwlx': '2',
        # 'rlkz': '0',
        # 'rlzlkz': '1',
        # 'sxbj': '1',
        # 'xxkbj': '0', 
        'qz': '0',
        # 'cxbj': '0',
        # 'xkkz_id': '216920FAF7755041E0638C28C4DA8BD6',
        'njdm_id': njdm_id,
        'zyh_id': zyh_id,
        # 'kklxdm': '10',
        # 'xklc': '2',
        'xkxnm': xkxnm,
        'xkxqm': xkxqm,
        'jcxx_id': '',  # 如果jcxx_id为空，可以省略
    }
    res_8=session.post('http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512',data)
    reji = json.loads(res_8.text)
    if reji['flag'] == 1:
        print('选择课程'+'"'+data_fin[a]['name']+'"成功')
    else:
        print('选择课程'+'"'+data_fin[a]['name']+'"失败')
        print('错误信息:'+reji['msg'])


# 选课part
data = {
    'jxb_ids': '2fafd050d85c190e3e262e8300db38199ee7a59dcee19fd0379516d61360f7aaf59e45b26ebb3aecdc1a787c07bde93b2b49a38e3b382e5ac07c106da5086f28d39d07262548ad4983ded03d78d4345686902f7dec09395ddc321588eb47e88343188e871b80df66bef22b631d0deabe84d9a031006bcee6f603ed51407087a5',
    'kch_id': '21A81C50E7E0C7E8E0638C28C4DA6C2B',
    # 'kcmc': '(RY000D2406)走进西方音乐 - 1.0 学分',
    # 'rwlx': '2',
    # 'rlkz': '0',
    # 'rlzlkz': '1',
    # 'sxbj': '1',
    # 'xxkbj': '0', 
    'qz': '0',
    # 'cxbj': '0',
    # 'xkkz_id': '216920FAF7755041E0638C28C4DA8BD6',
    'njdm_id': njdm_id,
    'zyh_id': zyh_id,
    # 'kklxdm': '10',
    # 'xklc': '2',
    'xkxnm': xkxnm,
    'xkxqm': xkxqm,
    'jcxx_id': '',  # 如果jcxx_id为空，可以省略
}


res_8=session.post('http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512',data)

print(res_8.status_code)
print(res_8.headers)
print(res_8.text)





# # test part

# res_x = session.get('http://jwxt.jwc.ccsu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default')

# print(res_x.status_code)
# print(res_x.headers)
# print(res_x.text)



# # with open('data_get_xkkzid.html','w',encoding='utf-8') as file:
# #     file.write(str(res_x.text))

# soup = BeautifulSoup(res_x.text,'html.parser')
# reji = soup.find('input', attrs={'id': 'firstXkkzId'})['value']


session.close