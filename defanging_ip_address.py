class Solution: 
    def defanging_ip_address(self,ip):
        def_ip=""
        for c in ip:
            if c!=".":
                def_ip+=c
            else:
                def_ip+="[.]"
        return def_ip


def main():
    ip="1.1.1.1"
    obj=Solution()
    res=obj.defanging_ip_address(ip)
    print("Result:",res)

if __name__=="__main__":
    main()