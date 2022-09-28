#include "funciones.h"

//constructor del vector
funciones::funciones(int c) : capacidad(c), tamano(0){
	digito = new long[c];
	for (int x = 0; x < capacidad; x++) {
		digito[x] = 0;
	}
}

//destructor del vector 
funciones::~funciones() {
	long* i = NULL;
	digito = i;
	delete[] digito;
}

int funciones::tamanoActual() {
 	return tamano; }

int funciones::capacidadActual() {
 	return capacidad; }


//Redimensionamiento

void funciones::add(int i, long f) {
		
	if (capacidadActual() == tamanoActual()) {
		
		funciones copy(capacidadActual());
		for (int x = 0; x < capacidadActual(); x++) {	copy.add(x, get(x));	} 
		
		
		
		capacidad = capacidadActual() * 2;
		
		tamano = 0;
		
		digito = new long[capacidadActual()];
		
		for (int y = 0; y < capacidadActual()/2; y++) {
			
			digito[y] = 0;
			
			add(y, copy.get(y));
		}
	}
	digito[i] = f;
	tamano++;
}





long funciones::get(int i) {
	return digito[i];
}



void funciones::imprimir() {
	std::cout << "Inicio  [0]";
	for (int p = 0; p < capacidad; p++) {
		
		if (digito[p] && p < tamano) {
			std::cout << " --> " << digito[p];			
		}else{
			std::cout << "";			
		} 		
	}
}





