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
