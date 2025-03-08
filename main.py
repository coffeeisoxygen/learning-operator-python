from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.additional.Binary_Solver import binary_converter_menu
from src.additional.Math_Solver import math_solver_menu
from src.arithmatics.Aritmatika import show_arithmetic_operators
from src.assignments.Penugasan import show_assignment_operators
from src.bitwises.Bitwise import show_bitwise_operators
from src.comparisons.Perbandingan import show_comparison_operators
from src.identities.Identitas import show_identity_operators
from src.logicals.Logika import show_logic_operators
from src.memberships.Keanggotaan import show_membership_operators

console = Console()


def main():
    console.print(
        Panel.fit(
            "[bold blue]Selamat Datang di Aplikasi Pengenalan Operator Python[/bold blue]",
            border_style="blue",
        )
    )

    while True:
        console.print(
            "\n[bold yellow]Pilih kategori operator yang ingin dipelajari:[/bold yellow]"
        )
        console.print("1. Operator Aritmatika")
        console.print("2. Operator Penugasan")
        console.print("3. Operator Perbandingan")
        console.print("4. Operator Logika")
        console.print("5. Operator Identitas")
        console.print("6. Operator Keanggotaan")
        console.print("7. Operator Bitwise")
        console.print("100. Math Solver")
        console.print("101. Binary Converter")
        console.print("0. Keluar")

        choice = Prompt.ask(
            "\nMasukkan pilihan",
            choices=["0", "1", "2", "3", "4", "5", "6", "7", "100", "101"],
            default="1",
        )

        if choice == "0":
            console.print(
                "[bold green]Terima kasih telah menggunakan aplikasi ini![/bold green]"
            )
            break
        elif choice == "1":
            show_arithmetic_operators()
        elif choice == "2":
            show_assignment_operators()
        elif choice == "3":
            show_comparison_operators()
        elif choice == "4":
            show_logic_operators()
        elif choice == "5":
            show_identity_operators()
        elif choice == "6":
            show_membership_operators()
        elif choice == "7":
            show_bitwise_operators()
        elif choice == "100":
            math_solver_menu()
        elif choice == "101":
            binary_converter_menu()

        # Add other menu options as you implement them
        else:
            console.print("[bold red]Maaf, fitur ini belum tersedia.[/bold red]")


if __name__ == "__main__":
    main()
