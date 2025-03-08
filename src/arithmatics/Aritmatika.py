from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table


def show_arithmetic_operators():
    # Display title and introduction
    console.print(
        Panel.fit("[bold cyan]Operator Aritmatika[/bold cyan]", border_style="cyan")
    )

    console.print("\n[yellow]Operator aritmatika adalah:[/yellow]")
    console.print(
        "Operator aritmatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum.\n"
    )

    # Create table for operators
    table = Table(title="Operator Aritmatika dalam Python")

    # Add columns
    table.add_column("Simbol", style="cyan", justify="center")
    table.add_column("Operator", style="green")
    table.add_column("Penjelasan", style="yellow")
    table.add_column("Contoh", style="magenta")
    table.add_column("Hasil", style="blue")

    # Add rows with data
    table.add_row(
        "+",
        "Penambahan",
        "Menambahkan dua buah operan",
        "x + y",
        "Jika x = 5, y = 3, maka x + y = 8",
    )
    table.add_row(
        "-",
        "Pengurangan",
        "Mengurangkan operan disebelah kiri operator dengan operan di sebelah kanan operator",
        "x - y",
        "Jika x = 5, y = 3, maka x - y = 2",
    )
    table.add_row(
        "*",
        "Perkalian",
        "Mengalikan dua buah operan",
        "x * y",
        "Jika x = 5, y = 3, maka x * y = 15",
    )
    table.add_row(
        "/",
        "Pembagian",
        "Membagi operan kiri dengan operan kanan (hasil float)",
        "x / y",
        "Jika x = 5, y = 3, maka x / y = 1.6667",
    )
    table.add_row(
        "//",
        "Pembagian Bulat",
        "Membagi operan kiri dengan operan kanan (hasil dibulatkan ke bawah)",
        "x // y",
        "Jika x = 5, y = 3, maka x // y = 1",
    )
    table.add_row(
        "%",
        "Modulus",
        "Sisa pembagian operan kiri dengan operan kanan",
        "x % y",
        "Jika x = 5, y = 3, maka x % y = 2",
    )
    table.add_row(
        "**",
        "Pangkat",
        "Operan kiri dipangkatkan dengan operan kanan",
        "x ** y",
        "Jika x = 5, y = 3, maka x ** y = 125",
    )

    # Print the table
    console.print(table)

    # Show practical examples
    console.print("\n[bold]Contoh Praktis:[/bold]")
    code = """
x = 10
y = 3

# Penambahan
print(f"x + y = {x + y}")  # Output: 13

# Pengurangan
print(f"x - y = {x - y}")  # Output: 7

# Perkalian
print(f"x * y = {x * y}")  # Output: 30

# Pembagian
print(f"x / y = {x / y}")  # Output: 3.3333333333333335

# Pembagian Bulat
print(f"x // y = {x // y}")  # Output: 3

# Modulus
print(f"x % y = {x % y}")  # Output: 1

# Pangkat
print(f"x ** y = {x ** y}")  # Output: 1000
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    # Interactive example
    console.print("\n[bold green]Ingin mencoba sendiri?[/bold green]")
    try_example = Prompt.ask(
        "Apakah Anda ingin mencoba contoh interaktif?", choices=["y", "n"], default="y"
    )

    if try_example.lower() == "y":
        interactive_arithmetic_example()

    # Return to main menu prompt
    console.print("\nTekan Enter untuk kembali ke menu utama...")
    input()


def interactive_arithmetic_example():
    console.print("\n[bold]Contoh Interaktif:[/bold]")

    try:
        x = Prompt.ask("Masukkan nilai x")
        y = Prompt.ask("Masukkan nilai y")

        # Validate inputs
        try:
            x = float(x)
        except ValueError:
            console.print("[bold red]Error: Nilai x harus berupa angka[/bold red]")
            return

        try:
            y = float(y)
        except ValueError:
            console.print("[bold red]Error: Nilai y harus berupa angka[/bold red]")
            return

        # Check for extremely large values
        if abs(x) > 1e100 or abs(y) > 1e100:
            console.print(
                "[bold yellow]Peringatan: Nilai yang sangat besar dapat menyebabkan ketidakakuratan[/bold yellow]"
            )

        console.print(f"\n[green]x = {x}, y = {y}[/green]")

        # Addition and subtraction (generally safe)
        console.print(f"x + y = [bold cyan]{x + y}[/bold cyan]")
        console.print(f"x - y = [bold cyan]{x - y}[/bold cyan]")

        # Multiplication (check for large results)
        product = x * y
        if abs(product) > 1e100:
            console.print(
                f"x * y = [bold cyan]Sangat besar: {format_large_number(product)}[/bold cyan]"
            )
        else:
            console.print(f"x * y = [bold cyan]{product}[/bold cyan]")

        # Division
        if y == 0:
            console.print(
                "x / y = [bold red]Error: Pembagian dengan nol tidak diperbolehkan[/bold red]"
            )
            console.print(
                "x // y = [bold red]Error: Pembagian dengan nol tidak diperbolehkan[/bold red]"
            )
            console.print(
                "x % y = [bold red]Error: Pembagian dengan nol tidak diperbolehkan[/bold red]"
            )
        else:
            console.print(f"x / y = [bold cyan]{x / y}[/bold cyan]")
            console.print(f"x // y = [bold cyan]{x // y}[/bold cyan]")
            console.print(f"x % y = [bold cyan]{x % y}[/bold cyan]")

        # Exponentiation (especially prone to overflow)
        try:
            # Check if the operation might result in a very large number
            if y > 0 and (abs(x) > 10 and y > 10):
                console.print(
                    "x ** y = [bold yellow]Peringatan: Hasil sangat besar[/bold yellow]"
                )
                result = x**y
                console.print(
                    f"x ** y = [bold cyan]{format_large_number(result)}[/bold cyan]"
                )
            elif y < 0 and x == 0:
                console.print(
                    "x ** y = [bold red]Error: 0 tidak bisa dipangkatkan dengan nilai negatif[/bold red]"
                )
            else:
                result = x**y
                console.print(f"x ** y = [bold cyan]{result}[/bold cyan]")
        except OverflowError:
            console.print(
                "x ** y = [bold red]Error: Hasil terlalu besar untuk dihitung[/bold red]"
            )

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")


def format_large_number(num):
    """Format large numbers for better readability."""
    if abs(num) < 1e6:
        return str(num)
    elif abs(num) < 1e15:
        return f"{num:.2e} ({num:,.2f})"
    else:
        return f"{num:.2e}"


if __name__ == "__main__":
    # This allows testing the module directly
    console = Console()
    show_arithmetic_operators()
