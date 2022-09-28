/* Matrix Chain
	
	Alexa Fernanda Iñiguez Jimenez 
	No.Control: 18011226  */
	
#include <string>	
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>
#include "matriz.h"



using namespace std;

int main(int argc, char** argv) {
	
	

	cout << "-------- Cadena de Matrices -------- \n";
	int digito;
	cout<<" Entrada: ";
	cin>> digito;
	cout<<endl;
	digito=digito+1;
	
//VECTOR -------------------------------------------------------	
	cout<<" Dimension del Vector: ";
	int* vector=new int[digito]; //p[]
	
	srand (time(NULL));
	
	//dar valores...
	for(int i=0; i<digito; i++ ){	
		vector[i] = rand() % 10 + 1;	//Llenara el vector con numeros aleatorios entre 1 y 10
	}
	
//PRUEBAS 
	/*vector[0]=3;
	vector[1]=2;
	vector[2]=9;
	vector[3]=9;
	vector[4]=1;
	vector[5]=8;
	vector[6]=5;
	vector[7]=10;
	vector[8]=8;
	vector[9]=9;
	vector[10]=1;*/
	
				
	cout<<"< ";
	for(int i=0; i<digito; i++ ){		
		cout<< vector[i] << " ";			
	}
	cout<<">";	
	cout<<endl;
	
// CATALAN --------------------------------------------------	
	
	cout<<" Numero de soluciones: ";
	cout<<Catalan(digito-2) <<" ";
	cout<<endl;
	cout<<endl;
	
// MATRIX CHAIN 	
	cout<<" Parentesizacion: ";	
	MatrixChain(vector,digito);
	return 0;
}

