/*
    Materia: Lenguajes de Programación
	Equipo:	* Aguilar Enriquez, Paul Sebastian - 415028130
			* Badillo Lora, Raúl - 415033808
			* Cabrera López, Oscar Emilio - 312333261
	Programa: Desarrollar los códigos necesarios para mostrar:
            * La forma en la que se realiza la elección y el encadenamiento de constructores
            * El uso de los diferentes tipos de vista que provee
            * La forma en la que se realiza la búsqueda dinámica de métodos


Copyright (c) 2017

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <iostream>

using namespace std;

// Clase Counter
class Counter {
    protected: int x;   // Se hereda a claes hija
    private: int y;     // No se hereda a la hija
    public: Counter(){
        cout<<"Constructor Counter"<<endl;
        x = 0;
        aPrivate();
    }
    // La palabra virtual nos permite crear metodos que se pueden redefinir en la clase hija
    // y que pueden ser utlizados por un objeto de la clase padre cuando se usa polimorfismo
    virtual void reset(){
        x = 0;
    }
    void reset2(){
        x = 0;
    }
    int get (){
        return x;
    }
    virtual void inc (){
        x = x+1;
    }
    void inc2 (){
        x = x+1;
    }

    private: void aPrivate(){
        cout<<"Esto es privado :("<<endl;
    }
};

// Clae NewCounter, hereda de Counter
class NewCounter : public Counter {
    private: int num_reset = 0 ;
    public: NewCounter(bool superduper){
        if(superduper){ // Bandera para llamar a la clase padre
            NewCounter::Counter();
        }
        cout<<"Constructor NewCounter"<<endl;
        x = 1;
        //aPrivate();   // No puede acceder porque no la heredo
    }
    void reset (){
        x = 1;
        num_reset++;
    }
    void inc(){
        x += 10;
    }
    void reset2(){
        x = 1;
        num_reset++;
    }
    void inc2(){
        x += 10;
    }
    int cuantos_resets (){
        return num_reset;
    }
};

int main()
{
    // Demostramos la selccion de constructores
    NewCounter* a = new NewCounter(false);
    a->inc();

    NewCounter* b = new NewCounter(true);
    Counter* c = new Counter();

    cout<<"Actualmente b->x = "<<b->get()<<endl;
    b->inc();
    cout<<"Incrementamos, ahora b->x = "<<b->get()<<endl;

    cout<<"Actualmente c->x = "<<c->get()<<endl;
    c->inc();
    cout<<"Incrementamos, ahora c->x = "<<c->get()<<endl;

    // Demostramos la resolucion de metodos
    c = b;  // Gracias al polimorfismo c ahora es un objeto de la clase B

    cout<<"Asignamos c = b"<<endl;
    cout<<"Actualmente c->x = "<<c->get()<<endl;
    c->inc();
    cout<<"Incrementamos, ahora c->x = "<<c->get()<<"\tSe utilizo una funcion \"virtual\""<<endl;
    c->reset();
    cout<<"Reiniciamos c, ahora c->x = "<<c->get()<<"\tSe utilizo una funcion \"virtual\""<<endl;
    c->inc2();
    cout<<"Incrementamos, ahora c->x = "<<c->get()<<"\tNo se utilizo una funcion \"virtual\""<<endl;
    c->reset2();
    cout<<"Reiniciamos c, ahora c->x = "<<c->get()<<"\tNo se utilizo una funcion \"virtual\""<<endl;


    return 0;
}
