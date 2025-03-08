from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

console = Console()


def show_bitwise_operators():
    # Display title and introduction
    console.print(
        Panel.fit("[bold cyan]Operator Bitwise[/bold cyan]", border_style="cyan")
    )

    console.print("\n[yellow]Operator Bitwise adalah:[/yellow]")
    console.print(
        "Operator bitwise digunakan untuk melakukan operasi logika bilangan biner "
        "dalam bentuk bit. Jika nilai asal yang dipakai bukan bilangan biner, "
        "akan dikonversi secara otomatis menjadi bilangan biner. "
        "Misalnya 7 desimal = 0111 dalam bilangan biner.\n"
    )

    # Create table for operators
    table = Table(title="Operator Bitwise dalam Python")

    # Add columns
    table.add_column("Operator", style="cyan", justify="center")
    table.add_column("Nama", style="green")
    table.add_column("Deskripsi", style="yellow")
    table.add_column("Contoh", style="magenta")
    table.add_column("Biner", style="blue")
    table.add_column("Hasil (biner)", style="blue")
    table.add_column("Hasil (desimal)", style="blue")

    # Add rows with data
    table.add_row(
        "&",
        "AND",
        "Set setiap bit ke 1 jika kedua bit adalah 1",
        "10 & 12",
        "1010 & 1100",
        "1000",
        "8",
    )
    table.add_row(
        "|",
        "OR",
        "Set setiap bit ke 1 jika salah satu dari dua bit adalah 1",
        "10 | 12",
        "1010 | 1100",
        "1110",
        "14",
    )
    table.add_row(
        "^",
        "XOR",
        "Set setiap bit ke 1 jika hanya salah satu bit yang 1",
        "10 ^ 12",
        "1010 ^ 1100",
        "0110",
        "6",
    )
    table.add_row(
        "~",
        "NOT",
        "Inversi semua bit",
        "~10",
        "~1010",
        "...0101",
        "-11",
    )
    table.add_row(
        "<<",
        "Left Shift",
        "Geser bit ke kiri sebanyak n posisi",
        "10 << 2",
        "1010 << 2",
        "101000",
        "40",
    )
    table.add_row(
        ">>",
        "Right Shift",
        "Geser bit ke kanan sebanyak n posisi",
        "10 >> 1",
        "1010 >> 1",
        "101",
        "5",
    )

    # Print the table
    console.print(table)

    # Show practical examples
    console.print("\n[bold]Contoh Praktis:[/bold]")
    code = """
# Contoh Operator AND (&)
a = 10  # 1010 dalam biner
b = 12  # 1100 dalam biner
print(f"a = {a} (biner: {bin(a)[2:]})")
print(f"b = {b} (biner: {bin(b)[2:]})")
print(f"a & b = {a & b} (biner: {bin(a & b)[2:]})")  # 1000 = 8

# Contoh Operator OR (|)
print(f"a | b = {a | b} (biner: {bin(a | b)[2:]})")  # 1110 = 14

# Contoh Operator XOR (^)
print(f"a ^ b = {a ^ b} (biner: {bin(a ^ b)[2:]})")  # 0110 = 6
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    console.print("\n[bold]Contoh Lain:[/bold]")
    code_examples = """
# Contoh Operator NOT (~)
a = 10  # 1010 dalam biner
print(f"a = {a} (biner: {bin(a)[2:]})")
print(f"~a = {~a} (biner: {bin(~a)[2:]})")  # NOT melakukan inversi bit

# Contoh Left Shift (<<)
print(f"a << 2 = {a << 2} (biner: {bin(a << 2)[2:]})")  # Shift left 2 bit: 101000 = 40

# Contoh Right Shift (>>)
print(f"a >> 1 = {a >> 1} (biner: {bin(a >> 1)[2:]})")  # Shift right 1 bit: 101 = 5

# Aplikasi dalam pemrograman
mask = 0b1100  # 12 dalam desimal
status = 0b1010  # 10 dalam desimal

# Memeriksa apakah bit-bit tertentu diaktifkan (menggunakan AND)
print(f"status & mask = {status & mask} (biner: {bin(status & mask)[2:]})")

