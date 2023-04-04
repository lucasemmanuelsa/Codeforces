#include <iostream>
#include <string>
#include <sstream>
#include <queue>

using namespace std;

int main(){
    int t;
    cin >> t;

    queue<int> fila;

    for(int i = 0; i < t; i++){
        int x,y;
        cin >> x;

        if(x == 1){
            cin >> y;
            fila.push(y);
        }
        else if (x == 2)
        {
            if(!fila.empty()){
                fila.pop();
            }
        }else if (x == 3)
        {   
            if(fila.empty()){
                cout << "Empty!\n";
            }else{
                cout << fila.front() + "\n";
            }
            
        }
        
        
    }

    
    return 0;   

}
    