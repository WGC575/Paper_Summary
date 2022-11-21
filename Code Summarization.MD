# Code Summarization Tools

## [FSE 2022] Are We Building on the Rock? On the Importance of Data Preprocessing for Code Summarization

<https://dl.acm.org/doi/10.1145/3540250.3549145>

- **Problem**: The quality of benchmark dataset may not be as high as expected.
- **Approach**: Proposed an automated code-comment cleaning tool that can detect noises in data that are caused by inappropriate preprocessing operations.
- **Evaluation**: Demonstrated these noises impact analysis negatively, and the proposed tool can effectively improve the performance of code summarization.

## [ICPS 2020] Improved Code Summarization via a Graph Neural Network

<https://arxiv.org/abs/2004.02843>


- **Problem**: Structural information are used to improve performance. However, only AST is used rather than GNN.
- **Approach**: GNN-based approach, applied to 2.1 million Java method-comment pairs.
- **Evaluation**: Compared to four baseline techniques, two from software engineering, other two from machine learning literature.

## [ICSE 2020] Retrieval-based Neural Source Code Summarization

<https://dl.acm.org/doi/10.1145/3377811.3380383>

- **Problem**: Neural-based approaches prefer the high frequency words in the corpus, but it's having trouble with the low-frequency ones.
- **Approach**: Retrival-based neural source code approach by enhancing the neural model with the most similar code snippets retrieved from the training set.
- **Evaluation**: 
- Code provided.
