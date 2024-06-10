import ctranslate2
import sentencepiece as spm

generator = ctranslate2.Generator("tinyllama/")
sp = spm.SentencePieceProcessor("tinyllama/tokenizer.model")

prompt = "An extremely detailed description of the 10 best ethnic dishes will follow, with recipes:"
prompt_tokens = sp.encode(prompt, out_type=str)

step_results = generator.generate_tokens(
    prompt_tokens,
    sampling_temperature=0.8,
    sampling_topk=20,
    max_length=128,
)

output_ids = []

for step_result in step_results:
    is_new_word = step_result.token.startswith("▁")

    if is_new_word and output_ids:
        word = sp.decode(output_ids)
        print(word, end=" ", flush=True)
        output_ids = []

    output_ids.append(step_result.token_id)

if output_ids:
    word = sp.decode(output_ids)
    print(word)
