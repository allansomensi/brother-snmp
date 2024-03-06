from printers_info import printers_list
from utils import clear


def menu():
    clear()
    for i, printer in printers_list.items():
        print(f"{i}. {printer.name}")
    print("\n0. Exit\n")


def main():
    while True:
        menu()
        try:
            user_option = int(input("Select a printer: "))
            if user_option == 0:
                print("Exiting...")
                break
            elif user_option in printers_list:
                pr = printers_list[user_option]
                print("Loading...")
                info = f"""Status: {pr.get_status()}
--------------------------------------------------
---               Device Info                  ---
--------------------------------------------------\n
Name: {pr.name}
IPv4: {pr.ip_address}
Model: {pr.model}
MAC: {pr.get_mac()}
Language: {pr.get_language()}
Activity: {pr.get_uptime()}
\n--------------------------------------------------
---                 Resources                  ---
--------------------------------------------------\n"""
                info += f"\nBlack Toner: {pr.get_toner('black')}\n"
                if pr.has_drum:
                    info += f"Drum: {pr.get_drum()}\n"

                if pr.is_colored:
                    info += f"Cyan Toner: {pr.get_toner('cyan')}\n"
                    info += f"Magenta Toner: {pr.get_toner('magenta')}\n"
                    info += f"Yellow Toner: {pr.get_toner('yellow')}\n"

                info += f"""
--------------------------------------------------
---                 Counting                   ---
--------------------------------------------------\n
Total pages: {pr.get_total_pages()}
Total double-sided pages: {pr.get_count_pages_double_sided()}
Total copies: {pr.get_total_copies()}
Total double-sided copies: {pr.get_count_copies_double_sided()}
Total PC pages: {pr.get_total_pages_pc()}
Total PC double-sided pages: {pr.get_count_pages_pc_double_sided()}
\n--- By type ---\n
A4/Letter: {pr.get_total_pages_a4_letter()}
Legal/Folio: {pr.get_total_pages_legal_a4_long()}
B5/Executive: {pr.get_total_pages_b5_executive()}
Envelope: {pr.get_total_pages_envelope()}
A5: {pr.get_total_pages_a5()}
Others: {pr.get_total_pages_other()}"""
                clear()
                print(info)
                input("")
            else:
                print("Invalid option!")
                input("")

        except ValueError:
            print("Error: Please enter a valid number.")
            input("")
        except Exception as e:
            print(f"Unexpected error: {e}")
            input("")


if __name__ == "__main__":
    main()
