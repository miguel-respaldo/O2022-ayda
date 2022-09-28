#include <iostream>
#include <stdlib.h>
#include "funciones.h"
#include <time.h>
#include <math.h>	

using namespace std;


//by Alexa Fernanda Iniguez Jimenez  18011226
//15 de Diciembre del 2021

int main(){
	
	int a, b, c;
	srand ((unsigned) time (NULL));
	
	cout << " A L G O R I T M O     S T R A S S E N "<<endl;
	
	cout << "---------------------------------------------- "<<endl;
	cout << "                    Entrada" << endl;
	cout << "---------------------------------------------- "<<endl;
	cout << "  a: ";
	cin >> a;
	cout << "  b: ";
	cin >> b;
	cout << "  c: ";
	cin >> c;	
    cout << "---------------------------------------------- "<<endl;
	cout << "                    Salida" << endl;
	cout << "---------------------------------------------- "<<endl;
	cout<<endl; 
	int ran=rango(a,c);
	
	matr mA(a,b,ran);
	mA.llenar();
	
	matr mB(b,c,ran);
	mB.llenar();
	
	/*	     	
    mA.escritura(0,0,3);
    mA.escritura(0,1,0);
    mA.escritura(1,0,1);
    mA.escritura(1,1,9);
    mA.escritura(2,0,6);
    mA.escritura(2,1,9);
    
    mB.escritura(0,0,7);
    mB.escritura(0,1,5);
    mB.escritura(0,2,2);
    mB.escritura(0,3,6);
    mB.escritura(1,0,4);
    mB.escritura(1,1,8);
    mB.escritura(1,2,9);
    mB.escritura(1,3,3);
    */
    
         
    cout << "  Matriz A:" << endl;      
	mA.imprimir();
	
	cout << "  Matriz B:" << endl;
	mB.imprimir();
	
	cout << "---------------------------------------------- "<<endl;
	//Redimensionamiento
	
	cout<<"  Redimensionamiento de A: "<<endl<<endl;
	mA.redmi(mA,maximo(a,b,c));
	cout<<"  Redimensionamiento de B: "<<endl<<endl;
	mB.redmi(mB,maximo(a,b,c));

  
	cout << "---------------------------------------------- "<<endl;
	
	
  matr C(maximo(a,b,c),maximo(a,b,c),0);

  C.set_a(a);
  C.set_c(c);
  C.set_mx(mA.get_mx());
  C.strassen2(mA,mB); 	
  
  //C.imprimirproducto(a,c);
	
	return 0;
}
