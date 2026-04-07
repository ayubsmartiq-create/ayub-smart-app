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
# --- الخطوة الخامسة: نظام إدارة الأكواد والتتبع ---
st.write("---")
st.markdown('<h3 style="color: #c5a059; text-align: right;">⚙️ نظام متابعة المعاملات الذكي</h3>', unsafe_allow_html=True)

# إنشاء "تبويبات" (Tabs) حتى يكون الشغل مرتب ومنفصل
tab_new, tab_track = st.tabs(["✨ تقديم وحجز كود", "🔍 مراقبة حالة الطلب"])

# --- 1. قسم التقديم وحجز الكود ---
with tab_new:
    st.markdown('<p style="color: #cbd5e1;">املأ بياناتك هنا حتى يصدر لك النظام "كود الطلب" الخاص بك:</p>', unsafe_allow_html=True)
    
    with st.form("generate_code_form"):
        u_name = st.text_input("اسم الزبون الكامل")
        u_phone = st.text_input("رقم الواتساب")
        u_service = st.selectbox("نوع الخدمة", [
            "استنساخ وملازم", "تحويل مالي", "تصميم ومنتاج", 
            "سحب صور", "إنشاء CV", "تقديم تعيينات"
        ])
        
        btn_generate = st.form_submit_button("إصدار كود المعاملة 🎟️")
        
        if btn_generate:
            if u_name and u_phone:
                # توليد كود عشوائي يبدأ بـ AY
                order_code = f"AY-{random.randint(1000, 9999)}"
                st.success(f"عاشت إيدك يا {u_name}! تم حجز طلبك بنجاح.")
                st.markdown(f"""
                    <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #facc15; text-align: center;">
                        <p style="color: white; margin-bottom: 5px;">كود الطلب الخاص بك هو:</p>
                        <h2 style="color: #facc15; margin: 0;">{order_code}</h2>
                        <p style="color: #94a3b8; font-size: 12px; margin-top: 10px;">يرجى تصوير الشاشة وحفظ الكود لمراجعة المكتبة.</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # إشعار الواتساب التلقائي
                wa_link = f"https://wa.me/{MY_WHATSAPP}?text=مرحباً أيوب، هذا كود طلبي: {order_code}"
                st.markdown(f'<a href="{wa_link}" target="_blank" style="display: block; background: #25d366; color: white; text-align: center; padding: 10px; border-radius: 10px; text-decoration: none; margin-top: 10px;">إرسال الكود لأيوب عبر الواتساب ✅</a>', unsafe_allow_html=True)
            else:
                st.warning("عيني، لازم تكتب الاسم والرقم حتى يطلع الكود!")

# --- 2. قسم مراقبة حالة الطلب ---
with tab_track:
    st.markdown('<p style="color: #cbd5e1;">أدخل الكود الخاص بك لمعرفة أين وصلت معاملتك:</p>', unsafe_allow_html=True)
    search_code = st.text_input("اكتب الكود هنا (مثلاً: AY-1234)")
    
    if st.button("فحص الحالة الآن 🔎"):
        if search_code:
            # رد افتراضي احترافي (مستقبلاً نربطه بجدول بيانات)
            st.markdown(f"""
                <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-right: 5px solid #facc15;">
                    <h4 style="color: #facc15;">🔍 نتيجة التتبع للكود: {search_code}</h4>
                    <p style="color: white;">الحالة الحالية: <span style="color: #34d399;">قيد التدقيق والمعالجة ⏳</span></p>
                    <p style="color: #94a3b8; font-size: 13px;">ملاحظة: أيوب حالياً يعمل على طلبك، سيتم إشعارك فور اكتماله.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("يرجى إدخال الكود أولاً!")
