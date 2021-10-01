
def main():
  x=int(input()) #renglones
  y=int(input()) #columnas
  z= x*y
  b=0
  lista=[]
  if x==y:
      for a in range(0,z):
          u=int(input())
          if b == 0:
                lista.append(u)  
          b= b+1
          if b == x+1:
                b=0      
      print(lista)              
               
  else:
      print('La matriz no es cuadrada')    

if __name__=='__main__':
    main()
