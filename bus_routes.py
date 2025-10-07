import collections

class Solution:
    def bus_routes(self,routes,source,target):
        if source==target:
            return 0
        
        graph=collections.defaultdict(set)
        queue=collections.deque([(source,0)])

        for bus,route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
        
        visited_stops=set()
        visited_buses=set()

        while queue:
            stop,route_len=queue.popleft()
            if stop==target:
                return route_len
            
            for bus in graph[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                for stop in routes[bus]:
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop,route_len+1))
        return -1

def main():
    routes=[[1,2,7],[3,6,7]]
    obj=Solution()
    res=obj.bus_routes(routes,1,6)
    print("Result:",res)

if __name__=="__main__":
    main()