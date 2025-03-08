from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

console = Console()


def show_identity_operators():
    # Display title and introduction
    console.print(
        Panel.fit("[bold cyan]Operator Identitas[/bold cyan]", border_style="cyan")
    )

    console.print("\n[yellow]Operator Identitas adalah:[/yellow]")
    console.print(
        "Operator identitas digunakan untuk membandingkan objek, bukan nilai mereka. "
        "Operator ini memeriksa apakah dua variabel merujuk ke objek yang sama di memori.\n"
    )

    # Create table for operators
    table = Table(title="Operator Identitas dalam Python")

    # Add columns
    table.add_column("Operator", style="cyan", justify="center")
    table.add_column("Nama", style="green")
    table.add_column("Penjelasan", style="yellow")
    table.add_column("Contoh", style="magenta")
    table.add_column("Hasil", style="blue")

    # Add rows with data
    table.add_row(
        "is",
        "Identitas",
        "Mengembalikan True jika kedua variabel merujuk ke objek yang sama",
        "x is y",
        "True jika x dan y merujuk ke objek yang sama",
    )
    table.add_row(
        "is not",
        "Bukan Identitas",
        "Mengembalikan True jika kedua variabel tidak merujuk ke objek yang sama",
        "x is not y",
        "True jika x dan y merujuk ke objek yang berbeda",
    )

    # Print the table
    console.print(table)

    # Show practical examples
    console.print("\n[bold]Contoh Praktis:[/bold]")
    code = """
# Contoh dengan list
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}, b = {b}, c = a")
print(f"a is b: {a is b}")      # False, meskipun nilainya sama
print(f"a is c: {a is c}")      # True, karena c merujuk ke objek yang sama dengan a

# Contoh dengan integer
x = 5
y = 5
z = 5.0

print(f"x = {x}, y = {y}, z = {z}")
print(f"x is y: {x is y}")      # True untuk beberapa nilai (perilaku khusus Python)
print(f"x is z: {x is z}")      # False, karena tipe datanya berbeda
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    console.print("\n[bold]Contoh Lain:[/bold]")
    code_examples = """
# Contoh dengan string
str1 = "Hello"
str2 = "Hello"
str3 = "Hello World"

print(f"str1 = '{str1}', str2 = '{str2}', str3 = '{str3}'")
print(f"str1 is not str2: {str1 is not str2}")  # False, string yang sama di lokasi yang sama
print(f"str1 is not str3: {str1 is not str3}")  # True, karena objeknya berbeda

# Perbedaan antara 'is' dan '=='
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"list1 = {list1}, list2 = {list2}")
print(f"list1 == list2: {list1 == list2}")  # True, karena nilainya sama
print(f"list1 is list2: {list1 is list2}")  # False, karena objeknya berbeda
"""
    syntax2 = Syntax(code_examples, "python", theme="monokai", line_numbers=True)
    console.print(syntax2)

    # Interactive example
    console.print("\n[bold green]Ingin mencoba sendiri?[/bold green]")
    try_example = Prompt.ask(
        "Apakah Anda ingin mencoba contoh interaktif?", choices=["y", "n"], default="y"
    )

    if try_example.lower() == "y":
        interactive_identity_example()

    # Return to main menu prompt
    console.print("\nTekan Enter untuk kembali ke menu utama...")
    input()


def interactive_identity_example():
    """Interactive demonstration of identity operators."""
    try:
        console.print(
            "\n[bold yellow]Mari mencoba operator identitas secara interaktif:[/bold yellow]"
        )

        # Create lists to demonstrate identity
        console.print(
            "\n[bold]Membuat dua list dengan nilai yang sama tetapi identitas berbeda:[/bold]"
        )
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = list1  # Referensi ke list yang sama

        console.print(f"list1 = {list1}")
        console.print(f"list2 = {list2} (list baru dengan nilai yang sama)")
        console.print("list3 = list1 (referensi ke list yang sama)")

        console.print("\n[bold green]Hasil Operator Identitas:[/bold green]")
        console.print(
            f"list1 == list2: [bold cyan]{list1 == list2}[/bold cyan] (nilai sama)"
        )
        console.print(
            f"list1 is list2: [bold cyan]{list1 is list2}[/bold cyan] (objek berbeda)"
        )
        console.print(
            f"list1 is list3: [bold cyan]{list1 is list3}[/bold cyan] (objek sama)"
        )
        console.print(
            f"list1 is not list2: [bold cyan]{list1 is not list2}[/bold cyan]"
        )
        console.print(
            f"list1 is not list3: [bold cyan]{list1 is not list3}[/bold cyan]"
        )

        # Let user try with custom values
        console.print("\n[bold]Mencoba dengan nilai kustom:[/bold]")
        console.print(
            "[yellow]Catatan: Nilai sederhana seperti angka kecil dan string pendek mungkin memiliki perilaku khusus[/yellow]"
        )

        value = Prompt.ask(
            "Masukkan sebuah nilai (akan dibuat dua objek terpisah dengan nilai sama)"
        )

        # Try to convert to appropriate type
        try:
            # Try as number
            num_value = int(value)
            obj1 = num_value
            obj2 = int(value)  # Create a new object with the same value
        except ValueError:
            try:
                num_value = float(value)
                obj1 = num_value
                obj2 = float(value)  # Create a new object with the same value
            except ValueError:
                # Handle as string
                obj1 = value
                obj2 = str(value)  # May or may not create a new string due to interning

        console.print(f"\nobj1 = {obj1}")
        console.print(f"obj2 = {obj2} (objek lain dengan nilai sama)")

        console.print(
            "\n[bold green]Hasil Operator Identitas dengan Nilai Kustom:[/bold green]"
        )
        console.print(
            f"obj1 == obj2: [bold cyan]{obj1 == obj2}[/bold cyan] (perbandingan nilai)"
        )
        console.print(
            f"obj1 is obj2: [bold cyan]{obj1 is obj2}[/bold cyan] (perbandingan identitas)"
        )

        if obj1 is obj2:
            console.print(
                "\n[yellow]Catatan: Python mengoptimasi beberapa objek seperti angka kecil dan string pendek.[/yellow]"
            )
            console.print(
                "[yellow]Hal ini menyebabkan objek dengan nilai yang sama bisa memiliki identitas yang sama.[/yellow]"
            )

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")


if __name__ == "__main__":
    # This allows testing the module directly
    show_identity_operators()
