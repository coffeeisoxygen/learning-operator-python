from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# --------------------- Helper Functions ---------------------#


def get_number_input(prompt_text, allow_binary=True):
    """Get user input and convert to integer, supporting binary/hex/octal formats."""
    input_value = Prompt.ask(prompt_text)

    try:
        # Handle prefixed numbers (0b, 0x, 0o)
        if allow_binary and input_value.startswith(("0b", "0x", "0o")):
            return int(input_value, 0), input_value
        else:
            # Handle binary without prefix
            if allow_binary and all(bit in "01" for bit in input_value):
                try:
                    return int(input_value, 2), "0b" + input_value
                except ValueError:
                    pass
            # Standard integer
            return int(input_value), input_value
    except ValueError:
        raise ValueError("Input harus berupa angka valid")


def show_binary_representation(value, label="Nilai"):
    """Display a value in both decimal and binary format."""
    console.print(f"{label} = {value} (desimal) = {bin(value)} (biner)")


def create_result_table(title, operations):
    """Create a table showing operation results in decimal and binary."""
    table = Table(title=title)
    table.add_column("Operasi", style="cyan")
    table.add_column("Hasil (Desimal)", style="green")
    table.add_column("Hasil (Biner)", style="yellow")

    for op, result in operations.items():
        if isinstance(result, float):
            table.add_row(op, f"{result:.2f}", "N/A")
        else:
            table.add_row(op, str(result), bin(result))

    return table


def show_bitwise_notation_guide():
    """Display a guide for bitwise operations notation."""
    console.print("\n[bold]Panduan Notasi Bitwise:[/bold]")
    notation_table = Table()
    notation_table.add_column("Operasi", style="cyan")
    notation_table.add_column("Simbol", style="green")
    notation_table.add_column("Contoh", style="yellow")
    notation_table.add_column("Penjelasan", style="magenta")

    notation_table.add_row(
        "AND", "&", "x & y", "Membandingkan bit-by-bit, menghasilkan 1 jika keduanya 1"
    )
    notation_table.add_row(
        "OR", "|", "x | y", "Membandingkan bit-by-bit, menghasilkan 1 jika salah satu 1"
    )
    notation_table.add_row(
        "XOR", "^", "x ^ y", "Membandingkan bit-by-bit, menghasilkan 1 jika bit berbeda"
    )
    notation_table.add_row(
        "NOT", "~", "~x", "Membalikkan semua bit (0 menjadi 1, 1 menjadi 0)"
    )
    notation_table.add_row(
        "Left Shift", "<<", "x << 2", "Menggeser bit ke kiri, menambahkan 0 di kanan"
    )
    notation_table.add_row(
        "Right Shift",
        ">>",
        "x >> 1",
        "Menggeser bit ke kanan, mengabaikan bit yang terpotong",
    )

    console.print(notation_table)


def wait_for_user():
    """Wait for user input before continuing."""
    console.print("\nTekan Enter untuk melanjutkan...")
    input()


# --------------------- Main Menu Functions ---------------------#


def binary_converter_menu():
    """Display the binary converter menu and handle user choices."""
    while True:
        console.print(
            Panel.fit(
                "[bold blue]Binary Converter & Calculator[/bold blue]",
                border_style="blue",
            )
        )
        console.print("[bold yellow]Pilih operasi:[/bold yellow]")
        console.print("1. Konversi Desimal ke Biner")
        console.print("2. Konversi Biner ke Desimal")
        console.print("3. Operasi Bitwise")
        console.print("4. Aritmatika dengan Biner")
        console.print("5. Contoh Soal Bitwise")
        console.print("0. Kembali ke Menu Utama")

        choice = Prompt.ask(
            "\nMasukkan pilihan", choices=["0", "1", "2", "3", "4", "5"], default="1"
        )

        if choice == "0":
            break
        elif choice == "1":
            decimal_to_binary()
        elif choice == "2":
            binary_to_decimal()
        elif choice == "3":
            bitwise_operations()
        elif choice == "4":
            binary_arithmetic()
        elif choice == "5":
            bitwise_examples()


# --------------------- Core Functions ---------------------#


