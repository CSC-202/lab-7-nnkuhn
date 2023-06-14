# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
POKEMON_LYRICS = 'I wanna be the very best. Like no one ever was. To catch them is my real test. To train them is my cause. I will travel across the land. Searching far and wide. Each Pokemon to understand. The power that\'s inside. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny. (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon. (gotta catch \'em all.) Gotta catch \'em all. Yeah. Every challenge along the way. With courage I will face. I will battle every day. To claim my rightful place. Come with me, the time is right. There\'s no better team. Arm in arm we\'ll win the fight. It\'s always been our dream. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon (gotta catch \'em all.) Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Yeah! (Pokemon, gotta catch \'em all). Its you and me. I know it\'s my destiny. (Pokemon) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you Pokemon. (gotta catch \'em all). Gotta catch \'em all. (Pokemon)'
JIGGLE_JIGGLE = 'You have to have something that sticks. You have to have something that\'s monumental. When you walk out on stage, that\'s been monumental. (Jiggle, jiggle) Can you remember any of the rap that you did? My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. I sip booze from chalices, holding my palaces. Crib is so crampy suckers suffer from paralysis. Rhymes, I write them in the castle. You try to diss me and pretty soon your ass. Will squat in a cell \'cause I can tell you it\'s illegal. Treason, that\'s the reason I\'m regal. You do the time for the crime of lèse-majesté. And **** the police \'cause they can\'t arrest me. (They can\'t arrest me, they can\'t arrest me). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?)'
ALPHABET = 'Now it\'s time for our wrap up. Let\'s give it everything we\'ve got. Ready, begin. Artificial amateurs aren\'t at all amazing. Analytically, I assault, animate things. Broken barriers bounded by the bomb beat. Buildings are broken, basically I\'m bombarding. Casually create catastrophes, casualties. Canceling cats got their canopies collapsing. Detonate a dime of dank daily doin\' dough. Demonstrations, Don Dada on the down low. Eatin\' other editors with each and every energetic. Epileptic episode, elevated etiquette. Furious fat fabulous fantastic. Flurries of funk felt feeding the fanatics. Imitators idolize, I intimidate. In a instant, I\'ll rise in a irate state. Juiced on my jams like jheri curls, jockin\' joints. Justly, it\'s just me, writin\' my journals. Kindly I\'m kindling all kinds of ink on. Karate kick type Brits in my kingdom. Let me live a long life, lyrically lessons is. Learned lame louses just lose to my livery. My mind makes marvelous moves, masses. Marvel and move, many mock what I\'ve mastered.  Niggas nap knowin\' I\'m nice naturally. Knack, never lack, make noise nationally.  Operation, opposition, off, not optional. Out of sight, out of mind, wide beaming opticals. Perfected poem, powerful punchlines. Pummeling petty powder puffs in my prime. Quite quaint quotes keep quiet it\'s Quannum Quarrelers ain\'t got a quarter of what we got, uh. Really raw raps, risin\' up rapidly. Riding the rushing radioactivity. Super scientifical sound search sought. Silencing super fire saps that are soft. Tales ten times talented, they\'re too tough. Take that, challengers, get a tune up. Universal, unique untouched. Unadulterated, the raw uncut. Verb vice Lord victorious valid. Violate vibes that are vain make \'em vanished. Why I\'m all well, would a wise wordsmith. Just weaving up words weeded up, on my work shift. Xerox, my X-ray-diation holes extra large. X-height letters and xylophone tones.'

# DATA - mantras
GREEN_LATTERN = 'In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil\'s might, Beware my power... Green Lantern\'s light!'
JEDI_CODE = 'Emotion, yet peace. Ignorance, yet knowledge. Passion, yet serenity. Chaos, yet harmony. Death, yet the Force.'
SITH_CODE = 'Peace is a lie. There is only Passion. Through Passion, I gain Strength. Through Strength, I gain Power. Through Power, I gain Victory. Through Victory my chains are Broken. The Force shall free me.'

# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding


    # STEP 0 - TODO
## defining our data structures
    class Node: # NOT given to students
        letter: str
        weight: int
        left: any
        right: any
        
        def __init__(self, letter, w, l, r):
            self.letter = letter
            self.weight = w
            self.left = l
            self.right = r


    ## defining operations
### recursively traverses the huffman tree to record the codes
    def retrieve_codes(v: Node, path: str=''):
        if v.letter != None:
            coding[v.letter] = path
        else:
            retrieve_codes(v.left, path + '0') 
            retrieve_codes(v.right, path + '1')

    # STEP 1
    ## counting the frequencies - TODO
    for i in message:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1


    # STEP 2
    ## initialize the nodes - TODO
    for letter in freq:
        nodes.append(Node(letter, freq[letter], None, None))


    # STEP 3 - TODO
    ## combine each nodes until there's only one item in the nodes list
    while len(nodes) > 1:
        ## sort based on weight
        nodes.sort(key=lambda x: x.weight, reverse=True)

        ## get the first min
        min_a: Node = nodes.pop()

        ## get the second min
        min_b: Node = nodes.pop()

        ## combine the two
        combined: Node = Node(letter = None,
                            w = min_a.weight + min_b.weight,
                            l = min_a,
                            r = min_b)

        ## put the combined nodes back in the list of nodes
        nodes.append(combined)


    # STEP 4
    ## reconstruct the codes
    huff_root = nodes[0]
    retrieve_codes(huff_root)
    result: str = '' # TODO (hint coding[letter] -> code)
    for letter in coding:
        for j in message:
            if letter == j:
                result = result + str(coding[i])

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Kuhn Analyzing Huffman')
plt.xlabel('length of message')
plt.ylabel('compression %')
#plt.set_drawstyle('-.')

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## POKEMON
ratios: list = list()
length: list = list()
for i in range(1, MAX_N):
    sub_message = POKEMON_LYRICS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
    length.append(len(sub_message))
plt.plot(length, ratios[:MAX_N], label = 'Pokemon', color = 'r',)

# JIGGLE JIGGLE
ratios: list = list()
length: list = list()
for i in range(1, MAX_N):
    sub_message = JIGGLE_JIGGLE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
    length.append(len(sub_message))
plt.plot(length, ratios[:MAX_N], label = 'Jiggle Jiggle', color = 'g')


## ALPHABET
ratios: list = list()
length: list = list()
for i in range(1, MAX_N):
    sub_message = ALPHABET[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
    length.append(len(sub_message))
plt.plot(length, ratios[:MAX_N], label = 'Alphabet', color = 'b')

plt.legend()


# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
ratios: list = list()
length: list = list()
for i in range(1, MAX_N):
    sub_message = SITH_CODE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
    length.append(len(sub_message))
plt.plot(length, ratios[:MAX_N], label = 'Sith Code', color = 'r')

## GREEN LATERN'S OATH
ratios: list = list()
length: list = list()
for i in range(1, MAX_N):
    sub_message = GREEN_LATTERN[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
    length.append(len(sub_message))
plt.plot(length, ratios[:MAX_N], label = 'Green Lantern', color = 'g')

## JEDI CODE
ratios: list = list()
length: list = list()
for i in range(1, MAX_N):
    sub_message = JEDI_CODE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
    length.append(len(sub_message))
plt.plot(length, ratios[:MAX_N], label = 'Jedi Code', color = 'b')
plt.legend()


plt.savefig('./figs/lab7_kuhn.png')

