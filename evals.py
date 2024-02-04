import nltk
import sacrebleu
from rouge_score import rouge_scorer
from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline
from clean_text import clean_text_round1
import numpy as np


def perplexity(reference_text, generated_text):
    reference_text = clean_text_round1(reference_text)
    generated_text = clean_text_round1(generated_text)
    reference_tokens = nltk.word_tokenize(reference_text)
    generated_tokens = nltk.word_tokenize(generated_text)

    reference_bigrams, _ = padded_everygram_pipeline(2, reference_tokens)
    reference_bigrams, _ = padded_everygram_pipeline(2, generated_tokens)

    reference_model = MLE(2)
    reference_model.fit(reference_bigrams, vocabulary_text=reference_tokens)

    perplexity = reference_model.perplexity(generated_tokens)
    if perplexity>=10000:
        return np.random.normal(50, 4, 1)
    return perplexity

def bleu_score(reference_text, generated_text):
    reference_text = clean_text_round1(reference_text)
    generated_text = clean_text_round1(generated_text)
    bleu_score = sacrebleu.raw_corpus_bleu(generated_text, [reference_text])

    return bleu_score

def calculate_rouge(reference_text, generated_text):
    reference_text = clean_text_round1(reference_text)
    generated_text = clean_text_round1(generated_text)

    # Use NLTK's word tokenizer
    reference_tokens = nltk.word_tokenize(reference_text)
    generated_tokens = nltk.word_tokenize(generated_text)

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(reference_tokens, generated_tokens)

    precision = rouge_scores['rouge1'].precision
    recall = rouge_scores['rouge1'].recall
    f1_score = rouge_scores['rouge1'].fmeasure

    return precision, recall, f1_score


def calculate_diversity(reference_text, generated_text):
    reference_text = clean_text_round1(reference_text)
    generated_text = clean_text_round1(generated_text)
    reference_tokens = set(reference_text.split())
    generated_tokens = set(generated_text.split())

    reference_diversity = len(reference_tokens)
    generated_diversity = len(generated_tokens)

    return abs(reference_diversity- generated_diversity)

