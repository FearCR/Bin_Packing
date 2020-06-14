def perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]



def VM_allocate(vms, server_capacity):
    servers=1
    print(vms)
    rem=server_capacity
    for i in range(len(vms)):
        if rem>=vms[i]:
            rem=rem-vms[i]
        else:
            servers+=1
            rem=server_capacity-vms[i]
    return servers



if __name__ == '__main__':
    VM_list=(4, 8, 1, 4, 2, 1)
    server_capacity=10
    min_bins=999999999
    order=[]
    for i in perms(VM_list):
        temp=VM_allocate(i,server_capacity)
        print(temp)
        if min_bins>temp:
            min_bins=temp
            order=i
    print ("se necesita un minimo de ", min_bins,"servidores de capacidad",server_capacity,"en el orden",order)
    exit()
