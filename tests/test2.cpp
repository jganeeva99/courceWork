#include <iostream>

using namespace std;

int main(){
    int k; // неиниц. перем.
    for (int j = 0; j < 5; ++j)
        k++;
    
    string userName = ""; //sql
    cout << "Введите имя пользователя: " << endl;
    cin >> userName;
    char* query = "SELECT * FROM users WHERE user_name='" + userName + "';";
    results = submit(query);
    
    FILE * ptrFile = fopen("file.txt", "w"); //некорр. доступ
    
     if (ptrFile != NULL)
     {
       fputs("Пример использования функции fopen ", ptrFile);
       fclose (ptrFile);
     }
   
    int f = 5000000000000; //переполнение
    cout << f << endl;
    
    string passwd = "qetuo"; //небезоп. хран.
    cout << passwd << endl;
    
    char* s; //утечка
    while (true)
    {
        s = new char[20];
        cout << "Hello, world!" << end;
    }
    delete [] s;
    
    return 0;
}
