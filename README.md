# Text-Readalily
The program can be used for evaluating text readability on a scale "easy, middle, hard".
It also computes the following readability metrics: SMOG, Flesh Kinkaid, Dale Chale, Coleman Liau, Automated Readability Index and a mean complexity metric based on them all.

To get results you should:

1. Run classifier.py to fit SVM classifier, scaler and normilazer.
2. Put in one directory all your texts in .txt format(convert to utf-8 if necessary) which readability you want to measure.
3. Then run measure_readability.py. The programm will ask you for a name of directory with imput texts.
4. Get your results.
