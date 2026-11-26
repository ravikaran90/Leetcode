import requests
import json

class GetInfo:
    def get_info(self,url):
        parameters={"name":"Ravi"}
        try:
            resp=requests.get(url,params=parameters,timeout=10)
            #print(json.dumps(resp.json(),indent=2))
            #print(resp)
            #print(resp.text)
            #print(resp.content)
            resp.raise_for_status()
            resp_json=resp.json()
            headers=resp_json['headers']
            method=resp_json['method']
            return headers

        except requests.exceptions.Timeout:
            print("Timeout")
        except requests.exceptions.HTTPError as err:
            print("Bad Status:",err)
        except requests.exceptions.RequestException as re:
            print("Status Failed:",re)

def main():
    url = "https://httpbin.org/get"
    obj=GetInfo()
    response=obj.get_info(url)
    print("Host:",response.get('Host'))
    print("Encoding:",response.get('Accept-Encoding'))
    print("User Agent:",response.get('User-Agent'))

if __name__=="__main__":
    main()
