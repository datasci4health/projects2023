import copy

exp_dict = {
    'log_apenas_habitos': 'Apenas hábitos',
    'log_apenas_dcnt': 'Apenas doenças crônicas',
    'log_apenas_habitos_dcnt': 'Apenas hábitos e doenças crônicas',
    'log_apenas_sociodemo': 'Apenas variáveis sociodemográficos',
    'log_all_dropna': 'Removendo Linhas Nulas',
    'log_all_meanimp': 'Substituindo NA pela média',
    'log_all_medianimp': 'Substituindo NA pela mediana',
    'log_all_smote': 'SMOTE',
    'log_best_grid': 'Melhor resultado Grid Search',
    'log_class_renda_baixa': 'Renda Baixa',
    'log_class_renda_alta': 'Renda Alta',
    'log_class_sexo_mulher': 'Sexo Mulher',
    'log_class_sexo_homem': 'Sexo Homem',
    'log_class_idade_less40': 'Idade < 40',
    'log_class_idade_more40': 'Idade >= 40',
    'log_class_idade1': 'Idade [20, 29]',
    'log_class_idade2': 'Idade [30, 39]',
    'log_class_idade3': 'Idade [40, 49]',
    'log_class_idade4': 'Idade [50, 59]',
    'log_class_r_norte': 'Região Norte',
    'log_class_r_nordeste': 'Região Nordeste',
    'log_class_r_sudeste': 'Região Sudeste',
    'log_class_r_sul': 'Região Sul',
    'log_class_r_centro_oeste': 'Região Centro Oeste',
    'rf_exp': 'Árvore de Decisão',
    'dt_exp': 'Floresta Randomica'
}

column_mapping = {
    'train_acc': 'Acc. Treino',
    'test_acc': 'Acc. Teste',
    'train_precision': 'P. Treino',
    'test_precision': 'P. Teste',
    'train_recall': 'R. Treino',
    'test_recall': 'R. Teste',
    'train_f1': 'F1 Treino',
    'train_auc': 'AUC Treino'
}

variables_names = {
    'intercept': 'Intercepto',
    'upf': 'Ultraprocessados',
    'exerc_fisico': 'Exercício Físico',
    'tabagismo': 'Tabagismo',
    'cons_alcool': 'Consumo Álcool',
    'cancer': 'Câncer',
    'hipertensao': 'Hipertensão',
    'diabetes': 'Diabetes',
    'cardiovascular': 'Cardiovascular',
    'hipercolesterolemia': 'Hipercolesterolemia',
    'avc': 'AVC',
    'artrite': 'Artrite',
    'obesidade': 'Obesidade',
    'sexo': 'Sexo',
    'estado_civil': 'Estado Civil',
    'escolaridade': 'Classificação Escolaridade',
    'class_idade': 'Classificação Idade',
    'class_renda': 'Classificação Renda',
    'depression': 'Depressão'
}


def gen_metrics_table(df_metrics_all, path):
    df = copy.deepcopy(df_metrics_all) * 100
    df['F1 Teste'] = df['test_f1'].map('{:.2f}'.format) + ' ± ' + df['test_f1_std'].map('{:.2f}'.format)
    df['AUC Teste'] = df['test_auc'].map('{:.2f}'.format) + ' ± ' + df['test_auc_std'].map('{:.2f}'.format)

    def _gen(df):

        df = df.rename(index=exp_dict, columns=column_mapping)

        for c in df.columns:
            try:
                df[c] = df[c].map('{:.2f}'.format)
            except:
                pass

        with open(path, 'a') as file:
            file.write(df.to_markdown() + "\n\n")

    with open(path, 'w') as file:
        file.write('')

    df_s = df[['train_acc', 'test_acc', 'train_precision', 'test_precision', 'train_recall', 'test_recall', 'train_f1',
               'F1 Teste', 'train_auc', 'AUC Teste']]
    df_s = df_s[df_s.index.isin(['log_apenas_habitos', 'log_apenas_dcnt', 'log_apenas_habitos_dcnt',
                                 'log_apenas_sociodemo', 'log_all_dropna'])]
    _gen(df_s)

    df_s = df[['train_f1', 'F1 Teste', 'train_auc', 'AUC Teste']]
    df_s = df_s[df_s.index.isin(['log_all_dropna', 'log_all_meanimp', 'log_all_medianimp',
                                 'log_all_smote', 'log_best_grid', 'rf_exp', 'dt_exp'])]
    _gen(df_s)

    df_s = df[['train_f1', 'F1 Teste', 'train_auc', 'AUC Teste']]
    df_s = df_s[df_s.index.isin(['log_class_renda_baixa', 'log_class_renda_alta', 'log_class_sexo_mulher',
                                 'log_class_sexo_homem', 'log_class_idade_less40', 'log_class_idade_more40',
                                 'log_class_idade1', 'log_class_idade2', 'log_class_idade3', 'log_class_idade4',
                                 'log_class_r_norte', 'log_class_r_nordeste', 'log_class_r_sudeste', 'log_class_r_sul',
                                 'log_class_r_centro_oeste'])]
    _gen(df_s)


def gen_coef_table(df_importances_all, path):
    df = copy.deepcopy(df_importances_all)

    def _gen(df):

        df = df.rename(index=variables_names, columns=exp_dict)
        if len(df.columns) == 2:
            df['Diferença'] = df.iloc[:, 1] - df.iloc[:, 0]

        for c in df.columns:
            try:
                df[c] = df[c].map('{:.2f}'.format)
            except:
                pass

        with open(path, 'a') as file:
            file.write(df.to_markdown() + "\n\n")

    with open(path, 'w') as file:
        file.write('')

    df_s = df[['log_apenas_habitos', 'log_apenas_dcnt', 'log_apenas_habitos_dcnt', 'log_apenas_sociodemo',
               'log_all_dropna']]
    _gen(df_s)

    df_s = df[['log_class_renda_baixa', 'log_class_renda_alta']]
    _gen(df_s)

    df_s = df[['log_class_sexo_mulher', 'log_class_sexo_homem']]
    _gen(df_s)

    df_s = df[['log_class_idade_less40', 'log_class_idade_more40']]
    _gen(df_s)

    df_s = df[['log_class_idade1', 'log_class_idade2', 'log_class_idade3', 'log_class_idade4']]
    _gen(df_s)

    df_s = df[['log_class_r_norte', 'log_class_r_nordeste', 'log_class_r_sudeste', 'log_class_r_sul',
               'log_class_r_centro_oeste']]

    _gen(df_s)
