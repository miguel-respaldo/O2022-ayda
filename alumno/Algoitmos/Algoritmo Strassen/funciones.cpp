#include "funciones.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <ctype.h>	
#include <algorithm>

using namespace std;
//Constructor que hace la matr 
matr::matr(int _ren,int _col, int ran){
	
	ren=_ren;
	col=_col;
	
	rango=ran;
	
    matr1= new int*[ren];
    
    for(int i=0;i<ren;i++){
    	matr1[i]=new int[col];
	}
     	
}
matr::~matr(){                                //Destructor de la matr
	
	for(int i=0;i<ren;i++){ delete[] matr1[i]; }
	
	delete[] matr1;
}
//Metodo para obtener un dato de la matr
int matr::lectura(int ren, int col){
	return matr1[ren][col];
}


//Metodo para poder modificar la matr en un lugar en especifico
void matr::escritura(int ren,int col, int v){
	matr1[ren][col]=v;
}

//Metodo para expandir la matr cuando se hace el redimensionamiento
void matr::expansion(int mx){
	
	matr1= new int*[mx];
	
    for(int i=0;i<mx;i++){
    	matr1[i]=new int[mx];
	}
	
}
//Metodo para llenar con datos la matr con un cierto rango de numeros
void matr::llenar(){
	
	
	for(int i=0; i<ren; i++){
            for(int j=0; j<col; j++){
            	
                matr1[i][j]=rand() % rango;
            }
        }
	
}
//Metodo que llena toda la matr con ceros y este metodo se usa para el redimensionamiento
void matr::llenarceros(int mx){
	
        for(int i=0; i<mx; i++){
            for(int j=0; j<mx; j++){
            			if(matr1[i][j]!=0){
            				matr1[i][j]=0;	
						}           							
            }
        }
        
    ren=mx;
	col=mx;
	maximo=mx;
	
}
//Metodo para imprimir cualquier matr
void matr::imprimir(){
	
	for(int i=0; i<ren; i++){
            for(int j=0; j<col; j++){
                cout<<" ["<<matr1[i][j]<<"] ";
            }
            cout<<endl;
        }
        
        cout<<endl;
}

//Metodo para obtener el rango de n�meros 
int rango(int a, int c){
	
	return a*c;
}

//Metodo para obtener el tama�o maximo cuadrado cuando se hace el redimensionamiento
int maximo(int a, int b, int c){
	
	
	int m=max(a,b);
	int ma= max(m,c);
	float loga=log2(ma);
	float pot=ceil(loga);
	int n=pow(2,pot);
	return n;
}


//Metodo que hace el redimensionamiento
//Declara una matr nueva con el tama�o de la original
//Metemos en esa matr nueva los datos de la orginal
//Se llaman los metodos para expandir la matr y la llenamos de ceros
//Se le introduce los datos guardados en la otra matr en esta nueva ya redimensionada con los ceros
//Se imprime
void matr::redmi(matr& m, int max){
	
	
    	
	matr m3(m.get_ren(),m.get_col(),1);
	
	for(int i=0; i<m.get_ren(); i++){
            for(int j=0; j<m.get_col(); j++){
            	
                m3.escritura(i,j,m.lectura(i,j));
            }
        }
	
    
	m.expansion(max);
	
	
	m.llenarceros(max);
	
	
	for(int i=0; i<m3.get_ren(); i++){
            for(int j=0; j<m3.get_col(); j++){
            	
                m.escritura(i,j,m3.lectura(i,j));
            }
        }

	m.imprimir();
	
  set_mx(max);
	
}

//Metodo de suma de matrices y duvuelve otra matr con la suma
matr suma(matr& m1, matr& m2, int mx){
	
	//cout<<"Suma"<<endl<<endl;
	
	matr m3(mx,mx,1);
    
    
	
	 for(int i=0; i<mx; i++){
        for(int j=0; j<mx; j++){
        m3.escritura(i,j,m1.lectura(i,j)+m2.lectura(i,j));
        }
    }
    
    
	
	
	return m3;

  m3.~matr();
    
    
}



//Metodo de resta de matrices y duvuelve otra matr con la resta
matr resta(matr& m1, matr& m2, int mx){
	
	//cout<<"Resta"<<endl<<endl;
	
	matr m3(mx,mx,1);
    
	 for(int i=0; i<mx; i++){
        for(int j=0; j<mx; j++){
        m3.escritura(i,j,m1.lectura(i,j)-m2.lectura(i,j));
        }
    }
    
    
	
	return m3;

  m3.~matr();
	
}

//Metodo de multiplicaci�n de matrices y duvuelve otra matr con la multiplicaci�n
matr multiplicacion(matr& m1, matr& m2, int mx){
	
	//cout<<"Multiplicacion"<<endl<<endl;
	
	matr m3(mx,mx,1);
    int aux;
    
	
	 for(int i=0; i<mx; i++){
        for(int j=0; j<mx; j++){
        	
        	m3.escritura(i,j,0);
        	for(int k=0;k<mx;k++){
              aux=m3.lectura(i,j)+(m1.lectura(i,k)*m2.lectura(k,j));
              m3.escritura(i,j,aux);
          }
        	
        }
    }
   
	return m3;

  m3.~matr();
    
    
}



