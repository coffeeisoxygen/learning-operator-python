import re

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from sympy import Eq, solve, symbols, sympify

console = Console()


def math_solver_menu():
    """Display the math solver menu and handle user choices."""
    while True:
        console.print(
            Panel.fit("[bold blue]Math Solver[/bold blue]", border_style="blue")
        )
        console.print("[bold yellow]Pilih operasi:[/bold yellow]")
        console.print("1. Evaluasi Ekspresi Matematika")
        console.print("2. Menampilkan Urutan Operasi")
        console.print("3. Solver Persamaan Sederhana")
        console.print("4. Contoh Penggunaan Operator")
        console.print("5. Panduan Notasi Matematika")
        console.print("0. Kembali ke Menu Utama")

        choice = Prompt.ask(
            "\nMasukkan pilihan", choices=["0", "1", "2", "3", "4", "5"], default="1"
        )

        if choice == "0":
            break
        elif choice == "1":
            evaluate_expression()
        elif choice == "2":
            show_operation_order()
        elif choice == "3":
            solve_equation()
        elif choice == "4":
            show_operator_examples()
        elif choice == "5":
            show_math_notation_guide()


def show_math_notation_guide():
    console.print("\n[bold]Panduan Notasi Matematika:[/bold]")
    notation_table = Table()
    notation_table.add_column("Notasi Matematika", style="yellow")
    notation_table.add_column("Cara Input", style="green")
    notation_table.add_column("Contoh", style="cyan")

    notation_table.add_row("Pangkat/Eksponen", "^ atau **", "2^3 atau 2**3")
    notation_table.add_row("Perkalian", "* atau ×", "2*3 atau 2×3")
    notation_table.add_row("Pembagian", "/ atau ÷", "6/3 atau 6÷3")
    notation_table.add_row("Pecahan", "a/b", "1/4 (bukan frac{1}{4})")
    notation_table.add_row(
        "Akar Kuadrat", "sqrt() atau **(1/2)", "sqrt(16) atau 16**(1/2)"
    )

    console.print(notation_table)


def evaluate_expression():
    """Evaluate a mathematical expression and show the result."""
    console.print(
        Panel.fit("[bold blue]Evaluasi Ekspresi[/bold blue]", border_style="blue")
    )
    expr = Prompt.ask(
        "[yellow]Masukkan ekspresi matematika[/yellow] (contoh: 2*(3+4)/5)"
    )

    try:
        # Support for common math notation
        expr = expr.replace("^", "**")  # Support for ^ as power
        expr = expr.replace("×", "*")  # Support for × symbol
        expr = expr.replace("÷", "/")  # Support for ÷ symbol

        # Create symbols for variables if needed
        x, y, z = symbols("x y z")

        # Show the expression with syntax highlighting
        console.print("\n[bold]Ekspresi yang dievaluasi:[/bold]")
        syntax = Syntax(expr, "python", theme="monokai")
        console.print(syntax)

        # Calculate and show result
        result = sympify(expr)

        console.print(
            Panel.fit(f"Hasil: [bold green]{result}[/bold green]", border_style="green")
        )

        # Show decimal approximation for complex results
        if result.is_real and not result.is_Integer:
            console.print(f"Nilai desimal: [cyan]{float(result):.6f}[/cyan]")

        # Show steps of calculation if possible
        show_calculation_steps(expr)

    except Exception as e:
        console.print(Panel.fit(f"Error: {e}", border_style="red"))
        console.print(
            Panel(
                "[yellow]Tips:[/yellow] Pastikan ekspresi valid. Contoh: 2*(3+4) atau x**2 + 5*x + 6",
                border_style="yellow",
            )
        )

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


def show_calculation_steps(expr):
    """Attempt to show calculation steps for educational purposes."""
    try:
        # Only attempt to show steps for simple expressions without variables
        if any(sym in expr for sym in "xyz"):
            return

        # Basic steps for a simple expression
        steps = []

        # Handle parentheses first
        pattern = r"\([^()]+\)"
        matches = re.findall(pattern, expr)
        mod_expr = expr

        for match in matches:
            sub_result = eval(match)
            steps.append(f"{mod_expr} → Evaluasi {match} = {sub_result}")
            mod_expr = mod_expr.replace(match, str(sub_result))

        # Show the final evaluation if we found parentheses
        if steps:
            steps.append(f"{mod_expr} = {eval(expr)}")
            console.print("\n[bold]Langkah Perhitungan:[/bold]")
            for step in steps:
                console.print(f"[cyan]{step}[/cyan]")

    except Exception:
        # Just skip showing steps if there's an issue
        pass


