from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

console = Console()
# type: ignore


def show_logic_operators():
    # Display title and introduction
    console.print(
        Panel.fit("[bold green]Operator Logika[/bold green]", border_style="green")
    )

    console.print("\n[yellow]Operator Logika adalah:[/yellow]")
    console.print(
        "Operator logika digunakan untuk menggabungkan dua atau lebih kondisi logika dan mengembalikan nilai boolean (True atau False).\n"
    )

    # Create main table for operators
    main_table = Table(title="Operator Logika dalam Python")

    # Add columns
    main_table.add_column("Operator", style="cyan", justify="center")
    main_table.add_column("Deskripsi", style="green")
    main_table.add_column("Penjelasan", style="yellow")
    main_table.add_column("Contoh", style="magenta")

    # Add rows with data
    main_table.add_row(
        "and",
        "Logika AND",
        "Mengembalikan True jika kedua operand bernilai True",
        "x and y",
    )
    main_table.add_row(
        "or",
        "Logika OR",
        "Mengembalikan True jika minimal salah satu operand bernilai True",
        "x or y",
    )
    main_table.add_row(
        "not", "Logika NOT", "Mengembalikan kebalikan dari nilai operand", "not x"
    )
    main_table.add_row(
        "XOR",
        "Exclusive OR",
        "Mengembalikan True jika jumlah operand True adalah ganjil",
        "(x or y) and not (x and y)",
    )
    main_table.add_row("NAND", "NOT AND", "Kebalikan dari AND", "not (x and y)")
    main_table.add_row("NOR", "NOT OR", "Kebalikan dari OR", "not (x or y)")
    main_table.add_row(
        "XNOR", "Exclusive NOR", "Kebalikan dari XOR", "(x and y) or (not x and not y)"
    )

    # Print the main table
    console.print(main_table)

    # Show truth tables for each logical gate
    show_truth_tables()

    # Show practical examples
    console.print("\n[bold]Contoh Praktis:[/bold]")
    code = """
# AND Operator
x = True
y = False
print(f"True and True: {True and True}")     # Output: True
print(f"True and False: {x and y}")          # Output: False
print(f"False and True: {y and x}")          # Output: False
print(f"False and False: {False and False}") # Output: False

# OR Operator
print(f"True or True: {True or True}")       # Output: True
print(f"True or False: {x or y}")            # Output: True
print(f"False or True: {y or x}")            # Output: True
print(f"False or False: {False or False}")   # Output: False

# NOT Operator
print(f"not True: {not True}")               # Output: False
print(f"not False: {not False}")             # Output: True
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    console.print("\n[bold]Contoh Kombinasi Operator Logika:[/bold]")
    code_examples = """
x = True
y = False
z = True

# Kombinasi AND dan OR
print(f"True and True or False: {True and True or False}")   # Output: True
print(f"False or True and False: {False or True and False}") # Output: False
print(f"(False or True) and False: {(False or True) and False}") # Output: False

# Kombinasi dengan NOT
print(f"not (True and False): {not (True and False)}")     # Output: True
print(f"not True or not False: {not True or not False}")   # Output: True

# XOR Implementation
def xor(a, b):
    return (a or b) and not (a and b)

