import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon="🦅", layout="wide")

# 2. تصميم الواجهة (CSS) - ألوان مستوحاة من اللوغو الخاص بك
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل النصوص العامة بيضاء */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important;
    }
    
    /* خلفية الموقع زرقاء غامقة ملكية */
    .stApp {
        background-color: #0f172a !important;
    }
    
    /* تصميم المربعات (Input Boxes): خلفية غامقة وكتابة بيضاء */
    input, textarea, select, div[data-baseweb="select"] > div {
        background-color: #1e293b !important; /* أزرق غامق مريح */
        color: #ffffff !important; /* الكتابة بيضاء */
        border: 2px solid #c5a059 !important; /* إطار ذهبي نفس اللوغو */
        border-radius: 10px !important;
    }

    /* ضمان ظهور النص المكتوب داخل المربعات باللون الأبيض */
    input { color: white !important; -webkit-text-fill-color: white !important; }
    textarea { color: white !important; -webkit-text-fill-color: white !important; }

    /* تصميم رأس الصفحة (الهيدر) */
    .header-box {
        background: linear-gradient(135deg, #0b3d61, #1e293b);
        padding: 20px; border-radius: 20px; border-bottom: 5px solid #c5a059;
        text-align: center; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. عرض اللوغو والهيدر
# ملاحظة: سنستخدم رابط اللوغو الذي رفعته أنت سابقاً أو يمكنك رفعه على GitHub باسم Ayub-Logo.png
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important;">🦅 مكتبة أيوب الذكية</h1>
        <p>دقة، سرعة، واحترافية رقمية من قلب القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")
st.success("تم تشغيل الخطوة الأولى بنجاح! الألوان والخطوط جاهزة الآن.")
# --- تحديث قائمة الخدمات في الاستمارة (توضع داخل st.form السابق) ---
# ملاحظة: قم بتحديث سطر الـ selectbox في الكود السابق بهذا السطر:
service = st.selectbox("اختر الخدمة اللي تلمع بعينك ✨", 
                      ["استنساخ وطباعة ملازم (أسود/ملون)", 
                       "تحويل ملفات (PDF to Word) والعكس", 
                       "سحب صور فوتوغرافية بجودة عالية",
                       "تحويل واستلام أموال (زين كاش/طيف)",
                       "إنشاء سيرة ذاتية (CV) احترافي",
                       "تصميم (منيو - كارت عمل - باركود)",
                       "تقديم تعيينات وعقود حكومية",
                       "مونتاج فيديو (CapCut) احترافي"])

# --- إضافة قسم "شبكة الخدمات" الملونة (تحت الاستمارة) ---
st.write("---")
st.markdown('<h3 style="color: #c5a059; text-align: center;">🌟 خدماتنا الرقمية المتكاملة</h3>', unsafe_allow_html=True)

# تقسيم الخدمات على شكل مربعات (Grid)
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("""
        <div style="background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #c5a059; text-align: center; height: 180px;">
            <h4 style="color: #facc15;">🖨️ طباعة وقرطاسية</h4>
            <p style="color: white; font-size: 13px;">طباعة ملازم، استنساخ، وتحويل ملفات PDF بوضوح تام.</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("") # مسافة
    st.markdown("""
        <div style="background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #c5a059; text-align: center; height: 180px;">
            <h4 style="color: #facc15;">💳 تحويل فلوس</h4>
            <p style="color: white; font-size: 13px;">حول واستلم فلوسك بأمان وثقة (زين كاش وغيرها).</p>
        </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div style="background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #c5a059; text-align: center; height: 180px;">
            <h4 style="color: #facc15;">🎨 تصميم وإبداع</h4>
            <p style="color: white; font-size: 13px;">تصميم منيو مطاعم، كارتات عمل، وباركدات ذكية (QR).</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("") # مسافة
    st.markdown("""
        <div style="background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #c5a059; text-align: center; height: 180px;">
            <h4 style="color: #facc15;">📄 سير ذاتية CV</h4>
            <p style="color: white; font-size: 13px;">نصمم لك CV يخلي صاحب العمل يتصل بيك فوراً!</p>
        </div>
    """, unsafe_allow_html=True)

with col_c:
    st.markdown("""
        <div style="background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #c5a059; text-align: center; height: 180px;">
            <h4 style="color: #facc15;">🖼️ سحب صور</h4>
            <p style="color: white; font-size: 13px;">حول صور موبايلك إلى صور فوتوغرافية تذكرك بأحلى اللحظات.</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("") # مسافة
    st.markdown("""
        <div style="background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #c5a059; text-align: center; height: 180px;">
            <h4 style="color: #facc15;">🚀 خدمات أونلاين</h4>
            <p style="color: white; font-size: 13px;">تقديم تعيينات، مونتاج فيديوهات، وكل ما يخص الإنترنت.</p>
        </div>
    """, unsafe_allow_html=True)
