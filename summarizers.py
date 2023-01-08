import string
import openai


class GptSummarizer():
    
    __api_key = ''
    
    def __init__(self, api_key, line_min_words, min_word_length):
        self.__api_key = api_key
        self.line_min_words = line_min_words
        self.min_word_length = min_word_length

    def summarize(self, text, length=256):
        openai.api_key = self.__api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.__clean_text(text),
            max_tokens=length,
            temperature=0.7,
            top_p=1,
            best_of=1,
            frequency_penalty=0,
            presence_penalty=0)
        return response['choices'][0]['text']
    
    def __clean_text(self, text, include_punct=True):
        lines = text.split('\n')
        lines_without_punctoation = list(map(lambda line: line.translate(str.maketrans('','',string.punctuation)), lines))
        line_min_len_condition = (lambda line: 
                                    len(line.split(' ')) > self.line_min_words and 
                                    any(list(map(lambda word: len(word.replace('.','')) > self.min_word_length, line.split(' ')))))
        clean_text_lines = list(filter(line_min_len_condition, lines if include_punct else lines_without_punctoation))
        return str(' '.join(clean_text_lines))


class Summary():

    def __init__(self, content):
        self.content = content