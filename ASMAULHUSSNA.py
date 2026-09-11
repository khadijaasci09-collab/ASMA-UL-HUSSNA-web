import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Asma-ul-Husna", page_icon="☪️", layout="centered")

ASMA_UL_HUSNA = [
    ("الرَّحْمَنُ", "Ar-Rahman", "Nihayat Meherban"),
    ("الرَّحِيمُ", "Ar-Raheem", "Nihayat Reham Farmane Wala"),
    ("الْمَلِكُ", "Al-Malik", "Badshah"),
    ("الْقُدُّوسُ", "Al-Quddus", "Pak"),
    ("السَّلَامُ", "As-Salam", "Salamati Dene Wala"),
    ("الْمُؤْمِنُ", "Al-Mu'min", "Aman Dene Wala"),
    ("الْمُهَيْمِنُ", "Al-Muhaymin", "Nigran"),
    ("الْعَزِيزُ", "Al-Aziz", "Ghalib"),
    ("الْجَبَّارُ", "Al-Jabbar", "Zabardast Qudrat Wala"),
    ("الْمُتَكَبِّرُ", "Al-Mutakabbir", "Buzurgi Wala"),
    ("الْخَالِقُ", "Al-Khaliq", "Paida Karne Wala"),
    ("الْبَارِئُ", "Al-Bari", "Banane Wala"),
    ("الْمُصَوِّرُ", "Al-Musawwir", "Soorat Banane Wala"),
    ("الْغَفَّارُ", "Al-Ghaffar", "Bohat Bakshne Wala"),
    ("الْقَهَّارُ", "Al-Qahhar", "Sab Par Ghalib"),
    ("الْوَهَّابُ", "Al-Wahhab", "Bohat Ata Karne Wala"),
    ("الرَّزَّاقُ", "Ar-Razzaq", "Rizq Dene Wala"),
    ("الْفَتَّاحُ", "Al-Fattah", "Kholne Wala"),
    ("الْعَلِيمُ", "Al-Alim", "Sab Kuch Jaanne Wala"),
    ("الْقَابِضُ", "Al-Qabid", "Rokne Wala"),
    ("الْبَاسِطُ", "Al-Basit", "Kushadgi Dene Wala"),
    ("الْخَافِضُ", "Al-Khafid", "Past Karne Wala"),
    ("الرَّافِعُ", "Ar-Rafi", "Buland Karne Wala"),
    ("الْمُعِزُّ", "Al-Mu'izz", "Izzat Dene Wala"),
    ("الْمُذِلُّ", "Al-Mudhill", "Zillat Dene Wala"),
    ("السَّمِيعُ", "As-Sami", "Sab Kuch Sunne Wala"),
    ("الْبَصِيرُ", "Al-Basir", "Sab Kuch Dekhne Wala"),
    ("الْحَكَمُ", "Al-Hakam", "Faisla Karne Wala"),
    ("الْعَدْلُ", "Al-Adl", "Adal Karne Wala"),
    ("اللَّطِيفُ", "Al-Latif", "Nihayat Meherban"),
    ("الْخَبِيرُ", "Al-Khabir", "Ba-Khabar"),
    ("الْحَلِيمُ", "Al-Halim", "Bardasht Karne Wala"),
    ("الْعَظِيمُ", "Al-Azim", "Bohat Azmat Wala"),
    ("الْغَفُورُ", "Al-Ghafur", "Bohat Bakshne Wala"),
    ("الشَّكُورُ", "Ash-Shakur", "Qadr Karne Wala"),
    ("الْعَلِيُّ", "Al-Ali", "Sab Se Buland"),
    ("الْكَبِيرُ", "Al-Kabir", "Sab Se Bara"),
    ("الْحَفِيظُ", "Al-Hafiz", "Hifazat Karne Wala"),
    ("الْمُقِيتُ", "Al-Muqit", "Rizq Dene Wala"),
    ("الْحسِيبُ", "Al-Hasib", "Hisab Lene Wala"),
    ("الْجَلِيلُ", "Al-Jalil", "Jalal Wala"),
    ("الْكَرِيمُ", "Al-Karim", "Kareem"),
    ("الرَّقِيبُ", "Ar-Raqib", "Nigrani Karne Wala"),
    ("الْمُجِيبُ", "Al-Mujib", "Dua Qabool Karne Wala"),
    ("الْوَاسِعُ", "Al-Wasi", "Wus'at Wala"),
    ("الْحَكِيمُ", "Al-Hakim", "Hikmat Wala"),
    ("الْوَدُودُ", "Al-Wadud", "Mohabbat Karne Wala"),
    ("الْمَجِيدُ", "Al-Majid", "Buzurgi Wala"),
    ("الْبَاعِثُ", "Al-Ba'ith", "Uthane Wala"),
    ("الشَّهِيدُ", "Ash-Shahid", "Gawah"),
    ("الْحَقُّ", "Al-Haqq", "Haq"),
    ("الْوَكِيلُ", "Al-Wakil", "Kaarsaaz"),
    ("الْقَوِيُّ", "Al-Qawiyy", "Quwwat Wala"),
    ("الْمَتِينُ", "Al-Matin", "Mazboot"),
    ("الْوَلِيُّ", "Al-Waliyy", "Dost aur Madadgar"),
    ("الْحَمِيدُ", "Al-Hamid", "Tareef Ke Laaiq"),
    ("الْمُحْصِي", "Al-Muhsi", "Shumar Karne Wala"),
    ("الْمُبْدِئُ", "Al-Mubdi", "Ibtida Karne Wala"),
    ("الْمُعِيدُ", "Al-Mu'id", "Dobara Paida Karne Wala"),
    ("الْمُحْيِي", "Al-Muhyi", "Zindagi Dene Wala"),
    ("الْمُمِيتُ", "Al-Mumit", "Maut Dene Wala"),
    ("الْحَيُّ", "Al-Hayy", "Hamesha Zinda"),
    ("الْقَيُّومُ", "Al-Qayyum", "Qaim Rakhne Wala"),
    ("الْوَاجِدُ", "Al-Wajid", "Paane Wala"),
    ("الْمَاجِدُ", "Al-Majid", "Buzurgi Wala"),
    ("الْوَاحِدُ", "Al-Wahid", "Yakta"),
    ("الْأَحَدُ", "Al-Ahad", "Ek"),
    ("الصَّمَدُ", "As-Samad", "Be-Niyaz"),
    ("الْقَادِرُ", "Al-Qadir", "Qudrat Wala"),
    ("الْمُقْتَدِرُ", "Al-Muqtadir", "Puri Qudrat Wala"),
    ("الْمُقَدِّمُ", "Al-Muqaddim", "Aage Karne Wala"),
    ("الْمُؤَخِّرُ", "Al-Mu'akhkhir", "Peeche Karne Wala"),
    ("الْأَوَّلُ", "Al-Awwal", "Sab Se Pehle"),
    ("الْآخِرُ", "Al-Akhir", "Sab Se Aakhir"),
    ("الظَّاهِرُ", "Az-Zahir", "Zahir"),
    ("الْبَاطِنُ", "Al-Batin", "Posheeda"),
    ("الْوَالِي", "Al-Wali", "Hukmran"),
    ("الْمُتَعَالِي", "Al-Muta'ali", "Sab Se Buland"),
    ("الْبَرُّ", "Al-Barr", "Neki Karne Wala"),
    ("التَّوَابُ", "At-Tawwab", "Tauba Qabool Karne Wala"),
    ("الْمُنْتَقِمُ", "Al-Muntaqim", "Inteqam Lene Wala"),
    ("الْعَفُوُّ", "Al-Afuww", "Maaf Karne Wala"),
    ("الرَّؤُوفُ", "Ar-Ra'uf", "Nihayat Shafeeq"),
    ("مَالِكُ الْمُلْكِ", "Malik-ul-Mulk", "Mulk Ka Malik"),
    ("ذُوالْجَلَالِ وَالْإِكْرَامِ", "Dhul-Jalali wal-Ikram", "Jalal aur Ikram Wala"),
    ("الْمُقْسِطُ", "Al-Muqsit", "Insaf Karne Wala"),
    ("الْجَامِعُ", "Al-Jami", "Jama Karne Wala"),
    ("الْغَنِيُّ", "Al-Ghani", "Be-Niyaz"),
    ("الْمُغْنِي", "Al-Mughni", "Be-Niyaz Karne Wala"),
    ("الْمَانِعُ", "Al-Mani", "Rokne Wala"),
    ("الضَّارُّ", "Ad-Darr", "Nuqsan Pahunchane Wala"),
    ("النَّافِعُ", "An-Nafi", "Nafa Dene Wala"),
    ("النُّورُ", "An-Nur", "Noor"),
    ("الْهَادِي", "Al-Hadi", "Hidayat Dene Wala"),
    ("الْبَدِيعُ", "Al-Badi", "Be-Misaal Paida Karne Wala"),
    ("الْبَاقِي", "Al-Baqi", "Hamesha Baqi"),
    ("الْوَارِثُ", "Al-Warith", "Warist"),
    ("الرَّشِيدُ", "Ar-Rashid", "Raah Dikhane Wala"),
    ("الصَّبُورُ", "As-Sabur", "Bohat Sabr Karne Wala"),
]


