import requests
import const

class http_client(object):
    def __init__(self, cookies):
        self._cov_cookies(cookies)
        #转换获取token
    def _cov_cookies(self,cookies):
        cookie = [item["name"] + "=" + item["value"] for item in cookies]
        # join()连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
        const.SUP_HEADERS['cookie'] = ';'.join(item for item in cookie)
        print(const.SUP_HEADERS)
    #get 无参
    def get(self,url):
        return self._get(url,const.SUP_HEADERS)



    def _get(self,url,h):
        r = requests.get(url,headers=h)
        return r



    def _post(self):

        return 0