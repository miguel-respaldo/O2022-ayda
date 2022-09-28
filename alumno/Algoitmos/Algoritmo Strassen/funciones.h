#ifndef funciones_h
#define funciones_h



class matr{
	
	int ren;
	int col;
	int rango;
	int maximo;
  int a;
  int c;
	
	int **matr1;

	typedef enum {
	above,
	down
} height;

typedef enum {
	left,
	right
} side;
	
	public:
		
		
		matr(int, int,int);
		
		matr(matr&, int, int );
		
		~matr();
		
		int lectura(int,int);
		
		void escritura(int, int,int);
		
		
		
		void expansion(int);
		
		void llenar();
		
		void llenarceros(int);
		
		void imprimir();

    void imprimirproducto(int,int);
		
    void redmi(matr&, int);
		
    matr strassen2(matr& , matr&  );
		
		int get_ren(){
			return ren;
		}
		
		void set_ren(int _ren){
			ren=_ren;
		}
		
		int get_col(){
			return col;
		}
		
		void set_col(int _col){
			col=_col;
		}
		
		int get_mx(){
			return maximo;
		}
		
		void set_mx(int _mx){
			maximo=_mx;
		}

    void set_a(int _a){	a=_a;}

    int get_a(){
			return a;
		}

    void set_c(int _c){
			c=_c;
		}

    int get_c(){
			return c;
		}
		
		
		
};

matr suma(matr&, matr&,int);

matr resta(matr&, matr&,int);

matr multiplicacion(matr&,matr&,int);

int rango(int, int);

int maximo(int, int, int);


matr agrupacion(matr&,matr&,matr&,matr&);

#endif
