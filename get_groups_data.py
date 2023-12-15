import os
import pandas as pd

def get_group_df(path):
    groups_list = list()
    for root, dirs, files in os.walk(path):
        for file_name in files:
                main_group_name = root.split('/')[-1] 
                group_name = file_name.split('_')[-1][:-4]
                df = pd.read_csv(f'{root}/{file_name}')
                df = df.melt(var_name='year', value_name='brewery_name').dropna()
                df['group'] = group_name
                df['main_group'] = main_group_name
                groups_list.append(df)

    group_df = pd.concat(groups_list)
    return group_df


if __name__ == '__main__':
    RB_groups_df = get_group_df('./data/BigGroups/RB')
    RB_groups_df.to_csv('./data/RB_groups.csv')

    BA_groups_df = get_group_df('./data/BigGroups/BA')
    BA_groups_df.to_csv('./data/BA_groups.csv')
