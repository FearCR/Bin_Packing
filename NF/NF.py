def nextfit(vms,server):
    containers=0
    rem=server
    for x in range(len(vms)):
        if rem>vms[x]:
            rem=rem-vms[x]
        else:
            containers+=1
            rem=c-vms[x]
    return containers

vms=[2,5,4,7,1,3,8]
c=10

print("se se necesitan ",nextfit(vms,c)," Contenedores")
