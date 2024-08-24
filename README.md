# Market Risk Hedging Using Genetic Algorithm and Solver
## Focusing on Maximizing the Sharpe Ratio

## I. Introduction

### Project Motivation

After the COVID-19 pandemic, stock market volatility has significantly increased. The rapid spread of COVID-19 and its economic repercussions have led to unpredictable fluctuations, with markets experiencing sharp declines and rises. Various factors such as policy changes, corporate performance uncertainties, and global economic conditions have further shaken the markets. Given the increasing volatility of the financial market, we aim to explore strategies for hedging market risk.

We propose two main strategies:

1. **Dividend Optimization in Asset Portfolio Construction**:  
   We aim to optimize dividend yields when constructing an asset portfolio. By reducing volatility, investors can better respond to unexpected market shocks, making a dividend-focused portfolio a stable investment that provides consistent returns. For example, in scenarios like the COVID-19 pandemic, considering dividends alongside simple stock returns can help derive more stable returns through optimized strategies.

2. **Using Sharpe Ratio as an Evaluation Metric**:  
   The Sharpe Ratio is a measure of risk-adjusted returns. It is calculated by subtracting the risk-free return from the portfolio’s expected return and dividing it by the standard deviation of the portfolio’s excess return. Investments with higher Sharpe Ratios yield higher returns with less risk, making them viable strategies for hedging market risk. By considering risk-adjusted return metrics, our research emphasizes optimizing risk itself, rather than merely constructing an asset portfolio.

## II. Data Collection

We will collect historical data for each ticker from [Yahoo Finance](https://finance.yahoo.com). The data, including dividends, market capitalization, stock splits, and capital gains, will be imported as CSV files and preprocessed using Python.

## III. Objective Function, Constraints, and Decision Variables

### Objective Function

Our primary objective is to maximize the Sharpe Ratio, which can be represented by the following formula:

$Max Sharpe = {R_p - R_}/sigma_p$

- $R_p$: Expected return of the portfolio
- $R_f$: Risk-free return
- $\sigma_p$: Standard deviation of the portfolio’s excess return

Instead of simplifying the problem to a simple sorting issue, we set the objective as maximizing the Sharpe Ratio, which simultaneously considers both volatility and returns. These two factors are in a trade-off relationship, creating various scenarios. Therefore, we aim to optimize the Sharpe Ratio using a metaheuristic algorithm.

Assuming the Gordon Growth Model to estimate expected returns using dividend growth rate ($g\%$), the equation can be expressed as:

$ E(p) = \sum_{i} g_i w_i + \sum_{i} w_i d_i (1 + g_i) $

$ \sigma_p = \sqrt{\sum_{i}\sum_{j} w_i w_j \text{Cov}(t_i, t_j)} $

For $R_f$, we typically use the yield of risk-free assets, such as government bonds. However, for simplicity, we assume $R_f = 0.01$ in this study.

Thus, the final objective function becomes:

$ \text{Max} \frac{\sum_{i} g_i w_i + \sum_{i} w_i d_i (1 + g_i) - 0.01}{\sqrt{\sum_{i}\sum_{j} w_i w_j \text{Cov}(t_i, t_j)}} $

### Constraints

- $4 \leq \sum_{i} \leq 10$: Upper and lower bounds on the number of shares purchased for each stock.
- $\sum(x_i \cdot a_i) \leq B$: Total investment cost cannot exceed available capital.
- $D \leq \sum(x_i \cdot v_{im}) \text{ for all } m (D > 0)$: Minimum monthly dividend payout is specified.
- $x_i \geq 0$, $x_i$ is an integer: Non-negativity and integer constraints.

### Decision Variables

- $x_i$: Number of shares purchased
- $w_i$: Investment proportion ($x_i \times a_i / B$)

### Parameters

- $i, j$: Stock indices ($i, j = 1, 2, \dots , 40$)
- $a_i$: Stock price
- $v_{im}$: Monthly dividend of stock $i$ ($m = 1, 2, \dots , 12$)
- $g_i$: Dividend growth rate
- $d_i$: Dividend yield
- $s_i$: Stock price return
- $t_i$: Total return ($ = d_i + s_i$)
- $B$: Budget (total available capital)
- $D$: Minimum monthly dividend payout

### Why Genetic Algorithms (GA)?

GA is an optimization algorithm that treats a population of chromosomes as the solution set and allows only the fittest chromosomes to survive. Here, each chromosome is treated as the number of stocks, and the population represents a portfolio of several stocks. Since the decision variable $x_i$ is an integer, we assumed it must be solved with Integer Programming (IP). However, due to the variety of cases, the solver might take a long time to find a solution. To address the time issue, we chose GA, a metaheuristic that is particularly suitable. By generating offspring through selection, crossover, and mutation of chromosomes after creating $N$ initial solutions, GA can consider various scenarios. Unlike LP, it is less likely to get trapped in local optima, and we expect to find global optima.

## IV. Expected Outcomes

This project aims to optimize the dividend stock portfolio under given investment constraints. We expect it to yield stable maximum returns by responding to market and volatility risks. By incorporating models such as the Gordon Growth Model, we can enhance the portfolio’s reliability. The project could propose asset allocation strategies that demonstrate robust alpha generation through risk optimization.
