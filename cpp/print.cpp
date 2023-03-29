#include <iostream> // biblioteca padrão de entrada e saida

using namespace std; // necessário para utilizar a função cout sem especificar o namespace

int main(){ // função principal do programa, todo programa em C++ deve ter uma função main, que é onde a execução começa
    cout << "Hello world" << endl; // operador "<<" é usado para inserir o texto
    //endl é um caractere de nova linha, serve para pular a linha depois de imprimir o texto.
    return 0; // é uma instrução que indica que o programa terminou com sucesso.

    // o retorno é uma forma de indicar ao Sistema Operacional se o programa foi executado com sucesso ou não
}   // se o valor de retorno for diferente de 0 o S.O. pode interpretar isso como um erro e exibir uma msg de erro
    //para o usuário


// Para compilar o código
// Passo 1: ir até a pasta do codigo fonte, pode ser pelo terminal ou abrir o terminal direto na pasta do codigo
// Passo 2: No terminal executar o seguinte codigo >> g++ meu_programa.cpp -o meu_programa
// Passo 3: ./meu_programa
// OBS: o compilador GCC precisa estar instalado no pc
//@author Lucas Emmanuel

