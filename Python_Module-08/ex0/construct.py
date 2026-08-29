#!/usr/bin/env python3
import sys#hangi python sürümünü kullangımızı görmek icin, aktif calısan pythonun ortam/kurulum dizinine ulasmak icin 
import site
import os


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix
    #prefix suan calısan python un(python3) ortam dizinlerini / base ise ana python un ortam dizinlerini gösterir


def print_in_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    #şuan calısmakta olan python yorumlayıcısının tam dosya yolu
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print(
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\\Scripts\\activate # On Windows\n"
    )


def print_out_matrix() -> None:
    #list basıyor o yüzden ilk eleman venv de zaten 1 sitepackages var
    site_packages = site.getsitepackages()[0]
    venv_name = os.path.basename(sys.prefix)
    #basename path ın son bileşenini gösterir

    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}\n")
    print(
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n"
    )
    print("Package installation path:")
    print(f"{site_packages}")
    #site packages pip ile kurulan üçüncü parti paketlerin saklandıgı klasör


def main() -> None:
    if not is_virtual_env():
        print_in_matrix()
    else:
        print_out_matrix()



if __name__ == "__main__":
    main()
