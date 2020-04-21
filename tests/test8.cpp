#include <stdio.h>

void run_test(int i)
{
  int delta = 123;
  char* mem = malloc(1024);
  strcpy(mem, "i = ");
  printf("%s %d\n", mem, i + delta);
}

int main ()
{
    char str[80]; // ошиб форм стр
    gets(str);
    int a =5, b=null;
    sprintf (str, "%s %d %d",str, a,b);
    
    char buf[100]; // переп буф
    int c =12;
    c++;
    strcpy(buf, argv[1]);
    
    char app[15]="вторая строка "; // переп буф
    char dst[15]="первая строка";
    strcat (dst, app);
    printf ("dst: %s\n",dst);
            
    char* str1 = "dir"; // внедр ком
    string s = "";
    std::cin >> s;
    int i=10;
    while (i>0)
    {
        system(s);
        i--;
    }
        
    int r; // неиниц перем
    r++;
    r += 456;
    cout << "Hello, world!" << endl;
    r--;
            
    int i; // утечка
    for(i = 0; i < 10; i++)
      run_test(i);
    
    return 0;
}

