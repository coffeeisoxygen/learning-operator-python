from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

console = Console()
# type: ignore


def show_comparison_operators():
    # Display title and introduction
    console.print(
        Panel.fit("[bold cyan]Operator Perbandingan[/bold cyan]", border_style="cyan")
    )

    console.print("\n[yellow]Operator Perbandingan adalah:[/yellow]")
    console.print(
        "Operator perbandingan digunakan untuk membandingkan dua nilai dan mengembalikan nilai boolean (True atau False).\n"
    )

    # Create table for operators
    table = Table(title="Operator Perbandingan dalam Python")

    # Add columns
    table.add_column("Simbol", style="cyan", justify="center")
    table.add_column("Operator", style="green")
    table.add_column("Penjelasan", style="yellow")
    table.add_column("Contoh", style="magenta")
    table.add_column("Hasil", style="blue")

    # Add rows with data
    table.add_row(
        "==",
        "Sama dengan",
        "Bernilai True jika kedua operan sama",
        "x == y",
        "Jika x = 5, y = 5, maka x == y menghasilkan True",
    )
    table.add_row(
        "!=",
        "Tidak sama dengan",
        "Bernilai True jika kedua operan tidak sama",
        "x != y",
        "Jika x = 5, y = 3, maka x != y menghasilkan True",
    )
    table.add_row(
        ">",
        "Lebih besar",
        "Bernilai True jika operan kiri lebih besar dari operan kanan",
        "x > y",
        "Jika x = 5, y = 3, maka x > y menghasilkan True",
    )
    table.add_row(
        "<",
        "Lebih kecil",
        "Bernilai True jika operan kiri lebih kecil dari operan kanan",
        "x < y",
        "Jika x = 3, y = 5, maka x < y menghasilkan True",
    )
    table.add_row(
        ">=",
        "Lebih besar atau sama dengan",
        "Bernilai True jika operan kiri lebih besar dari atau sama dengan operan kanan",
        "x >= y",
        "Jika x = 5, y = 5, maka x >= y menghasilkan True",
    )
    table.add_row(
        "<=",
        "Lebih kecil atau sama dengan",
        "Bernilai True jika operan kiri lebih kecil dari atau sama dengan operan kanan",
        "x <= y",
        "Jika x = 5, y = 5, maka x <= y menghasilkan True",
    )

    # Print the table
    console.print(table)

    # Show practical examples
    console.print("\n[bold]Contoh Praktis:[/bold]")
    code = """
x = 10
y = 5
z = 10

# Sama dengan
print(f"x == y: {x == y}")  # Output: False
print(f"x == z: {x == z}")  # Output: True

# Tidak sama dengan
print(f"x != y: {x != y}")  # Output: True
print(f"x != z: {x != z}")  # Output: False

# Lebih besar
print(f"x > y: {x > y}")   # Output: True
print(f"y > x: {y > x}")   # Output: False

# Lebih kecil
print(f"x < y: {x < y}")   # Output: False
print(f"y < x: {y < x}")   # Output: True
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    console.print("\n[bold]Contoh Lain:[/bold]")
    code_examples = """
x = 10
y = 5
z = 10

# Lebih besar atau sama dengan
print(f"x >= y: {x >= y}")   # Output: True
print(f"x >= z: {x >= z}")   # Output: True
print(f"y >= x: {y >= x}")   # Output: False

# Lebih kecil atau sama dengan
print(f"x <= y: {x <= y}")   # Output: False
print(f"x <= z: {x <= z}")   # Output: True
print(f"y <= x: {y <= x}")   # Output: True

