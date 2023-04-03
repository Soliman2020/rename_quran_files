import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog

# list of all surahs by the Musaf's order
surah_names = [
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

def select_quran_directory():
    """
    Open a GUI to select the Quran directory and return a Path object.
    """
    app = QtWidgets.QApplication([])
    quran_directory = QFileDialog.getExistingDirectory(None, "Select Quran Directory اختر مجلد القراءن المراد معالجته")
    return quran_directory
    
def rename_quran_mp3_files(quran_directory):
    """
    Rename Quran MP3 files in the given directory according to their surah name.
    MP3 files are renamed to "{surah_number} - {surah_name}.mp3"
    """
    for i, name in enumerate(surah_names):
        # Handle any name format (i.e. 001,01, or 1)
        for j in range(1, 4):
            old_filepath = os.path.join(quran_directory, f'{i+1:0{j}}.mp3')
            if os.path.exists(old_filepath):
                new_name = f'{i+1:03} - {name}.mp3'
                new_filepath = os.path.join(quran_directory, new_name)
                os.rename(old_filepath, new_filepath)
    print("Renaming complete.")

def main():
    quran_directory = select_quran_directory()
    rename_quran_mp3_files(quran_directory)

if __name__ == "__main__":
    main()
