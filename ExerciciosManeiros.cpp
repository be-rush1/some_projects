#include<iostream>
#include<vector>
#include<iterator>
#include<algorithm>
using namespace std;
int main()
{
    int x;
    int resto;
    int i;
    cout<<"Insira Número: ";
    cin>>x;
    vector<int>lista;
    vector<int>::iterator it;
    do {
        resto=x%7;
        x=x/7;
        lista.push_back(resto);
    } while(x>7);
    cout<<x;
    reverse(lista.begin(),lista.end());
    for(it=lista.begin();it!=lista.end();it++)
        cout<<*it;
    cout<<endl;
    
return 0;
}
