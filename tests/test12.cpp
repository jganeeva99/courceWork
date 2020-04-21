#include <iostream> // 7
using namespace std;
  
void func_to_show_mem_leak()
{
    int* ptr = new int(5);
    cout << "Hello!";
    return;
}
  
int main()
{
    
    FILE * ptrFile = fopen( "example.txt" , "w" ); // некорр дост к ф
    fputs( "This is sample." , ptrFile );
    fseek( ptrFile , 9 , SEEK_SET );
    fputs( "parta" , ptrFile );

    fclose ( ptrFile );
    func_to_show_mem_leak(); // утечка
    
    string password = "qwerty"; // небез хран
    cout << password << endl;
    int sum = 0;
    for (int i = 0; i < 5; ++i)
        sum += i;
    cout << sum << endl;
    string pass = "123456789";
    
    int *node;
    node = (int *) malloc(8); // утечка
    int j = 5;
    cout << j << endl;
    char *login = new char(50);
    
    FILE *file; // некорр дост к ф
       struct food {
           char name[20];
           unsigned qty;
           float price;
       };
       struct food shop[10];
       char i=0;
       file = fopen("fscanf.txt", "r");
       while (fscanf (file, "%s%u%f", shop[i].name, &(shop[i].qty), &(shop[i].price)) != EOF) {
           printf("%s %u %.2f\n", shop[i].name, shop[i].qty, shop[i].price);
           i++;
       }
    
    int b = 5; // разыменов
    int *a = &b;
    cout << *a << endl;
    a = 0;
    cout << *a << endl;
    
    return 0;
}
