import numpy as np
import pandas as pd
import random

dividends = pd.read_csv(r"C:\Users\82103\Desktop\YONSEI\2024-1\OR확정모델\프로젝트\data.csv")

# 배당금 데이터 (10개만 추출)
dividends = dividends.drop(dividends.columns[11:], axis=1)
dividends_A = dividends['ABBV']
dividends_B = dividends['ABT']
dividends_C = dividends['ADM']
dividends_D = dividends['ADP']
dividends_E = dividends['AFL']
dividends_F = dividends['ALB']
dividends_G = dividends['AOS']
dividends_H = dividends['APD']
dividends_I = dividends['ATO']
dividends_J = dividends['BDX']

# 임의의 월별 주가 데이터 10개 생성
np.random.seed(0)
prices_A = pd.Series(np.random.randn(124).cumsum() + 100)
prices_B = pd.Series(np.random.randn(124).cumsum() + 50)
prices_C = pd.Series(np.random.randn(124).cumsum() + 150)
prices_D = pd.Series(np.random.randn(124).cumsum() + 130)
prices_E = pd.Series(np.random.randn(124).cumsum() + 120)
prices_F = pd.Series(np.random.randn(124).cumsum() + 100)
prices_G = pd.Series(np.random.randn(124).cumsum() + 70)
prices_H = pd.Series(np.random.randn(124).cumsum() + 80)
prices_I = pd.Series(np.random.randn(124).cumsum() + 120)
prices_J = pd.Series(np.random.randn(124).cumsum() + 130)
prices = pd.concat([prices_A, prices_B, prices_C, prices_D, prices_E, prices_F, prices_G\
                    , prices_H, prices_I, prices_J], axis = 1)

def sharp(a, b, c, d, e, f, g, h, i, j):
    
    # 포트폴리오 비중
    weights = np.array([a, b, c, d, e, f, g, h, i, j])   
    
    # 주가 수익률 계산
    returns_A = prices_A.pct_change().dropna()
    returns_B = prices_B.pct_change().dropna()
    returns_C = prices_C.pct_change().dropna()
    returns_D = prices_D.pct_change().dropna()
    returns_E = prices_E.pct_change().dropna()
    returns_F = prices_F.pct_change().dropna()
    returns_G = prices_G.pct_change().dropna()
    returns_H = prices_H.pct_change().dropna()
    returns_I = prices_I.pct_change().dropna()
    returns_J = prices_J.pct_change().dropna()

    # 배당 수익률 계산
    dividend_yields_A = dividends_A / prices_A.shift(1)
    dividend_yields_B = dividends_B / prices_B.shift(1)
    dividend_yields_C = dividends_C / prices_C.shift(1)
    dividend_yields_D = dividends_D / prices_D.shift(1)
    dividend_yields_E = dividends_E / prices_E.shift(1)
    dividend_yields_F = dividends_F / prices_F.shift(1)
    dividend_yields_G = dividends_G / prices_G.shift(1)
    dividend_yields_H = dividends_H / prices_H.shift(1)
    dividend_yields_I = dividends_I / prices_I.shift(1)
    dividend_yields_J = dividends_J / prices_J.shift(1)

    # 총 수익률 계산
    total_returns_A = returns_A + dividend_yields_A[1:]
    total_returns_B = returns_B + dividend_yields_B[1:]
    total_returns_C = returns_C + dividend_yields_C[1:]
    total_returns_D = returns_D + dividend_yields_D[1:]
    total_returns_E = returns_E + dividend_yields_E[1:]
    total_returns_F = returns_F + dividend_yields_F[1:]
    total_returns_G = returns_G + dividend_yields_G[1:]
    total_returns_H = returns_H + dividend_yields_H[1:]
    total_returns_I = returns_I + dividend_yields_I[1:]
    total_returns_J = returns_J + dividend_yields_J[1:]

    # 포트폴리오의 총 수익률 계산
    total_returns = (total_returns_A * weights[0] +
                    total_returns_B * weights[1] +
                    total_returns_C * weights[2] +
                    total_returns_D * weights[3] +
                    total_returns_E * weights[4] +
                    total_returns_F * weights[5] +
                    total_returns_G * weights[6] +
                    total_returns_H * weights[7] +
                    total_returns_I * weights[8] +
                    total_returns_J * weights[9])

    # 무위험 수익률 (연간 3% 가정, 월간 (총 124개월) 수익률로 변환)
    risk_free_rate = 0.03 / 124

    # 포트폴리오의 평균 수익률
    mean_return = np.mean(total_returns)

    # 포트폴리오 수익률의 표준편차 (변동성)
    volatility = np.std(total_returns)

    # 샤프 지수 계산
    sharpe_ratio = (mean_return - risk_free_rate) / volatility
    return(sharpe_ratio)

# print(sharp(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1))

# 초기해 N개 생성 함수
def generate_initial_solution(N):
    initial_solution = np.random.randint(0, 10, (N, 10, 1))
    return initial_solution

# 적합도 평가 함수
def evaluate_fitness(solution):
    # 자본금 제약: constraint1 = sum([solution[i] * prices.iloc[123][i] for i in range(10)]) < C (수정해야함) 
    # 기타 제약들 추가
    
    if True:    # 제약식이 성립한다면
        weights = []
        for index in solution:
            index = [index[i]/sum(index) for i in index]
            weights.append(np.array(index).flatten())
        fitness_value = [sharp(*weights[i]) for i in range(len(solution))]
        
    else:   # 제약식이 성립하지 않는다면 0 부여
        fitness_value = 0
        
    return fitness_value



solution = generate_initial_solution(30)
print(evaluate_fitness(solution))

