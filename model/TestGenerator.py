from typing import List
import random

class TestGenerator:
    def __init__(self):
        self.err_code1 = ['char buf[100];' + '\n' + 'strcpy(buf, argv[1]);' + '\n']
        self.err_code2 = ['char f[32];' + '\n' + 'scanf("%s", f);' + '\n' + 'printf(f);' + '\n']
        self.err_code3 = ['char *query = "SELECT * FROM users WHERE user_name'" + userName + "';";"' + '\n' + 'char *results = submit(query);' + '\n']
        self.err_code4 = ['char *s1 = "dir";' + '\n' + 'char s2[32];' + '\n' + 'scanf("%s", s2);' + '\n' + 'system(s2);' + '\n',
                          'char str[];' + '\n' + 'system(str);' + '\n']
        self.err_code5 = ['string password = "";' + '\n',
                          'string pass = "";' + '\n',
                          'string pwd = "";' + '\n',
                          'string adminpassword = "";' + '\n',
                          'string passwd = "";' + '\n',
                          'string secret = "";' + '\n',
                          'string passphrase = "";' + '\n',
                          'string crypt = "";' + '\n',
                          'string cipher = "";' + '\n']
        self.err_code6 = ['char *prt = NULL;' + '\n' + 'ptr = new char[10];' + '\n' + 'char *ptr_new = NULL;' + '\n' + 'ptr_new = new char[10];' + '\n' + 'delete [] ptr_new;' + '\n']
        self.err_code7 = ['ifstream f;' + '\n' + 'string str;' + '\n' + 'getline(f,s)' + '\n' + 'cout << s;' + '\n']
        self.err_code8 = ['char *test(0);' + '\n' + 'cout << "Hello, World!" << endl' + '\n' + 'cout << *test << endl;' + '\n']
        self.err_code9 = ['int i = 2147483600;' + '\n' + 'i += 10000;' + '\n']
        self.err_code10 = []
        self.err_code11 = []
        self.err_code12 = ['int i;' + '\n' + 'cout << i << endl' + '\n',
                           'int i;' + '\n' + 'for (auto j = 0; j < 10; ++j){' + '\n' + 'i += 1;' + '}' + '\n',
                           'int d = 100000;' + '\n' + 'int e = d*920000000000;' + '\n']
        self.right_code = ['int i = 0;' + '\n' + 'cout << i << endl;' + '\n',
                           'cout << Hello, world << endl' + '\n',
                           'for (int j = 0; j < 5; ++j){' + '\n'
                           + 'cout << j << endl;' + '\n' + '}' + '\n',
                           'int k = 2;' + '\n' + 'k += 1;' + '\n',
                           'char *ptr = NULL;' + '\n' + 'ptr = new char[32];' + '\n' + 'delete [] ptr;' + '\n',
                           'int a = 11;' + '\n' + 'int b = 23;' + '\n' + 'int c = a + b;' + '\n']
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
                elif j == 7:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d8:
                        self.d8.append(k)
                        f.write(y)
                elif j == 8:
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d9:
                        self.d9.append(k)
                        f.write(y)
                elif j == 9:
                    pass
                    '''
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d10:
                        self.d10.append(k)
                        f.write(y)'''
                elif j == 10:
                    pass
                    '''
                    y = random.choice(x)
                    k = x.index(y)
                    if k not in self.d11:
                        self.d11.append(k)
                        f.write(y)'''
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
