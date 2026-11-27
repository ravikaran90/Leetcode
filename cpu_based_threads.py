import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class CPUBasedThreads:
    def get_info(self,url):
        try:
            parameters={"name":"Ravi"}
            resp=requests.get(url,params=parameters,timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.Timeout:
            print("Timeout")
        except requests.exceptions.HTTPError as err:
            print("Bad Status:",err)
        except requests.exceptions.RequestException as re:
            print("Request Failed:",re)

def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/status/404",
        "https://httpbin.org/delay/2"
    ]
    obj=CPUBasedThreads()
    start=time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures={executor.submit(obj.get_info,url):url for url in urls}

        for future in as_completed(futures):
            try:
                url=futures[future]
                status=future.result()
                print(f"Status: {url} -> {status}")
            except requests.exceptions.RequestException as reqex:
                print("Error:",reqex)
    end=time.perf_counter()
    print(f"Total Time Taken: {end-start:.2f}s")

if __name__=="__main__":
    main()
