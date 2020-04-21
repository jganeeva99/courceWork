#include <stdio.h>

int main(){
    char i[2]; // ошибка форм. стр.
    scanf("%s", i);
    printf(i);
    
    char str2[32]; //внедрение команд
    system("ds");
    system("help");
    system("help");
    system("help");
    system("help");
    scanf("%s", str2);
    system("help");
    system("help");
    system("help");
    system("help");
    system(str2);
    
    char buffer [20]; // переполнение
    int n, a=1000000, b=1000000;
    n=sprintf (buffer, "%d plus %d is %d", a, b, a+b);
    printf ("[%s] is a string %d chars long\n",buffer,n);
    
    int * p = new int; // утечка
    delete p;
    int * q = new int;
    
    int i = 2147483647; //переполнение
    i=i+2;
    
    std::ifstream file; // некорректный доступ к файлу
    string s;
    getline(file,s);
    cout << s << endl;
    
    return 0;
}

