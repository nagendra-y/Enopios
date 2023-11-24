from inference.engine import Model
import os 

model = Model(os.getcwd()+ "/ct2_model/indic-en-deploy/ct2_int8_model", device="cpu", model_type="ctranslate2")

src_lang= "hin_Deva"
tgt_lang = "eng_Latn"
result = model.translate_paragraph("जब मैं छोटा था, मैं हर रोज़ पार्क जाता था।", src_lang, tgt_lang)
print(result)
