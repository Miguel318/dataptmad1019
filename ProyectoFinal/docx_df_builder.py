import pandas as pd
import os

PATH = '/Users/MIGUEL/Documents/workforce/section2/'

def docx_files(path):
    text_files = []
    files = os.listdir(path)
    for file in files:
        if file[-5:] == '.docx':
            text_files.append(file)
    return text_files

def df_docx_titles(list_of_files):
    extract_1x = pd.DataFrame(list_of_files[0:100])
    extract_2x = pd.DataFrame(list_of_files[100:140])
    extract_3x = pd.DataFrame(list_of_files[140:150])
    extract_4x = pd.DataFrame(list_of_files[150:180])
    extract_5x = pd.DataFrame(list_of_files[180:184])
    extract_6x = pd.DataFrame(list_of_files[185:190])
    extract_7x = pd.DataFrame(list_of_files[190:200])
    extract_8x = pd.DataFrame(list_of_files[200:240])
    extract_9x = pd.DataFrame(list_of_files[241:249])
    extract_10x = pd.DataFrame(list_of_files[251:280])
    extract_11x = pd.DataFrame(list_of_files[280:284])
    extract_12x = pd.DataFrame(list_of_files[285:290])
    extract_13x = pd.DataFrame(list_of_files[290:300])
    extract_14x = pd.DataFrame(list_of_files[300:400])
    extract_15x = pd.DataFrame(list_of_files[400:500])
    extract_16x = pd.DataFrame(list_of_files[500:600])
    extract_17x = pd.DataFrame(list_of_files[600:700])
    extract_18x = pd.DataFrame(list_of_files[700:740])
    extract_19x = pd.DataFrame(list_of_files[740:750])
    extract_20x = pd.DataFrame(list_of_files[750:780])
    extract_21x = pd.DataFrame(list_of_files[780:784])
    extract_22x = pd.DataFrame(list_of_files[785:790])
    extract_23x = pd.DataFrame(list_of_files[790:800])
    extract_24x = pd.DataFrame(list_of_files[800:810])
    extract_25x = pd.DataFrame(list_of_files[811:814])
    extract_26x = pd.DataFrame(list_of_files[816:820])
    extract_27x = pd.DataFrame(list_of_files[825:830])
    extract_28x = pd.DataFrame(list_of_files[830:840])
    extract_29x = pd.DataFrame(list_of_files[840:849])
    extract_30x = pd.DataFrame(list_of_files[851:880])
    extract_31x = pd.DataFrame(list_of_files[880:884])
    extract_32x = pd.DataFrame(list_of_files[885:890])
    extract_33x = pd.DataFrame(list_of_files[890:900])
    extract_34x = pd.DataFrame(list_of_files[900:1000])
    extract_35x = pd.DataFrame(list_of_files[1000:1034])
    df_docx2_titles = pd.concat([extract_1x, extract_2x, extract_3x, extract_4x, extract_5x, extract_6x, extract_7x,
                            extract_8x, extract_9x, extract_10x, extract_11x, extract_12x, extract_13x, extract_14x,
                            extract_15x, extract_16x, extract_17x, extract_18x, extract_19x, extract_20x, extract_21x,
                            extract_22x, extract_23x, extract_24x, extract_25x, extract_26x, extract_27x, extract_28x,
                            extract_29x, extract_30x, extract_31x, extract_32x, extract_33x, extract_34x, extract_35x], axis=0)
    df_docx2_titles.to_csv('/Users/MIGUEL/Desktop/RDA/ProjectIH/DATA/df_docx2_titles.csv')
    return df_docx2_titles

def docx_titles_text():
    cv_data_docx = pd.read_csv('/Users/MIGUEL/Desktop/RDA/ProjectIH/DATA/df_docx_text.csv')
    title_docx = pd.read_csv('/Users/MIGUEL/Desktop/RDA/ProjectIH/DATA/df_docx2_titles.csv')
    DF_DOCX_TITLES = pd.concat([title_docx, cv_data_docx], axis=1, ignore_index=True)
    DF_DOCX_TITLES.to_csv('/Users/MIGUEL/Desktop/RDA/ProjectIH/DATA/DF_DOCX_TITLES.csv')
    return DF_DOCX_TITLES


def trigger_docx(path):
    a = df_docx_titles(docx_files(PATH))
    b = docx_titles_text()
    return b

df = trigger_docx(PATH)
print(df)
