import sys
from idaapi import *


bp1 = 0x004010C5

add_bpt(bp1, 0, BPT_SOFT)
enable_bpt(bp1, True)

flag = ""

v4 = regval_t()
v7 = regval_t()
v11 = regval_t()

StartDebugger("", "", "")

print("------------------------------------------------------")
print("[+] Finding flag... wait")
print("------------------------------------------------------")


for i in range(37):
    continue_process()
    GetDebuggerEvent(WFNE_SUSP, -1)

    get_reg_val('BX', v4)
    get_reg_val('EDI', v7)

    v4_val = v4.ival
    v7_val = v7.ival

    v11_val = get_byte(v7_val)
    v11.ival = v11_val

    keychar = (v11_val - 1 - (1 << (v4_val & 3))) ^ 0xC7

    sys.stdout.write("%c" % keychar)

    flag = flag + chr(keychar)

    set_reg_val('AX', v11)

print("")
print("------------------------------------------------------")
print("[+] Successfully found flag!")
print("[+] flag_{%s}" % flag)
print("------------------------------------------------------")

