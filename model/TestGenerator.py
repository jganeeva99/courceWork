from typing import List
import random

class TestGenerator:
    def __init__(self):
        self.err_code1 = ['char buf[100];' + '\n' + 'strcpy(buf, argv[1]);' + '\n',
                          'char str1[10], str2[15];' + '\n' + 'gets(str1);' + '\n' + 'gets(str2)' + '\n' + 'strcat(str1, str2);' + '\n',
                          'char src[5] = "hi";' + '\n' + 'char dst[5] = "Ray";' + '\n' + 'strcat(src, dst);' + '\n',
                          'char t1[1] = "o";' + '\n' + 'char t2[1] = "k";' + '\n' + 'strcat(t1, t2);' + '\n']
        self.err_code2 = ['char f[32];' + '\n' + 'scanf("%s", f);' + '\n' + 'printf(f);' + '\n',
                          'char fs[15];' + '\n' + 'gets(str);' + '\n' + 'int t = 23, b = 45;' + '\n' + 'sprintf(fs, "%s %d %d", fs, t, b);' + '\n']
        self.err_code3 = ['QSqlDatabase db = QsqlDatabase::addDatabase("SQL", "db");' + '\n' + 'db.setHostName("rtg");' + '\n' + 'db.setDatabaseName("ghtdb");' + '\n' + 'db.setUserName("lily");' + '\n' + 'db.setPassword("4gdjstf6");' + '\n' + 'bool ok = db.open();' + '\n' + 'QSqlQuery query;' + '\n' + 'scanf("%s", login);' + '\n' + 'query.exec("SELECT name, salary FROM dbtbl WHERE login = '" + login + "';");' + '\n']
        self.err_code4 = ['char *s1 = "dir";' + '\n' + 'char s2[32];' + '\n' + 'scanf("%s", s2);' + '\n' + 'system(s2);' + '\n',
                          'char str[];' + '\n' + 'system(str);' + '\n',
                          'char i1[];' + '\n' + 'system(i1);' + '\n',
                          'chat call[45];' + '\n' + 'system("help");' + '\n' + 'system("ds");' + '\n' + 'system(call);' + '\n']
        self.err_code5 = ['string password = "";' + '\n',
                          'string pass = "";' + '\n',
                          'string pwd = "";' + '\n',
                          'string adminpassword = "";' + '\n',
                          'string passwd = "";' + '\n',
                          'string secret = "";' + '\n',
                          'string passphrase = "";' + '\n',
                          'string crypt = "";' + '\n',
                          'string cipher = "";' + '\n']
        self.err_code6 = ['char *prt = NULL;' + '\n' + 'ptr = new char[10];' + '\n' + 'char *ptr_new = NULL;' + '\n' + 'ptr_new = new char[10];' + '\n' + 'delete [] ptr_new;' + '\n',
                          'int * p = new int;' + '\n' + 'double * w = new double;' + '\n' + 'delete p;' + '\n']
        self.err_code7 = ['char *filename = "file.txt";' + '\n' + 'FILE * ptrFile = fopen(filename, "w");' + '\n']
        self.err_code8 = ['#include <iostream>' + '\n\n' + 'class Y {' + '\n' + 'int y;' + '\n' + 'public:' + '\n' + 'void test() {' + '\n' + 'cout << y;' + '\n' + '}' + '\n' + '};' + '\n\n' + 'int main() {' + '\n' + 'Y* i = 0;' + '\n' + 'i->test();' + '\n',
                          '#include <iostream>' + '\n\n' + 'class book {' + '\n' + 'public:' + '\n' + 'int cnt;' + '\n' + 'int sales;' + '\n' + 'int res(){' + '\n' + 'return cnt*sales;' + '\n' + '}};' + '\n' + 'int main(){\nbook *b1 = 0;\nb1->res();\n']
        self.err_code9 = ['int i = 2147483600;' + '\n' + 'i += 10000;' + '\n',
                          'int f = 5060007080900;' + '\n' + 'cout << f << endl;',
                          'int d = 100000;' + '\n' + 'int e = d + 92000000450000;' + '\n',
                          'int h = 0;' + '\n' + 'for (int i = 0; i < 10000; ++i){' + '\n' + 'h = h + 304567767542;' + '\n' + '}' + '\n',
                          'int pl = 8989787876544;' + '\n',
                          'int o1 = 123456789876543;' + '\n']
        self.err_code10 = ['#include <iostream>' + '\n' + 'using namespace std;' + '\n' + 'int x = 10;\n int c = 2;\n\n void f1(void* tmp){ \nx++;\n}\nvoid f2(void* tmp){\nif(x % 2 == 0) {\nx = 0;\nprintf("x = %d", x);\n}\n}\nvoid f(void *tmp){\nc--;\n}\nint main(){\nDWORD th1, th2, th3;\n\nfor(int k = 0; k < 3; k++)\nCreateThread(NULL, 0, f1, NULL, 0, NULL);\nx = 0;\nprint("%d", x);\nwhile(1){\n c++;\n}\n']
        self.err_code11 = ['#include <stdio.h>\n#include <string.h>\n#include <pthread.h>\n#include <stdlib.h>\n#include <unistd.h>\n\npthread_t tidFReader;\npthread_t tidSReader;\npthread_t tidFWriter;\npthread_t tidSWriter;\n\nint g;\npthread_mutex_t lock;\nvoid* FirstReader(void *arg){\nwhile(1) {\npthread_mutex_lock(&lock);\nfor (i = 0; i<10; i++)\n printf("%d", g);\nprintf("%d\n", g * 2);\npthread_mutex_unlock(&lock);\n}\n}\nvoid* SecondReader(void *arg){\nwhile (1) {\npthread_mutex_lock(&lock);\nprintf("%d\n", g);\npthread_mutex_unlock(&lock);\n}}\nvoid* FirstWriter(void *arg){\nwhile(1) {\npthread_mutex_lock(&lock);\nfor (i = 0; i<10; i++);\n g += i;\npthread_mutex_unlock(&lock);\n}}\nvoid* SecondWriter(void *arg){\nwhile(1) {\npthread_mutex_lock(&lock);\nfor (i = 0; i<10; i++);\n g *= 2;\n}}\nint main(){\nint i = 0;\nint err;\n\nif(pthread_mutex_init(&lock, NULL) != 0){\nprintf("\n mutex init failed\n");\nreturn 1;\n}\n\nerr = pthread_create(&(tidFReader), NULL, &FirstReader, NULL);\nerr = pthread_create(&(tidSReader), NULL, &SecondReader, NULL);\nerr = pthread_create(&(tidFWriter), NULL, &FirstWriter, NULL);\nerr = pthread_create(&(tidSWriter), NULL, &SecondWriter, NULL);\n\npthread_join(tidFReader, NULL);\npthread_join(tidSReader, NULL);\npthread_join(tidFWriter, NULL);\npthread_join(tidSWriter, NULL);\n\npthread_mutex_destroy(&lock);\n']
        self.err_code12 = ['int i;' + '\n' + 'cout << i << endl' + '\n',
                           'int i;' + '\n' + 'for (auto j = 0; j < 10; ++j){' + '\n' + 'i += 1;' + '}' + '\n',
                           'char buf[];' + '\n' + 'for (int i = 0; i < 5; ++i){' + '\n' + 'cout << buf[i] << " ";' + '\n',
                           'int ff;' + '\n' + 'ff *= 77;' + '\n',
                           'int temp;' + '\n' + 'cout << temp << endl;' + '\n',
                           'int x,y,z;' + '\n' + 'z = x + 3;' + '\n']
        self.right_code = ['int i = 0;' + '\n' + 'cout << i << endl;' + '\n',
                           'cout << Hello, world << endl' + '\n',
                           'for (int j = 0; j < 5; ++j){' + '\n'
                           + 'cout << j << endl;' + '\n' + '}' + '\n',
                           'int k = 2;' + '\n' + 'k += 1;' + '\n',
                           'char *ptr = NULL;' + '\n' + 'ptr = new char[32];' + '\n' + 'delete [] ptr;' + '\n',
                           'int a = 11;' + '\n' + 'int b = 23;' + '\n' + 'int c = a + b;' + '\n',
                           'double pi = 3.14;' + '\n',
                           'float exp = 2.7;' + '\n'
                           'cout << "Hello!" << endl;' + '\n',
                           'int i = 5;' + '\n' + 'while(i > 0){' + '\n' + 'cout << i << " ";' + '\n' + '}' + '\n',
                           'bool tr = 1;' + '\n',
                           'bool fls = 0;' + '\n',
                           'int l1 = 2;' + '\n' + 'int l2 = 5;' + '\n' + 'int _res = l1*l2;' + '\n']
        self.d1 = []
        self.d2 = []
        self.d3 = []
        self.d4 = []
        self.d5 = []
        self.d6 = []
        self.d7 = []
        self.d8 = []
        self.d9 = []
        self.d10 = []
        self.d11 = []
        self.d12 = []
        self.list_err = [self.err_code1, self.err_code2, self.err_code3, self.err_code4,
                         self.err_code5, self.err_code6, self.err_code7, self.err_code8,
                         self.err_code9, self.err_code10, self.err_code11, self.err_code12]
        self.d = [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9, self.d10, self.d11,
                  self.d12]

    def generateTests(self):
        raund = random.randint(1, 5)  # число генераций кода
        w_r = []  # индексы правильных тестовых вариантов, которые были
        f = open('/Users/jganeeva/Desktop/test.cpp', 'tw', encoding='utf-8')
        f.write('#include <iostream>' + '\n' + 'using namespace std;' + '\n\n' + 'int main(){' + '\n')
        flag = 1
        flag1 = 1
        for i in range(raund):
            k = random.randint(1, 9)  # i опредлеяет, вставлять ошибочный код или нет
            k = k % 2
            if k == 1:
                x = random.choice(self.list_err)
                j = self.list_err.index(x)
                if j == 0:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d1:
                        self.d1.append(k)
                        f.write(y)
                elif j == 1:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d2:
                        self.d2.append(k)
                        f.write(y)
                elif j == 2:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d3:
                        self.d3.append(k)
                        f.write(y)
                elif j == 3:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d4:
                        self.d4.append(k)
                        f.write(y)
                elif j == 4:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d5:
                        self.d5.append(k)
                        f.write(y)
                elif j == 5:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d6:
                        self.d6.append(k)
                        f.write(y)
                elif j == 6:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d7:
                        self.d7.append(k)
                        f.write(y)
                elif j == 7 and flag == 1 and flag1 == 1:
                    f = open('/Users/jganeeva/Desktop/test.cpp', 'tw', encoding='utf-8')
                    y = random.choice(x)
                    f.write(y)
                    flag = 0
                elif j == 8:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d9:
                        self.d9.append(k)
                        f.write(y)
                elif j == 9 and flag1 == 1 and flag == 1:
                    f = open('/Users/jganeeva/Desktop/test.cpp', 'tw', encoding='utf-8')
                    y = random.choice(x)
                    f.write(y)
                    flag1 = 0
                elif j == 10:
                    pass
                elif j == 11:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d12:
                        self.d12.append(k)
                        f.write(y)
            else:
                z = random.choice(self.right_code)
                ind = self.right_code.index(z)
                if ind not in w_r:
                    w_r.append(ind)
                    f.write(z)
        f.write('return 0;' + '\n' + '}')
        f.close()
