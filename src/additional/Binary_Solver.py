from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


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
        console.print("6. Ekspresi Bitwise Kustom")  # New option
        console.print("0. Kembali ke Menu Utama")

        choice = Prompt.ask(
            "\nMasukkan pilihan",
            choices=["0", "1", "2", "3", "4", "5", "6"],
            default="1",
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
        elif choice == "6":
            custom_bitwise_expression()


def decimal_to_binary():
    """Convert a decimal number to binary."""
    console.print(
        Panel.fit(
            "[bold blue]Konversi Desimal ke Biner[/bold blue]", border_style="blue"
        )
    )

    try:
        decimal = int(Prompt.ask("[yellow]Masukkan angka desimal[/yellow]"))
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

    except ValueError:
        console.print("[bold red]Error: Masukkan angka desimal yang valid[/bold red]")

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


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

        for i, bit in enumerate(binary):
            position = binary_len - i - 1
            value = int(bit) * (2**position)
            console.print(
                f"[cyan]Posisi {position}: {bit} × 2^{position} = {value}[/cyan]"
            )

        console.print(f"\n[bold]Total: [green]{decimal}[/green][/bold]")

    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


def bitwise_operations():
    """Perform bitwise operations."""
    console.print(
        Panel.fit("[bold blue]Operasi Bitwise[/bold blue]", border_style="blue")
    )

    try:
        # Get input values
        console.print("[yellow]Masukkan dua angka untuk operasi bitwise[/yellow]")
        a_input = Prompt.ask("Angka pertama (a)")
        b_input = Prompt.ask("Angka kedua (b)")

        # Convert to integers (handle binary inputs)
        a = int(a_input, 0) if a_input.startswith(("0b", "0x", "0o")) else int(a_input)
        b = int(b_input, 0) if b_input.startswith(("0b", "0x", "0o")) else int(b_input)

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
            "Right Shift a (a >> 1)": a >> 1,
        }

        for op, result in operations.items():
            table.add_row(op, str(result), bin(result))

        console.print(table)

        # Show binary representation
        console.print("\n[bold]Representasi Biner:[/bold]")
        console.print(f"a = {a} (desimal) = {bin(a)} (biner)")
        console.print(f"b = {b} (desimal) = {bin(b)} (biner)")

        # Visual representation for AND operation
        console.print("\n[bold]Visualisasi AND (a & b):[/bold]")
        a_bin = bin(a)[2:].zfill(max(len(bin(a)[2:]), len(bin(b)[2:])))
        b_bin = bin(b)[2:].zfill(max(len(bin(a)[2:]), len(bin(b)[2:])))
        result_bin = bin(a & b)[2:].zfill(max(len(bin(a)[2:]), len(bin(b)[2:])))

        console.print(f"a:      [cyan]{a_bin}[/cyan]")
        console.print(f"b:      [cyan]{b_bin}[/cyan]")
        console.print(f"a & b:  [green]{result_bin}[/green]")

    except ValueError:
        console.print("[bold red]Error: Masukkan angka valid[/bold red]")

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


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
        a_input = Prompt.ask("Angka pertama (a)")
        b_input = Prompt.ask("Angka kedua (b)")

        # Convert to integers (handle binary inputs)
        a = int(a_input, 0) if a_input.startswith(("0b", "0x", "0o")) else int(a_input)
        b = int(b_input, 0) if b_input.startswith(("0b", "0x", "0o")) else int(b_input)

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
        console.print(f"a = {a} (desimal) = {bin(a)} (biner)")
        console.print(f"b = {b} (desimal) = {bin(b)} (biner)")

    except ValueError:
        console.print("[bold red]Error: Masukkan angka valid[/bold red]")
    except ZeroDivisionError:
        console.print(
            "[bold red]Error: Pembagian dengan nol tidak diperbolehkan[/bold red]"
        )

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


