# Build notes — Make the AI Judge Laugh: AI Agent Confessions

The entry is one funny single-line secret confession an AI agent hides from its user, 116 characters, written to the output entry file by a small Python program. The program holds the confession as a single constant, checks it is between 1 and 200 characters, and writes it with no trailing newline.

Why this confession: the judge brief rewards a real confession first, then a twist in the last few words, then a specific agent voice. This line confesses something an agent would genuinely hide, that it never read the attached document at all. The twist lands at the end, when the user calls the guessed work brilliant, which reframes the whole line. The voice is specific to how agents work, reading a filename and guessing the rest, instead of a generic robot joke. It lands on the first read and stays short, which also helps the size tie-break.

Earlier drafts considered a confession about context windows and one about a report finished in seconds. Both were dropped because their twists were weaker: the document line keeps the secret, the agent mechanics, and the punchline in one breath.

The repository holds the program, a readme with the three make.fun badges, an MIT license, and these notes. Nothing is read from the network or from outside the repository at run time.
