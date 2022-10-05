#include "matriz.h"

int matriz::getMatriz(int i,	int j) { return (*(*(puntero_matriz + i) + j)); }
void matriz::setMatriz(int i, int j, int v) { (*(*(puntero_matriz + i) + j)) = v ; }




matriz::matriz(int _filas, int _columnas) {
	puntero_matriz = new int* [_filas];
	for (int i = 0; i < _filas; i++) {
		puntero_matriz[i] = new int[_columnas];
	}

	filas = _filas;
	columnas = _columnas;

}

//Llenado de la matriz con numero aleatorios
void matriz::numerosAleatorios() {
	for (int i = 0; i < filas; i++) {
		for (int j = 0; j < columnas; j++) {
			setMatriz(i,j,0);
		}
	}
}


void matriz::mostrarMatriz() { 
	for (int i = 0; i < filas; i++) {
		for (int j = 0; j < columnas; j++) {
			std::cout <<" | "<< getMatriz(i,j) << " |";
		}
		std::cout << "\n";
	}
	
	std::cout << "\n";
}

//Liberar memoria utilizada de la matriz
matriz::~matriz() {
	for (int i = 0; i < filas; i++) {
		delete[] puntero_matriz[i];
	}
	delete[] puntero_matriz;
}


//CATALAN	
long int Catalan(int digito){
 
	int resultado = 0;
	
	if(digito <= 1) return 1;
	for(int i = 0; i <digito; i++){
		resultado += Catalan(i) * Catalan(digito - i - 1);
	}
	return resultado;
}

//PARENTESIZACION
void Parentesizacion( matriz& s,int i, int j ){
	
	if (i == j){
		std::cout<<"A_"<<i;		
	}else{
		std::cout<<"(";
		Parentesizacion(s,i,s.getMatriz(i,j));
		Parentesizacion(s,s.getMatriz(i,j)+1,j);
		std::cout<<")";		
	}		
}

// MATRIX CHAIN
void MatrixChain(int *&p, int n){
	
		for(int i=0; i<n; i++ ){		
		std::cout<< p[i] << " ";			
	}
	
	std::cout << "\n";
	
	matriz m(n,n);
	m.numerosAleatorios();
	matriz s(n,n);
	s.numerosAleatorios();
	
	for (int i=1; i<n; i++){
		m.setMatriz(i,i,0);
		for (int len=2; len<n; len++){
			for (int i = 1; i < (n-len+1); i++){
			
			int j = (i + len - 1);
			m.setMatriz(i,j,INT_MAX);
			
			for(int k= i; k<=j-1; k++){
				double q = m.getMatriz(i,k) + m.getMatriz(k+1,j) + p[i - 1] * p[k] * p[j];
				if(q < m.getMatriz(i,j)){
					m.setMatriz(i,j,q);
					s.setMatriz(i,j,k);					
				}
			}
		}
	}
	}
	
	m.mostrarMatriz();
	s.mostrarMatriz();
	
	std::cout<<"Parenterizacion optima: ";
	Parentesizacion(s,1,n-1);
	std::cout<<"\n";
	std::cout<<"\nCosto: ";
	std::cout<< m.getMatriz(1,n-1) << " ";
}









