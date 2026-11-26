from urllib.parse import urlparse, parse_qs, parse_qsl, quote

class GetInfo:
    def get_info(self,url):
        info=urlparse(url)
        print(info)
        print("Query Parameters:",info.query)
        print("Netloc:",info.netloc)
        print("Path:",info.path.strip("/").split("/")[1])

def main():
    url="https://example.com:8080/version/v1?name=Ravi&class=1"
    obj=GetInfo()
    info=obj.get_info(url)

if __name__=="__main__":
    main()
