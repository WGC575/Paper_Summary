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
