class routemap:
    def __init__(self,routes):
        self.mroutes={}
        self.distances={}
        for start,end,dist in routes:
            if start in self.mroutes:
                self.mroutes[start].append(end)
            else:
                self.mroutes[start]=[end]
    def directcheck(self,st,end):
        if end in self.mroutes[st]:
            return True
        return False 
        
    def get_paths(self, st, en, path=[]):
        if(len(path)>0) or (self.directcheck(st,en)==False):
            path=path+[st]
            if(st==en):
                return [path]
            if st not in self.mroutes:
                return []
            paths=[]
            for n in self.mroutes[st]:
                if n not in path:
                    tmp=self.get_paths(n,en,path)
                    for z in tmp:
                        paths.append(z)
            return paths
        else:
            path=[[st]+[en]]
            return path
        
     
    def routefinder(self,start,end,path=[]):
        st=start.upper()
        en=end.upper()
        path=path+[st]
        if(st==en):
            return [path]
        if st not in self.mroutes:
            return []
        paths=[]
        print("EEE")
        print(self.mroutes[st])
        if end in self.mroutes[st]:
            print("Direct route")
            
            
        for n in self.mroutes[st]:
            if n.upper() not in path:
                tpaths=self.routefinder(n,end,path)
                for p in tpaths:
                    paths.append(p)
        print(path)
        return paths
    
def routes():
    maincities=["Hyderabad","Chennai","Vizag","Vijayawada"]
    n=int(input("Enter total calculations\n"))
    route=[
        ("Hyderabad","Chennai","600"),
        ("Vijayawada","Hyderabad","300"),
        ("Hyderabad","Delhi","1500"),
        ("Anaparthi","Rajahmundry","35"),
        ("Rajahmundry","Vizag","200"),
        ("Rajahmundry","Vijayawada","170"),
        ("Vijayawada","Chennai","450"),
        ("Hyderabad","Vizag","800"),
        ("Vizag","Chennai","900"),
        ("Mahendrawada","Anaparthi","7")
        ]
    rt=routemap(route)
    for i in range(n):
        print(f"{i+1} th calculation ")
        src=input("Enter Source \n")
        de=input("Enter Destination \n")
        allpaths=rt.get_paths(src,de)
        print(f"We found total {len(allpaths)} routes")
        iroutes={}
        for a,b,c in route:
            k=str(a)+";"+str(b)
            iroutes[k]=c
        allc=0
        prefered={}
        for ic in allpaths:
            cost=0
            calcstart=False
            ct=0
            dist=0
            if(True):
                for cz in ic:
                    if(ct!=len(ic) and (calcstart==True)):
                        k=str(precz)+";"+str(cz)
                        dist=dist+int(iroutes[k])
                        print(dist)
                    print(f"{cz} => ")
                    if cz not in maincities:
                        cost=cost+100
                    else:
                        cost=cost+50
                    precz=cz
                    if(calcstart==False):
                        calcstart=True
                
            prefered[allc]=dist
            allc=allc+1
            print(f"Distance of this route is {dist}")
            print(f"Cost of this route is {cost}")
            ct=ct+1
            print("")
            print("")
            print("")
            print("")
            print("")
            
        print("Prefered route is ")
        final=[]
        fc=9999999
        for i in prefered:
            if(prefered[i]<fc):
                fc=prefered[i]
                final=allpaths[i]
        for i in final:
            print(i+"  =>  ")
        print(f"With distance {fc}")
routes();
