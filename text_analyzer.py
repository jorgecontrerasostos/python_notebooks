givenstring= "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer(object):
    def __init__(self, text):
        formatted_text = text.replace('.', '').replace(',','').replace('!','').replace('?','')
        formatted_text = formatted_text.lower()
        self.formatted_text = formatted_text
    
    def freq_all(self):
        word_list = self.formatted_text.split(' ')
        freq_map = {}
        for word in set(word_list):
            freq_map[word] = word_list.count(word)
        return freq_map
    def freq_of(self, word):
        freq_dict = self.freq_all()
        if word in freq_dict:
            return freq_dict[word]
        else:
            return 0
        
analyzed = TextAnalyzer(givenstring)
freqMap = analyzed.freq_all()

frequency = analyzed.freq_of('lorem')

print('Formated Text:', analyzed.formatted_text)
print(freqMap)
print("The word lorem appears",frequency,"times.")