//Segundo constructor en donde se divide cierta matr introducida en 4
//Se implmento above, down, left, right para indicar que parte de la matr se va a tomar
matr::matr(matr& m,int h,int s){
	
	
	//1=above 0=down
	//1=left 0=right
	
	height he;
	side si;
	
	int mx;
  int aux1;
  int aux2;
	
	if(h==1 && s==1){
		he=above;
		si=left;
    ren=m.get_mx()/2;
  col=m.get_mx()/2;
  mx=m.get_mx();
	}else if(h==1 && s==0){
		he=above;
		si=right;
    ren=m.get_mx()/2;
  col=m.get_mx()/2;
  mx=m.get_mx();
	}else if(h==0 && s==1){
		he=down;
		si=left;
    ren=m.get_mx()/2;
  col=m.get_mx()/2;
  mx=m.get_mx();
	}else if(h==0 && s==0){
		he=down;
		si=right;
    ren=m.get_mx()/2;
  col=m.get_mx()/2;
  mx=m.get_mx();
  m.set_mx(mx/2);
	}
	 
	
	
	 matr1= new int*[ren];
    
    for(int i=0;i<ren;i++){
    	matr1[i]=new int[col];
	}
	
	
	
	//Aqui toma la parte superior izquierda
	if(he==above && si==left){
		for(int i=0; i<mx/2; i++){
            for(int j=0; j<mx/2; j++){
            	
                matr1[i][j]=m.lectura(i,j);
            }
        }
		//Aqui toma la parte superior derecha
	}else if(he==above && si==right){
		
		for(int i=0; i<mx/2; i++){
			
            for(int j=mx/2; j<mx; j++){
            	
                matr1[i][j-mx/2]=m.lectura(i,j);
            }
        }
		//Aqui toma la parte inferior izquierda
	}else if(he==down && si==left){
		
		for(int i=mx/2; i<mx; i++){
			
            for(int j=0; j<mx/2; j++){
            	
                matr1[i-mx/2][j]=m.lectura(i,j);
            }
        }
		
		//Aqui toma la parte inferior derecha
	}else if(he==down && si==right){
	
		for(int i=mx/2; i<mx; i++){
			
            for(int j=mx/2; j<mx; j++){
            	
                matr1[i-mx/2][j-mx/2]=m.lectura(i,j);
            }
        }

        
	
	}	
}
//Se declara una matr nueva con el doble del tama�o para poder introducir las 4 matrices c11,c12,c21,c22
//Ingresa cada parte de la matr c11,c12,c21,c22 en la c
//Retorna la matr c
matr agrupacion( matr& c11, matr& c12, matr& c21, matr& c22){
	
	int ren=c11.get_ren()*2;
	int col=c11.get_col()*2;
	
	matr c(ren,col,1);
	
	for(int i=0; i<ren/2; i++){
            for(int j=0; j<col/2; j++){
            	
                c.escritura(i,j,c11.lectura(i,j));
            }
        }
        
        for(int i=0; i<ren/2; i++){
            for(int j=col/2; j<col; j++){
            	
            	c.escritura(i,j,c12.lectura(i,j-(col/2)));
                
            }
        }
        
        
        for(int i=ren/2; i<ren; i++){
			
            for(int j=0; j<col/2; j++){
            	
            	c.escritura(i,j,c21.lectura(i-ren/2,j));
                
            }
        }
        
        
        for(int i=ren/2; i<ren; i++){
			
            for(int j=col/2; j<col; j++){
            	
            	c.escritura(i,j,c22.lectura(i-ren/2,j-col/2));
                
            }
        }
        
	return c;
	
}


matr matr::strassen2(matr& A, matr& B){

  

	if(A.get_col()<=get_mx()/2){
		return multiplicacion(A,B,A.get_col());
	}
	 //Conquista
	 
	//Divison de matr A
	matr mA11(A,1,1);
	
	matr mA12(A,1,0);

	matr mA21(A,0,1);
  
	matr mA22(A,0,0);

	//Divison de matr B
	matr mB11(B,1,1);

	matr mB12(B,1,0);
	
	matr mB21(B,0,1);

	matr mB22(B,0,0);




	matr m1=suma(mA11,mA22,mA11.get_ren());
	matr m11=suma(mB11,mB22,mB11.get_ren());
	matr M1=strassen2(m1,m11);
	
	matr m2=suma(mA21,mA22,mA11.get_ren());
	matr M2=strassen2(m2,mB11);
	
	matr m3=resta(mB12,mB22,mB12.get_ren());
	matr M3=strassen2(mA11,m3);
	
	matr m4=resta(mB21,mB11,mB21.get_ren());
	matr M4=strassen2(mA22,m4);
	
	matr m5=suma(mA11,mA12,mA11.get_ren());
	matr M5=strassen2(m5,mB22);
	
	matr m6=resta(mA21,mA11,mA21.get_ren());
	matr m66=suma(mB11,mB12,mB11.get_ren());
	matr M6=strassen2(m6,m66);
	
	matr m7=resta(mA12,mA22,mA12.get_ren());
	matr m77=suma(mB21,mB22,mB21.get_ren());
	matr M7=strassen2(m7,m77);

	//  Combinacion se realizaron combinaciones para la matriz c 
	matr c111=suma(M1,M4,M1.get_ren());
	matr c112=suma(M5,M7,M5.get_ren());
	matr C11=resta(c111,c112,c111.get_ren());

	
	matr C12=suma(M3,M5,M3.get_ren());

	
	matr C21=suma(M2,M4,M2.get_ren());

	
	matr c221=resta(M1,M2,M1.get_ren());
	matr c222=suma(M3,M6,M3.get_ren());
	matr C22=suma(c221,c222,c221.get_ren());

	
  matr C=agrupacion(C11,C12,C21,C22);

  	cout<<"  Producto (Multiplicacion)"<<endl<<endl;

    

  C.imprimirproducto(get_a(),get_c());

	return C;

}



void matr::imprimirproducto(int ren1, int  col1){
	
for(int i=0; i<ren1; i++){
            for(int j=0; j<col1; j++){
                cout<<" ["<<matr1[i][j]<<"] ";
            }
            cout<<endl;
        }
        
        cout<<endl;
}