print(f"XOR(True, False): {xor(True, False)}")   # Output: True
print(f"XOR(True, True): {xor(True, True)}")     # Output: False
print(f"XOR(False, False): {xor(False, False)}") # Output: False
"""
    syntax2 = Syntax(code_examples, "python", theme="monokai", line_numbers=True)
    console.print(syntax2)

    # Interactive example
    console.print("\n[bold green]Ingin mencoba sendiri?[/bold green]")
    try_example = Prompt.ask(
        "Apakah Anda ingin mencoba contoh interaktif?", choices=["y", "n"], default="y"
    )

    if try_example.lower() == "y":
        interactive_logic_example()

    # Return to main menu prompt
    console.print("\nTekan Enter untuk kembali ke menu utama...")
    input()


def show_truth_tables():
    """Display truth tables for each logical gate."""
    console.print("\n[bold cyan]Tabel Kebenaran Gerbang Logika:[/bold cyan]")

    # AND Gate
    console.print("\n[bold]Tabel Kebenaran Gerbang AND:[/bold]")
    and_table = Table()
    and_table.add_column("A", style="cyan", justify="center")
    and_table.add_column("B", style="cyan", justify="center")
    and_table.add_column("A AND B", style="green", justify="center")
    and_table.add_row("False", "False", "False")
    and_table.add_row("False", "True", "False")
    and_table.add_row("True", "False", "False")
    and_table.add_row("True", "True", "True")
    console.print(and_table)

    # OR Gate
    console.print("\n[bold]Tabel Kebenaran Gerbang OR:[/bold]")
    or_table = Table()
    or_table.add_column("A", style="cyan", justify="center")
    or_table.add_column("B", style="cyan", justify="center")
    or_table.add_column("A OR B", style="green", justify="center")
    or_table.add_row("False", "False", "False")
    or_table.add_row("False", "True", "True")
    or_table.add_row("True", "False", "True")
    or_table.add_row("True", "True", "True")
    console.print(or_table)

    # NOT Gate
    console.print("\n[bold]Tabel Kebenaran Gerbang NOT:[/bold]")
    not_table = Table()
    not_table.add_column("A", style="cyan", justify="center")
    not_table.add_column("NOT A", style="green", justify="center")
    not_table.add_row("False", "True")
    not_table.add_row("True", "False")
    console.print(not_table)

    # NOR Gate
    console.print("\n[bold]Tabel Kebenaran Gerbang NOR:[/bold]")
    nor_table = Table()
    nor_table.add_column("A", style="cyan", justify="center")
    nor_table.add_column("B", style="cyan", justify="center")
    nor_table.add_column("A NOR B", style="green", justify="center")
    nor_table.add_row("False", "False", "True")
    nor_table.add_row("False", "True", "False")
    nor_table.add_row("True", "False", "False")
    nor_table.add_row("True", "True", "False")
    console.print(nor_table)

    # XOR Gate
    console.print("\n[bold]Tabel Kebenaran Gerbang XOR:[/bold]")
    xor_table = Table()
    xor_table.add_column("A", style="cyan", justify="center")
    xor_table.add_column("B", style="cyan", justify="center")
    xor_table.add_column("A XOR B", style="green", justify="center")
    xor_table.add_row("False", "False", "False")
    xor_table.add_row("False", "True", "True")
    xor_table.add_row("True", "False", "True")
    xor_table.add_row("True", "True", "False")
    console.print(xor_table)

    # XNOR Gate
    console.print("\n[bold]Tabel Kebenaran Gerbang XNOR:[/bold]")
    xnor_table = Table()
    xnor_table.add_column("A", style="cyan", justify="center")
    xnor_table.add_column("B", style="cyan", justify="center")
    xnor_table.add_column("A XNOR B", style="green", justify="center")
    xnor_table.add_row("False", "False", "True")
    xnor_table.add_row("False", "True", "False")
    xnor_table.add_row("True", "False", "False")
    xnor_table.add_row("True", "True", "True")
    console.print(xnor_table)


def interactive_logic_example():
    """Interactive demonstration of logical operators."""
    console.print(
        "\n[bold yellow]Mari mencoba operator logika secara interaktif:[/bold yellow]"
    )

    # Get user input for a and b
    a_input = Prompt.ask(
        "Masukkan nilai untuk A (True/False)", choices=["True", "False"], default="True"
    )
    b_input = Prompt.ask(
        "Masukkan nilai untuk B (True/False)",
        choices=["True", "False"],
        default="False",
    )

    # Convert to boolean
    a = a_input == "True"
    b = b_input == "True"

    # Display results
    console.print("\n[bold green]Hasil operasi logika:[/bold green]")
    console.print(f"A: [cyan]{a}[/cyan], B: [cyan]{b}[/cyan]\n")

    console.print(f"A AND B: [bold cyan]{a and b}[/bold cyan]")
    console.print(f"A OR B: [bold cyan]{a or b}[/bold cyan]")
    console.print(f"NOT A: [bold cyan]{not a}[/bold cyan]")
    console.print(f"NOT B: [bold cyan]{not b}[/bold cyan]")
    console.print(f"A XOR B: [bold cyan]{(a or b) and not (a and b)}[/bold cyan]")
    console.print(f"A NOR B: [bold cyan]{not (a or b)}[/bold cyan]")
    console.print(f"A XNOR B: [bold cyan]{(a and b) or (not a and not b)}[/bold cyan]")

    # Complex example
    console.print("\n[bold yellow]Contoh ekspresi logika kompleks:[/bold yellow]")
    complex_expr = ((a and not b) or (not a and b)) and (a or b)
    console.print(
        f"((A AND NOT B) OR (NOT A AND B)) AND (A OR B): [bold cyan]{complex_expr}[/bold cyan]"
    )

    # Allow user to try another example
    try_another = Prompt.ask(
        "\nApakah ingin mencoba contoh lain?", choices=["y", "n"], default="n"
    )
    if try_another.lower() == "y":
        interactive_logic_example()


if __name__ == "__main__":
    # This allows testing the module directly
    show_logic_operators()
