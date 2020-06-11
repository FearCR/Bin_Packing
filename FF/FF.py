import Servidor
Tam=20
SR=Servidor.servidor(Tam)
vmList=[11,2,15,5,6,17,7]
srList=[]
srList.append(SR)
agregado=False

for i in vmList:
    for j in srList:
        if i<j.getTam():
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