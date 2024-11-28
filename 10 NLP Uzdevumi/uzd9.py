from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from translate import Translator

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

translator = Translator(to_lang="lv")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# start_phrase = "Reiz kādā tālā zemē..."
start_phrase = "Once upon a time in a land far away..." # Neatradu bezmaksas modeļus kas strādā ar latviešu valodu tādēļ atkal caur tulkošanu

generated = generator(start_phrase, max_length=50, num_return_sequences=1, truncation=True)

english_text = generated[0]["generated_text"]
latvian_text = translator.translate(english_text)

print("\nĪss stāsts latviski:")
print(latvian_text)
