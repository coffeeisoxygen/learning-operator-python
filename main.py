from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.arithmatics.Aritmatika import show_arithmetic_operators

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
        console.print("0. Keluar")

        choice = Prompt.ask(
            "\nMasukkan pilihan",
            choices=["0", "1", "2", "3", "4", "5", "6", "7"],
            default="1",
        )

        if choice == "0":
            console.print(
                "[bold green]Terima kasih telah menggunakan aplikasi ini![/bold green]"
            )
            break
        elif choice == "1":
            show_arithmetic_operators()
        # Add other menu options as you implement them
        else:
            console.print("[bold red]Maaf, fitur ini belum tersedia.[/bold red]")


if __name__ == "__main__":
    main()
