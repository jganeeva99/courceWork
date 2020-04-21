#include <iostream>
class Test{
public:
    int a;
    int b;
    void printData(){
        cout << a << ", " << b << endl;
    }
    int setA(){
        return a;
    }
};
int main(){
    setlocale(LC_ALL, "rus"); // переп буф
    char someText1[10] = "Example!";
    char someText2[10] = "qwerty qwerty";
    cout << "Строка someText1 - \"" << someText1 << "\" \n";
    cout << "Строка someText2 - \"" << someText2 << "\" \n\n";
    strcat(someText1 , someText2); // передаём someText2 в функцию
    cout << "Строка someText1 после объединения с someText2 -\n\"" << someText1 << "\" \n\n";
    
    Test * tst = 0; // разымен нул указ
    cout << "Hello, world!" << endl;
    tst->printData();
    
    FILE * ask = fopen("somefile.txt", "w"); // неккор дост к файл
    if (ask != NULL)
    {
      fprintf(ask, "Запись данной строки в файл");
      fclose(ask);
    }
    
    vector<int> v(5); // переполнение
    for (int i = 0; i < 5; ++i)
        v[i] += 500000000000;
    
    char str2[32]; // внедр ком
    int c=30;
    for (int a =12;a<c;a++)
    {
        scanf("%s", str2);
        for(int i =0; i<2;i++)
            system(str2);
        i--;
    }
    
    char format[32]; // ошиб форм строк
    cout<<"print smth"<<endl;
    scanf("%s", format);
    strlen(format);
    printf(format);
    
    return 0;
}