# Mengaktifkan bit-bit tertentu (menggunakan OR)
print(f"status | mask = {status | mask} (biner: {bin(status | mask)[2:]})")

# Toggle bit-bit tertentu (menggunakan XOR)
print(f"status ^ mask = {status ^ mask} (biner: {bin(status ^ mask)[2:]})")
"""
    syntax2 = Syntax(code_examples, "python", theme="monokai", line_numbers=True)
    console.print(syntax2)

    # Interactive example
    console.print("\n[bold green]Ingin mencoba sendiri?[/bold green]")
    try_example = Prompt.ask(
        "Apakah Anda ingin mencoba contoh interaktif?", choices=["y", "n"], default="y"
    )

    if try_example.lower() == "y":
        interactive_bitwise_example()

    # Return to main menu prompt
    console.print("\nTekan Enter untuk kembali ke menu utama...")
    input()


def interactive_bitwise_example():
    """Interactive demonstration of bitwise operators."""
    try:
        console.print(
            "\n[bold yellow]Mari mencoba operator bitwise secara interaktif:[/bold yellow]"
        )

        # Get first number
        num1_str = Prompt.ask("Masukkan bilangan pertama (desimal)")
        try:
            num1 = int(num1_str)
        except ValueError:
            console.print(
                "[bold red]Input tidak valid, menggunakan nilai 10.[/bold red]"
            )
            num1 = 10

        # Get second number
        num2_str = Prompt.ask("Masukkan bilangan kedua (desimal)")
        try:
            num2 = int(num2_str)
        except ValueError:
            console.print(
                "[bold red]Input tidak valid, menggunakan nilai 12.[/bold red]"
            )
            num2 = 12

        # Show both numbers in binary
        console.print(f"\nBilangan 1: {num1} (biner: {bin(num1)[2:]})")
        console.print(f"Bilangan 2: {num2} (biner: {bin(num2)[2:]})")

        # Calculate and display results
        console.print("\n[bold green]Hasil Operasi Bitwise:[/bold green]")

        # AND operation
        and_result = num1 & num2
        console.print(f"\n{num1} & {num2} = {and_result}")
        console.print(
            f"Biner: {bin(num1)[2:]} & {bin(num2)[2:]} = {bin(and_result)[2:]}"
        )

        # OR operation
        or_result = num1 | num2
        console.print(f"\n{num1} | {num2} = {or_result}")
        console.print(
            f"Biner: {bin(num1)[2:]} | {bin(num2)[2:]} = {bin(or_result)[2:]}"
        )

        # XOR operation
        xor_result = num1 ^ num2
        console.print(f"\n{num1} ^ {num2} = {xor_result}")
        console.print(
            f"Biner: {bin(num1)[2:]} ^ {bin(num2)[2:]} = {bin(xor_result)[2:]}"
        )

        # NOT operation (for num1)
        not_result = ~num1
        console.print(f"\n~{num1} = {not_result}")
        console.print(
            f"Biner: ~{bin(num1)[2:]} = {bin(not_result)[2:] if not_result >= 0 else bin(not_result)[3:]}"
        )

        # Left shift (for num1)
        shift = 1  # Default shift by 1
        shift_str = Prompt.ask("Berapa bit untuk digeser? (left shift)", default="1")
        try:
            shift = int(shift_str)
        except ValueError:
            console.print(
                "[bold red]Input tidak valid, menggunakan nilai 1.[/bold red]"
            )
            shift = 1

        left_shift_result = num1 << shift
        console.print(f"\n{num1} << {shift} = {left_shift_result}")
        console.print(
            f"Biner: {bin(num1)[2:]} << {shift} = {bin(left_shift_result)[2:]}"
        )

        # Right shift (for num1)
        right_shift_result = num1 >> shift
        console.print(f"\n{num1} >> {shift} = {right_shift_result}")
        console.print(
            f"Biner: {bin(num1)[2:]} >> {shift} = {bin(right_shift_result)[2:]}"
        )

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")


if __name__ == "__main__":
    # This allows testing the module directly
    show_bitwise_operators()
