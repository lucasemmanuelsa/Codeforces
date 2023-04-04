#include <iostream>
#include <queue>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    queue<int> q;

    int tam_fila = 0;

    for (int i = 0; i < t; i++) {
        int opcao;
        scanf("%d", &opcao);

        if (opcao == 1) {
            int valor;
            scanf("%d", &valor);
            q.push(valor);
            tam_fila++;
        } else if (opcao == 2) {
            if (tam_fila > 0) {
                q.pop();
                tam_fila--;
            }
        } else {
            if (tam_fila == 0) {
                printf("Empty!\n");
            } else {
                printf("%d\n", q.front());
            }
        }
    }

    return 0;
}
