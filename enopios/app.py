from inference.engine import Model
import copy
import os
import streamlit as st
import mammoth
import docx
from io import BytesIO


def extract_text_from_docx(uploaded_file):
    result = mammoth.extract_raw_text(uploaded_file)
    text = result.value.splitlines()
    # Filter out empty lines
    text = [line for line in text if line.strip()]
    return text

def save_text_to_docx(text, file_path):
    doc = docx.Document()
    for line in text:
        doc.add_paragraph(line)
    
    # Save the document to a BytesIO object
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def translate_sentences(sentences):
    src_lang = "hin_Deva"
    tgt_lang = "eng_Latn"
    model = Model(os.getcwd()+ "/ct2_model/indic-en-deploy/ct2_int8_model", device="cpu", model_type="ctranslate2")
    # Perform translation using your inference engine model
    # Assuming 'batch_translate' is a function that performs batch translation
    en_translations = model.batch_translate(sentences, src_lang, tgt_lang)
    return en_translations

def main():
    st.title("DOCX Text Translation and Saving")
    
    uploaded_file = st.file_uploader("Upload DOCX file", type=["docx"])
    
    if not uploaded_file:
        return

    try:
        original_text = extract_text_from_docx(uploaded_file)
        # Translate the original text
        translated_text = translate_sentences(original_text)

        st.subheader("Translation Section:")

        # Collect translations
        for index, paragraph in enumerate(original_text):
            st.write(f"Line {index + 1}")
            st.write(f"Original Text: {paragraph}")
            translation = st.text_area(f"Translated Line {index + 1}", value=translated_text[index])
            translated_text[index] = translation  # Update translation value

        save_button = st.button("Save Translations")

        # Display the updated translations after saving
        if save_button:
            st.subheader("Updated Translations:")
            for index, translation in enumerate(translated_text):
                st.write(f"Line {index + 1}: {translation}")

        if st.button("Save Translated Text"):
            translated_doc = save_text_to_docx(translated_text, "/home/indra/Downloads/translated_resume.docx")
            st.download_button(
                    label="Download Translated Text",
                    data=translated_doc,
                    file_name="translated_resume.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

    except Exception as e:
        st.error("An error occurred while processing the file.")
        st.error(str(e))

if __name__ == '__main__':
    main()

