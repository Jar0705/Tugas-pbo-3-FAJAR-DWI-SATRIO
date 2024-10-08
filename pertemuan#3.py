class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self._nilai = nilai  # nilai privat

    def get_nilai(self):
        return self._nilai

    def set_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self._nilai = nilai_baru
        else:
            print("Nilai harus antara 0 dan 100")


class MahasiswaView:
    def render(self, mahasiswa):
        return f"""
Mahasiswa:
Nama: {mahasiswa.nama}
NIM: {mahasiswa.nim}
Nilai: {mahasiswa.get_nilai()}
        """


class MahasiswaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.mahasiswa_list = []  # Menyimpan daftar mahasiswa

    def tambah_mahasiswa(self, nama, nim, nilai):
        mahasiswa = self.model(nama, nim, nilai)
        self.mahasiswa_list.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        if self.mahasiswa_list:
            mahasiswa = self.mahasiswa_list[0]
            output = self.view.render(mahasiswa)
            print(output)
        else:
            print("Belum ada mahasiswa.")

    def ubah_nilai(self, nim, nilai_baru):
        mahasiswa = next((m for m in self.mahasiswa_list if m.nim == nim), None)
        if mahasiswa:
            mahasiswa.set_nilai(nilai_baru)
            print(f"{mahasiswa.nama} memiliki nilai baru: {mahasiswa.get_nilai()}")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")


# Inisialisasi dan Penggunaan
mahasiswa_view = MahasiswaView()
mahasiswa_controller = MahasiswaController(Mahasiswa, mahasiswa_view)

# Menambah mahasiswa dan menampilkan data
mahasiswa_controller.tambah_mahasiswa("Fajar dwi satrio", "2023011110031", 98)
mahasiswa_controller.tampilkan_mahasiswa()

# Mengubah nilai mahasiswa
mahasiswa_controller.ubah_nilai("2023011110031", 90)
