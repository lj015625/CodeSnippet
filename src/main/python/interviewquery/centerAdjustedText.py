words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16


def justify(words, max_width):
    """break into multiple lines and fill spaces between words."""
    cursor = 0
    currentLine = []
    result = []
    for w in words:
        # cannot add new word. instead format current line
        if cursor + len(w) >= max_width:
            spaceToAdd = max_width - cursor
            # insert at spaces between current words: for example 3 words means 2 spaces
            betweenWords = len(currentLine) - 1 if len(currentLine) > 0 else 1
            for i in range(spaceToAdd):
                currentLine[i % betweenWords] += ' '
            # save current line to result
            result.append(' '.join(currentLine))
            cursor, currentLine = 0, []

        # add new word
        if len(currentLine) > 0:
            cursor += 1
        cursor += len(w)
        currentLine.append(w)
    # end for
    return result + [' '.join(currentLine).ljust(max_width)]


print(justify(words, max_width))
