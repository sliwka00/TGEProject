import PySimpleGUI as sg

cale=['','Y_test1','Y_test2']
kwartaly=['','Q_testowy','Q2_test']
msc=['','Base_M05','Base_M06']

sg.theme("Black") #gotowe motywy z kolorystyka do podejrzenia w internecie

label=sg.Text("Spreadator")

Y_label=sg.Text("Y")
Y_combo=sg.Combo(cale, font=('Arial Bold', 14),  expand_x=True, enable_events=True, key='Y_droplist')

Q_label=sg.Text("Y")
Q_combo=sg.Combo(kwartaly, font=('Arial Bold', 14),  expand_x=True, enable_events=True, key='Q_droplist')

M_label=sg.Text("M")
M_combo=sg.Combo(msc, font=('Arial Bold', 14),  expand_x=True, enable_events=True, key='M_droplist')

chart=sg.Canvas(background_color="white",size=[500,400])  #w canvas wg internetu jest filmik dla wykresu
window=sg.Window("Spready",
                 layout=[[label],
                        [Y_label,Y_combo,Q_label,Q_combo,M_label,M_combo],
                         [chart]])
while True:
    event,values=window.read()
    print(f'events: {event}')
    print(f'values: {values}')
    match event:
        case sg.WIN_CLOSED:  # co się stanie po zamknięciu okna gui
            break
window.close()