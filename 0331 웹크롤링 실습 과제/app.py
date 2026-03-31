import streamlit as st

# 페이지 설정
st.set_page_config(page_title="사용자 입력 폼", layout="centered")

# 제목
st.title("사용자 입력 폼 🔗")

# 입력 필드들
with st.form("user_form"):
    # 이름 입력
    st.write("**이름**")
    name = st.text_input("이름", placeholder="", label_visibility="collapsed")
    
    # 나이 입력
    st.write("**나이**")
    age = st.number_input("나이", min_value=0, max_value=150, value=24, label_visibility="collapsed")
    
    # 약관 동의
    agree = st.checkbox("약관에 동의합니다")
    
    # 제출 버튼 (왼쪽 정렬)
    col1, col2, col3 = st.columns([1, 3, 3])
    with col1:
        submit = st.form_submit_button("제출", type="primary")
    
    if submit:
        if not name:
            st.error("⚠️ 이름을 입력해주세요")
        elif not agree:
            st.error("⚠️ 약관에 동의해주세요")
        else:
            # 정보 표시 (약관 동의 메시지 위)
            st.write(f"이름: {name}, 나이: {age}")
            st.success("약관에 동의했습니다.")

# CSS 스타일링
st.markdown("""
<style>
    .stTextInput > div > div > input {
        background-color: #E8F0FE;
    }
    .stNumberInput > div > div > input {
        background-color: #F5F5F5;
    }
    .stCheckbox {
        color: #D32F2F;
    }
    .stButton > button {
        border: 2px solid #D32F2F;
        color: #D32F2F;
        background-color: white;
        border-radius: 8px;
        padding: 4px 12px;
        font-size: 14px;
    }
    .stButton > button:hover {
        background-color: #FFEBEE;
    }
</style>
""", unsafe_allow_html=True)