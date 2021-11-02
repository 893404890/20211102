from API.baseapi import BaseApi

class Test1(BaseApi):
    def test_1(self):
        self.request('post',url='http://120.133.67.133:20007/rest/login',json={
  "accountName": "admin",
  "password": "Vayt32IzfiAG/16UBOpEMaV9O6RxlZSZwxQuzRaj4q4=",
  "captcha": "bonr2ee"},
                     headers={'Content-Type': 'application/json'}
                     )
