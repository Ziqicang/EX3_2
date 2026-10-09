### COMPLETE THE CODE ###

from rag_tool import rag_tool
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "Qwen/Qwen3-0.6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float16,
    device_map="auto"
)

def answer_question(question: str) -> str:
  
    context = rag_tool(question)

    
    messages = [
        {
            "role": "system",
            "content": "You are a university IT support assistant. Answer based ONLY on the provided policy documents. If the information is not in the documents, say 'I don't know.' Never invent phone numbers or details. Give only a short, direct answer."
        },
        {
            "role": "user",
            "content": f"Policy documents:\n{context}\n\nQuestion: {question}"
        }
    ]

    text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)


    
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=False,
        repetition_penalty=1.3,
        pad_token_id=tokenizer.eos_token_id
    )

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    
  
    response = response.strip().split("\n")[0].strip()
    return response


if __name__ == "__main__":
    question = "What exact phone number should I call for the University IT Service Desk?"
    print(answer_question(question))
