import streamlit as st

st.set_page_config(page_icon="π", layout="wide")
st.header("μλνμΈμπ λΉμ λ§μ λ©΄μ  λμ°λ―Έ, **HEY-I**_v1.0 μλλ€!")


with st.form("my_form"):
    name = st.text_input("μ΄λ¦μ μλ ₯νμΈμ")
    num = st.number_input("μνλ λ€ μλ¦¬ μλ₯Ό μλ ₯νμΈμ",min_value=1000,max_value=9999)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        if len(name) > 1:
            st.session_state.name = name
            st.session_state.num = num
            st.success(f"{name}_{num} νμΈλμ΅λλ€! λ€μ λ¨κ³λ‘ λμ΄κ°μΈμ!", icon='π')
            print(st.session_state.name, st.session_state.num)
        else:
            st.warning('μ΄λ¦μ λ κΈμ μ΄μ μλ ₯ν΄μ£ΌμΈμ!', icon="β οΈ")

    else:
        st.warning('μλ ₯ν΄μ£ΌμΈμ!', icon="β οΈ")


    
