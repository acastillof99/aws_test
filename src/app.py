from api_handler import BMEApiHandler
from eq_w import EqwAlgo


def handler(event, context):
    # Meteis el código completo del algo----->>>>
    ah = BMEApiHandler()
    df_san = ah.get_ohlcv_data('SAN')
    print(df_san)

    # Llamar al algo
    eq_w_1 = EqwAlgo(algo_tag='acastillo_algo1', n_days=10)
    eq_w_1.run_day_comp()

