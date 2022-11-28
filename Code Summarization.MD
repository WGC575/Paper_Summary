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
- **Evaluation**: Manual. A group of programmers reads the outputs from the tools while not owning extraneous knowledge and not missing any cri []tical information.

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