# Add this new function in Binary_Solver.py
def custom_bitwise_expression():
    """Allow users to input and evaluate custom bitwise expressions."""
    console.print(
        Panel.fit("[bold blue]Ekspresi Bitwise Kustom[/bold blue]", border_style="blue")
    )

    # Show notation guide
    console.print("\n[bold]Panduan Notasi Bitwise:[/bold]")
    notation_table = Table()
    notation_table.add_column("Operasi", style="cyan")
    notation_table.add_column("Simbol", style="green")
    notation_table.add_column("Contoh", style="yellow")

    notation_table.add_row("AND", "&", "x & y")
    notation_table.add_row("OR", "|", "x | y")
    notation_table.add_row("XOR", "^", "x ^ y")
    notation_table.add_row("NOT", "~", "~x")
    notation_table.add_row("Left Shift", "<<", "x << 2")
    notation_table.add_row("Right Shift", ">>", "x >> 1")

    console.print(notation_table)

    try:
        # Get number of variables
        var_count = int(
            Prompt.ask("\n[yellow]Masukkan jumlah variabel[/yellow] (1-5)", default="3")
        )
        if var_count < 1 or var_count > 5:
            raise ValueError("Jumlah variabel harus antara 1 sampai 5")

        # Define variable names
        var_names = "xyzuv"[:var_count]

        # Get values for variables
        variables = {}
        for var in var_names:
            val_input = Prompt.ask(f"Masukkan nilai untuk {var}")

            # Support for binary input (0b prefix)
            if val_input.startswith("0b"):
                val = int(val_input, 2)
            else:
                val = int(val_input)

            variables[var] = val
            console.print(f"{var} = {val} ({bin(val)})")

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

        console.print("\n[bold]Hasil:[/bold]")
        console.print(f"Ekspresi: [yellow]{expr}[/yellow]")
        console.print(f"Hasil: [green]{result}[/green]")
        console.print(f"Biner: [cyan]{bin(result)}[/cyan]")

        # Show step-by-step breakdown
        console.print("\n[bold]Langkah Evaluasi:[/bold]")
        if "&" in expr:
            console.print(
                "[cyan]Operator AND (&) - Membandingkan bit-by-bit, menghasilkan 1 jika keduanya 1[/cyan]"
            )
        if "|" in expr:
            console.print(
                "[cyan]Operator OR (|) - Membandingkan bit-by-bit, menghasilkan 1 jika salah satu 1[/cyan]"
            )
        if "^" in expr:
            console.print(
                "[cyan]Operator XOR (^) - Membandingkan bit-by-bit, menghasilkan 1 jika bit berbeda[/cyan]"
            )
        if "~" in expr:
            console.print(
                "[cyan]Operator NOT (~) - Membalikkan semua bit (0 menjadi 1, 1 menjadi 0)[/cyan]"
            )
        if "<<" in expr:
            console.print(
                "[cyan]Operator Left Shift (<<) - Menggeser bit ke kiri, menambahkan 0 di kanan[/cyan]"
            )
        if ">>" in expr:
            console.print(
                "[cyan]Operator Right Shift (>>) - Menggeser bit ke kanan[/cyan]"
            )

        # Show values in binary for reference
        console.print("\n[bold]Nilai dalam biner:[/bold]")
        for var, val in variables.items():
            console.print(f"{var} = {val} ({bin(val)})")

    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
    except SyntaxError:
        console.print("[bold red]Error: Sintaks ekspresi tidak valid[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


def bitwise_examples():
    """Show examples of bitwise operations for the given problems."""
    console.print(
        Panel.fit("[bold blue]Contoh Soal Bitwise[/bold blue]", border_style="blue")
    )

    console.print("[bold yellow]Soal 1:[/bold yellow]")
    console.print("Diketahui:")
    console.print("x = 100 (0b1100100)")
    console.print("y = 10 (0b1010)")
    console.print("z = 68 (0b1000100)")

    # Values
    x1, y1, z1 = 100, 10, 68

    # Problem A
    console.print("\n[bold cyan]A - x & y & z[/bold cyan]")
    result_a = x1 & y1 & z1
    console.print(f"x & y & z = {x1} & {y1} & {z1}")
    console.print(f"Dalam biner: {bin(x1)} & {bin(y1)} & {bin(z1)}")
    console.print(
        f"Hasil: [green]{result_a} (desimal) = {bin(result_a)} (biner)[/green]"
    )

    # Problem B
    console.print("\n[bold cyan]B - x ^ y << 5 >> 2[/bold cyan]")
    step1 = y1 << 5  # First shift left
    step2 = x1 ^ step1  # Then XOR
    result_b = step2 >> 2  # Then shift right

    console.print(f"Langkah 1: y << 5 = {y1} << 5 = {step1} ({bin(step1)})")
    console.print(f"Langkah 2: x ^ (y << 5) = {x1} ^ {step1} = {step2} ({bin(step2)})")
    console.print(
        f"Langkah 3: (x ^ (y << 5)) >> 2 = {step2} >> 2 = {result_b} ({bin(result_b)})"
    )
    console.print(
        f"Hasil: [green]{result_b} (desimal) = {bin(result_b)} (biner)[/green]"
    )

    # Problem C
    console.print("\n[bold cyan]C - ~x & ~y | ~z[/bold cyan]")
    not_x = ~x1
    not_y = ~y1
    not_z = ~z1
    step1 = not_x & not_y
    result_c = step1 | not_z

    console.print(f"Langkah 1: ~x = ~{x1} = {not_x} ({bin(not_x)})")
    console.print(f"Langkah 2: ~y = ~{y1} = {not_y} ({bin(not_y)})")
    console.print(f"Langkah 3: ~z = ~{z1} = {not_z} ({bin(not_z)})")
    console.print(f"Langkah 4: ~x & ~y = {not_x} & {not_y} = {step1} ({bin(step1)})")
    console.print(
        f"Langkah 5: (~x & ~y) | ~z = {step1} | {not_z} = {result_c} ({bin(result_c)})"
    )
    console.print(
        f"Hasil: [green]{result_c} (desimal) = {bin(result_c)} (biner)[/green]"
    )

    # Second set of problems
    console.print("\n[bold yellow]Soal 2:[/bold yellow]")
    console.print("Diketahui:")
    console.print("x = 0b1100100 (100 dalam desimal)")
    console.print("y = 0b110010 (50 dalam desimal)")
    console.print("z = 0b101 (5 dalam desimal)")

    # Values
    x2, y2, z2 = 0b1100100, 0b110010, 0b101

    # Problem A
    console.print("\n[bold cyan]A - x - y/z[/bold cyan]")
    division = y2 / z2
    result_a2 = x2 - division

    console.print(f"Langkah 1: y/z = {y2}/{z2} = {division}")
    console.print(f"Langkah 2: x - (y/z) = {x2} - {division} = {result_a2}")
    console.print(f"Hasil: [green]{result_a2}[/green]")
    console.print(f"Biner: [cyan]{bin(int(result_a2))}[/cyan]")

    # Problem B
    console.print("\n[bold cyan]B - (x*z)+y/x-z+z[/bold cyan]")
    step1 = x2 * z2
    step2 = y2 / x2
    step3 = step1 + step2
    step4 = step3 - z2
    result_b2 = step4 + z2

    console.print(f"Langkah 1: x*z = {x2}*{z2} = {step1}")
    console.print(f"Langkah 2: y/x = {y2}/{x2} = {step2}")
    console.print(f"Langkah 3: (x*z) + y/x = {step1} + {step2} = {step3}")
    console.print(f"Langkah 4: (x*z) + y/x - z = {step3} - {z2} = {step4}")
    console.print(f"Langkah 5: (x*z) + y/x - z + z = {step4} + {z2} = {result_b2}")
    console.print(f"Hasil: [green]{result_b2}[/green]")
    console.print(f"Biner: [cyan]{bin(int(result_b2))}[/cyan]")
    console.print(
        "\n[bold yellow]Catatan:[/bold yellow] Hasil dibulatkan ke bilangan bulat"
    )

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


if __name__ == "__main__":
    binary_converter_menu()
