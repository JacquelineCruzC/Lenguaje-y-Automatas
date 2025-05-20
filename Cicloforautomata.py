from FAdo.fa import*
from FAdo.reex import *
from FAdo.fio import *
def crea_DFA(ipData,evalua):
    sin_puntos=ipData.replace(".","")
    pun=len(ipData)
    arreglo12 = sin_puntos[:pun]
    comprueba=evalua.replace(".","")
    m3=DFA()
    m3.setSigma(['0','1','2','3','4','5','6','7','8','9'])
    for i in range(len(arreglo12)+1):
        estado=f"q{i}"
        m3.addState(estado)
    m3.setInitial("q0")
    m3.addFinal(f"q{len(arreglo12)}")
    for i in range(len(arreglo12)):
        actual=f"q{i}"
        trans=arreglo12[i]
        siguiente=f"q{i+1}"
        m3.addTransition(actual,trans,siguiente)
        print("Transiciones:")
        print(f"  ({actual}, '{trans}') -> {siguiente}")
    print("Autómata Finito Determinista (DFA) creado:")
    print("Estados:", m3.States)
    print("Estado inicial:", m3.Initial)
    print("Estados finales:", m3.Final)
    print("Ip que proporcionaste:", arreglo12 ,"\n La IP que se va a evaluar:",evalua)
    cadena = "".join(arreglo12)
    print("La comprobacion entre las IP que diste es:" ,m3.evalWordP(comprueba))
