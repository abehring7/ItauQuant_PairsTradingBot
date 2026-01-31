import pandas as pd
import numpy as np
import yfinance as yf
import vectorbt as vbt
from statsmodels.tsa.stattools import coint, adfuller
from scipy import stats
from itertools import combinations
from pathlib import Path
base_path = Path("excel_folder")


## spread sendo a difernça estatisticaemente ajustada dos ativos, medida pelo produto da diferenca pelo beta permite visualizar estacionaridade nos oreços [ativo sintetico estacionario]
## zscore suaviza isso para medidas de desvio padrao, tornando melhor a visualização  [gatilhos de mercado]

acoes_bovespa = ["ALOS3", "ABEV3", "AZZA3", "B3SA3", "BBSE3",
"BBDC3", "BBDC4", "BRAP4", "BBAS3", "BRKM5", "BPAC11", "CEAB3", "CMIG4",
"COGN3", "CPLE6", "CSAN3", "CPFE3", "CURY3", "CVCB3", "CYRE3", "DIRR3", "ELET3",
"ELET6", "EMBR3", "ENGI11", "ENEV3", "EGIE3", "EQTL3", "FLRY3", "GGBR4", "GOAU4",
"HAPV3", "HYPE3", "IRBR3", "ISAE4", "ITSA4", "ITUB4", "KLBN11", "RENT3",
"LREN3", "MGLU3", "POMO4", "BEEF3", "MRVE3", "MULT3",
"PCAR3", "PETR3", "PETR4", "PRIO3", "PSSA3", "RADL3",
"RAIL3", "SBSP3", "SUZB3", "TAEE11", "TOTS3", "UGPA3", "USIM5", "VALE3", "WEGE3"]
acoes_bovespa = [ativo + ".SA" for ativo in acoes_bovespa]

 
def puxar_precos():
    acoes_df = pd.DataFrame()
    acoes = yf.download(acoes_bovespa, period="5y")["Close"]
    acoes_df = pd.concat([acoes, acoes_df] ,axis=1)
    return acoes_df


def open_excel():
    caminho = base_path / "close_papeis.xlsx"
    arquivo = pd.read_excel(caminho, engine="openpyxl", index_col=0, parse_dates=True)
    return arquivo

## fetch de dados e formatação dos mesmos
## --------------------------------------
                          ## x eh o benchmark
def lin_regress_p(x,y):   ##  preditora e independente(quer prever)
    x = np.asarray(x).astype(float) ## duas colunas vao como arrayNP
    y = np.asarray(y).astype(float)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    residuals = y - (intercept+slope*x) ## calcula a diferenca entre o valor de y real eh o previsto baseado em x
    adf_result = adfuller(residuals) 
    p_value_adf = adf_result[1]
    return p_value_adf ## tava adf_result[1] preciso do residuo pra coint
## funcao retorna o valor do adf no residuo (p_value residuo)

""" def lin_regress_r(x,y):   ## regressao preditora e independente
    x = np.asarray(x).astype(float)
    y = np.asarray(y).astype(float)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    residuals = y - (intercept+slope*x) ## calcula a diferenca entre o valor de y real eh o previsto
    return residuals """
## essa faz o adf mas so returna o residuo mesmo

## fazer  teste de cointegração de Dickey-Fuller aumentado (Cointegrating augmented Dickey-Fuller test) e teste de Johansen no df

resultados_augment = []
def cointegration(): ## abrir o coint_ativos fazer os a coint pegar os residuos e meter adf test
    for papel1 , papel2 in combinations(arquivo.columns, 2):          ## combinations faz todas as iteracoes possiveis entre os papeis sem ser redundante
        adf_p_value = lin_regress_p(arquivo[papel1], arquivo[papel2]) ## encontro o p_value dos dois papeis
        score, pvalue, _ = coint(arquivo[papel1], arquivo[papel2]) 
        if (pvalue<0.05 and adf_p_value<0.05): ## se a coint for bem sucedida vai appendar com o papel, c e adfpvalue
            resultados_augment.append([papel1, papel2, pvalue, adf_p_value])
    stationary_df = pd.DataFrame(resultados_augment, columns=[
        "stock1",
        "stock2",
        "coint_r",
        "adf_pvalue"
    ])                                          ## armazena os resultados da lista do no df
    try:                                        ## try e except no envio do df para .xlsx
        if not stationary_df.empty:
            with pd.ExcelWriter(base_path/ "coint_result2.xlsx") as writer:
                stationary_df.to_excel(writer, index=False)
                print("arquivo enviado")
    except Exception as e:
        print(f"erro : {e}")
    return stationary_df        ## df retornando quais sao os papeis estacionarios (pvalue e coint(pvalue))

betas = []
alphas = []
stock1 = []
stock2 = []
def lin_regress_result():


    base_path = Path("excel_folder")
    camino = base_path / "close_cointegravel.xlsx"
    path = base_path / "coint_result2.xlsx"


    df_cointegravel = pd.read_excel(path)
    df_close_coint = pd.read_excel(camino,index_col=0, parse_dates=True)


    for index, row in df_cointegravel.iterrows(): ## percorre o df por linha/index
        s1_name = row["stock1"]                   ## pega o nome do primeiro papel por row["stock1"]
        s2_name = row["stock2"]                   ## mesma coisa soq com o papel2  
        
        

        precos_stock1 = df_close_coint[s1_name]  ## acha o preco pegando o nome do ativo(acima) na coluna do close_coint
        precos_stock2 = df_close_coint[s2_name]  ## mesma coisa, 
        
        precos_stock1 = np.log(precos_stock1)           ## transforma em array e escala log para nao quebrar o alpha
        precos_stock2 = np.log(precos_stock2)
        

        beta, alpha, _, _, _ = stats.linregress(precos_stock1, precos_stock2)
        betas.append(beta)
        alphas.append(alpha)
        stock1.append(s1_name)
        stock2.append(s2_name)
    
    caminho = base_path / "linregress_resultado.xlsx"
    df_linregress = pd.DataFrame({"stock1":stock1,         ##  alinha os elementos correspondentes a suas colunas
                                  "stock2":stock2,
                                  "alpha":alphas,
                                  "beta":betas})
    return df_linregress

