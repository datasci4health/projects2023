import copy


def add_new_atributes(df_pns, pns_dict):
    pns_dict = copy.deepcopy(pns_dict)

    # Categoria idade

    dict_desc = {
        1: 'Adulto Jovem (<40)',
        2: 'Meia Idade (>=40)'
    }

    row = {
        'index': 'idade_cat',
        'origin': '*',
        'desc': 'Categoria idade',
        'pv': dict_desc,
    }

    def categories(idade):
        if idade < 40:
            return 1
        else:
            return 2

    df_pns[row['index']] = df_pns['idade'].apply(categories)

    pns_dict.df.loc[len(pns_dict.df)] = row

    return df_pns, pns_dict
