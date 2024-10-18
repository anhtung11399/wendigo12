import streamlit as st
import fugashi
import romkan

# Tạo đối tượng tagger từ fugashi
tagger = fugashi.Tagger()

# Tạo giao diện bằng Streamlit
st.title('Chuyển đổi từ tiếng Nhật sang Romaji')

# Nhập chuỗi tiếng Nhật
nihongo_text = st.text_input('Nhập chuỗi tiếng Nhật có Kanji', 'タスクを編集した内容を左側の表に')

# Khi nhấn nút "OK", thực hiện chuyển đổi
if st.button('OK'):
    # Duyệt qua các từ và chuyển sang Romaji
    romanji_text = " ".join([romkan.to_roma(word.feature.kana) if word.feature.kana else word.surface for word in tagger(nihongo_text)])

    # In kết quả ra giao diện
    st.write('Kết quả Romaji:')
    st.write(romanji_text)
