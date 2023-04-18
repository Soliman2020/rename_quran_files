import os
import sys
from PyQt5 import QtWidgets, QtCore

# list of all surahs by the Musaf's order
surah_names_Arabic = [
    "الفاتحة",
    "البقرة",
    "آل عمران",
    "النساء",
    "المائدة",
    "الأنعام",
    "الأعراف",
    "الأنفال",
    "التوبة",
    "يونس",
    "هود",
    "يوسف",
    "الرعد",
    "إبراهيم",
    "الحجر",
    "النحل",
    "الإسراء",
    "الكهف",
    "مريم",
    "طه",
    "الأنبياء",
    "الحج",
    "المؤمنون",
    "النور",
    "الفرقان",
    "الشعراء",
    "النمل",
    "القصص",
    "العنكبوت",
    "الروم",
    "لقمان",
    "السجدة",
    "الأحزاب",
    "سبأ",
    "فاطر",
    "يس",
    "الصافات",
    "ص",
    "الزمر",
    "غافر",
    "فصلت",
    "الشورى",
    "الزخرف",
    "الدخان",
    "الجاثية",
    "الأحقاف",
    "محمد",
    "الفتح",
    "الحجرات",
    "ق",
    "الذاريات",
    "الطور",
    "النجم",
    "القمر",
    "الرحمن",
    "الواقعة",
    "الحديد",
    "المجادلة",
    "الحشر",
    "الممتحنة",
    "الصف",
    "الجمعة",
    "المنافقون",
    "التغابن",
    "الطلاق",
    "التحريم",
    "الملك",
    "القلم",
    "الحاقة",
    "المعارج",
    "نوح",
    "الجن",
    "المزمل",
    "المدثر",
    "القيامة",
    "الإنسان",
    "المرسلات",
    "النبأ", 
    "النازعات", 
    "عبس", 
    "التكوير", 
    "الإنفطار", 
    "المطففين", 
    "الإنشقاق", 
    "البروج", 
    "الطارق", 
    "الأعلى", 
    "الغاشية", 
    "الفجر", 
    "البلد", 
    "الشمس", 
    "الليل", 
    "الضحى", 
    "الشرح", 
    "التين", 
    "العلق", 
    "القدر", 
    "البينة", 
    "الزلزلة", 
    "العاديات", 
    "القارعة", 
    "التكاثر", 
    "العصر", 
    "الهمزة", 
    "الفيل", 
    "قريش", 
    "الماعون", 
    "الكوثر" ,
    "الكافرون", 
    "النصر", 
    "المسد", 
    "الإخلاص", 
    "الفلق",  
    "الناس"
]

surah_names_English = [
    "Al-Fatihah",
    "Al-Baqarah",
    "Ali 'Imran",
    "An-Nisa'",
    "Al-Ma'idah",
    "Al-An'am",
    "Al-A'raf",
    "Al-Anfal",
    "At-Tawbah",
    "Yunus",
    "Hud",
    "Yusuf",
    "Ar-Ra'd",
    "Ibrahim",
    "Al-Hijr",
    "An-Nahl",
    "Al-Isra'",
    "Al-Kahf",
    "Maryam",
    "Ta-Ha",
    "Al-Anbiya'",
    "Al-Hajj",
    "Al-Mu'minun",
    "An-Nur",
    "Al-Furqan",
    "Ash-Shu'ara'",
    "An-Naml",
    "Al-Qasas",
    "Al-'Ankabut",
    "Ar-Rum",
    "Luqman",
    "As-Sajdah",
    "Al-Ahzab",
    "Saba'",
    "Fatir",
    "Ya-Sin",
    "As-Saffat",
    "Sad",
    "Az-Zumar",
    "Ghafir",
    "Fussilat",
    "Ash-Shuraa",
    "Az-Zukhruf",
    "Ad-Dukhan",
    "Al-Jathiya",
    "Al-Ahqaf",
    "Muhammad",
    "Al-Fath",
    "Al-Hujurat",
    "Qaf",
    "Adh-Dhariyat",
    "At-Tur",
    "An-Najm",
    "Al-Qamar",
    "Ar-Rahman",
    "Al-Waqi'ah",
    "Al-Hadid",
    "Al-Mujadilah",
    "Al-Hashr",
    "Al-Mumtahanah",
    "As-Saff",
    "Al-Jumu'ah",
    "Al-Munafiqun",
    "At-Taghabun",
    "At-Talaq",
    "At-Tahrim",
    "Al-Mulk",
    "Al-Qalam",
    "Al-Haqqah",
    "Al-Ma'arij",
    "Nuh",
    "Al-Jinn",
    "Al-Muzzammil",
    "Al-Muddaththir",
    "Al-Qiyamah",
    "Al-Insan",
    "Al-Mursalat",
    "An-Naba'",
    "An-Nazi'at",
    "'Abasa",
    "At-Takwir",
    "Al-Infitar",
    "Al-Mutaffifin",
    "Al-Inshiqaq",
    "Al-Buruj",
    "At-Tariq",
    "Al-A'la",
    "Al-Ghashiyah",
    "Al-Fajr",
    "Al-Balad",
    "Ash-Shams",
    "Al-Lail",
    "Ad-Duha",
    "Ash-Sharh",
    "At-Tin",
    "Al-'Alaq",
    "Al-Qadr",
    "Al-Bayyinah",
    "Az-Zalzalah",
    "Al-'Adiyat",
    "Al-Qari'ah",
    "At-Takathur",
    "Al-'Asr",
    "Al-Humazah",
    "Al-Fil",
    "Quraysh",
    "Al-Ma'un",
    "Al-Kauthar",
    "Al-Kafiroun",
    "An-Nasr",
    "Al-Masad",
    "Al-Ikhlas",
    "Al-Falaq",
    "An-Nas"
]

