import re
encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift_back(text, n):
    return ''.join(
        alphabet[(alphabet.index(ch) - n) % 26] if ch in alphabet else ch
        for ch in text
    )

fragments = []
for num, jumbled, status in re.findall(r"\[(\d+)::([^:]+)::(ok|bad)\]", encoded):
    if status == "ok":
        fragments.append((int(num), shift_back(jumbled, int(num))))

fragments.sort()
raw_message = " ".join(dec for _, dec in fragments)
final_message = raw_message.replace("_", " ")

print("\nDecoded fragments:", raw_message)
print("Final message:", final_message)