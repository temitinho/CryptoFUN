import streamlit as st



alphabet_list = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

alphabet_dict = {item: index for index, item in enumerate(alphabet_list)}

def encrypt_letter(letter, crypto_delta):
    if letter in alphabet_dict.keys():
        letter_crypto_index = alphabet_dict[letter] + crypto_delta
        temp_crypto_index = letter_crypto_index % len(alphabet_list)
        letter_crypto = alphabet_list[temp_crypto_index]
        return letter_crypto
    else:
        return letter

def encrypt_text(text, crypto_delta):
    text = text.lower()
    text_encripted = ""
    for char in text:
        text_encripted +=  encrypt_letter(char, crypto_delta)
    return f" {text_encripted} "


def main():
    st.title("CryptoFun")
    
    # Create a form
    with st.form("text_converter_form"):
        crypto_delta = st.selectbox("Select Encryption delta", list(range(1, 27)))
        st.write("Enter your text to encrypt:")
        text = st.text_area(
        "",
        )

        st.write(f'You wrote {len(text)} characters.')
        submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        result = encrypt_text(text, crypto_delta)
        Path = f'''{result}'''
        st.code(Path, language="text", line_numbers=False)
        decrypto_delta = 26 - crypto_delta
        st.write(f"COPY the text above and Use DELTA = **{decrypto_delta}** to reveal the original text")


if __name__ == "__main__":
    main()