# Perbandingan dengan tipe data lain
print(f"'abc' == 'abc': {'abc' == 'abc'}")         # Output: True
print(f"'abc' == 'def': {'abc' == 'def'}")         # Output: False
print(f"5 == '5': {5 == '5'}")                     # Output: False (tipe data berbeda)
print(f"[1, 2] == [1, 2]: {[1, 2] == [1, 2]}")     # Output: True
"""
    syntax2 = Syntax(code_examples, "python", theme="monokai", line_numbers=True)
    console.print(syntax2)

    # Interactive example
    console.print("\n[bold green]Ingin mencoba sendiri?[/bold green]")
    try_example = Prompt.ask(
        "Apakah Anda ingin mencoba contoh interaktif?", choices=["y", "n"], default="y"
    )

    if try_example.lower() == "y":
        interactive_comparison_example()

    # Return to main menu prompt
    console.print("\nTekan Enter untuk kembali ke menu utama...")
    input()


def interactive_comparison_example():
    """Interactive demonstration of comparison operators."""
    try:
        # Get input values
        x, y = get_comparison_values()

        # Determine types
        x_is_num = is_numeric(x)
        y_is_num = is_numeric(y)

        # Handle comparisons based on type compatibility
        if (x_is_num and y_is_num) or (not x_is_num and not y_is_num):
            perform_same_type_comparison(x, y)
        else:
            handle_different_type_comparison(x, y, x_is_num, y_is_num)

    except Exception as e:
        handle_comparison_error(e)


def get_comparison_values():
    """Get two values from the user for comparison."""
    console.print(
        "\n[bold yellow]Mari mencoba operator perbandingan secara interaktif:[/bold yellow]"
    )
    x_input = Prompt.ask("\nMasukkan nilai pertama (x)")
    y_input = Prompt.ask("Masukkan nilai kedua (y)")

    # Convert to appropriate types if possible
    return convert_input_value(x_input), convert_input_value(y_input)


def convert_input_value(value):
    """Try to convert input to int or float if possible."""
    try:
        # Try converting to int first
        return int(value)
    except ValueError:
        try:
            # Then try float
            return float(value)
        except ValueError:
            # Keep as string if conversion fails
            return value


def is_numeric(value):
    """Check if a value is numeric (int or float)."""
    return isinstance(value, (int, float))


def perform_same_type_comparison(x, y):
    """Handle comparisons when both values have compatible types."""
    console.print("\n[bold green]Hasil perbandingan:[/bold green]")
    console.print(f"x == y: [bold cyan]{x == y}[/bold cyan]")
    console.print(f"x != y: [bold cyan]{x != y}[/bold cyan]")
    console.print(f"x > y:  [bold cyan]{x > y}[/bold cyan]")
    console.print(f"x < y:  [bold cyan]{x < y}[/bold cyan]")
    console.print(f"x >= y: [bold cyan]{x >= y}[/bold cyan]")
    console.print(f"x <= y: [bold cyan]{x <= y}[/bold cyan]")


def handle_different_type_comparison(x, y, x_is_num, y_is_num):
    """Handle comparisons when values have different types."""
    console.print(
        "[bold yellow]Catatan: Membandingkan tipe data yang berbeda mungkin tidak memberikan hasil yang diharapkan[/bold yellow]"
    )
    console.print("\n[bold magenta]Perbandingan Kesetaraan:[/bold magenta]")
    console.print(f"x == y: [bold cyan]{x == y}[/bold cyan]")
    console.print(f"x != y: [bold cyan]{x != y}[/bold cyan]")

    # Ask if user wants to try type conversion
    try_convert = Prompt.ask(
        "\nApakah Anda ingin mencoba mengkonversi tipe data? (y/n)",
        choices=["y", "n"],
        default="y",
    )

    if try_convert.lower() == "y":
        handle_type_conversion(x, y, x_is_num, y_is_num)


def handle_type_conversion(x, y, x_is_num, y_is_num):
    """Handle type conversion for comparison."""
    choice = Prompt.ask(
        "Pilih konversi:\n1. Konversi ke numerik\n2. Konversi ke string",
        choices=["1", "2"],
        default="1",
    )

    if choice == "1":
        convert_to_numeric(x, y, x_is_num, y_is_num)
    else:
        convert_to_string(x, y, x_is_num, y_is_num)


def convert_to_numeric(x, y, x_is_num, y_is_num):
    """Convert values to numeric types for comparison."""
    if x_is_num and not y_is_num:
        convert_y_to_numeric(x, y)
    else:
        convert_x_to_numeric(x, y)


def convert_y_to_numeric(x, y):
    """Convert y to numeric for comparison with numeric x."""
    y_orig = y
    try:
        y_conv = float(y_orig)
        console.print(
            f"\n[green]Setelah konversi: x = {x} ({type(x).__name__}), y = {y_conv} ({type(y_conv).__name__})[/green]"
        )
        display_comparison_results(x, y_conv)
    except ValueError:
        console.print(
            f"[bold red]Tidak dapat mengkonversi '{y_orig}' ke tipe numerik[/bold red]"
        )


def convert_x_to_numeric(x, y):
    """Convert x to numeric for comparison with numeric y."""
    x_orig = x
    try:
        x_conv = float(x_orig)
        console.print(
            f"\n[green]Setelah konversi: x = {x_conv} ({type(x_conv).__name__}), y = {y} ({type(y).__name__})[/green]"
        )
        display_comparison_results(x_conv, y)
    except ValueError:
        console.print(
            f"[bold red]Tidak dapat mengkonversi '{x_orig}' ke tipe numerik[/bold red]"
        )


def convert_to_string(x, y, x_is_num, y_is_num):
    """Convert values to strings for comparison."""
    if x_is_num and not y_is_num:
        x_str = str(x)
        console.print(
            f"\n[green]Setelah konversi: x = '{x_str}' ({type(x_str).__name__}), y = '{y}' ({type(y).__name__})[/green]"
        )
        display_comparison_results(x_str, y)
    else:
        y_str = str(y)
        console.print(
            f"\n[green]Setelah konversi: x = '{x}' ({type(x).__name__}), y = '{y_str}' ({type(y_str).__name__})[/green]"
        )
        display_comparison_results(x, y_str)


def display_comparison_results(x, y):
    """Display all comparison results between two values."""
    console.print(f"x > y:  [bold cyan]{x > y}[/bold cyan]")
    console.print(f"x < y:  [bold cyan]{x < y}[/bold cyan]")
    console.print(f"x >= y: [bold cyan]{x >= y}[/bold cyan]")
    console.print(f"x <= y: [bold cyan]{x <= y}[/bold cyan]")


def handle_comparison_error(e):
    """Handle exceptions during comparison."""
    console.print(f"[bold red]Error: {e}[/bold red]")
    console.print(
        "[yellow]Ini adalah contoh pembelajaran bagaimana error dapat terjadi dalam pemrograman.[/yellow]"
    )
    console.print(
        "[green]Tip: Pastikan untuk selalu memeriksa tipe data sebelum melakukan operasi perbandingan.[/green]"
    )


if __name__ == "__main__":
    # This allows testing the module directly
    show_comparison_operators()
