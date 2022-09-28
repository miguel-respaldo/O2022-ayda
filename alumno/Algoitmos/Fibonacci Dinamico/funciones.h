#ifndef funciones_h
#define funciones_h
#include <iostream>

class funciones{
	
	int capacidad; //llenar
	int tamano;  //conforme se van guardando 
	long* digito;

public:
	//Constructor y destructor 
	funciones(int);
	~funciones();

	//Agregar un dato nuevo 
	void add(int, long);
	
	//Retorna un dato almacenado en el vector
	long get(int);
	
	int capacidadActual();
	int tamanoActual();
	void imprimir();
	
};

#endif


