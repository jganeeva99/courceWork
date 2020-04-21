#include <iostream> // 3
using namespace std;

class TestClass {
public:
int x;
int y;
};

int main() {
TestClass* ptr1 = new TestClass();// утечка пам
TestClass* ptr2 = (TestClass*)malloc(sizeof(TestClass));
delete ptr1;
TestClass* ptr3 = new TestClass();
TestClass* ptr4 = new TestClass();
    
char c[10]; // ошиб форм стр
int a=0,b=2;
a=a*b;
b=b/2+b;
gets(c);
printf("%d%d%s",a,b,c);
    
char str[80]; // переполн буф
int i=0, a=0;
scanf("%d", &i);
cout<<"good!"<<endl;
a = a+i;
scanf ("%s", str);

char str2[32]; // внедр ком
string a ="cd";
int k=30;
scanf("%s", str2);
for (int a =12;a<18;a++)
{
    for(int i =0; i<2;i++)
        scanf("%d",k)
    i--;
}
system(str2);
    
string adminpassword = "ytrewq"; // пренебр без хран
int sum = 0;
cout << sum + 100 << endl;
    
int i = 2147083600; // переполнение целых чисел
int j = 2147;
int l;
l = i*j;
    
return 0;
}
