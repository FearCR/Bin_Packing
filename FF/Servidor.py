class servidor:
    def __init__(self,tam):
        self.tam=tam
        self.vmList = []
    def setVm(self, VM):
        self.vmList.append(VM)

    def setNewTam(self, newTam):
        self.tam = newTam

    def getTam(self):
        return self.tam