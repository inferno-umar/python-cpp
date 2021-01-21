import os
import subprocess
import platform


def execute(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.wait()
    if p.returncode != 0:
        print("\nYou have an error somewhere..!")
    elif p.returncode == 0:
        print("\nAll done")


def invalid():
    print("Invalid input\n")
    print("-------------------------------")


def fn_bdot(filename):
    filename.split(".")
    return filename.split(".")[0]


def fn_adot(filename):
    filename.split(".")
    return filename.split(".")[1]


filename = input("Enter filename\n")
if filename.find(".") == -1:
    print("Enter a valid filetype, supported types are: .asm, .s, .cpp, .c")
else:
    raw_filename = fn_bdot(filename)
    file_format = fn_adot(filename)
    while True:
        build_input = input("\nBuild or Assemble(Enter)\nExit(0)\n")
        if build_input == "0":
            break
        elif build_input == "chfile":
            filename = input("\nEnter filename\n")
            if filename == "0":
                break
            else:
                raw_filename = fn_bdot(filename)
                file_format = fn_adot(filename)
        elif build_input == "":
            if file_format in {"asm", "s"}:
                print("Building:" + filename + "\n")
            execute(
                "nasm -f elf64 "
                + filename
                + " && ld -o "
                + raw_filename
                + " "
                + raw_filename
                + ".o"
            )
            print("Executing--------\n")
            os.system("./" + raw_filename + " && $?")
            print("\n-------------")
        elif file_format in {"c", "cpp"}:
            print("Assembling---------")
            if file_format == "cpp":
                execute("g++ -S " + filename + " -masm=intel")
            elif file_format == "c":
                execute("gcc -S " + filename + " -masm=intel")
        else:
            invalid()
