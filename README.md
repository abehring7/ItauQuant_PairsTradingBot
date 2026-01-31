
Bot de Trading de Arbitragem Estatística ("Pairs Trading"). Este projeto implementa um bot de trading de arbitragem estatística aplicado aos ativos do Ibovespa (com dados disponíveis no Yahoo Finance), utilizando técnicas de cointegração, modelos dinâmicos de hedge e normalização de risco. O programa coleta os preços históricos das ações do Ibovespa no período de 26/01/2021 a 15/01/2026 e realiza testes estatísticos para identificar pares elegíveis para arbitragem. Para todos os pares possíveis de ativos, são calculados o Teste de Cointegração (Engle–Granger) e o Teste ADF (Augmented Dickey-Fuller) aplicado ao spread. Os pares que apresentam p-value estatisticamente significativo em ambos os testes são classificados como cointegráveis e utilizados nas etapas seguintes do modelo. Para cada par cointegrável, os betas e alphas são estimados dinamicamente por meio de regressões rolling com janela de 63 dias. O beta é travado e atualizado apenas quando ocorre uma variação superior a 7% em relação ao último beta aceito, reduzindo ruído e turnover excessivo. Com os parâmetros dinâmicos estimados, o spread é calculado incorporando o beta dinâmico e o alpha dinâmico. O Z-score do spread é calculado utilizando uma janela de 20 dias, representando o desvio padronizado do spread em relação à sua média histórica recente. Os sinais de trading são definidos com base em thresholds fixos: compra (long spread) quando Z-score < -1.5, venda (short spread) quando Z-score > 1.5, e neutro quando o Z-score está entre os limites. Para garantir neutralidade de delta e controle de risco, o tamanho das posições é dinâmico, ajustado com base no beta dinâmico travado. As posições são normalizadas para que a exposição total permaneça balanceada e o peso relativo dos ativos reflita corretamente a relação de hedge do par.

Metodologia baseada no artigo: ARBITRAGEM ESTATÍSTICA E ESTRATÉGIA LONG-SHORT
PAIRS TRADING, ABORDAGEM DA COINTEGRAÇÃO
APLIACADA A DADOS DO MERCADO BRASILEIRO
JOÃO F. CALDEIRA DEPARTAMENTO DE ECONOMIA UFRS

                                    B3SA3.SA_COGN3.SA  \      Backtest individual de cada par.
Start                             2021-01-05 00:00:00   
End                               2026-01-05 00:00:00   
Period                             1247 days 00:00:00   
Start Value                                   10000.0   
End Value                                11785.452281   
Total Return [%]                            17.854523   
Benchmark Return [%]                        39.534683   
Max Gross Exposure [%]                     274.905071   
Total Fees Paid                                   0.0   
Max Drawdown [%]                            16.323863   
Max Drawdown Duration               666 days 00:00:00   
Total Trades                                      408   
Total Closed Trades                               408   
Total Open Trades                                   0   
Open Trade PnL                                    0.0   
Win Rate [%]                                     50.0   
Best Trade [%]                              15.065785   
Worst Trade [%]                            -18.852472   
Avg Winning Trade [%]                        2.617433   
Avg Losing Trade [%]                        -2.994544   
Avg Winning Trade Duration  1 days 17:03:31.764705882   
Avg Losing Trade Duration   1 days 18:40:47.290640394   
Profit Factor                                1.089509   
Expectancy                                   4.135269   
Sharpe Ratio                                 0.375873   
Calmar Ratio                                 0.301768   
Omega Ratio                                  1.112751   
Sortino Ratio                                0.510586   

                                    B3SA3.SA_FLRY3.SA  \
Start                             2021-01-05 00:00:00   
End                               2026-01-05 00:00:00   
Period                             1247 days 00:00:00   
Start Value                                   10000.0   
End Value                                 11758.04947   
Total Return [%]                            17.580495   
Benchmark Return [%]                        39.534683   
Max Gross Exposure [%]                     278.365481   
Total Fees Paid                                   0.0   
Max Drawdown [%]                            20.145727   
Max Drawdown Duration               697 days 00:00:00   
Total Trades                                      378   
Total Closed Trades                               378   
Total Open Trades                                   0   
Open Trade PnL                                    0.0   
Win Rate [%]                                 50.26455   
Best Trade [%]                              14.093949   
Worst Trade [%]                             -9.199713   
Avg Winning Trade [%]                        1.745829   
Avg Losing Trade [%]                        -2.028241   
Avg Winning Trade Duration  1 days 15:01:53.684210526   
Avg Losing Trade Duration   1 days 19:01:16.595744680   
Profit Factor                                1.131271   
Expectancy                                   4.650925   
Sharpe Ratio                                 0.501895   
Calmar Ratio                                 0.240972   
Omega Ratio                                  1.146929   
Sortino Ratio                                0.756839   

                                    B3SA3.SA_GGBR4.SA  \
