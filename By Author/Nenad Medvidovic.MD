# Nenad Medvidovic

## 1. [ICTD 2021] Architectural Archipelagos: Technical Debt in Long-Lived Software Research Platforms

- **Online source**: <https://ieeexplore.ieee.org/document/9462988>

- **Summary**: This paper identifies a model specifically for the evolution of 3L-ARTS, large, long-lived academic research tool suites.
- **Motivation**: Work in a 3L project can be separate, though related, parts that form, architecturally speaking, an archipelago, thus inducing technical debts.

- **Approach**: Case studies on projects:

  - ARCADE family
  - c2.fw family

- **Conclusions**: The archipelagos may have advantages for researcher to reach their goals efficiently, but this will leave the project hard to maintain and accumulating technical debt. It is important to further study this type of technical debt and provide mature solutions to it.

- **Questions and concerns**: It is easy to understand that technical debt will cause problems when others are trying to use these 3L-ARTS. However, it might be hard to compare whether it's valuable and practical enough to encourage every researcher to pay more attention to the reliability, robustness, and reusability of their work when the major goal for many of them doesn't rely on those aspects. Time paid on these aspects may mostly be a burden for them when they are doing research.

## 2. [ICSA 2021]Architectural Decay as Predictor of Issue- and Change-Proneness

- **Online source**: <https://ieeexplore.ieee.org/document/9426752>

## 3. [ESEC/FSE 2021] Identifying Casualty Changes in Software Patches

- **Online source**: <https://dl.acm.org/doi/10.1145/3468264.3468624>
- **Summary**: This work focuses on identifying common non-essential casualty changes, which are noises in software patches. It categorizes these noises and brings a tool, CASCADE, to automatically and accurately identify these noises. By doing so, improving the results of a previously published approach.
- **Motivation**: Noises reduce the efficiency for patch analysis, and noises, casual changes, may have different types.
- **Database**: National Vulnerability Database, security patches.
- **Approach**: The tool, CASCADE, analyze patch noises with their dependency information, with categorizing at the very beginning of the workflow.
- **Conclusions**: 