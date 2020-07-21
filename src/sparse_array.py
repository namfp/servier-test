from typing import List, Dict


class SparseArray:
    """
    Compute de frequencies of words

    """
    def __init__(self, word_list: List[str]):
        """
        :param word_list: a list of words to be computed
        """
        self.word_list = word_list
        self.cache = {}

    def _compute_one(self, query: str) -> int:
        """
        :param query: str, a word to compute the frequency
        :return: the number of occurrences of the word
        """
        found = self.cache.get(query)
        if found is None:  # test if the word can be found in cache
            count = 0
            for word in self.word_list:
                if query == word:
                    count = count + 1
            self.cache[query] = count  # update cache
            return count
        else:
            return found  # return directly value in cache

    def compute(self, query: List[str]) -> Dict[str, int]:
        """
        :param query: a list of string
        :return: a dictionary of words and the corresponded frequency
        """
        results = {}
        for word in query:
            results[word] = self._compute_one(word)
        return results
