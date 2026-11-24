import requests
import threading

def get_data(url):
    parameters={"name":"Ravi"}
    try:
        resp=requests.get(url,params=parameters,timout=10)
        resp.raise_for_status()
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.HTTPError as err:
        print("Bad Status:",err)
    except requests.exceptions.RequestException as re:
        print("Request Failed:,re")
    return None

def main():
    url = "https://httpbin.org"
    s=threading.Thread(target=get_data,args=(url,))
    s.start()
    s.join()

if __name__=="__main__":
    main()
