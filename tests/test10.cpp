#include <iostream>
using namespace std;

void printPointVal(int *a){
    cout << *a << endl;
}

class A {
    int x;
    public:
    void bar() {
    cout << x << " Test!";
    }
};
int main() {
    A* a = 0; // разымен 0-го *
    a->bar();
    
    int *pr = NULL; // разым 0-го
    printPointVal(pr);
    
    ifstream file; // некорр дост к ф
    file.open("d:\\1\\файл.txt");
    if (!file)
    {
    cout << "Файл не открыт\n\n";
    }
    else
    {
    cout << "Все ОК! Файл открыт!\n\n";
    }
    
    int i1 = 1000000000; // переполн цел чис
    int i2 = i1*i1 + i1;
    
    int x, y, z; // исп неиниц пер
    z = x + 3;
    y = pow(z, 2.0);
    
    double s; //исп неиниц перем
    s += 3.14;
    cout << s << endl;
    
    return 0;
}
