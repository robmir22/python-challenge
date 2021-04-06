import os
import re

filepath = os.path.join("Resources", "raw_data_paragraph_2.txt")
with open(filepath, mode='r', encoding='utf-8') as textfile:
    text = textfile.read()

# text = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."
    words = re.split(r'\W+', text)
    sentence = re.split("(?<=[.!?]) +", text)

    # Approximate word count
    aa = (len(words))
    # Approximate sentence count
    bb = (len(sentence))

    a = 0
    for abc in words:
       a = a + (len(abc))

    # Approximate letter count (per word)
    cc = (a/len(words))

    # Average sentence length (in words)
    dd = (len(words)/len(sentence))


    print("----------------------------------")
    print("Paragraph Analysis")
    print("----------------------------------")
    print(f"Approximate Word Count: {aa}")
    print(f"Approximate Sentence Count: {bb}")
    print(f"Average Letter Count: {cc:.2f}")
    print(f"Average Sentence Length: {dd:.2f}")
    print("----------------------------------")