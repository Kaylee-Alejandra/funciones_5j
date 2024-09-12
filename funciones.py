print("ejemplo de funciones")
#declaro funciones
def hola():
    print("alguien uso la funcion hola")

def chat(mensa):
        print(f"chat {mensa}")

def ellacontesta(mensa):
    print(f"chatella {mensa}")
def escribenombre(ap,n):
    print(f"tu nombre completo es :{n} {ap}")

def suma(a,b):
    s=a+b
    return s

def resta(c,d):
    r=c-d
    return r

def mult(f,g):
    p=f*g
    return p

def div(k,l):
    w=k/l
    return w

    #llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("luevano ","kaylee ")
print("operacion suma")
c1=int(input("ingresa un numero"))
c2=int(input("ingresa un numero"))
damesuma=suma(c1,c2)
print(f"lasuma de {c1}+ {c2}= {damesuma}")

print("operacion resta")
r1=int(input("ingresa un numero"))
r2=int(input("ingresa un numero"))
dameres=resta(r1,r2)
print(f"la resta de {r1} - {r2}= {dameres}")

print("operacion multiplicacion")
v1=int(input("ingresa un numero"))
v2=int(input("ingresa un numero"))
damemulti=mult(v1,v2)
print(f"la multiplicacion de {v1} * {v2}= {damemulti}")

print("operacion division")
s1=int(input("ingresa un numero"))
s2=int(input("ingresa un numero"))
damediv=div(s1,s2)
print(f"la division de {s1} / {s2}= {damediv}")
