fichero = open('0_palabras_todas.txt', 'r',encoding="utf-8") #en las siguientes lineas lee un txt y crea una lista con todas las palabras
diccionario=[]
for linea in fichero: 
    linea = linea.replace('\n', '')
    if len(linea)==5:
        diccionario.append(linea)
#diccionario=["patas","copos","abran","bebed","cerra","donan","acero","corto","aireo","edita","falle","gafas","habed","irian","japon","kenia",
# "labia","mecen","niños","pesad","pleno","quito","ramos","sabia","tacos","usate","vacan","yemen","zarca"]
def eligePalabraDiccionario(nuevoDiccionario):
    a=0; b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0;m=0;n=0;ñ=0;o=0;p=0;q=0;r=0;s=0;t=0;u=0;v=0;w=0;x=0;y=0;z=0;
    diccionarioValores = dict.fromkeys(nuevoDiccionario)
    abecedario=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z]
    #le asigno a las letras un valor según el número de veces que aparezcan en el diccionario. Una vez por palabra
    for palabra in nuevoDiccionario:
        #le quito a la palabra las letras repetidas
        palabraNoRepe=set(palabra)
        palabraNoRepe="".join(palabraNoRepe)
        for letra in palabraNoRepe:
            if letra=="a": a=a+1
            if letra=="b": b=b+1
            if letra=="c": c=c+1
            if letra=="d": d=d+1
            if letra=="e": e=e+1
            if letra=="f": f=f+1
            if letra=="g": g=g+1
            if letra=="h": h=h+1
            if letra=="i": i=i+1
            if letra=="j": j=j+1
            if letra=="k": k=k+1
            if letra=="l": l=l+1
            if letra=="m": m=m+1
            if letra=="n": n=n+1
            if letra=="ñ": ñ=ñ+1
            if letra=="o": o=o+1
            if letra=="p": p=p+1
            if letra=="q": q=q+1
            if letra=="r": r=r+1
            if letra=="s": s=s+1
            if letra=="t": t=t+1
            if letra=="u": u=u+1
            if letra=="v": v=v+1
            if letra=="w": w=w+1
            if letra=="x": x=x+1
            if letra=="y": y=y+1
            if letra=="z": z=z+1
    abecedario=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z]
    #le asigno a las palabras (en el diccionario) un valor que es el sumatorio de los valores que tienen asignadas las letras. Sin repetir letra.
    valor=0
    valorPalabra=0
    for palabra in nuevoDiccionario:
        #le quito a la palabra las letras repetidas
        palabraNoRepe=set(palabra)
        palabraNoRepe="".join(palabraNoRepe)
        for letra in palabraNoRepe:
            if letra=="a": valor=valor+a
            if letra=="b": valor=valor+b
            if letra=="c": valor=valor+c
            if letra=="d": valor=valor+d
            if letra=="e": valor=valor+e
            if letra=="f": valor=valor+f
            if letra=="g": valor=valor+g
            if letra=="h": valor=valor+h
            if letra=="i": valor=valor+i
            if letra=="j": valor=valor+j
            if letra=="k": valor=valor+k
            if letra=="l": valor=valor+l
            if letra=="m": valor=valor+m
            if letra=="n": valor=valor+n
            if letra=="ñ": valor=valor+ñ
            if letra=="o": valor=valor+o
            if letra=="p": valor=valor+p
            if letra=="q": valor=valor+q
            if letra=="r": valor=valor+r
            if letra=="s": valor=valor+s
            if letra=="t": valor=valor+t
            if letra=="u": valor=valor+u
            if letra=="v": valor=valor+v
            if letra=="w": valor=valor+w
            if letra=="x": valor=valor+x
            if letra=="y": valor=valor+y
            if letra=="z": valor=valor+z
            valorPalabra=valorPalabra+valor
            valor=0
        diccionarioValores[palabra]=valorPalabra
        valorPalabra=0
    palabraSugeridaPorDef=max(diccionarioValores, key=diccionarioValores.get)
    return(palabraSugeridaPorDef);
palabraSugerida=eligePalabraDiccionario(diccionario)
print("Empieza escribiendo la palabra "+ palabraSugerida + " y ya vamos viendo.")
diccionario.remove(palabraSugerida)
diccionarioAyuda=diccionario.copy()
while 1==1: 
    resultado=input("¿Qué tal ha ido? Escribe los fallos con (-), los aciertos en minusculas y las letras correctas en lugar incorrecto en mayusculas: ")
    if resultado==palabraSugerida:#rompe el bucle si pones la misma palabra que te ha sugerido
        break
    contadorLetra=0
    if resultado!="0": #le pongo un 0 para quitar esa palabra por si no existe en el juego
        for letraResultado in resultado:
            diccionario=diccionarioAyuda.copy()
            if letraResultado=="-":
                for palabra in diccionario:
                    if palabraSugerida[contadorLetra] in palabra:
                        #print("- "+palabraSugerida[contadorLetra]+" "+palabra)
                        diccionarioAyuda.remove(palabra)
            if letraResultado.isupper():
                for palabra in diccionario:
                    if (palabraSugerida[contadorLetra] == palabra[contadorLetra]) or not(palabraSugerida[contadorLetra] in palabra):
                        #print("M "+palabraSugerida[contadorLetra]+" "+palabra)
                        diccionarioAyuda.remove(palabra)
            if letraResultado.islower():
                for palabra in diccionario:
                    if not(palabraSugerida[contadorLetra] == palabra[contadorLetra]):
                        #print("m "+palabraSugerida[contadorLetra]+" "+palabra)
                        diccionarioAyuda.remove(palabra)
            contadorLetra=contadorLetra+1
            #con esto he modificado el diccionario con las pistas que me ha dado el juego
    else: #lo que pasa si le pongo el 0
        diccionarioAyuda.remove(palabraSugerida)
    palabraSugerida=eligePalabraDiccionario(diccionarioAyuda) #saca la palabra con mas puntos del nuevo diccionario
    print("De acuerdo, ahora prueba con "+ palabraSugerida)
print("Eso significa que hemos acertado,¡Enhorabuena!")