## ---------------------------------------------------------------------------------------------------

def spread_zcore():
    base_path = Path("excel_folder")
    arquivo_coint = pd.read_excel(
    base_path / "coint_result2.xlsx"
    )
    a = pd.unique(arquivo_coint["stock1"].tolist() + arquivo_coint["stock2"].tolist())  ## acoes unicas nas duas colunas
    close = pd.read_excel(
    base_path / "close_papeis.xlsx",
    index_col=0,
    parse_dates=True
    )
    close_filtrado = close[a]

    df_linregress = df_linregress()

    z_scoredf = pd.DataFrame(index=close.index)
    for index, row in df_linregress.iterrows():
        beta = row["betas"]
        alpha = row["alphas"]
        p1_name = row["papel1"]
        p2_name = row["papel2"]
        spread = np.log(close_filtrado[p2_name])-(np.log(close_filtrado[p1_name])*beta_dyn+alpha)
        z_score = (spread-spread.mean()) / np.std(spread)
        par = f"{p1_name}_{p2_name}"
        z_scoredf[par] = z_score


def signals_df():
    base_path = Path("excel_folder")
    z_scoredf = pd.read_excel(base_path / "z_scoredf.xlsx", index_col=0, parse_dates=True)
    signal_df = pd.DataFrame(index=z_scoredf.index)
    for pairs in z_scoredf.columns:         
        conditions = [                      ## [lista_(matematica_bool)_lista]
            (z_scoredf[pairs]<-2),
            (z_scoredf[pairs]>2)
        ]
        choices = [1, -1]
        signal_df[f"{pairs}_signal"] = np.select(   ## como sao 3 condicoes(compra,venda,fazer nada) o np.where fica rui, assim usa-se select
            conditions,
            choices,
            default=0
        )
    signal_df.to_excel(base_path/"signals_df.xlsx")



## Funcoes estatisticas e criação do df z_score, sinais
## ----------------------------------
def backtest():  
    base_path = Path("excel_folder")

close_df = pd.read_excel(
    base_path / "close_papeis.xlsx",
    index_col=0,
    parse_dates=True
)                                                                  ## inicializacao de dfs
coint_result = pd.read_excel(base_path/"coint_result2.xlsx")
z_scoredf = pd.read_excel(
    base_path/"z_scoredf.xlsx",
    index_col=0,
    parse_dates=True                     
)

size_df = pd.read_excel(
    base_path/"signals_df.xlsx",
    index_col=0,
    parse_dates=True
)
backtest_df = pd.DataFrame()
benchmark_df = yf.download("^BVSP", period="5y")["Close"]

benchmark_df = benchmark_df.loc["2021-01-26":"2026-01-15"]
benchmark_df = benchmark_df.pct_change()
benchmark_df = benchmark_df.reindex(close_df.index)
benchmark_df = benchmark_df.squeeze()           ## remove dimensoes a coluna (redundante)

unic_tickers = pd.unique(coint_result["stock1"].to_list() + coint_result["stock2"].tolist())
unic_tickers = unic_tickers.tolist()
open_df = yf.download(unic_tickers, period="5y")["Open"] ## baixa o df de precos de abertura com base nos tickers unicos
open_df = open_df.loc["2021-01-26":"2026-01-15"]
open_df = open_df.reindex(close_df.index)
open_df = open_df.interpolate(method="time", axis=0, limit_direction="backward", limit_area="outside")   ## interpola os NANS com valores aceitaveis
beta_dinamico = pd.read_excel(base_path/"alpha_beta.xlsx", index_col=0, parse_dates=True)   ## inicializa os betas para calcular o notional

## ------------------------------------
## inicializaco e transformacao de dfs 
## ------------------------------------

for pair in z_scoredf.columns:
    papel1, papel2 = pair.split("_")        ## tira o "_" e assinala cada variavel no lugar dela
    sinal = size_df[f"{pair}_signal"]

    beta_dyn = beta_dinamico[f"{pair}_beta"].clip(-3, 3)
    
    fator_nor = abs(beta_dyn).fillna(0)+1
    
    
    signals_split = pd.DataFrame({                        ## cria a cada loop o df balanceado pelo beta para cada par
        papel1:(-sinal*beta_dyn) / fator_nor,
        papel2:sinal / fator_nor
    }, index=close_df.index) ## assinala di
    signals_split = signals_split.shift(1).fillna(0).clip(-1,1) ## evita lookaheadbias preenche os nan se tiver e resitringe a posivcao para -1,1
        
    portif = vbt.Portfolio.from_orders(
        close=close_df[[papel1, papel2]],
        size=signals_split[[papel1, papel2]],
        price=open_df[[papel1, papel2]],
        val_price=open_df[[papel1, papel2]],             ## da o notional da ordem, com base no sinal
        freq="d",
        size_type="targetpercent",
        init_cash=10000,
        direction="both",
        fees = 0.0003,
        slippage = 0.0005,
        cash_sharing=True                                 ## permite o financiamento do long pelo short
    )
    estatisticas = portif.stats(                          ## determina o benchmark e mostra os valores do benchmark
        settings=dict(
            benchmark_rets=benchmark_df,
            verbose=True
        )
    )
    backtest_df[pair] = estatisticas

print(backtest_df)


def main():
    backtest_df = backtest()

if __name__ == "__main__":
    main()



## git