Start                             2021-01-05 00:00:00   
End                               2026-01-05 00:00:00   
Period                             1247 days 00:00:00   
Start Value                                   10000.0   
End Value                                 7073.339475   
Total Return [%]                           -29.266605   
Benchmark Return [%]                        39.534683   
Max Gross Exposure [%]                      155.59123   
Total Fees Paid                                   0.0   
Max Drawdown [%]                            34.149455   
Max Drawdown Duration              1216 days 00:00:00   
Total Trades                                      376   
Total Closed Trades                               376   
Total Open Trades                                   0   
Open Trade PnL                                    0.0   
Win Rate [%]                                40.957447   
Best Trade [%]                               6.314639   
Worst Trade [%]                            -12.385236   
Avg Winning Trade [%]                        1.682814   
Avg Losing Trade [%]                        -2.361529   
Avg Winning Trade Duration  1 days 16:59:13.246753246   
Avg Losing Trade Duration   2 days 01:56:45.405405405   
Profit Factor                                0.758082   
Expectancy                                  -7.783672   
Sharpe Ratio                                -0.596478   
Calmar Ratio                                -0.282237   
Omega Ratio                                  0.842856   
Sortino Ratio                               -0.806475   

                                    MGLU3.SA_MRVE3.SA  \
Start                             2021-01-05 00:00:00   
End                               2026-01-05 00:00:00   
Period                             1247 days 00:00:00   
Start Value                                   10000.0   
End Value                                 5002.119032   
Total Return [%]                            -49.97881   
Benchmark Return [%]                        39.534683   
Max Gross Exposure [%]                     229.146499   
Total Fees Paid                                   0.0   
Max Drawdown [%]                            56.337164   
Max Drawdown Duration              1213 days 00:00:00   
Total Trades                                      433   
Total Closed Trades                               431   
Total Open Trades                                   2   
Open Trade PnL                               123.6537   
Win Rate [%]                                39.907193   
Best Trade [%]                              26.136364   
Worst Trade [%]                            -24.265108   
Avg Winning Trade [%]                        3.278479   
Avg Losing Trade [%]                        -4.794997   
Avg Winning Trade Duration  1 days 18:41:51.627906976   
Avg Losing Trade Duration   2 days 05:50:16.216216216   
Profit Factor                                0.718288   
Expectancy                                 -11.882911   
Sharpe Ratio                                -0.770274   
Calmar Ratio                                -0.325766   
Omega Ratio                                   0.81357   
Sortino Ratio                               -0.990137   

                                    MGLU3.SA_PCAR3.SA  
Start                             2021-01-05 00:00:00  
End                               2026-01-05 00:00:00  
Period                             1247 days 00:00:00  
Start Value                                   10000.0  
End Value                                11931.182161  
Total Return [%]                            19.311822  
Benchmark Return [%]                        39.534683  
Max Gross Exposure [%]                     172.577199  
Total Fees Paid                                   0.0  
Max Drawdown [%]                            34.494229  
Max Drawdown Duration               743 days 00:00:00  
Total Trades                                      443  
Total Closed Trades                               441  
Total Open Trades                                   2  
Open Trade PnL                             -42.100177  
Win Rate [%]                                42.176871  
Best Trade [%]                              68.004012  
Worst Trade [%]                            -26.136364  
Avg Winning Trade [%]                        3.827303  
Avg Losing Trade [%]                        -4.031565  
Avg Winning Trade Duration  1 days 15:36:46.451612903  
Avg Losing Trade Duration   2 days 02:51:25.714285714  
Profit Factor                                1.065837  
Expectancy                                    3.66547  
Sharpe Ratio                                 0.312109  
Calmar Ratio                                 0.153769  
Omega Ratio                                  1.106114  
Sortino Ratio                                 0.55374




    
Start                             2021-01-05 00:00:00        Backtest da estratégia como carteira unificada.
End                                 2026-01-05 00:00:00
Period                               1247 days 00:00:00
Start Value                                     10000.0
End Value                                   2596.799086
Total Return [%]                             -74.032009
Benchmark Return [%]                          39.534683
Max Gross Exposure [%]                      7110.448427
Total Fees Paid                             2678.613532
Max Drawdown [%]                             297.126447
Max Drawdown Duration                1081 days 00:00:00
Total Trades                                       1364
Total Closed Trades                                1362
Total Open Trades                                     2
Open Trade PnL                             -2587.724369
Win Rate [%]                                  42.951542
Best Trade [%]                                67.932392
Worst Trade [%]                              -20.249212
Avg Winning Trade [%]                          2.950936
Avg Losing Trade [%]                          -3.202522
Avg Winning Trade Duration    2 days 10:35:04.615384615
Avg Losing Trade Duration     2 days 11:57:13.204633204
Profit Factor                                  0.937433
Expectancy                                    -3.535592
Sharpe Ratio                                   1.240844
Calmar Ratio                      47873701905841.109375
Omega Ratio                                    1.582608
Sortino Ratio                                  2.033174


o Calmar Ratio extremamente alto se deve ao fato que o empilhamento de ordens em decorrencia da funcao from_orders da classe Portifolio distorceu a verdadeira metrica. Tendo em vista esse agrupamento é mais acentuado em decorrência do formato "carteira" do backtest.

O empilhamento de orders da função from_orders() também é observado no gross Exposure acentuado no backtest individuais, visto que gross mostra (long+short).

O desafio ItaúQuant também requisitava o uso de IA generativa em algum processo de criação do bot.

Foi utilizado IA para entender a lógica e a matemática por trás da estratégia de arbitragem, além de otimizar a sintaxe e o manejo do código.

O bot teve as seguintes métricas de execução, taxas = 0.0003,
slippage = 0.0005. Como a "slippage" eh dependente da liquidez e as taxas da boa vontade da corretora que o bot ira operar, foram atribuidos essas métricas com a tentativa se aproximar duma execução real.
