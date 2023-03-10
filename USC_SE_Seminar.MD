# USC Software Engineering Seminar Research Work Presentations

## 9/16 Sasha

## 9/30 Amirmohammad - Explainable Program Synthesis by Localizing Specifications

- Online source:

- **Summary**: Allow the users to interrogate the program synthesizer.
- **Motivation**: Help programmers with coding tedious code, but the synthesis doesn't work for all situations. So we want to have ability to help users to interrogate the synthesizer.
- **Approach**: Two groups with 9 students each, tested with/without sub-specification. The sub-specifications are some more information, details about part of the entire requirement.
- **Potential application**: localizing bugs, generate information that helps fix the bugs.
- **Questions**: The average coding level may vary between two groups. (By the way, the times given to two groups are also different.)
- **Potentially useful information**: OpenAI Codex, which can explain code. This may be used for generating comments/documentations.

## 10/7 Xin - Make Verification scalable

- **Performing sampling**
- **Black box**
- **Guess the robustness value**: Previous approach only provide solutions to find one point, but here they tried to find all in a certain region.
- **Gaussian regression**: Prediction model.
- **Conformal inference**

## 10/21 Synthesis and Verification for Distributed Systems - Mosen Lesani

- high level specifications
- midware, instructions
- apps

### Byzantine General Problem

- Assuming the messaging is trustworthy, we need to solve the problem of potential erroneous information.

### Web Assembly Obfuscation from JavaScript - Alan

#### Obfuscation tools, studies, and detection

Code obfuscation takes well-engineered code and makes it difficult for an attacker to understand.

- Between JS and WS. JS is dynamically-typed while WS is not.
- AST
- Synchronous and asynchronous transformations.

#### Models

- Identify code locations.
- Transform JS to JS and WA.
- Obfuscated cases.

## 11/4 Dominik Winterer - SMT Solver

- **SMT**: Satisfiability Modulo Theory. This is a higher level of SAT. SAT focuses only on boolean expressions but SMT works on more general entities in programming, such as real numbers and some data structures.
- **Key Idea**: Fuse two existing equi-satisfiable formula into one that preserve the satisfiability, which will be used for validating SMT solvers.
- **Tool**: YinYang, a tool for SMT solver testing.

### Semantic Fusion

## Tracer: Signature-based Static Analysis for Detecting Recurring Vulnerabilities

**Problem**: Some vulnerabilities are recurring with some identifiable text ("similar to CVE...").

**Insights**: reuse of code, packages and libraries.

**Goal**: accuracy, robustness, generalizability, scalablilty, usability.

**Methodology**:

- Data dependency
- Detect new vulnerabilities
- Check similarities
- Compare the trace (a line from the source to the sink of a bug/vulnerability)

**Dataset**:

- OWASP
- Juliet test suite (NSA)

Challenges for manually collecting data: CVE reports are given in nature language. The code needs to be checked to identify the actual cause of those vulnerability bugs.

## 2022/11/18 AI for Financial Loan Predictions

- Reduce risk and grow loan profit: traditional method (credit score) does not provide information about health, future health, and future income, etc.

- Data warehouse: correlation and verification (make sure the data are true).

## 2022/12/2 Program Fuzzing

- **Problem**: To automatically expose vulnerabilities. Previous approaches are simply applying default setting for Havoc without seeking for potential improvements.
- **Approach**: Adjusting settings for Havoc and integrating approaches, such Multi-armed Bandits to improve coverage.
- **Evaluation**: Comparing the coverage of the tools.

## 2023/1/27 Trustworthy Software Enabled by Program Analysis and Synthesis

- **Problem**: Quality problems in non-functional properties.

Some advices on job interview:

- Reduce the amount of details, making it less verbose.
- Future plans should be close to the past work.
- More introduction and more future plan details.
- Tell one story, make things connected strictly.
- What do they care? Money, basically.

## 2023/2/17 Fairness of KNN - Yannan Li

### Fairness

Similar people should be treated similarly, regardless of protected attributes. That's to say, we give similar decisions for those with similar public attributes.

### Biased-annotated Data

Conservatively assuming all data might be wrong.

### KNN K-Nearest Neighbor

## 2023/3/3 Toward Efficient Identification of Exploitable Code - Adriana (Job Talk)

Graph representation of Vulnerability

### Differential Privacy

<https://en.wikipedia.org/wiki/Differential_privacy>

Differential privacy (DP) is a system for publicly sharing information about a dataset by describing the patterns of groups within the dataset while withholding information about individuals in the dataset. The idea behind differential privacy is that if the effect of making an arbitrary single substitution in the database is small enough, the query result cannot be used to infer much about any single individual, and therefore provides privacy.

Another way to describe differential privacy is as a constraint on the algorithms used to publish aggregate information about a statistical database which limits the disclosure of private information of records whose information is in the database. For example, differentially private algorithms are used by some government agencies to publish demographic information or other statistical aggregates while ensuring confidentiality of survey responses, and by companies to collect information about user behavior while controlling what is visible even to internal analysts.

Roughly, an algorithm is differentially private if an observer seeing its output cannot tell if a particular individual's information was used in the computation. Differential privacy is often discussed in the context of identifying individuals whose information may be in a database. Although it does not directly refer to identification and re-identification attacks, differentially private algorithms probably resist such attacks.

Differential privacy was developed by cryptographers and thus is often associated with cryptography, and draws much of its language from cryptography.

### General Takeaways for research presentations

- Show the newness: show the related works and the problem has not been explored yet
- Show the important: give evidence about the significance of solving the given problem
- Show the hardness: how is the research challenging

## Persistent Memory- 03/10 Zunchen Huang

<https://en.wikipedia.org/wiki/Persistent_memory>

In computer science, persistent memory is any method or apparatus for efficiently storing data structures such that they can continue to be accessed using memory instructions or memory APIs even after the end of the process that created or last modified them.

Often confused with [non-volatile random-access memory (NVRAM)](https://en.wikipedia.org/wiki/Non-volatile_random-access_memory), persistent memory is instead more closely linked to the concept of persistence in its emphasis on program state that exists outside the fault zone of the process that created it. (A process is a program under execution. The fault zone of a process is that subset of program state which could be corrupted by the process continuing to execute after incurring a fault, for instance due to an unreliable component used in the computer executing the program.)

## Automated Testing for Transferred Applications - Saghar 03/10

### General concerns
- Code coverage-based test is not enough for projects.
- Usage-based testing.

### 