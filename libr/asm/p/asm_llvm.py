# Asm plugin for LLVM
# ===========================================

import r2lang

def asm_llvm(a):
    def assemble(s):
        print("Assembling %s"%(s))
        return [ 1, 2, 3, 4 ]

    def disassemble(buf):
        try:
            return [ 2, "opcode %d" % (ord(buf[0])) ]
        except:
            print("err")
            print(sys.exc_info())
            return [ 2, "opcode" ]

    return {
        "name": "llvm",
        "arch": "llvm",
        "bits": 32,
        "license": "GPL",
        "desc": "LLVM Disassembler Plugin",
        "assemble": assemble,
        "disassemble": disassemble,
    }


print("[*] Registering LLVM asm plugin...")
if r2lang.plugin("asm", asm_llvm):
    print("[+] Registered LLVM asm plugin")
else:
    print("[-] Failed to register LLVM asm plugin")
