

# native urllib
# 3rd-party requests
import requests
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r=requests.get(url)
        # restful
        # json
        if r.status_code !=200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


        # if r.status_code==200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     return {}
