import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon="🦅", layout="wide")

# 2. تصميم الواجهة (CSS) - لجعل النص أبيض والمربعات واضحة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل النصوص العامة بيضاء تماماً */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important;
    }
    
    /* خلفية الموقع زرقاء غامقة (نفس روح اللوغو) */
    .stApp {
        background-color: #0f172a !important;
    }
    
    /* تصميم المربعات: خلفية غامقة متميزة وإطار ذهبي */
    input, textarea, select, div[data-baseweb="select"] > div {
        background-color: #1e293b !important; /* لون المربع */
        color: #ffffff !important; /* لون النص داخل المربع */
        border: 2px solid #c5a059 !important; /* إطار ذهبي */
        border-radius: 10px !important;
    }

    /* ضمان أن النص الذي يكتبه الزبون يظهر بالأبيض */
    input { color: white !important; -webkit-text-fill-color: white !important; }
    textarea { color: white !important; -webkit-text-fill-color: white !important; }

    /* تصميم رأس الصفحة */
    .header-box {
        background: linear-gradient(135deg, #0b3d61, #1e293b);
        padding: 25px; border-radius: 20px; border-bottom: 5px solid #c5a059;
        text-align: center; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر (رأس الصفحة)
# ملاحظة: يمكنك وضع رابط اللوغو المباشر هنا
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important;">🦅 مكتبة أيوب الذكية</h1>
        <p style="font-size: 18px;">دقة، سرعة، واحترافية رقمية من قلب القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")
st.success("عاشت إيدك يا بطل! الخطوة الأولى (التأسيس) اشتغلت بنجاح.")
# --- الخطوة الثانية: عرض الخدمات باحترافية ---

st.markdown('<h2 style="color: #c5a059; text-align: center;">🌟 خدماتنا الرقمية المتكاملة</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #94a3b8;">اختر الفئة التي تهمك وشاهد ماذا نقدم لك</p>', unsafe_allow_html=True)

# تقسيم الخدمات لثلاثة أعمدة (Layout)
col_tech, col_design, col_money = st.columns(3)

with col_tech:
    st.markdown("""
        <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-top: 5px solid #c5a059; height: 350px;">
            <h3 style="color: #facc15; text-align: center;">📂 الخدمات المكتبية</h3>
            <p style="font-size: 14px; line-height: 1.8;">
                ✅ استنساخ وملازم (أسود/ملون)<br>
                ✅ طباعة ملفات وبحوث<br>
                ✅ تحويل ملفات (PDF to Word)<br>
                ✅ إنشاء سيرة ذاتية (CV) ملكية<br>
                ✅ تقديم تعيينات وعقود حكومية
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_design:
    st.markdown("""
        <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-top: 5px solid #c5a059; height: 350px;">
            <h3 style="color: #facc15; text-align: center;">🎬 المونتاج والإبداع</h3>
            <p style="font-size: 14px; line-height: 1.8;">
                ✅ مونتاج CapCut ترند (TikTok/Insta)<br>
                ✅ تصميم منيو مطاعم وكافيهات<br>
                ✅ كارتات عمل (Business Cards)<br>
                ✅ تصميم باركود (QR) ذكي<br>
                ✅ سحب صور فوتوغرافية احترافية
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_money:
    st.markdown("""
        <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-top: 5px solid #c5a059; height: 350px;">
            <h3 style="color: #facc15; text-align: center;">💰 المعاملات المالية</h3>
            <p style="font-size: 14px; line-height: 1.8;">
                ✅ تحويل واستلام (زين كاش)<br>
                ✅ دفع فواتير وخدمات أونلاين<br>
                ✅ تعبئة رصيد وبطاقات ألعاب<br>
                ✅ استشارات تقنية وذكاء اصطناعي<br>
                ✅ تحويل أموال داخلي وخارجي
            </p>
        </div>
    """, unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.info("💡 ملاحظة: جميع الخدمات تتم بدقة وسرعة وبإشراف مباشر من أخوكم أيوب.")
