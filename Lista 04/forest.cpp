#include <iostream>
#include <vector>
using namespace std;

int main() {
    
    int tam;
    int queries;

    cin >> tam >> queries;

    string matriz[tam];

    for(int i = 0; i < tam; i++){
        string entrada;
        cin >> entrada;
        matriz[i] = entrada;
    }

    int resultado[tam+1][tam+1];

    for(int i = 1; i < tam+1; i++){
        for(int j = 1; j < tam+1; j++){
            int soma = 0;
            if(matriz[i-1][j-1] == '*'){
                soma = 1;
            }
            resultado[i][j] = resultado[i-1][j] + resultado[i][j-1] + soma - resultado[i-1][j-1];
        }
    }
    
    for(int i = 0; i < queries; i++){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int soma = resultado[x2][y2] - resultado[x2][y1 - 1] - resultado[x1-1][y2] + resultado[x1 - 1][y1 - 1];
        cout << soma << "\n";
    }
    
    return 0;
}
