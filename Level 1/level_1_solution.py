original_text = """CHAPTER I. Down the Rabbit-Hole

Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, ‘and what is the use of a book,’ thought Alice ‘without pictures or conversations?’

So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.

There was nothing so VERY remarkable in that; nor did Alice think it so VERY much out of the way to hear the Rabbit say to itself, ‘Oh dear! Oh dear! I shall be late!’ (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge.

In another moment down went Alice after it, never once considering how in the world she was to get out again."""

arr = [
'6',
'17',
'17',
'44',
'12',
'3A',
'/',
'/',
'3D',
'09',
'26A',
'18',
'1B',
'/',
'58',
'19C',
'58',
'13',
'31',
'18']

import string

# Remove whitespaces from text
sanitized_original_text = [c for c in original_text if c not in string.whitespace]

def decode(arr, original_text, base, multipication):
    decoded = ''
    is_sucess_encodingflag = False
    try:
        # Try decode message from original_text
        for x in arr:
            t = '/'
            if t != x:
                i = int(int(x, base) * multipication)
                t = original_text[i]
            decoded += t
        is_sucess_encodingflag = True
    except:
        # If failed to decode message
        pass
    finally:
        # Validate decoding message succeddeded
        if is_sucess_encodingflag:
            print(f'Base: {base} multipication is {multipication} => {decoded}')

for base in range(12, 65):
    for multipication in range(1, 10):
        # Decodinge message succeddeded with
        # Base: 15 multipication is 2 => nttps://rb.gy/uquefg
        # This is the URL of the next level
        decode(arr, sanitized_original_text, base=base, multipication=multipication)
