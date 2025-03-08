from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

console = Console()


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
    """Interactive demonstration of arithmetic operators."""
    try:
        # Get input values
        x, y = get_arithmetic_values()

        # Display arithmetic operations
        display_arithmetic_operations(x, y)

    except Exception as e:
        handle_arithmetic_error(e)


def get_arithmetic_values():
    """Get two numeric values from the user for arithmetic operations."""
    console.print(
        "\n[bold yellow]Mari mencoba operator aritmatika secara interaktif:[/bold yellow]"
    )
    x_input = Prompt.ask("\nMasukkan nilai pertama (x)")
    y_input = Prompt.ask("Masukkan nilai kedua (y)")

    # Convert to appropriate types if possible
    return convert_to_numeric(x_input), convert_to_numeric(y_input)


def convert_to_numeric(value):
    """Convert input to a numeric value."""
    try:
        # Try converting to int first
        return int(value)
    except ValueError:
        try:
            # Then try float
            return float(value)
        except ValueError:
            # If both fail, explain and ask for numeric input
            console.print("[bold red]Nilai harus berupa angka.[/bold red]")
            return convert_to_numeric(Prompt.ask("Masukkan nilai numerik"))


def display_arithmetic_operations(x, y):
    """Display the results of all arithmetic operations."""
    console.print("\n[bold green]Hasil operasi aritmatika:[/bold green]")
    console.print(f"Penjumlahan (x + y): [bold cyan]{x + y}[/bold cyan]")
    console.print(f"Pengurangan (x - y): [bold cyan]{x - y}[/bold cyan]")
    console.print(f"Perkalian (x * y): [bold cyan]{x * y}[/bold cyan]")

    # Handle division by zero
    display_division(x, y)

    console.print(
        f"Modulus (x % y): [bold cyan]{x % y if y != 0 else 'Tidak dapat dibagi dengan nol'}[/bold cyan]"
    )
    console.print(f"Pemangkatan (x ** y): [bold cyan]{x**y}[/bold cyan]")
    console.print(
        f"Pembagian bulat (x // y): [bold cyan]{x // y if y != 0 else 'Tidak dapat dibagi dengan nol'}[/bold cyan]"
    )


def display_division(x, y):
    """Handle division operation with proper error checking."""
    if y != 0:
        console.print(f"Pembagian (x / y): [bold cyan]{x / y}[/bold cyan]")
    else:
        console.print(
            "Pembagian (x / y): [bold red]Tidak dapat dibagi dengan nol[/bold red]"
        )


def handle_arithmetic_error(e):
    """Handle exceptions during arithmetic operations."""
    console.print(f"[bold red]Error: {e}[/bold red]")
    console.print(
        "[yellow]Terjadi kesalahan saat melakukan operasi aritmatika.[/yellow]"
    )
    console.print(
        "[green]Tip: Pastikan input adalah nilai numerik dan tidak melakukan pembagian dengan nol.[/green]"
    )


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
