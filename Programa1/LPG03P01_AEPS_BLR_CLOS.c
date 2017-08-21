/*
	Materia: Lenguajes de Programación
	Equipo:	* Aguilar Enriquez, Paul Sebastian - 415028130
		* Badillo Lora, Raúl -
		* Cabrera López, Oscar Emilio - 312333261
	Programa: Programa que realiza las siguientes operaciones con vectores de n-dimensionales:
		* Suma
		* Resta
		* Producto por un escalar
		* Norma
		* Ángulo entre 2 vectores
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAXVECTORES 5
#define MINTAMANIOVECTOR 2
#define MAXTAMANIOVECTOR 5
#define PI 3.1416

float** leerVectores(int* nVectores, int* tamanioVector, int minVectores, int vectoresDefault);

int main()
{
    int opcion; // Variable para el menu
    opcion = -1;
    float** vectores;   // Apuntador para almacenar los vectores
    float* resultado; // Apuntdor para el vector resultante de las operaciones
    int nVectores;  // Cantidad de vectores a operar
    int tamanioVector;  // Tamaño de los vectores a operar
    int i,j; // Variables temporales, funcionan como contadores

    // Se imprime el menu y se selcciona una opcion
    do{
        printf("Seleccione una opción\n");
        printf("\t1.- Suma de vectores\n");
        printf("\t2.- Resta de vectores\n");
        printf("\t3.- Producto por un escalar\n");
		printf("\t4.- Norma de un vector\n");
		printf("\t5.- Ángulo entre 2 vectores\n");
		printf("\t0.- Salir\n");
		printf("Opción: ");
        scanf("%i", &opcion);

        // Ejecutamos la opcion seleccionada
        switch(opcion){
        case 1:
            printf("\nSuma de vectores A + B + ... + n\n");
            // Leemos los vectores
            vectores = leerVectores(&nVectores, &tamanioVector, 2, 0);
            // Imprimimos valores en pantalla, para verificar que no haya basura o valores corruptos
            printf("Numero de vectores a operar: %i\n", nVectores);
            printf("Tamaño de los vectores a operar: %i\n", tamanioVector);
            for(i = 0; i < nVectores; i++){
                printf("Vector #%i\t", i+1);
                for(j = 0; j < tamanioVector; j++){
                    printf("%.2f ", vectores[i][j]);
                }
                printf("\n");
            }
            printf("\n");

            resultado = (float*) calloc(tamanioVector, sizeof(float));

            // Operamos
            for(i = 0; i < nVectores; i++){
                for(j = 0; j < tamanioVector; j++){
                    resultado[j] = resultado[j] + vectores[i][j];
                }
            }

            // Imprimimos resultado
            printf("Resultado: ");
            for(j = 0; j < tamanioVector; j++){
                printf("%.2f ", resultado[j]);
            }
            printf("\n\n");
            break;
        case 2:
            printf("\nResta de vectores  A - B - ... - n\n");
            // Leemos los vectores
            vectores = leerVectores(&nVectores, &tamanioVector, 2, 0);
            // Imprimimos valores en pantalla, para verificar que no haya basura o valores corruptos
            printf("Numero de vectores a operar: %i\n", nVectores);
            printf("Tamaño de los vectores a operar: %i\n", tamanioVector);
            for(i = 0; i < nVectores; i++){
                printf("Vector #%i\t", i+1);
                for(j = 0; j < tamanioVector; j++){
                    printf("%.2f ", vectores[i][j]);
                }
                printf("\n");
            }
            printf("\n");

            // Movemos el primer vector al resultado para que la operacion tenga logica
            resultado = (float*) calloc(tamanioVector, sizeof(float));
            for(j = 0; j < tamanioVector; j++){
                resultado[j] = vectores[0][j];
            }

            // Operamos
            for(i = 1; i < nVectores; i++){
                for(j = 0; j < tamanioVector; j++){
                    resultado[j] = resultado[j] - vectores[i][j];
                }
            }

            // Imprimimos resultados
            printf("Resultado: ");
            for(j = 0; j < tamanioVector; j++){
                printf("%.2f ", resultado[j]);
            }
            printf("\n\n");
            break;
        case 3:
            ;
            float escalar; // Valor escalar por el que multiplicaremos

            printf("\nProducto por un escalar\n");
            // Leemos los vectores
            vectores = leerVectores(&nVectores, &tamanioVector, 1, 0);
            printf("Ingrese el escalar por el cual multiplicaremos: ");
            scanf("%f", &escalar);
            // Imprimimos valores en pantalla, para verificar que no haya basura o valores corruptos
            printf("Numero de vectores a operar: %i\n", nVectores);
            printf("Tamaño de los vectores a operar: %i\n", tamanioVector);
            for(i = 0; i < nVectores; i++){
                printf("Vector #%i\t", i+1);
                for(j = 0; j < tamanioVector; j++){
                    printf("%.2f ", vectores[i][j]);
                }
                printf("\n");
            }
            printf("\n");

            // Operamos
            for(i = 0; i < nVectores; i++){
                for(j = 0; j < tamanioVector; j++){
                    vectores[i][j] *= escalar;
                }
            }

            // Imprimimos resultado
            printf("Resultado:\n");
            for(i = 0; i < nVectores; i++){
                printf("Vector #%i\t", i+1);
                for(j = 0; j < tamanioVector; j++){
                    printf("%.2f ", vectores[i][j]);
                }
                printf("\n");
            }

            printf("\n\n");
            break;
        case 4:
            printf("\nNorma de un vector\n");
            // Leemos los vectores
            vectores = leerVectores(&nVectores, &tamanioVector, 1, 0);
            // Imprimimos valores en pantalla, para verificar que no haya basura o valores corruptos
            printf("Numero de vectores a operar: %i\n", nVectores);
            printf("Tamaño de los vectores a operar: %i\n", tamanioVector);
            for(i = 0; i < nVectores; i++){
                printf("Vector #%i\t", i+1);
                for(j = 0; j < tamanioVector; j++){
                    printf("%.2f ", vectores[i][j]);
                }
                printf("\n");
            }
            printf("\n");

            resultado = (float*) calloc(nVectores, sizeof(float));

            // Operamos
            for(i = 0; i < nVectores; i++){
                for(j = 0; j < tamanioVector; j++){
                    resultado[i] += vectores[i][j]*vectores[i][j];
                }
                resultado[i] = sqrt(resultado[i]);
            }

            // Imprimimos resultado
            printf("Resultado:\n");
            for(j = 0; j < tamanioVector; j++){
                printf("Modulo del Vector#%i: %.2f\n", j+1, resultado[j]);
            }

            printf("\n\n");
            break;
        case 5:
            ;
            float numerador, denominador; // Valores para el cociente que corresponde al cos(ang)
            float cosang;   // Varibale del cociente de la formula

            printf("\nÁngulo entre 2 vectores\n");
            // Leemos los vectores
            vectores = leerVectores(&nVectores, &tamanioVector, 2, 2);
            // Imprimimos valores en pantalla, para verificar que no haya basura o valores corruptos
            printf("Numero de vectores a operar: %i\n", nVectores);
            printf("Tamaño de los vectores a operar: %i\n", tamanioVector);
            for(i = 0; i < nVectores; i++){
                printf("Vector #%i\t", i+1);
                for(j = 0; j < tamanioVector; j++){
                    printf("%.2f ", vectores[i][j]);
                }
                printf("\n");
            }
            printf("\n");

            // Operamos

            numerador = 0;
            // Producto punto entre dos vectores
            for(j = 0; j < tamanioVector; j++){
                numerador += vectores[0][j] * vectores[1][j];
            }

            resultado = (float*) calloc(nVectores, sizeof(float));

            denominador = 0;
            for(j = 0; j < tamanioVector; j++){
                resultado[0] += vectores[0][j]*vectores[0][j];
                resultado[1] += vectores[1][j]*vectores[1][j];
            }
            resultado[0] = sqrt(resultado[0]);
            resultado[1] = sqrt(resultado[1]);
            denominador = resultado[0] * resultado[1];

            cosang = numerador / denominador;
            cosang = acos(cosang) * 180/PI;

            // Imprimimos resultado
            printf("Resultado: %.2f°",cosang);
            printf("\n\n");
            break;
        case 0:
            printf("\nTlasohcamati! Totasqueh!\n");
            break;
        default:
            printf("Error!\tLa opcion seleccionada es incorrecta.\nPresione Enter para continuar ...");
            while(getchar() != '\n');   // Limpiamos el buffer de entrada
            getchar();
        }
    }while(opcion != 0);
    return 0;
}

float** leerVectores(int* nVectores, int* tamanioVector, int minVectores, int vectoresDefault){
    float** vectores; // Apuntador donde se almacenaran los vectores
    int i,j; // Variables temporales, funcionan como contadores

    if(!vectoresDefault){
        // Leemos la cantidad de vectores a operar
        do{
            printf("Ingrese la cantidad de vectores a operar [max %i, solo por cuestiones de memoria]: ", MAXVECTORES);
            scanf("%i", nVectores);
            // Validamos la cantidad de vectores a operar
            if(*nVectores < minVectores || *nVectores > MAXVECTORES){
                printf("Error!\tIngrese un valor valido entre %i y %i.\nPresione Enter para continuar ...", minVectores, MAXVECTORES);
                while(getchar() != '\n');   // Limpiamos el buffer de entrada
                getchar();
            }
        }while(*nVectores < minVectores || *nVectores > MAXVECTORES);
    }else{
        *nVectores = vectoresDefault;
    }

    // Leemos la cantidad de vectores a operar
    do{
        printf("Ingrese el tamaño de los vectores a operar [max %i, solo por cuestiones de memoria]: ", MAXTAMANIOVECTOR);
        scanf("%i", tamanioVector);
        // Validamos el tamaño del vector a operar
        if(*tamanioVector < MINTAMANIOVECTOR || *tamanioVector > MAXTAMANIOVECTOR){
            printf("Error!\tIngrese un valor valido entre %i y %i.\nPresione Enter para continuar ...", MINTAMANIOVECTOR, MAXTAMANIOVECTOR);
            while(getchar() != '\n');   // Limpiamos el buffer de entrada
            getchar();
        }
    }while(*tamanioVector < MINTAMANIOVECTOR || *tamanioVector > MAXTAMANIOVECTOR);

    // Creamos los apuntadores para almacenar los vectores
    vectores = (float**) malloc(*nVectores);
    for(i = 0; i < *nVectores; i++){
        vectores[i] = (float*) malloc(*tamanioVector);
    }

    // Leemos valores de los vectores
    for(i = 0; i < *nVectores; i++){
        printf("Ingrese valores del vector #%i\n", i + 1);
        for(j = 0; j < *tamanioVector; j++){
            printf("Posicion[%i]: ", j + 1);
            scanf("%f", &vectores[i][j]);
        }
        printf("\n");
    }

    return vectores;
}
