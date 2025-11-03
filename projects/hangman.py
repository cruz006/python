import random

def generate_random_word():
    """Generates a random English word from a list."""

    words = [
    # Fruits
    "apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape", "honeydew",
    "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua",
    "yellowplum", "zucchini", "apricot", "blackberry", "blueberry", "cranberry",
    "date", "gooseberry", "grapefruit", "lychee", "mulberry", "olive", "passionfruit",
    "pear", "persimmon", "pineapple", "plum", "pomegranate", "redcurrant", "soursop",
    "starfruit", "tomato", "avocado", "coconut", "durian", "guava", "rambutan",

    # Animals
    "aardvark", "antelope", "bear", "buffalo", "cat", "cheetah", "chicken", "chimpanzee",
    "cow", "coyote", "crab", "deer", "dog", "dolphin", "duck", "eagle", "elephant", "falcon",
    "ferret", "flamingo", "fox", "frog", "giraffe", "goat", "gorilla", "hamster", "hedgehog",
    "hippopotamus", "horse", "jaguar", "jellyfish", "kangaroo", "koala", "lemur", "leopard",
    "lion", "lizard", "lobster", "monkey", "moose", "octopus", "ostrich", "otter", "owl",
    "panda", "parrot", "peacock", "penguin", "pig", "porcupine", "rabbit", "raccoon",
    "rat", "reindeer", "rhino", "seal", "shark", "sheep", "sloth", "snail", "snake",
    "sparrow", "spider", "squid", "squirrel", "tiger", "turtle", "vulture", "walrus",
    "weasel", "whale", "wolf", "yak", "zebra",

    # Colors
    "red", "orange", "yellow", "green", "blue", "indigo", "violet", "white", "black",
    "gray", "pink", "purple", "brown", "teal", "turquoise", "magenta", "gold", "silver",
    "bronze", "beige", "maroon", "navy", "olive", "coral", "mint", "lavender",

    # Objects
    "table", "chair", "desk", "lamp", "window", "door", "carpet", "mirror", "clock",
    "bottle", "cup", "plate", "spoon", "fork", "knife", "pencil", "book", "notebook",
    "computer", "keyboard", "mouse", "monitor", "phone", "camera", "headphones", "microphone",
    "television", "remote", "backpack", "wallet", "watch", "key", "guitar", "violin",
    "drum", "piano", "bicycle", "skateboard", "helmet", "umbrella", "blanket", "candle",
    "suitcase", "toothbrush", "comb", "soap", "towel", "pillow", "bed", "couch", "fan",
    "fridge", "oven", "microwave", "toaster", "blender", "printer", "router", "pen", "eraser",

    # Nature / Miscellaneous
    "mountain", "river", "forest", "tree", "flower", "cloud", "rain", "snow", "storm",
    "wind", "sun", "moon", "star", "planet", "galaxy", "ocean", "beach", "island", "valley",
    "hill", "volcano", "earthquake", "fire", "sand", "rock", "grass", "leaf", "mushroom",
    "stone", "breeze", "dew", "fog", "ice", "thunder", "tornado",

    # Random concepts / adjectives
    "happy", "sad", "angry", "calm", "brave", "curious", "clever", "lazy", "kind", "bold",
    "shy", "strong", "weak", "fast", "slow", "quiet", "loud", "funny", "serious", "smart",
    "creative", "logical", "emotional", "optimistic", "pessimistic", "confident", "humble",
    "patient", "wild", "free", "energetic", "tired", "gentle", "chaotic", "focused",

    # Verbs
    "run", "walk", "jump", "swim", "fly", "sing", "dance", "sleep", "eat", "drink",
    "read", "write", "draw", "paint", "talk", "listen", "think", "build", "create",
    "learn", "teach", "code", "play", "laugh", "cry", "smile", "bake", "drive", "ride",
    "throw", "catch", "push", "pull", "carry", "lift", "cut", "open", "close", "clean",
    "wash", "fix", "break", "help", "save", "explore", "travel", "discover", "invent"
]


    random_index = random.randint(0, len(words) - 1)
    random_word = words[random_index]
    tries = len(random_word)

    return random_word, tries

def play_word_guessing_game():
    """Plays a word guessing game with the generated word."""

    random_word, tries = generate_random_word()
    guessed_letters = set()  # Keep track of guessed letters
    guessed_word = ["_"] * len(random_word)  # Initialize with underscores

    while tries > 0:
        print("The word:", " ".join(guessed_word))  # Display current guessed word
        guess = input("Guess a letter: ").lower()  # Convert input to lowercase for consistency

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)  # Add the guessed letter to the set

        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    guessed_word[i] = guess
        else:
            tries -= 1
            print("Incorrect guess. You have", tries, "tries remaining.")

        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", random_word)
            break

    if tries == 0:
        print("You ran out of tries. The word was:", random_word)

# Start the game
play_word_guessing_game()