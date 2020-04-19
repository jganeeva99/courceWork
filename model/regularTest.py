class regularTest:
    def __init__(self):
        self.err_code1 = ['char buf[100];' + '\n' + 'strcpy(buf, argv[1]);' + '\n']
        self.err_code2 = ['char f[32];' + '\n' + 'scanf("%s", f);' + '\n' + 'printf(f);' + '\n']
        self.err_code3 = [
            'char *query = "SELECT * FROM users WHERE user_name'" + userName + "';";";' + '\n' + 'char *results = submit(query);' + '\n']
        self.err_code4 = [
            'char *s1 = "dir";' + '\n' + 'char s2[32];' + '\n' + 'scanf("%s", s2);' + '\n' + 'system(s2);' + '\n',
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
        self.err_code6 = [
            'char *prt = NULL;' + '\n' + 'ptr = new char[10];' + '\n' + 'char *ptr_new = NULL;' + '\n' + 'ptr_new = new char[10];' + '\n' + 'delete [] ptr_new;' + '\n']
        self.err_code7 = ['ifstream f;' + '\n' + 'string str;' + '\n' + 'getline(f,s)' + '\n' + 'cout << s;' + '\n']
        self.err_code8 = [
            'char *test(0);' + '\n' + 'cout << "Hello, World!" << endl' + '\n' + 'cout << *test << endl;' + '\n']
        self.err_code9 = ['int i = 2147483600;' + '\n' + 'i += 10000;' + '\n']
        self.err_code10 = []
        self.err_code11 = []
        self.err_code12 = ['int i;' + '\n' + 'cout << i << endl' + '\n',
                           'int i;' + '\n' + 'for (auto j = 0; j < 10; ++j){' + '\n' + 'i += 1;' + '}' + '\n',
                           'int d = 100000;' + '\n' + 'int e = d*920000000000;' + '\n']
        self.right_code = ['int i = 0;' + '\n' + 'cout << i << endl;' + '\n',
                           'cout << "Hello, world" << endl;' + '\n',
                           'for (int j = 0; j < 5; ++j){' + '\n'
                           + 'cout << j << endl;' + '\n' + '}' + '\n',
                           'int k = 2;' + '\n' + 'k += 1;' + '\n',
                           'char *ptr = NULL;' + '\n' + 'ptr = new char[32];' + '\n' + 'delete [] ptr;' + '\n',
                           'int a = 11;' + '\n' + 'int b = 23;' + '\n' + 'int c = a + b;' + '\n']

    def generateTest(self):
            k = 4
            i = 0
            i_ind = 0
            j = 0
            j_ind = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ind1 = 0
            f = open('/Users/jganeeva/Desktop/test.cpp', 'tw', encoding='utf-8')
            f.write('#include <iostream>' + '\n' + 'using namespace std;' + '\n\n' + 'int main(){' + '\n')
            for inc in range(k):
                i = i + 1
                i_inc = i % 2
                if i_inc == 1:
                    j = j + 1
                    j_inc = j % 12
                    if j_inc == 0:
                        y = self.err_code1[j_ind[0]]
                        j_ind[0] = (j_ind[0] + 1) % (len(self.err_code1))
                        f.write(y)
                    elif j_inc == 1:
                        y = self.err_code2[j_ind[1]]
                        j_ind[1] = (j_ind[1] + 1) % (len(self.err_code2))
                        f.write(y)
                    elif j_inc == 2:
                        y = self.err_code3[j_ind[2]]
                        j_ind[2] = (j_ind[2] + 1) % (len(self.err_code3))
                        f.write(y)
                    elif j_inc == 3:
                        y = self.err_code4[j_ind[3]]
                        j_ind[3] = (j_ind[3] + 1) % (len(self.err_code4))
                        f.write(y)
                    elif j_inc == 4:
                        y = self.err_code5[j_ind[4]]
                        j_ind[4] = (j_ind[4] + 1) % (len(self.err_code5))
                        f.write(y)
                    elif j_inc == 5:
                        y = self.err_code6[j_ind[5]]
                        j_ind[5] = (j_ind[5] + 1) % (len(self.err_code6))
                        f.write(y)
                    elif j_inc == 6:
                        y = self.err_code7[j_ind[6]]
                        j_ind[6] = (j_ind[6] + 1) % (len(self.err_code7))
                        f.write(y)
                    elif j_inc == 7:
                        y = self.err_code8[j_ind[7]]
                        j_ind[7] = (j_ind[7] + 1) % (len(self.err_code8))
                        f.write(y)
                    elif j_inc == 8:
                        y = self.err_code9[j_ind[8]]
                        j_ind[8] = (j_ind[8] + 1) % (len(self.err_code9))
                        f.write(y)
                    elif j_inc == 9:
                        pass
                    elif j_inc == 10:
                        pass
                    elif j_inc == 11:
                        y = self.err_code12[j_ind[11]]
                        j_ind[11] = (j_ind[11] + 1) % (len(self.err_code12))
                        f.write(y)
                else:
                    y = self.right_code[i_ind]
                    i_ind = (i_ind + 1) % (len(self.right_code))
                    f.write(y)
            f.write('return 0;' + '\n' + '}')
            f.close()
