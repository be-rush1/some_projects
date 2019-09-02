#include<iostream>
#include<vector>
#include<iterator>
using namespace std;
int main()
{
    int x=0;
    int y;
    int i;
    cout<<"Insira Número: ";
    cin>>y;
    vector<int>lista;
    vector<int>::iterator it;
    do {
        x+=1;
        if (x>10)
        {
            if(x%2!=0)
            {
                if(x%3!=0)
                {
                    if(x%5!=0)
                    {
                        if(x%7!=0)
                        {
                            lista.push_back(x);
                        }
                    }
                }
            }
        }
    if(x==2||x==3||x==5||x==7)
    {
        lista.push_back(x);
    } 
    } while(x<y);
    cout<<"Os Primos São: ";
    for(it=lista.begin();it!=lista.end();it++)
        cout<<' '<<*it;
    cout<<endl;
return 0;
}
