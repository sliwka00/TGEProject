import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


cale=[]
kwartaly=[]
msc=[]
print(cale)
df = pd.read_excel(r'abc.xlsx')


df = df.replace('-',np.nan)   #zamienia  "-" na Nan w komórkach gdzie nie ma ceny
df = df.astype({'DKR':float})  #zamienia kolumne DKR na floaty (dane były jako string)
df['kontrakt short'] = df['Kontrakt'].str.split("_").str[-1]       #Skraca nazwe kontraktu do uniwersalnego (dla base i peak) żeby je sparować
df['Data']=pd.to_datetime(df['Data'], format='%d-%m-%Y')
df['wolumen'] = [float(str(val).replace(u'\xa0','').replace(',','.')) for val in df['wolumen'].values]   #wyrzucenie dziwnych znaków z wolumenu i zamiana na float
df3 = df[['Data','DKR','typ','wolumen','kontrakt short']]  #stworzenie skróconego df bez zbędnych kolumn
df_base = df3[df3['typ'] == 'BASE']     #stworzenie df dla base
df_peak = df3[df3['typ'] == 'PEAK']
df_wsp = pd.merge(df_base,df_peak, on=['Data','kontrakt short'])  #połączenie df_base i df_peak dzieki temu można dodać kolumne ratio
df_wsp['ratio']=df_wsp['DKR_y']/df_wsp['DKR_x']  #kolumna z ratio

# Pętla do uzupełniania listy produktów, które znajdują sie w pliku zródłowym
for produkt in df['Kontrakt']:
    if "_Y-" in produkt:
        if produkt not in cale:
            cale.append(produkt)
    elif "_Q-" in produkt:
        if produkt not in kwartaly:
            kwartaly.append(produkt)
    elif "_M-" in produkt:
        if produkt not in msc:
            msc.append(produkt)
    else:
        continue

msc.sort()
kwartaly.sort()
cale.sort()
print(cale)
print(kwartaly)
print(msc)
# Funkcja rysujaca wykres w matplotlib
def draw_chart(produkt):
    df2=df[df['Kontrakt']==produkt]
    data=df2['Data']
    cena=(df2['DKR'])
    wolumen=(df2['wolumen'])
    # Tworzenie figury i osi
    fig, ax1 = plt.subplots()
    ax1.bar(data, wolumen, color='gray', alpha=0.5)
    ax1.set_ylabel('Wolumen')
    ax2 = ax1.twinx()

    ax2.plot(data, cena, marker='o', linestyle='-', color='blue')
    ax2.set_title(produkt)
    ax2.set_xlabel('Data')
    ax2.set_ylabel('cena')
    #
    #myFmt = mdates.DateFormatter('%d-%m-%Y')
    fig.autofmt_xdate(rotation=35, ha='right')    #rotuje daty wyświetlane pod wykresem
    plt.show()

#draw_chart("BASE_Y-25")
def draw_ratio(produkt):
    df_temp=df_wsp[df_wsp['kontrakt short']==produkt]
    data=df_temp['Data']
    ratio=df_temp['ratio']
    plt.plot(data, ratio,marker='o', linestyle='-', color='blue')
    plt.title(produkt)
    plt.xlabel('Data')
    plt.ylabel('ratio')
    plt.show()

#draw_ratio("Y-24")

sg.theme("Black") #gotowe motywy z kolorystyka do podejrzenia w internecie

label=sg.Text("Wykres liniowy DKR, wraz z słupkami z wolumenem")

Y_label=sg.Text("Y")
Y_combo=sg.Combo(cale, font=('Arial Bold', 14),  expand_x=True, enable_events=True, key='Y_droplist')

Q_label=sg.Text("Q")
Q_combo=sg.Combo(kwartaly, font=('Arial Bold', 14),  expand_x=True, enable_events=True, key='Q_droplist')

M_label=sg.Text("M")
M_combo=sg.Combo(msc, font=('Arial Bold', 14),  expand_x=True, enable_events=True, key='M_droplist')




window=sg.Window("Wykresy",
                 layout=[[label],
                        [Y_label,Y_combo,Q_label,Q_combo,M_label,M_combo]],size=(800,100),element_justification='c')


while True:
    event,values=window.read()
    print(f'events: {event}')
    print(f'values: {values}')
    match event:
        case sg.WIN_CLOSED:  # co się stanie po zamknięciu okna gui
            break
        case 'Y_droplist':
            draw_chart(values['Y_droplist'])
        case 'Q_droplist':
            draw_chart(values['Q_droplist'])
        case 'M_droplist':
            draw_chart(values['M_droplist'])
window.close()