def decimal_to_binary():
    """Convert a decimal number to binary."""
    console.print(
        Panel.fit(
            "[bold blue]Konversi Desimal ke Biner[/bold blue]", border_style="blue"
        )
    )

    try:
        decimal, _ = get_number_input(
            "[yellow]Masukkan angka desimal[/yellow]", allow_binary=False
        )
        binary = bin(decimal)

        console.print(f"[green]Hasil: {decimal} (desimal) = {binary} (biner)[/green]")

        # Show conversion steps for educational purposes
        console.print("\n[bold]Langkah Konversi:[/bold]")
        steps = []
        temp = decimal
        while temp > 0:
            steps.append(f"{temp} ÷ 2 = {temp // 2} dengan sisa {temp % 2}")
            temp //= 2

        # Print steps in reverse (bottom-up)
        for step in reversed(steps):
            console.print(f"[cyan]{step}[/cyan]")

        # Format the binary digits
        binary_digits = binary[2:]  # Remove '0b' prefix
        console.print("\n[bold]Hasil dari bawah ke atas (sisa):[/bold]")
        console.print(f"[green]{binary_digits}[/green]")

    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

    wait_for_user()


def binary_to_decimal():
    """Convert a binary number to decimal."""
    console.print(
        Panel.fit(
            "[bold blue]Konversi Biner ke Desimal[/bold blue]", border_style="blue"
        )
    )

    try:
        binary = Prompt.ask(
            "[yellow]Masukkan angka biner[/yellow] (contoh: 1010 atau 0b1010)"
        )

        # Remove 0b prefix if present
        if binary.startswith("0b"):
            binary = binary[2:]

        # Validate binary input
        if not all(bit in "01" for bit in binary):
            raise ValueError("Input hanya boleh berisi 0 dan 1")

        decimal = int(binary, 2)

        console.print(f"[green]Hasil: 0b{binary} (biner) = {decimal} (desimal)[/green]")

        # Show conversion steps
        console.print("\n[bold]Langkah Konversi:[/bold]")
        binary_len = len(binary)

        total = 0
        for i, bit in enumerate(binary):
            position = binary_len - i - 1
            value = int(bit) * (2**position)
            total += value
            console.print(
                f"[cyan]Posisi {position}: {bit} × 2^{position} = {value}[/cyan]"
            )

        console.print(f"\n[bold]Total: [green]{total}[/green][/bold]")

    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

    wait_for_user()


def bitwise_operations():
    """Perform bitwise operations with variable number of inputs."""
    console.print(
        Panel.fit("[bold blue]Operasi Bitwise[/bold blue]", border_style="blue")
    )

    # Show notation guide first
    show_bitwise_notation_guide()

    # Ask user for simple or advanced mode - FIX: remove the conflicting first argument
    mode = Prompt.ask(
        prompt="[bold]Pilih mode:[/bold]\n1. Quick mode (2 variabel, semua operasi)\n2. Custom mode (ekspresi kustom)\n> ",
        choices=["1", "2"],
        default="1",
    )

    if mode == "1":
        quick_bitwise_operations()
    else:
        custom_bitwise_expression()


def quick_bitwise_operations():
    """Simple mode with two variables and all bitwise operations."""
    try:
        # Get input values
        console.print("[yellow]Masukkan dua angka untuk operasi bitwise[/yellow]")
        a, _ = get_number_input("Angka pertama (a)")
        b, _ = get_number_input("Angka kedua (b)")

        # Create a table for results
        table = Table(title="Hasil Operasi Bitwise")
        table.add_column("Operasi", style="cyan")
        table.add_column("Hasil (Desimal)", style="green")
        table.add_column("Hasil (Biner)", style="yellow")

        # Bitwise operations
        operations = {
            "AND (a & b)": a & b,
            "OR (a | b)": a | b,
            "XOR (a ^ b)": a ^ b,
            "NOT a (~a)": ~a,
            "NOT b (~b)": ~b,
            "Left Shift a (a << 1)": a << 1,
            "Left Shift b (b << 1)": b << 1,
            "Right Shift a (a >> 1)": a >> 1,
            "Right Shift b (b >> 1)": b >> 1,
        }

        for op, result in operations.items():
            table.add_row(op, str(result), bin(result))

        console.print(table)

        # Show binary representation
        console.print("\n[bold]Representasi Biner:[/bold]")
        show_binary_representation(a, "a")
        show_binary_representation(b, "b")

        # Visual representation for AND operation
        console.print("\n[bold]Visualisasi AND (a & b):[/bold]")
        a_bin = bin(a)[2:].zfill(max(len(bin(a)[2:]), len(bin(b)[2:])))
        b_bin = bin(b)[2:].zfill(max(len(bin(a)[2:]), len(bin(b)[2:])))
        result_bin = bin(a & b)[2:].zfill(max(len(bin(a)[2:]), len(bin(b)[2:])))

        console.print(f"a:      [cyan]{a_bin}[/cyan]")
        console.print(f"b:      [cyan]{b_bin}[/cyan]")
        console.print(f"a & b:  [green]{result_bin}[/green]")

    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

    wait_for_user()


