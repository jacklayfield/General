def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],  # deletion
                                   dp[i][j - 1],  # insert
                                   dp[i - 1][j - 1])  # sub

    return dp[m][n]


def correct_spelling(word, word_list):
    min_distance = float('inf')
    corrected_word = None

    for real_word in word_list:
        distance = edit_distance(word, real_word)
        if distance < min_distance:
            min_distance = distance
            corrected_word = real_word

    return corrected_word


# Example
# --------------------------------------------------------
word_list = [
    "accommodate", "acknowledge", "acquire", "aggressive", "amateur", "apparent", "argument", "atheist", "believe", "calendar",
    "category", "committee", "conscience", "conscious", "definitely", "embarrass", "existence", "fascinate", "fiery", "foreign",
    "friend", "gauge", "grateful", "guarantee", "harass", "height", "humorous", "independent", "judgment", "knowledge",
    "liaison", "lightning", "maintenance", "medieval", "millennium", "miniature", "misspell", "necessary", "noticeable", "occasionally",
    "occurred", "pavilion", "perceive", "perseverance", "pharaoh", "playwright", "possession", "precede", "privilege", "pronunciation",
    "publicly", "queue", "receive", "recommend", "referendum", "relevant", "restaurant", "rhythm", "ridiculous", "schedule",
    "separate", "sergeant", "supersede", "their", "threshold", "tragedy", "tyranny", "unforeseen", "unfortunately", "until",
    "vacuum", "vengeance", "weird", "weirdo", "weirdos", "weirdest", "wholly", "wrestle", "write", "written",
    "wrote", "yield", "your", "you're", "yourselves", "yours"
]

user_word = input("Enter a word to correct (See word list for options): ")

spell_correct_word = correct_spelling(user_word, word_list)

if user_word == spell_correct_word:
    print("You spelled the word right!")
elif spell_correct_word:
    print(f"The corrected word for '{user_word}' is '{spell_correct_word}'.")
else:
    print("No correction found (See word list for options).")
