from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

console = Console()


def show_membership_operators():
    # Display title and introduction
    console.print(
        Panel.fit("[bold cyan]Operator Keanggotaan[/bold cyan]", border_style="cyan")
    )

    console.print("\n[yellow]Operator Keanggotaan adalah:[/yellow]")
    console.print(
        "Operator keanggotaan digunakan untuk menguji apakah suatu nilai atau variabel "
        "ada dalam sebuah urutan (seperti string, list, tuple, atau dictionary). "
        "Operator ini mengembalikan nilai boolean True atau False.\n"
    )

    # Create table for operators
    table = Table(title="Operator Keanggotaan dalam Python")

    # Add columns
    table.add_column("Operator", style="cyan", justify="center")
    table.add_column("Nama", style="green")
    table.add_column("Penjelasan", style="yellow")
    table.add_column("Contoh", style="magenta")
    table.add_column("Hasil", style="blue")

    # Add rows with data
    table.add_row(
        "in",
        "Keanggotaan",
        "Mengembalikan True jika nilai ada dalam urutan",
        "x in y",
        "True jika x adalah anggota dari y",
    )
    table.add_row(
        "not in",
        "Bukan Keanggotaan",
        "Mengembalikan True jika nilai tidak ada dalam urutan",
        "x not in y",
        "True jika x bukan anggota dari y",
    )

    # Print the table
    console.print(table)

    # Show practical examples
    console.print("\n[bold]Contoh Praktis:[/bold]")
    code = """
# Contoh dengan list
fruits = ['apple', 'banana', 'orange']
print(f"fruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")      # True
print(f"'grape' in fruits: {'grape' in fruits}")      # False
print(f"'grape' not in fruits: {'grape' not in fruits}")  # True

# Contoh dengan string
text = "Hello World"
print(f"text = '{text}'")
print(f"'H' in text: {'H' in text}")     # True
print(f"'x' in text: {'x' in text}")     # False
print(f"'x' not in text: {'x' not in text}")  # True
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    console.print("\n[bold]Contoh Lain:[/bold]")
    code_examples = """
# Contoh dengan dictionary
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}

print(f"student = {student}")
print(f"'name' in student: {'name' in student}")       # True, kunci ada dalam dictionary
print(f"'Alice' in student: {'Alice' in student}")     # False, nilai tidak diperiksa
print(f"'address' not in student: {'address' not in student}")  # True, kunci tidak ada

# Contoh dengan tuple
numbers = (1, 2, 3, 4, 5)
print(f"numbers = {numbers}")
print(f"3 in numbers: {3 in numbers}")       # True
print(f"6 not in numbers: {6 not in numbers}")  # True
"""
    syntax2 = Syntax(code_examples, "python", theme="monokai", line_numbers=True)
    console.print(syntax2)

    # Interactive example
    console.print("\n[bold green]Ingin mencoba sendiri?[/bold green]")
    try_example = Prompt.ask(
        "Apakah Anda ingin mencoba contoh interaktif?", choices=["y", "n"], default="y"
    )

    if try_example.lower() == "y":
        interactive_membership_example()

    # Return to main menu prompt
    console.print("\nTekan Enter untuk kembali ke menu utama...")
    input()


def interactive_membership_example():
    """Interactive demonstration of membership operators."""
    try:
        console.print(
            "\n[bold yellow]Mari mencoba operator keanggotaan secara interaktif:[/bold yellow]"
        )

        # Create a collection for testing membership
        console.print("\n[bold]Membuat koleksi untuk menguji keanggotaan:[/bold]")

        # Create a list
        my_list = ["apel", "pisang", "jeruk", "mangga", "anggur"]
        console.print(f"List: {my_list}")

        # Get user input
        item_to_check = Prompt.ask("\nMasukkan item yang ingin diperiksa dalam list")

        # Check membership
        console.print("\n[bold green]Hasil Operator Keanggotaan:[/bold green]")
        console.print(
            f"'{item_to_check}' in list: [bold cyan]{item_to_check in my_list}[/bold cyan]"
        )
        console.print(
            f"'{item_to_check}' not in list: [bold cyan]{item_to_check not in my_list}[/bold cyan]"
        )

        # Try with a string
        console.print("\n[bold]Mencoba dengan string:[/bold]")
        my_string = "Python Programming"
        console.print(f"String: '{my_string}'")

        # Get user input for string check
        char_to_check = Prompt.ask(
            "\nMasukkan karakter atau substring yang ingin diperiksa"
        )

        # Check membership in string
        console.print(
            "\n[bold green]Hasil Operator Keanggotaan dengan String:[/bold green]"
        )
        console.print(
            f"'{char_to_check}' in string: [bold cyan]{char_to_check in my_string}[/bold cyan]"
        )
        console.print(
            f"'{char_to_check}' not in string: [bold cyan]{char_to_check not in my_string}[/bold cyan]"
        )

        # Try with a dictionary
        console.print("\n[bold]Mencoba dengan dictionary:[/bold]")
        my_dict = {"nama": "Budi", "usia": 20, "kota": "Jakarta", "hobi": "membaca"}
        console.print(f"Dictionary: {my_dict}")

        # Get user input for dictionary check
        key_to_check = Prompt.ask("\nMasukkan kunci yang ingin diperiksa")

        # Check membership in dictionary
        console.print(
            "\n[bold green]Hasil Operator Keanggotaan dengan Dictionary:[/bold green]"
        )
        console.print(
            f"'{key_to_check}' in dictionary keys: [bold cyan]{key_to_check in my_dict}[/bold cyan]"
        )
        console.print(
            f"'{key_to_check}' not in dictionary keys: [bold cyan]{key_to_check not in my_dict}[/bold cyan]"
        )

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")


if __name__ == "__main__":
    # This allows testing the module directly
    show_membership_operators()