def custom_bitwise_expression():
    """Allow users to input and evaluate custom bitwise expressions."""
    try:
        # Get number of variables
        var_count = int(
            Prompt.ask("\n[yellow]Masukkan jumlah variabel[/yellow] (1-5)", default="3")
        )
        if var_count < 1 or var_count > 5:
            raise ValueError("Jumlah variabel harus antara 1 sampai 5")

        # Define variable names and get values
        var_names = "xyzuv"[:var_count]
        variables = {}

        for var in var_names:
            val, _ = get_number_input(f"Masukkan nilai untuk {var}")
            variables[var] = val
            show_binary_representation(val, var)

        # Get expression
        console.print(
            "\n[bold yellow]Masukkan ekspresi bitwise[/bold yellow] (contoh: x & y | ~z)"
        )
        console.print("[dim]Gunakan variabel yang telah didefinisikan[/dim]")
        expr = Prompt.ask("Ekspresi")

        # Create restricted namespace with only our variables
        namespace = {var: val for var, val in variables.items()}

        # Evaluate expression safely
        result = eval(expr, {"__builtins__": {}}, namespace)

        # Show results
        console.print("\n[bold]Hasil:[/bold]")
        console.print(f"Ekspresi: [yellow]{expr}[/yellow]")
        console.print(f"Hasil: [green]{result}[/green]")
        console.print(f"Biner: [cyan]{bin(result)}[/cyan]")

        # Highlight operators used
        console.print("\n[bold]Operator yang digunakan:[/bold]")
        operators = {
            "&": "AND - Membandingkan bit-by-bit, menghasilkan 1 jika keduanya 1",
            "|": "OR - Membandingkan bit-by-bit, menghasilkan 1 jika salah satu 1",
            "^": "XOR - Membandingkan bit-by-bit, menghasilkan 1 jika bit berbeda",
            "~": "NOT - Membalikkan semua bit (0 menjadi 1, 1 menjadi 0)",
            "<<": "Left Shift - Menggeser bit ke kiri, menambahkan 0 di kanan",
            ">>": "Right Shift - Menggeser bit ke kanan",
        }

        for op, desc in operators.items():
            if op in expr:
                console.print(f"[cyan]Operator {op}: {desc}[/cyan]")

    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
    except SyntaxError:
        console.print("[bold red]Error: Sintaks ekspresi tidak valid[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

    wait_for_user()


def binary_arithmetic():
    """Perform arithmetic operations with binary numbers."""
    console.print(
        Panel.fit("[bold blue]Aritmatika dengan Biner[/bold blue]", border_style="blue")
    )

    try:
        # Get input values
        console.print(
            "[yellow]Masukkan dua angka dalam format biner atau desimal[/yellow]"
        )
        a, _ = get_number_input("Angka pertama (a)")
        b, _ = get_number_input("Angka kedua (b)")

        # Create a table for results
        table = Table(title="Hasil Operasi Aritmatika")
        table.add_column("Operasi", style="cyan")
        table.add_column("Hasil (Desimal)", style="green")
        table.add_column("Hasil (Biner)", style="yellow")

        # Arithmetic operations
        operations = {
            "Penjumlahan (a + b)": a + b,
            "Pengurangan (a - b)": a - b,
            "Perkalian (a * b)": a * b,
        }

        # Add division if b is not zero
        if b != 0:
            operations["Pembagian (a / b)"] = a / b  # type: ignore
            operations["Pembagian Bulat (a // b)"] = a // b
            operations["Modulus (a % b)"] = a % b

        for op, result in operations.items():
            # Handle float results from division
            if isinstance(result, float):
                table.add_row(op, f"{result:.2f}", "N/A")
            else:
                table.add_row(op, str(result), bin(result))

        console.print(table)

        # Show binary representation
        console.print("\n[bold]Representasi Biner:[/bold]")
        show_binary_representation(a, "a")
        show_binary_representation(b, "b")

    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
    except ZeroDivisionError:
        console.print(
            "[bold red]Error: Pembagian dengan nol tidak diperbolehkan[/bold red]"
        )

    wait_for_user()


def bitwise_examples():
    """Show examples of bitwise operations for the given problems."""
    console.print(
        Panel.fit("[bold blue]Contoh Soal Bitwise[/bold blue]", border_style="blue")
    )

    # Problem Set 1
    console.print("[bold yellow]Soal 1:[/bold yellow]")
    console.print("Diketahui:")
    console.print("x = 100 (0b1100100)")
    console.print("y = 10 (0b1010)")
    console.print("z = 68 (0b1000100)")

    # Values
    x1, y1, z1 = 100, 10, 68

    examples = [
        {
            "title": "A - x & y & z",
            "steps": [
                ("x & y & z", f"{x1} & {y1} & {z1}"),
                ("Dalam biner", f"{bin(x1)} & {bin(y1)} & {bin(z1)}"),
            ],
            "result": x1 & y1 & z1,
        },
        {
            "title": "B - x ^ y << 5 >> 2",
            "steps": [
                ("Langkah 1: y << 5", f"{y1} << 5 = {y1 << 5} ({bin(y1 << 5)})"),
                (
                    "Langkah 2: x ^ (y << 5)",
                    f"{x1} ^ {y1 << 5} = {x1 ^ (y1 << 5)} ({bin(x1 ^ (y1 << 5))})",
                ),
                (
                    "Langkah 3: (x ^ (y << 5)) >> 2",
                    f"{x1 ^ (y1 << 5)} >> 2 = {(x1 ^ (y1 << 5)) >> 2} ({bin((x1 ^ (y1 << 5)) >> 2)})",
                ),
            ],
            "result": (x1 ^ (y1 << 5)) >> 2,
        },
        {
            "title": "C - ~x & ~y | ~z",
            "steps": [
                ("Langkah 1: ~x", f"~{x1} = {~x1} ({bin(~x1)})"),
                ("Langkah 2: ~y", f"~{y1} = {~y1} ({bin(~y1)})"),
                ("Langkah 3: ~z", f"~{z1} = {~z1} ({bin(~z1)})"),
                (
                    "Langkah 4: ~x & ~y",
                    f"{~x1} & {~y1} = {~x1 & ~y1} ({bin(~x1 & ~y1)})",
                ),
                (
                    "Langkah 5: (~x & ~y) | ~z",
                    f"{~x1 & ~y1} | {~z1} = {(~x1 & ~y1) | ~z1} ({bin((~x1 & ~y1) | ~z1)})",
                ),
            ],
            "result": (~x1 & ~y1) | ~z1,
        },
    ]

    for example in examples:
        console.print(f"\n[bold cyan]{example['title']}[/bold cyan]")
        for step_name, step_val in example["steps"]:
            console.print(f"{step_name}: {step_val}")
        console.print(
            f"Hasil: [green]{example['result']} (desimal) = {bin(example['result'])} (biner)[/green]"
        )

    # Problem Set 2
    console.print("\n[bold yellow]Soal 2:[/bold yellow]")
    console.print("Diketahui:")
    console.print("x = 0b1100100 (100 dalam desimal)")
    console.print("y = 0b110010 (50 dalam desimal)")
    console.print("z = 0b101 (5 dalam desimal)")

    # Values
    x2, y2, z2 = 0b1100100, 0b110010, 0b101

    arithmetic_examples = [
        {
            "title": "A - x - y/z",
            "steps": [
                ("Langkah 1: y/z", f"{y2}/{z2} = {y2 / z2}"),
                ("Langkah 2: x - (y/z)", f"{x2} - {y2 / z2} = {x2 - y2 / z2}"),
            ],
            "result": x2 - y2 / z2,
            "is_float": True,
        },
        {
            "title": "B - (x*z)+y/x-z+z",
            "steps": [
                ("Langkah 1: x*z", f"{x2}*{z2} = {x2 * z2}"),
                ("Langkah 2: y/x", f"{y2}/{x2} = {y2 / x2}"),
                (
                    "Langkah 3: (x*z) + y/x",
                    f"{x2 * z2} + {y2 / x2} = {x2 * z2 + y2 / x2}",
                ),
                (
                    "Langkah 4: (x*z) + y/x - z",
                    f"{x2 * z2 + y2 / x2} - {z2} = {x2 * z2 + y2 / x2 - z2}",
                ),
                (
                    "Langkah 5: (x*z) + y/x - z + z",
                    f"{x2 * z2 + y2 / x2 - z2} + {z2} = {x2 * z2 + y2 / x2}",
                ),
            ],
            "result": x2 * z2 + y2 / x2,
            "is_float": True,
        },
    ]

    for example in arithmetic_examples:
        console.print(f"\n[bold cyan]{example['title']}[/bold cyan]")
        for step_name, step_val in example["steps"]:
            console.print(f"{step_name}: {step_val}")

        if example["is_float"]:
            result = example["result"]
            console.print(f"Hasil: [green]{result}[/green]")
            console.print(f"Biner: [cyan]{bin(int(result))}[/cyan] (dibulatkan)")
        else:
            result = example["result"]
            console.print(f"Hasil: [green]{result}[/green]")
            console.print(f"Biner: [cyan]{bin(result)}[/cyan]")

    console.print(
        "\n[bold yellow]Catatan:[/bold yellow] Hasil pecahan dibulatkan untuk representasi biner"
    )

    wait_for_user()


if __name__ == "__main__":
    binary_converter_menu()
