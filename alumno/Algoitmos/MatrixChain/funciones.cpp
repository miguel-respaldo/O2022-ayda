#include "funciones.h"


// Algoritmo Matrix Chain 
long funciones::AlgoritmoMatrixChain(int i){
}

// Algoritmo Catalan
long funciones::Catalan(int digito){
	
	int resultado = 0;
	if(digito <= 1) return 1;
	for(int i = 0; i <digito; i++){
		resultado += Catalan(i) * Catalan(digito - i - 1);
	}
	return resultado;
}



