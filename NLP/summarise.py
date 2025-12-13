import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from heapq import nlargest # Used for finding the n largest values

# Download necessary NLTK resources if you haven't already
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
try:
    word_tokenize("test")
except LookupError:
    nltk.download('punkt')

def text_summarizer(text, num_sentences=3):
    """
    Performs extractive text summarization using word frequency scoring.

    :param text: The input paragraph/text (str).
    :param num_sentences: The desired number of sentences in the summary (int).
    :return: The summarized text (str).
    """
    if not text:
        return "Error: Input text is empty."

    # 1. Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    if len(sentences) < 5:
        return "Error: Input text must contain a minimum of 5 sentences."
    
    if num_sentences > len(sentences):
        num_sentences = len(sentences)

    # 2. Tokenize the text into words and remove stop words
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    
    # 3. Filter out stop words and calculate word frequency
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    word_freq = FreqDist(filtered_words)

    # 4. Score each sentence based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word.isalnum() and word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]

    # 5. Get the 'num_sentences' most highly scored sentences
    # nlargest returns a list of tuples: [(score, sentence), ...]
    # We only need the sentence strings.
    
    # We use nlargest to get the top 'num_sentences' scores from the dictionary values
    select_length = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # 6. Join the selected sentences to form the final summary
    summary = ' '.join(select_length)
    
    return summary

# --- User Input and Execution ---

# Input: A multi-line paragraph (minimum 5 lines/sentences)
user_input_paragraph = """
The Amazon rainforest is the largest tropical rainforest in the world. It spans nine countries, with the majority of it located in Brazil. It is often referred to as "the lungs of the Earth" because its vast forests produce a significant portion of the world's oxygen. However, the ecosystem is under severe threat from deforestation. This process, driven by cattle ranching, logging, and agriculture, is causing irreversible damage. Protecting the Amazon is crucial not only for the local environment but also for global climate stability. Scientists estimate that millions of species of insects, plants, and animals live there, many of which have not yet been discovered. The destruction of this biome could lead to catastrophic biodiversity loss. Therefore, international cooperation is necessary to implement sustainable development practices and conservation efforts. Local indigenous communities also play a vital role in protecting the forest. Their traditional knowledge is invaluable for maintaining the ecological balance of the region.
"""

# The number of sentences desired in the output summary
summary_length = 3

print("Original Paragraph (Min 5 Sentences): ")
print(user_input_paragraph)

# Get the summarized text
summarized_text = text_summarizer(user_input_paragraph, summary_length)

print(f"Summarized Text ({summary_length} Sentences): ")
print(summarized_text)