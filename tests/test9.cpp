#include <iostream>
#include <string>
using namespace std;
class user{
    public:
    string pwd;
    void print() {
    cout << pwd;
    }
};

int main(){
    user u1("qwerty"); // пренебр без хран
    string pass = u1.pwd;
    cout << pass;
    
    int h = 0; // переп
    while (h == 0){
        cout << "Введите число :" << endl;
        cin >> h;
    }
    int result = 2147080000*h;
    
    FILE *file; // некорр дост к ф
    char arr[80];
    file = fopen("fscanf.txt", "r");
    while (fgets (arr, N, file) != NULL)
        printf("%s", arr);
    fclose(file);
    
    int *a = NULL; // разымен нулев *
    int *b = NULL;
    *b = 5;
    cout << *a << " " << *b << endl;
    
    double *y = NULL; // разым нул *
    cout << *y << endl;
    
    FILE * pFile; // ошиб форм стр
    int n;
    char name [100];
    pFile = fopen ("myfile.txt","w");
    puts ("please, enter a name: ");
    gets (name);
    fprintf (pFile, "Name %d %s",n,name);
    fclose (pFile);
    
    return 0;
}
