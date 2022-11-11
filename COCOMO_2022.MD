# COCOMO II - 2022

## SRDR (Software Resources Data Reports)

- SRDR are the DoD's mechanism for collecting data from software projects.
- Frequency of the vocabulary with NLP methodology.
- Effective words vs. less effective works

## Spacecraft Flight Software Cost Estimation

- It's difficult to budget with uncertain cost estimation.
- KNN, clustering.
- Effort model, SLOC clustering model.

## Automated Continuous Program Estimation for Pipelines and Factories

(From <https://en.wikipedia.org/wiki/Monte_Carlo_method>) **Monte Carlo**: Monte Carlo methods, or Monte Carlo experiments, are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle. They are often used in physical and mathematical problems and are most useful when it is difficult or impossible to use other approaches. Monte Carlo methods are mainly used in three problem classes: optimization, numerical integration, and generating draws from a probability distribution.

- Data from Jira, Gitlab, Rally.
- Data collection context: Factory Pipelines.

## Software Licenses: A Bill You Can't Pay

- Programs do not always track purchases, support, and service costs.
- Variety of license strategies: enterprise, site, program, supplier purchases
- Inconsistent information on licenses...

## Naval System Product Line Modeling Research with COPLI(Product LInes)MO

### Models and Tools

- OVM

## Agile Research Reviews and Working with DoD

- Comparisons between waterfalls and agile efficiencies

Challenges:

- Flexibility and delay in knowing the overall architecture, design and requirements
- Balance practices that ensure quality with doing just enough
- Uncertainty of which metrics to use to track projects or estimate costs
- It seems for agile project, cost estimation is no longer important. But in fact, that's not the case.

Metrics for Agile:

- Function points require longer learning curves.

## Simplifying Software Sizing with Simple Function Points

- Simple function points will over-estimate the cost (actually, cost estimations are usually over-estimations)
- Using simple function points will reduce the learning cost for non-experts. It's easy, quick, while standard FP requires and provides more details.
- SFP is applicable to Agile.
- A concept of operations (abbreviated CONOPS, CONOPs, or ConOps) is a document describing the characteristics of a proposed system from the viewpoint of an individual who will use that system. <https://en.wikipedia.org/wiki/Concept_of_operations>

## Agile Estimation – Software Developers and Software Estimators Working Together

### Agile Techniques

- Story points
- planning poker

### Traditional Techniques

- Expert Judgement
- Function points
- Application points

## Standardize Software Intellectual Property

**Valuation Approaches**:

### Cost Approach: not quite reflective since cost does not cover all the intellectual

- Historical cost method: cost of development and opportunity costs, also not reflective.
- Replacement cost method: replace or use existing tools.

### Market Approach

- ...
- Discount cash flow

### Required Data

- Detailed evidence of software to be evaluated
- Time frame of IP protection
- Business plans
- Financial ...

## General Error Regression Method

## Causal Analysis in Software Engineering

New Causal Algorithms

### BOSS

- Score-based search algorithm based on permutations
- Adaptation and optimization of the Greedy Relaxations of Sparsest Permutation algorithm
- In testing, near-perfect adjacency and orientation of graph edges.

### Markov Checker

- The Causal Markov Condition (CMC) is "all graph-implied conditional independencies hold in the dataset"
- Many causal algorithms assume CMC
- The new Markov Checker algorithm (MC) tests for CMC
- MC reports what % of CIs implied by the graph hold in the dataset.
- 1% is the expected rate of CIs failing due to chance; an actual rate near this suggests that the CMC holds, so the causal algorithm results can be trusted.
