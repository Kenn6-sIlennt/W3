"""Modul untuk demonstrasi perbaikan kode_bau.py agar lolos Pylint."""

def proses_data(angka_pertama, angka_kedua, kondisi):
    """
    Memproses data berdasarkan kondisi yang diberikan.

    Args:
        angka_pertama (int): Angka pertama.
        angka_kedua (int): Angka kedua.
        kondisi (bool): Status kondisi.

    Returns:
        int or None: Hasil penjumlahan jika kondisi True, else None.
    """
    if kondisi:
        return angka_pertama + angka_kedua
    return None

def main():
    """Fungsi utama program."""
    hasil = proses_data(10, 20, True)
    print(f"Hasil proses: {hasil}")

if __name__ == "__main__":
    main()