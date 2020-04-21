#include <iostream> //6
   #include <fstream>
   #include <string>

   using namespace std;
   
   class user {
   public:
   string firstname;
   string lastname;
   string password;
   };

   int main(){
   user A;
   A.firstname = "Ivan";
   A.lastname="Ivanov";
   string password = ""; // пренебрежение безоп хран данн
   cout << "Введите пароль: " << endl;
   cin >> password;
   std::ofstream out("D:\\hello.txt", std::ios::app);
   if (out.is_open())
   {
   out <<A.firstname << ""<< A.lastname << ""<< password<< std::endl;
   }
   out.close();
       
    string file_path = ""; // некорр дост к файлу
    char buf[50];
    cin >> file_path;
    FILE* file = fopen("file_path", "r"); /* в данном месте возникает уязвимость, так нет проверки существования файла (проверка должна осуществляться с помощью функции access) */
    while (!feof(file)) {
    fgets(buf, 50, file);
    cout << buf << endl;
    }
    getchar();
       
    char * test(0); // разыменование 0-го
    std::cout << "Hello, World!" << std::endl;
    std::cout << *test << std::endl;
       
    QSqlDatabase db = QsqlDatabase::addDatabase("QMYSQL", "mydb"); // sql
        db.setHostName("bigblue");
        db.setDatabaseName("flightdb");
        db.setUserName("acarlson");
        db.setPassword("1uTbSbAs");
        bool ok = db.open();
    
        QSqlQuery query;
        scanf("%s", login);
        query.exec("SELECT name, salary FROM employee WHERE login = '" + login + "';"); //
       
    int tmp; // неиниц перем
    cout << tmp << endl;
       
    char *pointer = null; // утечка памяти
    for (int j = 0; j < 10; ++j){
        pointer = new char[100];
    }
    delete [] pointer; /* освобождается только последний блок */
       
   return 0;

   }
