class Solution:
    def mostCommonWord(self, parag: str, banned: List[str]) -> str:
        parag = parag.lower()
        
        for i in parag:
            if i in "!?',;.":
                parag = parag.replace(i, " ")
        words = parag.split()
        
        return collections.Counter(word for word in words if word not in banned).most_common(1)[0][0]        
        