player_code = f"""
<!DOCTYPE html>
<html lang="ur">
<head>
<meta charset="UTF-8">
<style>
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        background: radial-gradient(circle at top, #183d35 0%, #071c18 55%, #020908 100%);
        color: #ffffff;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        text-align: center;
        padding: 24px 16px;
    }}
    .header h1 {{
        font-size: 36px;
        color: #f5d98b;
        letter-spacing: 1px;
    }}
    .header p {{
        font-size: 15px;
        color: #b3c9bf;
        margin-top: 4px;
        margin-bottom: 28px;
    }}
    .card {{
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(245, 217, 139, 0.25);
        border-radius: 20px;
        padding: 36px 20px;
        min-height: 230px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        backdrop-filter: blur(8px);
    }}
    .arabic {{
        font-size: 60px;
        color: #f5d98b;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        line-height: 1.2;
    }}
    .roman {{
        font-size: 24px;
        font-weight: 600;
        margin-top: 12px;
    }}
    .meaning {{
        font-size: 16px;
        color: #d1ded8;
        margin-top: 6px;
    }}
    .status {{
        font-size: 14px;
        color: #f5d98b;
        margin-top: 18px;
        opacity: 0.85;
    }}
    .controls {{
        margin-top: 24px;
        display: flex;
        justify-content: center;
        gap: 12px;
    }}
    .btn {{
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(245, 217, 139, 0.3);
        color: #ffffff;
        padding: 10px 20px;
        font-size: 15px;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.2s ease;
    }}
    .btn:hover {{
        background: rgba(245, 217, 139, 0.15);
        border-color: #f5d98b;
        color: #f5d98b;
    }}
    .btn-primary {{
        min-width: 140px;
    }}
</style>
</head>
<body>

<div class="header">
    <h1>أَسْمَاءُ اللَّهِ الْحُسْنَى</h1>
    <p>Asma-ul-Husna — Allah Ta'ala ke Mubarak Naam</p>
</div>

<div class="card">
    <div id="txtArabic" class="arabic"></div>
    <div id="txtRoman" class="roman"></div>
    <div id="txtMeaning" class="meaning"></div>
</div>

<div id="txtCounter" class="status"></div>

<div class="controls">
    <button class="btn" onclick="prev()">⬅️ Prev</button>
    <button id="btnPlay" class="btn btn-primary" onclick="togglePlay()">▶️ Auto Play</button>
    <button class="btn" onclick="next()">Next ➡️</button>
</div>

<script>
    // State management
    const dataset = {json.dumps(ASMA_UL_HUSNA)};
    let currentIndex = 0;
    let autoPlayActive = false;
    let speechTimer = null;
    let selectedVoice = null;

    // DOM Elements
    const elArabic = document.getElementById('txtArabic');
    const elRoman = document.getElementById('txtRoman');
    const elMeaning = document.getElementById('txtMeaning');
    const elCounter = document.getElementById('txtCounter');
    const elBtnPlay = document.getElementById('btnPlay');

    // Init voices
    function initVoices() {{
        if (!('speechSynthesis' in window)) return;
        
        const voices = window.speechSynthesis.getVoices();
        selectedVoice = voices.find(v => v.lang.startsWith('ar')) || null;
    }}

    if ('speechSynthesis' in window) {{
        window.speechSynthesis.onvoiceschanged = initVoices;
        initVoices();
    }}

    function render() {{
        const [arabic, roman, meaning] = dataset[currentIndex];
        elArabic.textContent = arabic;
        elRoman.textContent = roman;
        elMeaning.textContent = meaning;
        elCounter.textContent = `Naam ${{currentIndex + 1}} / ${{dataset.length}}`;
    }}

    function speak(text) {{
        if (!('speechSynthesis' in window)) return;

        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'ar-SA';
        utterance.rate = 0.8;

        if (selectedVoice) {{
            utterance.voice = selectedVoice;
        }}

        utterance.onend = () => {{
            if (autoPlayActive) {{
                speechTimer = setTimeout(() => next(true), 1000);
            }}
        }};

        utterance.onerror = () => {{
            if (autoPlayActive) {{
                speechTimer = setTimeout(() => next(true), 1000);
            }}
        }};

        window.speechSynthesis.speak(utterance);
    }}

    function playCurrent() {{
        render();
        speak(dataset[currentIndex][0]);
    }}

    function togglePlay() {{
        autoPlayActive = !autoPlayActive;
        
        if (autoPlayActive) {{
            elBtnPlay.textContent = "⏸️ Pause";
            playCurrent();
        }} else {{
            elBtnPlay.textContent = "▶️ Auto Play";
            clearTimeout(speechTimer);
            if ('speechSynthesis' in window) window.speechSynthesis.cancel();
        }}
    }}

    function next(fromAuto = false) {{
        if (!fromAuto && autoPlayActive) {{
            clearTimeout(speechTimer);
        }}
        currentIndex = (currentIndex + 1) % dataset.length;
        playCurrent();
    }}

    function prev() {{
        if (autoPlayActive) {{
            clearTimeout(speechTimer);
        }}
        currentIndex = (currentIndex - 1 + dataset.length) % dataset.length;
        playCurrent();
    }}

    // Initial boot
    render();
</script>

</body>
</html>
"""

components.html(player_code, height=600, scrolling=False)