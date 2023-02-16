# Code Summarization Tools

## [FSE 2022] Are We Building on the Rock? On the Importance of Data Preprocessing for Code Summarization

<https://dl.acm.org/doi/10.1145/3540250.3549145>

- **Problem**: The quality of benchmark dataset may not be as high as expected.
- **Approach**: Proposed an automated code-comment cleaning tool that can detect noises in data that are caused by inappropriate preprocessing operations.
- **Evaluation**: Statistical. Demonstrated these noises impact analysis negatively, and the proposed tool can effectively improve the performance of code summarization.

## [ICPC 2013] Automatic generation of natural language summaries for Java classes

<https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6613830>

- **Problem**: Documentation for developers to read and understand the program is often absent or outdated.
- **Approach**: To automatically generate human-readable summaries for java classes, with an assumption that no documentation exists. It uses existing lexicalization tools.
**This is specifically for class summarization, and it focuses on the contents of the classes instead of the relationships between classes.**
- **Evaluation**: Manual. A group of programmers reads the outputs from the tools while not owning extraneous knowledge and not missing any critical information.

## [ASE 2010] Towards automatically generating summary comments for Java methods

<https://dl.acm.org/doi/10.1145/1858996.1859006>

- **Problem**: Few software projects adequately comment the code. Besides this, there are obsolete.
- **Approach**: Automatically generate descriptive summary comments for Java methods. The final generation of text is through calling methods that output sentences, different methods for different signatures.
- **Evaluation**: Manual. Programmers judge whether the generated summaries are concise and accurate.

## [ICPC 2013] Evaluating Source Code Summarization Techniques: Replication and Expansion

<https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6613829>

- **Problem**: Not specified.
- **Approach**: Replication and extension of an existing tool, based on topic-modeling.
- **Evaluation**: 14 programmers to evaluate.

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

## [ACL 2020] A Transformer-based Approach for Source Code Summarization

<https://arxiv.org/pdf/2005.00653.pdf>


## [arxiv 2019] Automatic Code Summarization: A Systematic Literature Review

<https://arxiv.org/pdf/1909.04352>

### Contribution

- Compared to Moreno's and Nazar's work, while they include text-to-text summarization and code-to-code summarization such as summarizing **mailing list** and **bug reports**, this review focus on **text-to-code** summarization.
- Reviewed 41 studies focusing on source code summarization from 2010 to 2019
- Comparing different approaches
- Synthesis of current SOTA over source code summarization
- Future research

### Contents

- IE (Information Extraction Techniques)
- How to generate and what to generate
- Evaluation
- Categorization of Approaches

