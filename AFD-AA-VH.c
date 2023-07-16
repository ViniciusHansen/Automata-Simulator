#include <stdio.h>
#include <string.h>
#define TAM_MAX 50
#define INVALIDO -1

int posicao_alfabeto(char alfabeto[], int tam_alfabeto, char input);
int aceita_fita(int estado, int finais[], int quant_finais);
int alfabeto_invalido(char alfabeto[]);

int main() {

    int estado, quant_estados, tam_alfabeto,
        tam_fita, inicial, quant_finais, i,
        j, continuar, linha, coluna, fita_invalida;

    char alfabeto[TAM_MAX], fita[TAM_MAX];

    printf("Informe a quantidade de estados do automata: ");
    scanf("%d", &quant_estados);
    while ( quant_estados <= 0 ) { 
        printf("Quantidade inválida!\n");
        printf("Informe a quantidade de estados do automata: ");
        scanf("%d", &quant_estados);
    }
    int estados[quant_estados];

    // Popula vetor de estados
    for(i = 0; i < quant_estados; i++) 
        estados[i] = i;

    // Limpa o buffer
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }

    printf("Informe o alfabeto do automata: ");
    scanf("%s", alfabeto);
    tam_alfabeto = strlen(alfabeto);

    while ( alfabeto_invalido(alfabeto) ) {
        printf("Alfabeto inválido!\n");
        printf("Informe o alfabeto do automata: ");
        scanf("%s", alfabeto);
        tam_alfabeto = strlen(alfabeto);
    };

    printf("Informe o estado inicial: ");
    scanf("%d", &inicial);

    while ( inicial < 0 || inicial >= quant_estados ) {
        printf("Estado inválido!\n");
        printf("Informe o estado inicial: ");
        scanf("%d", &inicial);
    }
    
    printf("Informe a quantidade de estados finais: ");
    scanf("%d", &quant_finais);

    while ( quant_finais < 0 || quant_finais >= quant_estados ) {
        printf("Estado inválido\n");
        printf("Informe a quantidade de estados finais: ");
        scanf("%d", &quant_finais);
    }

    int finais[quant_finais];
    
    // Popula o vetor de estados finais
    for(i = 0; i < quant_finais; i++) {
        printf("%d* final: ", i + 1);
        scanf("%d", &finais[i]);
        while ( finais[i] < 0 || finais[i] >= quant_estados ) {
            printf("Estado invalido!\n");
            printf("%d* final: ", i + 1);
            scanf("%d", &finais[i]);
        }
    }

    int matriz_transicao[quant_estados][tam_alfabeto];
    printf("\nPreencha a matriz de transição:\n");
    printf("Estado|Input\n");
    
    // Popula a matriz de transição
    for(i = 0; i < quant_estados; i++)
        for(j = 0; j < tam_alfabeto; j++) {
            printf("%d | %c = ", estados[i], alfabeto[j]);
            scanf("%d", &matriz_transicao[i][j]);
            while ( matriz_transicao[i][j] < 0 || matriz_transicao[i][j] >= quant_estados ) {
                printf("Estado invalido!\n");
                printf("%d | %c = ", estados[i], alfabeto[j]);
                scanf("%d", &matriz_transicao[i][j]);
            }
        }
    
    
    // Lê a fita e evolui o automata
    do {
        estado = inicial;
        printf("\nInforme a fita: ");
        scanf("%s", fita);
        i = 0;
        fita_invalida = 0;
        tam_fita = strlen(fita);
    
        while ( i < tam_fita ) {
            linha = estado;
            coluna = posicao_alfabeto(alfabeto, tam_alfabeto, fita[i]);
            if ( coluna == INVALIDO ) {
                fita_invalida = 1;
                break;
            }
            i++;
            estado = matriz_transicao[linha][coluna];
        }

        if ( fita_invalida )
            printf("A fita é inválida!\n");

        else if ( aceita_fita(estado, finais, quant_finais) ) 
            printf("A fita foi aceita!\n");
        
        else
            printf("A fita foi rejeitada!\n");
        
        printf("Deseja verificar mais uma fita? (1 - Sim / Qualquer - Não): ");
        scanf("%d", &continuar);

    } while ( continuar == 1 );

    return 0;
}

int aceita_fita(int estado, int finais[], int quant_finais) {
    int i = 0, nao_achou = 1;
    while ( i < quant_finais && nao_achou ) {
        nao_achou = !(finais[i] == estado);
        i++;
    }

    return !nao_achou;
}

int posicao_alfabeto(char alfabeto[], int tam_alfabeto, char input) {
    char *auxiliar;
    auxiliar = strchr(alfabeto, input);

    if( auxiliar == NULL )
        return INVALIDO;
    
    return (int)(auxiliar - alfabeto);
}

int alfabeto_invalido(char str[]) {
    int i, j, len;
    len = strlen(str);

    for (i = 0; i < len; i++) 
        for (j = i+1; j < len; j++) 
            if (str[i] == str[j]) 
                return 1; // Letras repetidas encontradas, retorna verdadeiro
            
    return 0; // Letras não repetidas, retorna falso
}