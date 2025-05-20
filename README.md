# Lenguaje y Automatas.Tercer Seguimiento
##
Se muestra como se fue desarrollado el tercer seguimiento donde se vio automatas finitos deterministas y no Deterministas. Se implemento programas con ciclos y librerias como fado, sys y time. 

<a id='contents'></a>
## Contenido.
<ul>
<li><a href="#intro">Introdución.</a></li>
<li><a href="#def">Definicion Formal de un Automata.</a></li>
<li><a href="#prom1">Se realizo un programa donde se implemento el automata finito deterministico.</a></li>
<li><a href="#prom2">Programa con la libreria fado</a></li>
<li><a href="#conclusions">Conclusions</a></li>
<li><a href="#reference">Referencias</a></li>
</ul>
  
<a id='intro'></a>
### Introdución.

Un automata es un conjunto de estados + Control → Cambio de
estados en respuesta a una entrada.
<h3><font color="red">Tipo de Control:</font></h3>
<ul>
<li>Deterministico: Para cada entrada, hay solo un estado
al que el automata puede ir desde el estado en que se
encuentre.</li>
<li>No deterministico: Un automata finito es
no-deterministico cuando se permite que el Automata Finito tenga 0 o mas estados siguientes para cada par estado-entrada.</li></ul>

<img style="float: right" 
src="https://automatasylenguajesformales.wordpress.com/wp-content/uploads/2012/02/automatafinitodeterminista2.jpg" 
height="250px" width="600px"
alt="Automata Finito"/>

Si anadimos la propiedad de **no-determinismo** , no añadimos poder al automata. Osea que no podemos definir ningun
lenguaje que no se pueda definir con el automata deterministico.
Con la propiedad de no-determinismo se agrega eficiencia
al describir una aplicacion:
<ul><li>Permite programar soluciones en un lenguaje de mas
alto nivel</li>
<li>Hay un algoritmo para compilar un N-DFA en un DFA y
poder ser ejecutado en una computadora convencional
El diagrama de carpetas y archivos de la aplicación</li></ul>

<a id='def'></a>
### Definicion Formal de un Automata.

Un AF se representa como una 5-tupla: A = (Q, Σ, δ, q0, F).
Donde:
<ol>
<li>Q: Un conjunto finito de estados.</li>
<li>Σ: Un conjunto finito de s´ımbolos de entrada (alfabeto)</li>
<li>q0: El estado inicial/de comienzo.</li>
<li>F: cero o mas´ estados finales/de aceptacion.</li></ol> 

El lenguaje de un automata finito determinista es el conjunto de todas las cadenas que el DFA acepta, dada una cadena (e.g., s1, s2, . . . , sn) el DFA empieza en su estado inicial (e.g., q0), consulta si existe una transicion de q0 con el primer simbolo (s1) a otro estado (e.g., q1) y si existe (i.e., δ(q0, s1) = q1) se mueve al estado descrito en la transicion. Se procesa el siguiente simbolo de la cadena (i.e., s2) y
asi continua y si logra procesar toda la cadena y el estado al que llega es uno de los estados finales, entonces se dice
que el automata acepta esa cadena.

<a id='prom1'></a>
### Se realizo un programa donde se implemento el automata finito deterministico.
El programa que se solicito trata de un asistente telefonico donde se ejecutara un menu acerca de opciones como (queja, hablar con un operador, seguimiento de la queja, etc) 
<img style="float: right" 
src="https://www.muycomputerpro.com/wp-content/uploads/2020/07/python-lenguaje-programacion-popular-cobol.jpg"
height="250px" width="600px"
alt="Automata Finito"/>

<h4>Si te interesa conocer todo el codigo implementado puedes ir a la carpeta y buscar Estados_finitos_Jacqueline</h4>

https://github.com/JacquelineCruzC/Lenguaje-y-Automatas/blob/main/Estados_finitos_Jacqueline.py

<a href="#contents">Ir a Contenido.</a>

<a id='prom2'></a>
### Programa donde se instalo fado en la computadora para poder crear automatas finitos con metodos.

Se realizo un programa en python con la libreria fado, donde el objetivo principal es implementar metodos donde se creara una clase, de esa clase se llamaran metodos como setSigma, setInitial, etc.
<img style="float: right" 
src="https://www.mtp.es/wp-content/uploads/2020/01/python_MTP.jpg"
height="250px" width="600px"
alt="Automata Finito"/>
<h4>Si te interesa conocer todo el codigo implementado puedes ir a la carpeta y buscar Cicloforautomata</h4>

https://github.com/JacquelineCruzC/Lenguaje-y-Automatas/blob/main/Cicloforautomata.py


<a href="#contents">Ir a Contenido.</a>

<a id='conclusions'></a>
### Conclusiones.

Se conocio acerca de los automatas finitos, su implementacion con diferentes metodos o desarrollos del programa. Vimos mas a detalle los automatas finitos deterministas y no deterministas. Y los programas que se vieron anteriormente se desarrollaron paso a paso con ayuda del profesor e implementacion de ideas de los alumnos.

<a href="#contents">Ir a Contenido.</a>

<a id='reference'></a>
### Referencias.

Ciencias Computacionales documento desarrollado por inade
https://posgrados.inaoep.mx/archivos/PosCsComputacionales/Curso_Propedeutico/Automatas/02_Automatas_AutomatasFinitos/Capitulo_2_Automatas_finitos_Curso_Anterior.pdf

Automatas Finitos Deterministas y No Deterministas, Marzo 13 del 2017
https://ricardogeek.com/automatas-finitos-deterministas-y-no-deterministas/

<a href="#contents">Ir a Contenido.</a>
