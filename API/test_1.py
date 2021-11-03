from API.baseapi import BaseApi

class TestDemo(BaseApi):
    def test_demo(self):
        self.request('post',url='/rest/login',json={
  "accountName": "admin",
  "password": "Vayt32IzfiAG/16UBOpEMaV9O6RxlZSZwxQuzRaj4q4=",
  "captcha": "bonr2ee"},
                     headers={'Content-Type': 'application/json'}
                     )
