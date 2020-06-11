# Bin Packing  
Para este proyecto se usara una versión imaginando maquinas virtuales y una infraestructura definida.   
- [x] Investigar que es bin packing
- [ ] Programar la solucion optima
- [ ] Encontrar combinaciones de cantidadespara las cuales se necesite mas tiempo para encontrar la solucion
## En que consiste el problema de Bin Packing?  
- Items de diferentes tamaños deben ser empacados en un numero finito de contenedores de tamaño fijo de manera que se minimize el numero de contenedores usado. (Combinatorial NP-Hard problem)  
## Como se puede programar la solución optima?  
- Puede ayudar ordenar  la lista de items de manera decendiente. (first fit decreasing algorithm) aunque esto no garantiza una solucion optima.
- **Next-Fit algorithm** Revisar si el item actual cabe en el bin, si si, se pone ahi, si no se empieza en un nuevo bin
- **First-Fit algorithm** Revisar los bons en orden y poner el item en el primer bin que sea lo suficientemente grande para contenerlo. se crea un nuevo bin solo cuando un item no cabe en todos los anteriores.
- **Best-Fit algorithm** Un nuevo item se coloca en el bin donde quepa de manera mas ajustada, si no cabe en ninguno, se crea uno nuevo. (se puede hacer en tiempo O(nlogn) usando un balanced binary tree que contenga los bins ordenados por capacidad restante)

