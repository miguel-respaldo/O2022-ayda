#ifndef matriz_h
#define matriz_h

#include <ctime>
#include <stdlib.h>
#include <iostream>



class matriz{
	
	int** puntero_matriz; //señala a otra matriz 
	
	//Filas y columnas de la matriz
	int filas;
	int columnas;
	
	//Para respaldar los datos de la matriz, esto lo use para cuando nos vamos a mover a la siguiente y no se pierdan los datos
	int RespaldoFilas;
	int RespaldoColumnas;
	int maxRandom;
	

public:
	matriz(int, int);
	~matriz();


	//Creacion del get y el set para la matriz
	int getMatriz(int, int);
	void setMatriz(int, int, int);
	
	// Obtener el tamaño de las filas y columnas de la matriz
	int LongitudFilas();
	int LongitudColumnas();
	
	//Funcion para que los datos de la matriz sean numeros aleatorios
	void numerosAleatorios();
	
	
	void mostrarMatriz();
	
	

	
	
};


long int Catalan(int);
	void Parentesizacion(matriz&,int, int);
	void MatrixChain(int*&, int);
#endif