def show_operation_order():
    """Show the order of operations in Python."""
    console.print(
        Panel.fit("[bold blue]Urutan Operasi (PEMDAS)[/bold blue]", border_style="blue")
    )

    table = Table(title="Urutan Operasi dalam Python")
    table.add_column("Urutan", style="cyan")
    table.add_column("Operasi", style="green")
    table.add_column("Operator", style="yellow")
    table.add_column("Contoh", style="magenta")

    table.add_row("1", "Parentheses (Kurung)", "()", "(2 + 3) * 4 = 20")
    table.add_row("2", "Exponentiation (Pangkat)", "**", "2 ** 3 = 8")
    table.add_row("3", "Multiplication (Perkalian)", "*", "2 * 3 = 6")
    table.add_row("3", "Division (Pembagian)", "/", "6 / 3 = 2.0")
    table.add_row("3", "Floor Division (Pembagian Bulat)", "//", "7 // 3 = 2")
    table.add_row("3", "Modulus (Sisa Bagi)", "%", "7 % 3 = 1")
    table.add_row("4", "Addition (Penambahan)", "+", "2 + 3 = 5")
    table.add_row("4", "Subtraction (Pengurangan)", "-", "5 - 2 = 3")

    console.print(table)

    console.print("\n[bold]Contoh dengan Ekspresi Kompleks:[/bold]")
    example = "2 + 3 * 4 ** 2 / (6 - 2)"
    console.print(f"Ekspresi: [yellow]{example}[/yellow]")
    console.print(f"Hasil: [bold green]{eval(example)}[/bold green]")

    console.print("\n[bold]Langkah-langkah Evaluasi:[/bold]")
    console.print("1. Evaluasi kurung: (6 - 2) = 4")
    console.print("2. Evaluasi pangkat: 4 ** 2 = 16")
    console.print("3. Evaluasi perkalian dan pembagian dari kiri ke kanan:")
    console.print("   3 * 16 = 48, kemudian 48 / 4 = 12")
    console.print("4. Evaluasi penambahan: 2 + 12 = 14")

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


def solve_equation():
    """Solve a simple equation."""
    console.print(
        Panel.fit("[bold blue]Solver Persamaan[/bold blue]", border_style="blue")
    )
    console.print("[yellow]Masukkan persamaan dengan format: ax + b = c[/yellow]")
    equation = Prompt.ask("Persamaan")

    try:
        # Parse left and right sides
        if "=" not in equation:
            raise ValueError("Persamaan harus mengandung tanda '='")

        left, right = equation.split("=", 1)
        left = left.strip()
        right = right.strip()

        # Replace common notations
        left = left.replace("^", "**")
        right = right.replace("^", "**")

        # Define symbol and create equation
        x = symbols("x")
        eq = Eq(sympify(left), sympify(right))

        # Solve equation
        solution = solve(eq, x)

        console.print(
            Panel.fit(
                f"Solusi: x = [bold green]{solution}[/bold green]", border_style="green"
            )
        )

    except Exception as e:
        console.print(Panel.fit(f"Error: {e}", border_style="red"))
        console.print(
            Panel(
                "[yellow]Contoh persamaan valid: 2*x + 3 = 7 atau x^2 - 4 = 0[/yellow]",
                border_style="yellow",
            )
        )

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


def show_operator_examples():
    """Show examples of different operators in calculations."""
    console.print(
        Panel.fit(
            "[bold blue]Contoh Penggunaan Operator[/bold blue]", border_style="blue"
        )
    )

    examples = [
        ("Aritmatika", "2 + 3 * 4 - 5 / 2", eval("2 + 3 * 4 - 5 / 2")),
        ("Pembagian Bulat", "17 // 5", eval("17 // 5")),
        ("Modulus", "17 % 5", eval("17 % 5")),
        ("Pangkat", "2 ** 8", eval("2 ** 8")),
        ("Perbandingan", "3 > 2 and 5 <= 5", eval("3 > 2 and 5 <= 5")),
        (
            "Operator Logika",
            "True and False or not False",
            eval("True and False or not False"),
        ),
    ]

    for category, expr, result in examples:
        console.print(f"\n[bold]{category}:[/bold]")
        console.print(f"Ekspresi: [yellow]{expr}[/yellow]")
        console.print(f"Hasil: [bold green]{result}[/bold green]")

    console.print("\nTekan Enter untuk melanjutkan...")
    input()


if __name__ == "__main__":
    math_solver_menu()