class RenameQuranMp3Files(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rename Quran MP3 Files  📖 برنامج تعيين اسماء سور القراءن')
        self.setGeometry(700, 200, 800, 150)

        # Create the GUI elements
        self.language_combo = QtWidgets.QComboBox(self)
        self.language_combo.addItem("Arabic - العربية")
        self.language_combo.addItem("English - الإنجليزية")
        self.language_combo.setCurrentIndex(0)

        self.select_directory_button = QtWidgets.QPushButton("2.\nClick to Select Quran Files Directory\nاضغط لاختيار مجلد القراءن المراد معالجته")
        self.select_directory_button.clicked.connect(self.select_quran_directory)


        self.status_label = QtWidgets.QLabel('')

        # Add the GUI elements to the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("1.\nSurahs names: in Arabic or English?\nاسماء السور تريدها باللغة العربية أو الانجليزية؟"))
        layout.addWidget(self.language_combo)
        layout.addWidget(self.select_directory_button)
        layout.addWidget(self.status_label)
        layout.addWidget(QtWidgets.QLabel("🌙 Ramadan 1444 Hijri"))
        label = QtWidgets.QLabel('<a href="https://linkedin.com/in/mohamed-hamed-soliman">الفقير إلي الله </a>')
        label.setOpenExternalLinks(True)
        layout.addWidget(label)
        self.setLayout(layout)

    def select_quran_directory(self):
        """
        Open a GUI to select the Quran directory and return a Path object.
        """
        quran_directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Quran Directory', QtCore.QDir.homePath())
        self.rename_quran_mp3_files(quran_directory)

    def rename_quran_mp3_files(self, quran_directory):
        """
        Rename Quran MP3 files in the given directory according to their surah name.
        MP3 files are renamed to "{surah_number} - {surah_name}.mp3"
        """
        if self.language_combo.currentText() == "Arabic - العربية":
            surah_list = surah_names_Arabic
        else:
            surah_list = surah_names_English

        for i, name in enumerate(surah_list):
            # Handle any name format (i.e. 0001,001,01, or 1)
            for j in range(1, 5):
                old_filepath = os.path.join(quran_directory, f'{i+1:0{j}}.mp3')
                if os.path.exists(old_filepath):
                    new_name = f'{i+1:03} - {name}.mp3'
                    new_filepath = os.path.join(quran_directory, new_name)
                    os.rename(old_filepath, new_filepath)
        # self.status_label.setText('Renaming complete.')
        # QtWidgets.QMessageBox.information(self, 'Success', 'Quran MP3 files have been renamed successfully!\nتمت عملية تعيين اسماء سور القراءن الكريم بنجاح 🌟 ')
        
        # Show message only if files are renamed
        if any([os.path.exists(os.path.join(quran_directory, f'{i+1:03} - {name}.mp3')) for i, name in enumerate(surah_list)]):
            QtWidgets.QMessageBox.information(self, 'Success', 'Quran MP3 files have been renamed successfully!\nتمت عملية تعيين اسماء سور القراءن الكريم بنجاح 🌟 ')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RenameQuranMp3Files()
    window.show()
    sys.exit(app.exec_())