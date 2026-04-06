import streamlit as st
import requests

# --- إعدادات الصفحة والهوية ---
st.set_page_config(page_title="مكتبة أيوب الذكية | Ayub Smart Library", page_icon="🦅", layout="wide")

# رابط Formspree الخاص بك
FORMSPREE_URL = "https://formspree.io/f/xvzvdjzq"

# --- ستايل CSS الملكي (معدل ليكون احترافي 100%) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"], .stApp { 
        font-family: 'Cairo', sans-serif !important; 
        direction: rtl !important; text-align: right !important;
        background-color: #0f172a !important; color: white !important;
    }
    .chat-bubble-user { 
        background: #075e54; color: white; padding: 12px; border-radius: 15px 15px 0 15px; 
        margin: 10px; float: right; clear: both; max-width: 80%; border: 1px solid #128c7e;
    }
    .chat-bubble-bot { 
        background: #1e293b; color: white; padding: 12px; border-radius: 15px 15px 15px 0; 
        margin: 10px; float: left; clear: both; max-width: 80%; border: 1px solid #334155;
    }
    .stButton>button { background-color: #facc15 !important; color: #0f172a !important; font-weight: 900; width: 100%; border-radius: 10px; }
    .header-box { background: linear-gradient(90deg, #1e3a8a, #312e81); padding: 20px; border-radius: 15px; border: 2px solid #facc15; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- الهيدر ---
st.markdown("""<div class="header-box">
    <h1 style='color: white; margin:0;'>🦅 مكتبة أيوب الذكية 🦅</h1>
    <p style='color: #facc15; font-size:18px;'>خبير الذكاء الاصطناعي والخدمات الإلكترونية في العراق</p>
</div>""", unsafe_allow_html=True)

# --- نظام الدردشة الاحترافي ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "هلا بيك عيني! أنا المساعد الذكي لمكتبة أيوب.. اسألني عن (القرطاسية، الذكاء الاصطناعي، التعيينات) وأبشر بالجواب! 😊"}]

for msg in st.session_state.messages:
    div_class = "chat-bubble-bot" if msg["role"] == "bot" else "chat-bubble-user"
    st.markdown(f<div class='{div_class}'>{msg['content']}</div>, unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك هنا... (مثلاً: شنو خدمات الذكاء الاصطناعي؟)")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    p = user_input.lower()
    
    # --- محرك الردود العملاق (عقل أيوب المطور) ---
    if any(x in p for x in ["هلا", "هلو", "سلام", "مرحبا", "مساء", "صباح"]):
        ans = "يا مية هلا بجيتك! نورت مكتبة أخوك أيوب.. تفضل عيني شمحتاج اليوم؟"
    
    elif any(x in p for x in ["شلونك", "اخبارك", "اشلونك"]):
        ans = "بخير ونعمة من الله، ربي يحفظك ويخليك! المهم أنت شلونك؟ شأقدر أقدملك؟"
        
    elif any(x in p for x in ["ذكاء", "ai", "تكنولوجيا", "بوت", "أتمتة"]):
        ans = """**🚀 في مجال الذكاء الاصطناعي، أيوب يقدم لك:**
        1. **بناء بوتات دردشة:** مثل هذا البوت اللي دا تحجي وياه، نبرمجه لشركتك أو صفحتك.
        2. **أتمتة الأعمال:** تخلي الحاسبة تشتغل بدالك وتخلص معاملاتك تلقائياً.
        3. **تحليل البيانات:** تحويل جداول البيانات المعقدة إلى تقارير ذكية.
        4. **توليد المحتوى:** كتابة محتوى وتصميم صور خرافية باستخدام الـ AI."""
        
    elif any(x in p for x in ["قرطاسية", "اقلام", "دفاتر", "رسم", "تجهيز"]):
        ans = """**📚 قسم القرطاسية يضم كل شي ببالك:**
        * **ماركات عالمية:** أقلام (روترينج، فابر كاستل) ودفاتر فاخرة.
        * **تجهيز مدرسي وجامعي:** سجلات، حقائب، وأدوات هندسية دقيقة.
        * **قسم الرسم:** لوحات، ألوان زيتية وأكريليك للمبدعين.
        * **هدايا:** تغليف ملكي وطباعة حرارية على كل شي."""
        
    elif any(x in p for x in ["تساعد", "خدمة", "عالم", "ناس", "تعيين", "تقديم"]):
        ans = """**🤝 شلون نساعد العالم؟**
        1. **التعيينات:** نتابع كل استمارة تفتح (عقود، ملاك، أمنية) ونقدملك بدون أخطاء.
        2. **المعاملات الإلكترونية:** تحديث البطاقة التموينية، الانتخابية، والتقديم على القروض.
        3. **الطلاب:** تقديم الجامعات (مركزي، مسائي، أهلي) والمنح الدراسية.
        4. **الاستشارات التقنية:** أي مشكلة بموبايلك أو حاسبتك، أيوب يحلها لك."""
        
    elif any(x in p for x in ["موقع", "مكان", "عنوان", "وين"]):
        ans = "مقرنا الأساسي في **بغداد - اليوسفية - حي الصقور**، وعندنا خدمة توصيل (طيارة ✈️) لكل محافظات العراق من الشمال للجنوب!"
        
    elif any(x in p for x in ["شكرا", "رحم الله", "عاشت ايدك"]):
        ans = "تدلل عيني، هذا واجبي! مكتبة أيوب دائماً بالخدمة وتفخر بزبائنها."
        
    else:
        ans = "والله يا طيب ما فهمت سؤالك تمام، بس تقدر تسألني عن (الذكاء الاصطناعي، القرطاسية، التعيينات، أو موقعنا) وتدلل!"

    st.session_state.messages.append({"role": "bot", "content": ans})
    st.rerun()

# --- استمارة الطلب (المرحلة النهائية) ---
st.divider()
with st.form("main_order"):
    st.markdown("### 📥 اطلب خدمتك الآن")
    f_name = st.text_input("الأسم الكامل")
    f_phone = st.text_input("رقم الواتساب")
    f_type = st.selectbox("مجال الطلب", ["ذكاء اصطناعي", "قرطاسية وهدايا", "تعيينات وتقديم", "أخرى"])
    f_details = st.text_area("اشرح لنا شمحتاج بالضبط")
    
    if st.form_submit_button("إرسال الطلب إلى أيوب"):
        if f_name and f_phone:
            requests.post(FORMSPREE_URL, data={"Name": f_name, "Phone": f_phone, "Type": f_type, "Details": f_details})
            st.balloons()
            st.success(f"عاشت إيدك يا {f_name}! طلبك وصل وراح نتواصل وياك بأسرع وقت.")
