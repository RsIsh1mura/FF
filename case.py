# Этап постановки проблемы:
# Сформулируй несколько гипотез.


# Этап извлечения данных:
# Здесь должен быть твой код
# Дополнительную информацию о синтаксисе можно найти здесь: https://pandas.pydata.org/docs/
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

df = pd.read_csv('IMDB-Movie-Data.csv')
df.info()
print(df.head)
def detect_JasonStatham(value):
    if value.find("Jason Statham") != -1:
        return "есть"
    else:
        return "нема его"

def detected_KeanuReeves(value):
    if value.find("Keanu Reeves") != -1:
        return "есть"
    else:
        return "нема его"

df['Jason Statham'] = df['Actors'].apply(detect_JasonStatham)

#act = df.groupby(by="Jason Statham")["Rating"].agg(["min","mean","max"])
#act.plot(kind="pie",subplots=True)]
df.plot(x = 'Year', y = 'Rating', kind = 'scatter')
df.plot()
d = sns.pairplot(df)


temp = df[df["Revenue (Millions)"]>1]
temp.plot(x = 'Votes', y = 'Revenue (Millions)', kind = 'scatter')

df['Keanu Reeves'] = df['Actors'].apply(detected_KeanuReeves)
df.plot()

plt.show()
# Этап подготовки данных:
# Здесь должен быть твой код


# Этап исследования данных:
# Здесь должен быть твой код


# Этап визуализации данных:
# Здесь должен быть твой код


# Этап решения:
# Подготовь презентацию с описанием гипотез и результатами исследования.