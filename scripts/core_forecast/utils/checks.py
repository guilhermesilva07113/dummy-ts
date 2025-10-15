import pandas as pd


def check_if_variaveis_usuario_are_in_the_df(
    df: pd.DataFrame, VARIAVEIS_USUARIO: list
) -> KeyError | None:
    """Check if user variables are presented in the dataset. If they are not, it gives a Key Error

    Args:
        df (pd.DataFrame): Dataframe to be predicted
        VARIAVEIS_USUARIO (list): List of variables

    Raises:
        KeyError: _description_

    Returns:
        KeyError: _description_
    """
    if len(VARIAVEIS_USUARIO) > 0:
        missing_user_vars = []
        for v in VARIAVEIS_USUARIO:
            if v not in df.columns.values:
                missing_user_vars.append(v)
        if len(missing_user_vars) > 0:
            raise KeyError(f"As colunas {missing_user_vars} nao foram encontradas.")
