import time 
import sys 
WORD_DELAY = 0.3
LINE_PAUSE = 1.5

def print_lyrics():
    """Prints the lyrics word by word with a short pause for dramatic effect."""
    
    lines = [
       "Jaane Kyoon Dil Ye Tera",
       "Hai Mere Pyaar Mein",
       "Laakhon Kataar Mein Hain",
       "Mere Intezaar Mein",
       "Rokoon Jo Dil Ko To Ruke Na",
       "Aankhein Dikhaun Par Jhuke Na",
       "Hai Ye Tujhpe Fidda",

       "Dil Ke Kahayalon Mein",
       "Beete Sawaalon Mein",
       "Shabd Naye Buno",
       "Kuch To Naya Kaho",
       
    ]
    for line in lines:
        words = line.split()
        for word in words:
            print(word, end=' ', flush=True)
            time.sleep(WORD_DELAY)
        print()
        time.sleep(LINE_PAUSE) 
if __name__ == "__main__":
    print("--- Starting Lyric Playback (Word-by-Word) ---")
    print_lyrics()
    print("--- Playback Complete ---")