# Bin Packing  
Para este proyecto se usara una versión imaginando maquinas virtuales y una infraestructura definida.   
**PRIMERA PARTE**
- [x] Investigar que es bin packing
- [x] Programar la solucion optima(Fuerza bruta)

**SEGUNDA PARTE**
- [ ] Programar algoritmo Heuristico en version online (aproximacion)  
**explicacion:** Algoritmo que tiene el problema de poder caer en minimos locales, un nuevo bin se abre si no cabe en los anteriores (first fit)
                 online: llegan solicitudes 1 por 1 no se puede modificar el orden de la lista  

**TERCERA PARTE**
- [ ] Programar algoritmo Heuristico en version offline (aproximacion)  
**explicacion:** Algoritmo que tiene el problema de poder caer en minimos locales (first fit Decreasing o modified FFD)   
                  offonline: se tiene visibilidad sobre toda la lista por lo que se puede modificar  
                  
**CUARTA PARTE**
- [x] Programar algoritmo Metaheuristico (aproximacion)  
**explicacion:** Algoritmos que mediante distintas estrategias intentan evitar el problema de caer en minimos locales(taboo,genetic,annealing)  



## En que consiste el problema de Bin Packing?  

- Items de diferentes tamaños deben ser empacados en un numero finito de contenedores de tamaño fijo de manera que se minimize el numero de contenedores usado. (Combinatorial NP-Hard problem)  
## Como se puede programar la solución aproximada? (con heuristicas offline) 
- **Next-Fit algorithm** Revisar si el item actual cabe en el bin, si si, se pone ahi, si no se empieza en un nuevo bin
- **First-Fit algorithm** Revisar los bons en orden y poner el item en el primer bin que sea lo suficientemente grande para contenerlo. se crea un nuevo bin solo cuando un item no cabe en todos los anteriores.
- **Best-Fit algorithm** Un nuevo item se coloca en el bin donde quepa de manera mas ajustada, si no cabe en ninguno, se crea uno nuevo. (se puede hacer en tiempo O(nlogn) usando un balanced binary tree que contenga los bins ordenados por capacidad restante)
## Como se puede programar la solución aproximada? (con heuristicas online)  
- Puede ayudar ordenar  la lista de items de manera decendiente. (first fit decreasing algorithm) aunque esto no garantiza una solucion optima.
## Como se puede programar la solución aproximada? (con metaheuristicas)   
- Se usó un algoritmo genético, en el cual se intenta evitar caer en mínimos locales creando generaciones de población de un tamaño fijo(cada miembro de la población es una combinación al azar de la lista de vms). Se hace un proceso de "mating" en el cual se combinan los genes de parejas de padres en sus hijos para encontrar soluciones óptimas.
