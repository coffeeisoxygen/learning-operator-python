from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

console = Console()


def show_assignment_operators():
    # Display title and introduction
    console.print(
        Panel.fit("[bold cyan]Operator Penugasan[/bold cyan]", border_style="cyan")
    )

    console.print("\n[yellow]Operator Penugasan adalah:[/yellow]")
    console.print("Operator penugasan digunakan untuk menetapkan nilai ke variabel.\n")

    # Create table for operators
    table = Table(title="Operator Penugasan dalam Python")

    # Add columns
    table.add_column("Simbol", style="cyan", justify="center")
    table.add_column("Operator", style="green")
    table.add_column("Penjelasan", style="yellow")
    table.add_column("Contoh", style="magenta")
    table.add_column("Hasil", style="blue")

    # Add rows with data
    table.add_row(
        "=",
        "Penugasan",
        "Mengisikan nilai di sebelah kanan operator ke nilai di sebelah kiri operator",
        "x = 5",
        "Jika x = 5, maka x = 5",
    )
    table.add_row(
        "+=",
        "Penugasan Penambahan",
        "Menambahkan operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri",
        "x += 3",
        "Jika x = 5, maka x = 8",
    )
    table.add_row(
        "-=",
        "Penugasan Pengurangan",
        "Mengurangi operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri",
        "x -= 3",
        "Jika x = 5, maka x = 2",
    )
    table.add_row(
        "*=",
        "Penugasan Perkalian",
        "Mengalikan operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri",
        "x *= 3",
        "Jika x = 5, maka x = 15",
    )
    table.add_row(
        "/=",
        "Penugasan Pembagian",
        "Membagi operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri",
        "x /= 3",
        "Jika x = 5, maka x = 1.6667",
    )
    table.add_row(
        "%=",
        "Penugasan Modulus",
        "Mengambil sisa bagi dari operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri",
        "x %= 3",
        "Jika x = 5, maka x = 2",
    )
    table.add_row(
        "//=",
        "Penugasan Pembagian Bulat",
        "Membagi bulat operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri",
        "x //= 3",
        "Jika x = 5, maka x = 1",
    )
    table.add_row(
        "**=",
        "Penugasan Pangkat",
        "Memangkatkan operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri",
        "x **= 3",
        "Jika x = 5, maka x = 125",
    )

    # Print the table
    console.print(table)

    # Show practical examples
    console.print("\n[bold]Contoh Praktis:[/bold]")
    code = """
x = 10
y = 3

# Penugasan sederhana
x = y
print(f"Setelah x = y: x = {x}")  # Output: 3

# Reset nilai
x = 10

# Penugasan dengan penambahan
x += y  # sama dengan x = x + y
print(f"Setelah x += y: x = {x}")  # Output: 13

# Reset nilai
x = 10

# Penugasan dengan pengurangan
x -= y  # sama dengan x = x - y
print(f"Setelah x -= y: x = {x}")  # Output: 7

# Reset nilai
x = 10

# Penugasan dengan perkalian
x *= y  # sama dengan x = x * y
print(f"Setelah x *= y: x = {x}")  # Output: 30
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    console.print("\n[bold]Contoh Lain:[/bold]")
    code_examples = """
x = 10
y = 3

# Penugasan dengan pembagian
x /= y  # sama dengan x = x / y
print(f"Setelah x /= y: x = {x}")  # Output: 3.3333333333333335

# Reset nilai
x = 10

# Penugasan dengan pembagian bulat
x //= y  # sama dengan x = x // y
print(f"Setelah x //= y: x = {x}")  # Output: 3

# Reset nilai
x = 10

# Penugasan dengan modulus
x %= y  # sama dengan x = x % y
print(f"Setelah x %= y: x = {x}")  # Output: 1

# Reset nilai
x = 10

# Penugasan dengan pangkat
x **= y  # sama dengan x = x ** y
print(f"Setelah x **= y: x = {x}")  # Output: 1000
"""
    syntax2 = Syntax(code_examples, "python", theme="monokai", line_numbers=True)
    console.print(syntax2)

    # Interactive example
    console.print("\n[bold green]Ingin mencoba sendiri?[/bold green]")
    try_example = Prompt.ask(
        "Apakah Anda ingin mencoba contoh interaktif?", choices=["y", "n"], default="y"
    )

    if try_example.lower() == "y":
        interactive_assignment_example()

    # Return to main menu prompt
    console.print("\nTekan Enter untuk kembali ke menu utama...")
    input()


def interactive_assignment_example():
    console.print("\n[bold]Contoh Interaktif:[/bold]")

    try:
        x = float(Prompt.ask("Masukkan nilai awal x"))
        y = float(Prompt.ask("Masukkan nilai y"))

        console.print(f"\n[green]Nilai awal: x = {x}, y = {y}[/green]")

        # Clone the initial value for demonstrating each operator
        original_x = x

        # Demonstrate each assignment operator
        x = original_x  # Reset to initial value
        console.print(f"x = y → [cyan]x = {y}[/cyan] (nilai x diubah menjadi nilai y)")

        x = original_x  # Reset to initial value
        x += y
        console.print(f"x += y → [cyan]x = {x}[/cyan] (x = x + y)")

        x = original_x  # Reset to initial value
        x -= y
        console.print(f"x -= y → [cyan]x = {x}[/cyan] (x = x - y)")

        x = original_x  # Reset to initial value
        x *= y
        console.print(f"x *= y → [cyan]x = {x}[/cyan] (x = x * y)")

        x = original_x  # Reset to initial value
        if y != 0:
            x /= y
            console.print(f"x /= y → [cyan]x = {x}[/cyan] (x = x / y)")

            x = original_x  # Reset to initial value
            x //= y
            console.print(f"x //= y → [cyan]x = {x}[/cyan] (x = x // y)")

            x = original_x  # Reset to initial value
            x %= y
            console.print(f"x %= y → [cyan]x = {x}[/cyan] (x = x % y)")
        else:
            console.print(
                "[bold red]Tidak dapat melakukan operasi pembagian karena y = 0[/bold red]"
            )

        x = original_x  # Reset to initial value
        try:
            x **= y
            console.print(f"x **= y → [cyan]x = {x}[/cyan] (x = x ** y)")
        except OverflowError:
            console.print("[bold red]Hasil perpangkatan terlalu besar![/bold red]")

    except ValueError:
        console.print("[bold red]Error: Masukkan angka yang valid[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")


if __name__ == "__main__":
    # This allows testing the module directly
    show_assignment_operators()
