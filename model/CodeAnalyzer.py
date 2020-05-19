from model.lexer import *
import copy


class CodeAnalyzer:
    def __init__(self, source):
        self.source = source

    # Обнаружение уязвимостей типа 1:
    def search_buffer_overflow(self):
        error = list()
        not_safe_functions = ['strcpy', 'strncpy', 'sprintf', 'gets', 'strcat', 'scanf']
        for i in range(len(self.source)):
            for f in not_safe_functions:
                if f in self.source[i] and f + '_s' not in self.source[i]:
                    error.append(i)
        return error

    def warn_buffer_overflow(self):
        error = list()
        not_safe_functions = ['scanf']
        for i in range(len(self.source)):
            for f in not_safe_functions:
                if f in self.source[i]:
                    error.append(i)
        return error

    # Обнаружение уязвимостей типа 2:
    def search_format_string_error(self):
        functions = [r'printf', r'sprintf', r'syslog', r'fprintf', r'snprintf']
        error = []
        for i in range(len(self.source)):
            for f in functions:
                if f + '(' in self.source[i] or f + ' (' in self.source[i]:
                    vskobke = self.source[i].split("(")[1].split(")")[0].strip()
                    if "\"" in vskobke:
                        overtext = vskobke.split("\"")[2]
                        for format_letter in ['%c', '%d', '%i', '%s', '%e', '%Е', '%f', '%g', '%G', '%o', '%u', '%x',
                                              '%X', '%р', '%n']:
                            if (format_letter in vskobke) and (not overtext):
                                if i not in error:
                                    error.append(i)
                                break
                    elif vskobke:
                        if i not in error:
                            error.append(i)
                        break
        return error

    def warn_format_string_error(self):
        functions = [r'printf', r'sprintf', r'fprintf', r'snprintf']
        error = []
        for i in range(len(self.source)):
            for f in functions:
                if f + '(' in self.source[i] or f + ' (' in self.source[i]:
                    if i not in error:
                        error.append(i)
        return error

    # Обнаружение уязвимостей типа 3:
    def search_sql_injection(self):
        error = []
        program_code = ""
        variables = []
        for line in self.source:
            program_code += line
        try:
            lexer = Lexer().get_lexer()
            tokens = lexer.lex(program_code)
            for token in tokens:
                if token.gettokentype() == 'VAR' and token.value not in variables:
                    variables.append(token.value)
        except Exception:
            return []

        for i in range(len(self.source)):
            dangerous_variables = []
            if self.source[i].find("scanf") != -1:
                for var in variables:
                    if self.source[i].find(var) != -1:
                        dangerous_variables.append(var)
                for j in range(i, len(self.source)):
                    if self.source[j].find("exec") != -1 and j not in error:
                        flag = False
                        for d_var in dangerous_variables:
                            if self.source[j].find(d_var) != -1:
                                flag = True
                                break
                        if flag:
                            error.append(j)
        if len(error) > 0:
            error.sort()
        return error

    # Обнаружение уязвимостей типа 4:
    def search_command_intrusion(self):
        vulnlist = []
        charmas = []
        danger = ['system', 'popen', 'execlp', 'execvp', '_wsystem']
        for i in range(len(self.source)):
            line = self.source[i]
            if 'char ' in line:
                if '[' and ']' in line:
                    newchar = line.split('char')[1].split('[')[0].strip()
                    charmas.append(newchar)
        for i in range(len(self.source)):
            line = self.source[i]
            for d in danger:
                if d in line and (line.find(d) < line.find('(') < line.find(')')):
                    templine = line.split('(')[1].split(')')[0].strip()
                    command = line.split('(')[0].strip()
                    for char in charmas:
                        if templine.find(char) != -1 and command.find(d) != -1:
                            if i not in vulnlist:
                                vulnlist.append(i)
        return vulnlist

    # Обнаружение уязвимостей типа 5:
    def not_safe_data_store(self):
        words = ['pass', 'password', 'pwd', 'adminpassword', 'passwd', 'secret', 'passphrase', 'crypt', 'cipher',
                 'cypher']
        vulnerabilitylines = []
        for i in range(len(self.source)):
            for word in words:
                line = self.source[i]
                if word in line or word in line.lower():
                    if ('=' in line) or ('==' in line and 'if' in line):
                        tmp = line.split('=')[1].strip()
                        if ('\"' in tmp) or ('\'' in tmp) or ('&' in tmp):
                            if not i in vulnerabilitylines:
                                vulnerabilitylines.append(i)
        return vulnerabilitylines

    # Обнаружение уязвимостей типа 6:
    def memory_leak(self):
        error = []
        program_code = ""
        ptr_types = []
        variables = []
        class_names = []
        dangerous_variables = []

        for line in self.source:
            program_code += line
        try:
            lexer = Lexer().get_lexer()
            tokens = lexer.lex(program_code)

            for token in tokens:
                if token.gettokentype() == 'CLASS':
                    class_names.append(tokens.next().value)
                if token.gettokentype() == 'PTR_TYPE' and token.value not in ptr_types:
                    ptr_types.append(token.value)
                if token.gettokentype() == 'VAR' and token.value not in variables and token.value not in class_names:
                    variables.append(token.value)

        except Exception:
            return []
        for i in range(len(self.source)):
            for ptr_type in ptr_types:
                if self.source[i].find(ptr_type) != -1:
                    for var in variables:
                        if self.source[i].find(var) != -1 and self.source[i].find("=") != -1 and (
                                self.source[i].find("new") != -1 or self.source[i].find("malloc") != -1):
                            dangerous_variables.append(var)
                    for j in range(i, len(self.source)):
                        for d_var in dangerous_variables:
                            if (self.source[j].find("delete") != -1 or self.source[j].find("free") != -1) and \
                                    self.source[j].find(d_var) != -1:
                                dangerous_variables.remove(d_var)
                    if len(dangerous_variables) > 0:
                        error.append(i)
                        dangerous_variables = []
        return error

    # Обнаружение уязвимостей типа 7:
    def search_bad_file_access(self):
        error = []
        safe_functions = ['access']
        files = []
        for i in range(len(self.source)):
            if ('fopen' in self.source[i]) or ('.open' in self.source[i]):
                char_name = self.source[i].split('(')[1]
                char_name = char_name.split(')')[0]
                char_name = char_name.split(',')[0]
                if char_name != "":
                    files.append(char_name)
                for num in range(i - 10, i):
                    if num in range(len(self.source)):
                        for func in safe_functions:
                            if self.source[num].find(func) != -1 and self.source[num].find(char_name) != -1:
                                if char_name in files:
                                    files.remove(char_name)
        for file in files:
            for j in range(len(self.source)):
                if file in self.source[j] and ('fopen(' in self.source[j] or '.open(' in self.source[j]):
                    error.append(j)
        return error

    # Обнаружение уязвимостей типа 8:
    def null_pointer_derefence(self):
        error = []
        program_code = ""
        pointers = []
        safe_pointers = []
        for line in self.source:
            program_code += line
        try:
            lexer = Lexer().get_lexer()
            tokens = lexer.lex(program_code)

            is_pointer_list = False
            for token in tokens:
                if token.gettokentype() == 'PTR_TYPE':
                    is_pointer_list = True
                if token.gettokentype() == 'SEMI_COLON':
                    is_pointer_list = False
                if is_pointer_list and token.gettokentype() == 'VAR':
                    pointers.append(token.value)

        except Exception:
            return []

        for i in range(len(self.source)):
            if self.source[i].find("if") != -1:
                for ptr in pointers:
                    if self.source[i].find(ptr) != -1 and ptr not in safe_pointers:
                        safe_pointers.append(ptr)
            if self.source[i].find("->") != -1:
                for ptr in pointers:
                    if self.source[i].find(ptr) != -1 and ptr not in safe_pointers:
                        error.append(i)
        return error

    # Обнаружение уязвимостей типа 9:
    def number_overflow(self):
        def toInt(num, numbermas, numvalmas):
            if num in numbermas:
                out = numvalmas[numbermas.index(num)]
            else:
                try:
                    out = int(num)
                except Exception:
                    out = -1
            return out

        def scissors(line, numbermas, numvalmas):
            tmp = toInt(line, numbermas, numvalmas)
            if tmp != -1:
                return tmp
            else:
                if ' + ' in line:
                    f = scissors(line.split("+", 1)[0].strip(), numbermas, numvalmas)
                    s = scissors(line.split("+", 1)[1].strip(), numbermas, numvalmas)
                    return f + s
                elif ' - ' in line:
                    f = scissors(line.split("-", 1)[0].strip(), numbermas, numvalmas)
                    s = scissors(line.split("-", 1)[1].strip(), numbermas, numvalmas)
                    return f - s
                elif ' * ' in line:
                    f = scissors(line.split("*", 1)[0].strip(), numbermas, numvalmas)
                    s = scissors(line.split("*", 1)[1].strip(), numbermas, numvalmas)
                    return f * s
                elif ' / ' in line:
                    f = scissors(line.split("/", 1)[0].strip(), numbermas, numvalmas)
                    s = scissors(line.split("/", 1)[1].strip(), numbermas, numvalmas)
                    return f // s
                else:
                    return -1

        error = []
        # warnings = []
        numbers = []
        numervalues = []
        numberplaces = []
        int_max_val = 2147483647
        code_backup = copy.deepcopy(self.source)
        for i in range(len(self.source)):
            if 'int ' in self.source[i]:
                if 'main' not in self.source[i] and 'for' not in self.source[i] and ' ' in self.source[i]:
                    newint = 'error!'
                    startval = -1
                    if '=' not in self.source[i]:
                        newint = self.source[i].replace('int ', '', 1).split(';')[0].strip()
                        startval = 0
                    else:
                        newint = self.source[i].replace('int ', '', 1).split('=')[0].strip()
                        startval = scissors(self.source[i].split("=")[1].split(";")[0].strip(), numbers, numervalues)
                        self.source[i] = self.source[i].replace('=', '', 1)
                    numbers.append(newint)
                    numberplaces.append(i)
                    numervalues.append(startval)
                elif 'for ' in self.source[i]:
                    znak = self.source[i].split(";")[1]
                    if ('>' in znak) and ('++' or '+=' in self.source[i]):
                        if '*=' in self.source[i]:
                            a = toInt(self.source[i].split(";")[0].split('=')[1].strip(), numbers, numervalues)
                            b = toInt(self.source[i].split(";")[1].split('>')[1].strip(), numbers, numervalues)
                            mnozh = self.source[i].split(";")[2].split('*=')[1].split(')')[0].strip()
                            mnozh2 = toInt(mnozh, numbers, numervalues)
                            if mnozh2 == -1:
                                mnozh = float(mnozh)
                            else:
                                mnozh = mnozh2
                            if a > b and mnozh > 1:
                                error.append(i)
                        elif '+=':
                            a = toInt(self.source[i].split(";")[0].split('=')[1].strip(), numbers, numervalues)
                            b = toInt(self.source[i].split(";")[1].split('>')[1].strip(), numbers, numervalues)
                            if a > b:
                                error.append(i)
                    elif '<' in znak:
                        a = toInt(self.source[i].split(";")[0].split('=')[1].strip(), numbers, numervalues)
                        b = toInt(self.source[i].split(";")[1].split('<')[1].strip(), numbers, numervalues)
                        if a < b and '--' in self.source[i]:
                            error.append(i)
        for i in range(len(self.source)):
            for inta in numbers:
                if (inta + ' ' in self.source[i]) and (self.source[i].find(inta) < self.source[i].find('=')):
                    if ' += ' in self.source[i]:
                        addval = scissors(self.source[i].split("=")[1].split(";")[0].strip(), numbers, numervalues)
                        numervalues[numbers.index(inta)] += addval
                    elif ' -= ' in self.source[i]:
                        addval = scissors(self.source[i].split("=")[1].split(";")[0].strip(), numbers, numervalues)
                        numervalues[numbers.index(inta)] -= addval
                    elif ' = ' in self.source[i]:
                        numervalues[numbers.index(inta)] = scissors(self.source[i].split("=")[1].split(";")[0].strip(),
                                                                    numbers, numervalues)
                    elif ' *= ' in self.source[i]:
                        addval = scissors(self.source[i].split("=")[1].split(";")[0].strip(), numbers, numervalues)
                        numervalues[numbers.index(inta)] *= addval
                    elif ' /= ' in self.source[i]:
                        addval = scissors(self.source[i].split("=")[1].split(";")[0].strip(), numbers, numervalues)
                        numervalues[numbers.index(inta)] /= addval
        for i in range(len(numbers)):
            if abs(numervalues[i]) > int_max_val:
                error.append(numberplaces[i])
        self.source = copy.deepcopy(code_backup)
        return error

    # Обнаружение уязвимостей типа 10:
    def search_race_condition(self):
        error = []
        self.thread_funcs = []
        self.global_vars = []
        self.global_vars_in_thread = []
        self.global_vars_all = []
        for s in self.source:
            if r"pthread_create" in s or r"CreateThread" in s:
                self.thread_funcs.append(s.split('(', 1)[1].split(',')[2].strip().replace('&', ''))
        for s in self.source:
            if '(' in s:
                if self.global_vars == []:
                    return error
                else:
                    break
            if 'int' in s or 'double' in s:
                for v in s.strip().split(' ', 1)[1][:-1].split(','):
                    v1 = v.split('=')[0].strip()
                    self.global_vars.append(v1)
                    self.global_vars_in_thread.append(False)
        open_brackets = 0
        find_thread = False
        for i in range(len(self.source)):
            for j in range(len(self.thread_funcs)):
                if "{0}(".format(self.thread_funcs[j]) in self.source[i]:
                    find_thread = True
            if "{" in self.source[i]:
                open_brackets += 1
            if "}" in self.source[i]:
                open_brackets -= 1
                find_thread = False
            if ("=" in self.source[i] or "++" in self.source[i] or "--" in self.source[i]) and open_brackets > 0:
                for k in range(len(self.global_vars)):
                    if self.source[i].strip()[0] == self.global_vars[k]:
                        error.append(i)
                        self.global_vars_all.append(self.global_vars[k])
                        if find_thread:
                            self.global_vars_in_thread[k] = True
        for k in range(len(self.global_vars)):
            if self.global_vars_all.count(self.global_vars[k]) == 1 or self.global_vars_in_thread[k] == False:
                for i in range(self.global_vars_all.count(self.global_vars[k])):
                    error[self.global_vars_all.index(self.global_vars[k])] = -1
                    self.global_vars_all[self.global_vars_all.index(self.global_vars[k])] = ''
        while error.count(-1) > 0:
            error.remove(-1)
        return error

    # Обнаружение уязвимостей типа 11:
    def incorr_rw_synchr(self):
        program_code = ""
        global_vars = []
        thread_funcs = []
        start_main = False
        start_func = False
        start_var = False

        for s in self.source:
            if r"pthread_create" in s or r"CreateThread" in s:
                thread_funcs.append(s.split('(', 1)[1].split(',')[2].strip().replace('&', ''))

        for line in self.source:
            program_code += line
        try:
            lexer = Lexer().get_lexer()
            tokens = lexer.lex(program_code)

            for token in tokens:
                if token.gettokentype() == 'INT' or token.gettokentype() == 'BOOL' or token.gettokentype() == 'STRING_TYPE' or token.gettokentype() == 'AT':
                    start_var = True
                    continue
                if token.gettokentype() == 'SEMI_COLON':
                    start_var = False
                    continue
                if token.gettokentype() == 'OPEN_PAREN' and start_var:
                    start_var = False
                    continue
                if token.gettokentype() == 'MAIN':
                    start_main = True
                    continue
                if token.gettokentype() == 'OPEN_BRACE':
                    start_func = True
                    continue
                if token.gettokentype() == 'CLOSE_BRACE':
                    start_func = False
                    continue

                if start_var and token.gettokentype() == 'VAR' and token.value not in global_vars and not start_main and \
                        not start_func:
                    global_vars.append(token.value)
        except Exception:
            return []
        start_main = False
        start_func = False
        cnt = 0
        error = list()
        for i in range(len(self.source)):
            if 'main' in self.source[i]:
                start_main = True
            for func in thread_funcs:
                if func in self.source[i]:
                    start_func = True
            if '{' in self.source[i]:
                cnt += 1
            if '}' in self.source[i]:
                if cnt == 0:
                    start_func = False
                cnt -= 1
            if start_func and cnt > 0 and not start_main:
                for var in global_vars:
                    if var in self.source[i] and ('load' not in self.source[i] and 'store' not in self.source[i]):
                        error.append(i)
        mutexs = list()
        for i in range(len(self.source)):
            if "pthread_mutex_t" in self.source[i]:
                mutexs.append(self.source[i].split(" ")[1].split(";")[0]);
        mutex_count_dict = dict(zip(mutexs, len(mutexs) * [0]));
        last_dict = dict(zip(mutexs, len(mutexs) * [0]));
        for i in range(len(self.source)):
            if "pthread_mutex_lock" in self.source[i]:
                mutex_name = self.source[i].split("&")[1].split(")")[0];
                last_dict[mutex_name] = i;
                if (mutex_count_dict[mutex_name] == 0):
                    mutex_count_dict[mutex_name] += 1;
                else:
                    error.append(i);
            if "pthread_mutex_unlock" in self.source[i]:
                mutex_name = self.source[i].split("&")[1].split(")")[0];
                if (mutex_count_dict[mutex_name] == 1):
                    mutex_count_dict[mutex_name] -= 1;
                else:
                    error.append(i)
        for keyvalue in mutex_count_dict.items():
            key, value = keyvalue[0], keyvalue[1]
            if value != 0 and last_dict[key] not in error:
                error.append(last_dict[key])
        return error

    # Обнаружение уязвимостей типа 12:
    def search_uninitialized_variable(self):
        error = list()
        for i in range(len(self.source)):
            n = 0
            if "int " in self.source[i] \
                    or "float " in self.source[i] \
                    or "double " in self.source[i] \
                    or "bool " in self.source[i] \
                    or "char " in self.source[i]:
                n += 1
                for j in self.source[i]:
                    if j == '(' or j == '{':
                        n = 0
                        break
                    if j == ',':
                        n += 1
                    if j == '=':
                        n -= 1
            if n > 0:
                error.append(i)
        return error


if __name__ == "__main__":
    file = open("../tests/test113.cpp", mode="r", encoding="utf8")
    source = []
    for line in file:
         source.append(line)
    codeA = CodeAnalyzer(source)
    codeA.incorr_rw_synchr()
