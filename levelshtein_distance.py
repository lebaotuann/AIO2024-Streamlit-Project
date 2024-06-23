import streamlit as st

from constants import DATA_DIRECTORY_PATH


class WorldCorrection:
    def __init__(self, file_path: str):
        self._file_path = file_path  # The data file path.

    def load_vocab(self):
        """Loads vocabulary from the data file

        Returns:
            list: List of words in file.
        """
        with open(self._file_path, "r") as f:
            lines = f.readlines()
        # Normalize data
        # strip() -> remove the newline character (\n)
        words = sorted(set([line.strip().lower() for line in lines]))
        return words

    @staticmethod
    def levenshtein_distance(source: str, target: str):
        """Calculates the Levenshtein distance between two strings.
        The minimum edits to transform the source string to the target string (bottom right corner).
        Args:
            source (str): The source string.
            target (str): The target string.

        Returns:
            int: The Levenshtein distance.
        """
        row = len(source) + 1  # m
        column = len(target) + 1  # n
        # Create a storage matrix
        storage_matrix = [[0] * column for _ in range(row)]
        # Initialize first row and column.
        for i in range(row):
            storage_matrix[i][0] = i
        for j in range(column):
            storage_matrix[0][j] = j
        # Calculate edits
        for i in range(1, row):
            for j in range(1, column):
                if source[i - 1] == target[j - 1]:
                    sub_cost = (
                        0  # Substitution cost is 0 because characters are the same.
                    )
                else:
                    sub_cost = 1  # Substitution cost is 1
                # min(Deletion from source string, Insertion into source string, Substitution cost)
                storage_matrix[i][j] = min(
                    storage_matrix[i - 1][j] + 1,
                    storage_matrix[i][j - 1] + 1,
                    storage_matrix[i - 1][j - 1] + sub_cost,
                )

        return storage_matrix[row - 1][column - 1]

    def run(self):
        """Run word corrections"""
        st.title("Word Correction using Levenshtein Distance")
        word = st.text_input("Word: ")
        if st.button("Compute"):
            vocabs = self.load_vocab()  # Load data
            # compute levenshtein distance
            levenshtein_distances = dict()
            for vocab in vocabs:
                levenshtein_distances[vocab] = self.levenshtein_distance(word, vocab)
            # sorted by distance
            sorted_distances = dict(
                sorted(levenshtein_distances.items(), key=lambda item: item[1])
            )  # item = ("apple", 5)
            correct_word = list(sorted_distances.keys())[0]
            st.write("Correct word: ", correct_word)

            vocabulary_col, distance_col = st.columns(2)
            vocabulary_col.write("Vocabulary:")
            vocabulary_col.write(vocabs)
            distance_col.write("Distances:")
            distance_col.write(sorted_distances)


if __name__ == "__main__":
    vocab_file_path = DATA_DIRECTORY_PATH + "/data/vocab.txt"
    WorldCorrection(vocab_file_path).run()
