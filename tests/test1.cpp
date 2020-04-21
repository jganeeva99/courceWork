#include <iostream>

using namespace std;

void printUserAndPassword(string user, string password) {
    cout << user << " " << password << endl;
}

int main(){
    int i; // неиниц. перем
    i += 95;
    
    int x = 0, y = 0;
    cout << "Эта программа вычисляет квадрат суммы!" << endl;
    cout << "Введите первое число: ";
    cin >> x;
    cout << "Введите второе число: " << endl;
    cin >> y;
    int result = x*x + 2*x*y + y*y;
    int s = 100000000000 + result; // переполнение
       
    char * first(0);
    char * second(0);
    cout << *first << " " << *second << endl; //разыменов.
    
    string admin = "admin";
    string password = "password"; //небезоп. хран. данных
    printUserAndPassword(admin, password);
    
    char str1 [80], str2 [80]; //переполнение
    std::cout << "Hello, World!" << std::endl;
    gets (str1);
    gets (str2);
    int a = 12;
    strcat(str2, str1);
    
    char str3[32]; //внедрение команд
    if (system(str3))
        cout << "Command processor exists";
    else
        cout << "Command processor doesn't exists";
    
    return 0;
}
