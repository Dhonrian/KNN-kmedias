import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\Leo\Documents\Analise Knn kmedia\2019-summer-match-data-OraclesElixir-2019-09-16.xlsx"

del_cols = ['playerid', 'player', 'side','position','gameid', 'url', 'split', 'date', 'week', 'game', 'patchno',
            'champion', 'ban1', 'ban2', 'ban3', 'ban4', 'ban5', 'result']

df_tmp = pd.read_excel(path)
df_tmp = df_tmp.drop(columns = del_cols)
df_tmp = df_tmp.rename(columns={"kmp": "KillsPerMin", "okpm": "OppKillsPmin",
                       "cpkm": "CombinedKillPmin", "fd": "FirstDragon", "fdtime": "FDrTime",
                       "teamdragkills": "TeamDragKills", "oppdragkills": "OppDrKills",
                       "oppelders": "OppElders", "ft": "FirstTower", "fttime": "FTtime",
                       "firstmidouter": "FirstMidTower", "firsttothreetowers": "FirstTo3Twr",
                       "oppbaronkills": "OppBaronKills", "dmgtochamps": "DmgToChamps",
                       "dmgtochampsperminute": "Dmg2ChmpsPMin", "wpm": "WardsPerMin",
                       "visiblewardclearrate": "VisibleWrdClearedByOpp", "gspd": "GoldSpentDiff",
                       "csmp": "CreepScorePMin", "ccsharepost15": "CreepPost15", "csat10": "CreepScoreAt10",
                       "oppcsat10": "OppCsAt10", "csdat10": "CsDiffAt10", "oppgoldat10": "OppGoldAt10",
                       "gdat10": "GoldDiffAt10", "oppgoldat15": "OppGoldAt15", "gdat15": "GoldDiffAt15",
                       "xpat10": "ExpAt10", "oppxpat10": "OppExpAt10", "xpdat10": "ExpDiffAt10"})


df_tmp['duplicated'] = df_tmp.duplicated(['team'])
teams = df_tmp.loc[df_tmp['duplicated'] == False, 'team'].values


df = pd.DataFrame()

for team in teams:
    series = df_tmp.loc[df_tmp['team'] == team].mean()
    aux = series.to_frame(name = team).T
    df = df.append(aux)

print(df)
df = df.drop(columns = ['duplicated'])

fig = plt.figure(figsize=[9,9])
ax = fig.add_subplot(111)
im = ax.matshow(df.corr(method='spearman'),cmap='bwr')

ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns, fontsize=7)
ax.set_yticklabels(df.columns, fontsize=7)

plt.colorbar(im)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
