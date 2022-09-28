#include <iostream>
#include "funciones.h"

// capacidad 1 
funciones funcion(1);
int contador = 0;

long fibonacci(int f) {
	contador ++;
		
	if (f < 2) {
		
	
		funcion.add(f, 1);
		return 1;
		
	} else {
		
		long value = fibonacci(f - 1) + fibonacci(f - 2);
		
		funcion.add(f, value);
		return value;		
	}
	
}


using namespace std;

int main() {
	
	int digito;
	cout << "-------- Fibonacci con Vector Dinamico -------- \n";
	cout << " Numero: ";
	cin >> digito;
	cout << " \n";
	
	funcion.add(0,1);
	funcion.add(1,1);
	cout<<" Resultado: "<<fibonacci(digito);
	fflush(stdin);  
	cout << "\n\n Sucesion: ";
	funcion.imprimir();
	cout << " \n\n";
	cout << " Conteo de instancias: "<<contador;

	return 0;
}






