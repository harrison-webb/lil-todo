from os import system
from time import sleep


def main():
    f = open("./.list.txt", "a")
    file = f.read()
    f.close()
    items = [x for x in file.split("\n") if x.strip()]
    exit = False
    while not exit:
        _ = system("clear")
        print_header()
        if items:
            for item in items:
                print(f"- {item}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        command = input("Enter a command (add <item>, delete <item>, exit): ")
        if command.startswith("add"):
            items.append(command[4:])
        elif command.startswith("delete"):
            try:
                items.remove(command[7:])
            except:
                print(f"{command[7:]} is not in the list")
                sleep(1)
        elif command in ["exit", "exit()", "quit", "quit()"]:
            with open("./.list.txt", "w") as f:
                for item in items:
                    f.write(f"{item}\n")
            exit = True
        else:
            print("Command not recognized")
            sleep(1)


def print_header():
    display = """
            ========================= lil todo list =========================
            """
    print(display)


if __name__ == "__main__":
    main()
