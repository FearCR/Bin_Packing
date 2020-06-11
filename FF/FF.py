import Servidor
Tam=10
SR=Servidor.servidor(Tam)
vmList=[2, 1, 1, 2, 3, 9, 1, 7, 6, 8, 5, 6, 1, 2, 8, 8, 7, 6, 2, 8, 4, 9, 6, 2, 2, 6, 7, 8, 6, 8, 7, 2, 4, 1, 2, 2, 7, 3, 1, 3, 6, 5, 7, 6, 9, 9, 6, 7, 1, 8, 3, 4, 2, 6, 3, 6, 5, 3, 7, 5, 3, 5, 9, 8, 8, 2, 9, 3, 8, 2, 1, 8, 1, 7, 2, 2, 4, 3, 9, 2, 5, 3, 8, 3, 2, 4, 7, 4, 2, 4, 8, 6, 8, 8, 2, 6, 4, 1, 2, 7]
srList=[]
srList.append(SR)
agregado=False

for i in vmList:
    for j in srList:
        if i<=j.getTam():
            newTam=j.getTam()-i
            j.setVm(i)
            j.setNewTam(newTam)
            agregado = True
            break
    if agregado == False:
        newSR = Servidor.servidor(Tam)
        newTam = newSR.getTam() - i
        newSR.setVm(i)
        newSR.setNewTam(newTam)
        srList.append(newSR)
    else:
        agregado = False

print("Se ocupan: ",len(srList), "servidores")

cant=0
for j in srList:
    cant=cant+1
    print("Servidor ",cant," con: ")
    print(j.vmList)
    print("Tamaño disponible: ",j.getTam())